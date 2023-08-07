
import torch
import clip
import numpy as np


device = "cuda" if torch.cuda.is_available() else "cpu"

model, preprocess = clip.load("ViT-B/32", device=device, download_root=".")

def rank_categories_with_clip(model, image, categories, top_n=1):
    text = clip.tokenize(categories).to(device)

    with torch.no_grad():
        logits_per_image, logits_per_text = model(image, text)
        probs = logits_per_image.softmax(dim=-1).cpu().numpy()

    # Get the top_n indices sorted by probabilities
    top_indices = np.argsort(-probs)[0, :top_n]
    decoded = [categories[idx] for idx in top_indices]

    # Return as a list if top_n > 1, else return the first element
    return decoded if top_n > 1 else str(decoded[0])