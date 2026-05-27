import nltk
import string
import pandas as pd
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

df = pd.read_csv("FAQ chatbot/faqs.csv")

short_forms = {
    "ai": "artificial intelligence",
    "ml": "machine learning",
    "dl": "deep learning",
    "nlp": "natural language processing",
    "cv": "computer vision"
}

# =========================================================
# PREPROCESSING FUNCTION
# =========================================================

def preprocess_text(text):

    text = str(text).lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    # EXPAND SHORT FORMS
    expanded_words = []

    for word in words:
        if word in short_forms:
            expanded_words.extend(short_forms[word].split())
        else:
            expanded_words.append(word)

    # =====================================================
    # SPELLING CORRECTION
    # =====================================================

    corrected_words = []

    technical_words = [
        "artificial",
        "intelligence",
        "machine",
        "learning",
        "deep",
        "python",
        "natural",
        "language",
        "processing",
        "computer",
        "vision",
        "chatbot"
    ]

    for word in expanded_words:
        if word in technical_words:
            corrected_words.append(word)
        else:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)

    # Join words
    text = " ".join(corrected_words)

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))

    filtered_tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    return " ".join(filtered_tokens)

# =========================================================
# PREPROCESS FAQ QUESTIONS
# =========================================================

df["Processed_Question"] = df["Question"].apply(preprocess_text)

# =========================================================
# TF-IDF VECTORIZATION
# =========================================================

vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(df["Processed_Question"])

# =========================================================
# CHATBOT RESPONSE FUNCTION
# =========================================================

def chatbot_response(user_input):

    # Preprocess user input
    cleaned_input = preprocess_text(user_input)

    # Convert to vector
    user_vector = vectorizer.transform([cleaned_input])

    # Similarity
    similarity_scores = cosine_similarity(user_vector, faq_vectors)

    # Best match
    best_match_index = similarity_scores.argmax()

    best_score = similarity_scores[0][best_match_index]

    print(f"\n[Similarity Score: {best_score:.2f}]")

    # Threshold
    if best_score < 0.10:
        return "Sorry, I could not understand your question."

    return df.iloc[best_match_index]["Answer"]

# =========================================================
# CHATBOT INTERACTION
# =========================================================

print("==============================================")
print("        WELCOME TO AI FAQ CHATBOT")
print("==============================================")
print("Ask questions related to:")
print("- Artificial Intelligence")
print("- Machine Learning")
print("- Deep Learning")
print("- NLP")
print("- Data Science")
print("- Python")
print("Type 'exit' anytime to quit.")
print("==============================================\n")

while True:

    user_question = input("You: ")

    if user_question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = chatbot_response(user_question)

    print("Chatbot:", response, "\n")