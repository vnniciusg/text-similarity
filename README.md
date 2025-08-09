# Text Similarity Libraries Benchmark

This repository contains a benchmark comparing three different Python libraries for measuring text similarity:

- **[difflib](https://docs.python.org/3/library/difflib.html)** – built-in Python library using `SequenceMatcher`
- **[rapidfuzz](https://github.com/maxbachmann/rapidfuzz)** – fast string matching based on Levenshtein distance
- **[sentence-transformers](https://www.sbert.net/)** – semantic similarity using transformer-based embeddings

The goal is to provide a reproducible test set and see how each library scores across different types of text changes (synonyms, rewording, semantic shifts, and meaning changes).

---

## Example Output

| Original Phrase                     | Changed Phrase                         | Difflib | RapidFuzz | SBERT         |
| ----------------------------------- | -------------------------------------- | ------- | --------- | ------------- |
| The cat sleeps on the couch         | The feline rests on the couch          | 0.68    | 0.75      | 0.60 (High)   |
| It will rain a lot today            | It will rain heavily today             | 0.84    | 0.84      | 0.91 (High)   |
| I like coffee                       | I love tea                             | 0.52    | 0.52      | 0.64 (Medium) |
| The house is blue                   | The residence is yellow                | 0.55    | 0.55      | 0.46 (Medium) |
| He bought a new car                 | He sold an old car                     | 0.59    | 0.59      | 0.84 (Low)    |
| We are going to the cinema tomorrow | We are going to watch a movie tomorrow | 0.77    | 0.82      | 0.87 (High)   |
| The dog is barking                  | The dog is running                     | 0.83    | 0.83      | 0.44 (Medium) |
| The bread is fresh                  | The bread is spoiled                   | 0.74    | 0.76      | 0.77 (Low)    |
| The child plays in the park         | The girl plays in the garden           | 0.80    | 0.80      | 0.43 (High)   |
| I need to study for the test        | I need to rest after work              | 0.53    | 0.64      | 0.33 (Low)    |

> **Note:** SBERT scores represent cosine similarity between embeddings. The last column also includes a qualitative classification (**High**, **Medium**, **Low**) based on score thresholds.

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/text-similarity-benchmark.git
cd text-similarity-benchmark
```

2. Install dependencies using [uv](https://github.com/astral-sh/uv):

```bash
uv sync
```

3. Run the benchmark:

```bash
uv run main
```

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
