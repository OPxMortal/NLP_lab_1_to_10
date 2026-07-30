# Experiment 1
# Tokenization and Comparison of Stemming vs Lemmatization
# for Sentiment Analysis Text Preprocessing

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer


# --------------------------------------------------
# Download Required NLTK Data
# --------------------------------------------------

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("wordnet")


# --------------------------------------------------
# Initialize Stemmer and Lemmatizer
# --------------------------------------------------

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


# --------------------------------------------------
# Get Input from User
# --------------------------------------------------

text = input("\nEnter a sentence: ")


# --------------------------------------------------
# Tokenization
# --------------------------------------------------

tokens = word_tokenize(text)


# --------------------------------------------------
# Stemming
# --------------------------------------------------

stemmed_words = []

for word in tokens:
    stemmed_word = stemmer.stem(word)
    stemmed_words.append(stemmed_word)


# --------------------------------------------------
# Lemmatization
# --------------------------------------------------

lemmatized_words = []

for word in tokens:
    lemmatized_word = lemmatizer.lemmatize(word)
    lemmatized_words.append(lemmatized_word)


# --------------------------------------------------
# Display Results
# --------------------------------------------------

print("\n" + "=" * 50)
print("TEXT PREPROCESSING RESULTS")
print("=" * 50)

print("\nOriginal Text:")
print(text)

print("\nTokens:")
print(tokens)

print("\nStemmed Words:")
print(stemmed_words)

print("\nLemmatized Words:")
print(lemmatized_words)


# --------------------------------------------------
# Comparison
# --------------------------------------------------

print("\n" + "=" * 50)
print("COMPARISON")
print("=" * 50)

print(
    "Stemming reduces words to their root forms, "
    "which may not always be meaningful."
)

print(
    "Lemmatization converts words into meaningful "
    "base or dictionary forms."
)

print(
    "\nConclusion: Lemmatization generally provides "
    "more meaningful text preprocessing for sentiment analysis."
)