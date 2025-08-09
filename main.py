import difflib
from rapidfuzz import fuzz
from sentence_transformers import SentenceTransformer, util


TestCase = tuple[str, str, str]

test_cases: list[TestCase] = [
    ("The cat sleeps on the couch", "The feline rests on the couch", "High"),
    ("It will rain a lot today", "It will rain heavily today", "High"),
    ("I like coffee", "I love tea", "Medium"),
    ("The house is blue", "The residence is yellow", "Medium"),
    ("He bought a new car", "He sold an old car", "Low"),
    ("We are going to the cinema tomorrow", "We are going to watch a movie tomorrow", "High"),
    ("The dog is barking", "The dog is running", "Medium"),
    ("The bread is fresh", "The bread is spoiled", "Low"),
    ("The child plays in the park", "The girl plays in the garden", "High"),
    ("I need to study for the test", "I need to rest after work", "Low"),
]

model = SentenceTransformer("all-MiniLM-L6-v2")


def similarity_difflib(a: str, b: str) -> float:
    """Calculate similarity using difflib."""
    return difflib.SequenceMatcher(None, a, b).ratio()


def similarity_rapidfuzz(a: str, b: str) -> float:
    """Calculate similarity using rapidfuzz."""
    return fuzz.WRatio(a, b) / 100.0


def similarity_sentence_transformers(a: str, b: str) -> float:
    """Calculate similarity using embedding of SentenceTransformers."""
    emb_a = model.encode(a, convert_to_tensor=True)
    emb_b = model.encode(b, convert_to_tensor=True)
    return util.pytorch_cos_sim(emb_a, emb_b).item()


if __name__ == "__main__":
    print(
        f"{'Original Phrase':40} | {'Changed Phrase':40} | Difflib | RapidFuzz | SBERT"
    )
    print("-" * 120)
    for original, modified, esperado in test_cases:
        score_difflib = similarity_difflib(original, modified)
        score_rapidfuzz = similarity_rapidfuzz(original, modified)
        score_sbert = similarity_sentence_transformers(original, modified)
        print(
            f"{original:40} | {modified:40} | {score_difflib:.2f}   | {score_rapidfuzz:.2f}       | {score_sbert:.2f} ({esperado})"
        )
