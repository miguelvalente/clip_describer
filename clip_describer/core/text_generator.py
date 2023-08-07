from pathlib import Path
from PIL import Image

from clip_describer.core.lists import product_categories, qualities_list, colours_list
from clip_describer.core.model import device, preprocess, rank_categories_with_clip
from clip_describer.core.wordnet_parse import get_words_one_level_below, get_related_words


def get_qualities(image, context: str):
    contextualized_keys = {f"This {context} has a {key} of ": key for key in qualities_list.keys()}
    cats = rank_categories_with_clip(image, list(contextualized_keys.keys()), 2)

    colours = rank_categories_with_clip(image, colours_list)

    for cat in cats:
        qualities_list[contextualized_keys[cat]] = qualities_list.pop(contextualized_keys[cat])

    return [rank_categories_with_clip(image, qualities_list[contextualized_keys[cat]]) for cat in cats] + [colours]


def generate_description(uploaded_image):
    image = Image.open(uploaded_image)
    image = preprocess(image).unsqueeze(0).to(device)

    root_category = rank_categories_with_clip(image, list(product_categories.keys()))
    sub_category = rank_categories_with_clip(image, product_categories[root_category])

    if len(root_category.split()) > 1:
        root_category = rank_categories_with_clip(image, root_category.split())

    level1 = list(set(get_related_words(root_category) + get_related_words(sub_category)))
    level1_rank = rank_categories_with_clip(image, level1, 3)

    level2 = [get_words_one_level_below(word) for word in level1]
    if level2:
        level2 = list(set(sum(level2, [])))
        level2_rank = rank_categories_with_clip(image, level2, 3)

    final_categories = list(set(level1_rank + level2_rank))

    qualities = get_qualities(image, " ".join(final_categories))

    return [word.lower().split() for word in sorted(set(final_categories + qualities))]