import nltk
def nltk_corpus_dl(corpus: str):
    try:
        nltk.data.find(f"corpora/{corpus}")
        corpus_module = getattr(__import__("nltk.corpus", fromlist=[corpus]), corpus)
        return corpus_module
    except LookupError:
        nltk.download(corpus)
        corpus_module = getattr(__import__("nltk.corpus", fromlist=[corpus]), corpus)
        return corpus_module
wn = nltk_corpus_dl("wordnet")

def get_words_one_level_below(category: str):
    # Get synsets for the given category
    synsets = wn.synsets(category)

    # Collect hyponyms one level below
    words_below = []
    for synset in synsets:
        for hyponym in synset.hyponyms():
            # Get the word form for each hyponym and add it to the list
            words_below.extend(lemma.name() for lemma in hyponym.lemmas())

    return words_below


def get_related_words(word):
    # Finding synsets for the given word
    synsets = wn.synsets(word)

    related_words = set()

    for synset in synsets:
        # Adding lemmas from the synsets
        related_words.update(lemma.name() for lemma in synset.lemmas())

        # Adding lemmas from the hypernyms
        related_words.update(
            lemma.name()
            for hypernym in synset.hypernyms()
            for lemma in hypernym.lemmas()
        )

        # Adding lemmas from the hyponyms
        related_words.update(
            lemma.name() for hyponym in synset.hyponyms() for lemma in hyponym.lemmas()
        )

    # Removing the original word from the set
    related_words.discard(word)

    return list(related_words)


def get_root_hypernyms(word):
    synsets = word.synsets(word)
    root_hypernyms = [syn.root_hypernyms()[0] for syn in synsets]
    return set(root_hypernyms)