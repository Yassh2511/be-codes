# Import necessary libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# Input text
text = """Text preprocessing is an essential step in Natural Language Processing.
It involves cleaning and preparing raw text for further analysis."""

# Step 1: Tokenization
tokens = word_tokenize(text)
print("Tokens:")
print(tokens)
print("\n")

# Step 2: Stopword Removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words and word.isalpha()]
print("After Stopword Removal:")
print(filtered_tokens)
print("\n")

# Step 3: Stemming
ps = PorterStemmer()
stemmed_words = [ps.stem(word) for word in filtered_tokens]
print("After Stemming:")
print(stemmed_words)
