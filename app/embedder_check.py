from sentence_transformers import SentenceTransformer

MODEL_NAME = "BAAI/bge-m3"


def load_embedder():
    return SentenceTransformer(MODEL_NAME)


if __name__ == "__main__":
    model = load_embedder()
    vectors = model.encode([
        "Kalaallisut oqaaseqarnermik suliaq",
        "Dansk-grønlandsk sprogteknologi",
    ])
    print(vectors.shape)
