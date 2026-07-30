# Natural Language Processing (NLP) Lab Experiments 1 to 6

This repository contains the python implementations and execution outputs for NLP Lab Experiments 1 through 6.

---

## 📁 Repository Structure

```
NLP_Lab_Experiments_1_to_6/
├── exp1.py          # Exp 1: Tokenization, Stemming & Lemmatization
├── exp2.py          # Exp 2: Part-of-Speech (POS) Tagging
├── exp3.py          # Exp 3: Cosine Similarity, Clustering & WordNet Similarity
├── exp4.py          # Exp 4: Information Retrieval using TF-IDF & LSA
├── exp5.py          # Exp 5: Named Entity Recognition (NER) for Legal Domain
├── exp6.py          # Exp 6: Biomedical Relation Extraction & Evaluation
├── outputs.txt      # Text file with complete output log for all 6 experiments
└── README.md        # Documentation and experiment details
```

---

## 🧪 Experiments Summary & Output

### 🔹 Experiment 1: Tokenization, Stemming & Lemmatization
- **Objective:** Tokenize text and compare root word extraction via Stemming (PorterStemmer) vs Lemmatization (WordNetLemmatizer).
- **Input:** `"The striped bats were hanging upside down for eating small insects."`
- **Output:**
  ```text
  Tokens: ['The', 'striped', 'bats', 'were', 'hanging', 'upside', 'down', 'for', 'eating', 'small', 'insects', '.']
  Stemmed Words: ['the', 'stripe', 'bat', 'were', 'hang', 'upsid', 'down', 'for', 'eat', 'small', 'insect', '.']
  Lemmatized Words: ['The', 'striped', 'bat', 'were', 'hanging', 'upside', 'down', 'for', 'eating', 'small', 'insect', '.']
  ```

---

### 🔹 Experiment 2: Part-of-Speech (POS) Tagging
- **Objective:** Tokenize text and tag grammatical components (Nouns, Verbs, Adjectives, etc.).
- **Input:** `"The quick brown fox jumps over the lazy dog."`
- **Output:**
  ```text
  POS Tags:
  The -> DT
  quick -> JJ
  brown -> NN
  fox -> NN
  jumps -> VBZ
  over -> IN
  the -> DT
  lazy -> JJ
  dog -> NN
  ```

---

### 🔹 Experiment 3: Text Clustering & WordNet Semantic Similarity
- **Objective:** Calculate TF-IDF Cosine Similarity Matrix between headlines, group headlines using K-Means Clustering, and compute WordNet path similarity between synsets.
- **Inputs:**
  - Headlines:
    1. `"Government announces new economic policy"`
    2. `"Economy grows as government releases new policy"`
    3. `"Local team wins championship match"`
    4. `"Sports team celebrates victory in final match"`
  - Words: `"dog"`, `"cat"`
- **Output:**
  - Cosine Similarity Matrix computed
  - Headline Clusters: Grouped into Cluster 0 (Sports) and Cluster 1 (Politics/Economy)
  - WordNet Similarity (`dog` vs `cat`): `0.2`

---

### 🔹 Experiment 4: Information Retrieval (TF-IDF vs Latent Semantic Analysis - LSA)
- **Objective:** Compare document retrieval accuracy using TF-IDF vs LSA (Truncated SVD).
- **Input Query:** `"machine learning and artificial intelligence"`
- **Output:**
  ```text
  TF-IDF Similarity Scores:
  Document 1 : 0.762
  Document 2 : 0.111
  Document 3 : 0.103

  LSA Similarity Scores:
  Document 1 : 1.0
  Document 2 : 0.625
  Document 3 : 0.571

  Most Relevant Document: Artificial intelligence and machine learning are revolutionizing technology.
  ```

---

### 🔹 Experiment 5: Named Entity Recognition (NER) in Legal Domain
- **Objective:** Extract Proper Noun (NNP) entities from legal text and compute NER accuracy percentage.
- **Input:** `"Supreme Court of India delivered judgment in New Delhi regarding Article 370 on Monday."`
- **Output:**
  - Detected Entities: `Supreme`, `Court`, `India`, `New`, `Delhi`, `Article`, `Monday` (7 predicted)
  - NER Accuracy: `57.14%`

---

### 🔹 Experiment 6: Biomedical Relation Extraction & Classification Metrics
- **Objective:** Extract target biomedical relations from text using keyword matching and evaluate precision, recall, and F1-score.
- **Input:** `"Aspirin treats headache and reduces inflammation in patients."` (Actual Relation: 1)
- **Output:**
  ```text
  Predicted Relation: 1
  Precision: 1.0
  Recall: 1.0
  F1-Score: 1.0
  ```

---

## 🚀 How to Run

To execute any experiment:
```bash
python exp1.py
python exp2.py
python exp3.py
python exp4.py
python exp5.py
python exp6.py
```
