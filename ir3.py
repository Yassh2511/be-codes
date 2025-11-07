# Program: Email Spam Filtering using Text Classification (Naive Bayes)

# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Load Dataset
# You can download the dataset: https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv
# It contains 2 columns: 'label' (spam/ham) and 'message' (text)
#url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
#data = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])


data=pd.read_csv('sms.tsv',sep='\t',names=['label', 'message'])
print("Sample Data:")
print(data.head())

# Step 2: Data Preprocessing
# Convert labels to numeric (spam = 1, ham = 0)
data['label_num'] = data.label.map({'ham': 0, 'spam': 1})

# Step 3: Split Data
X_train, X_test, y_train, y_test = train_test_split(
    data['message'], data['label_num'], test_size=0.25, random_state=42
)

# Step 4: Convert Text to Feature Vectors
vectorizer = CountVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Step 5: Train Naive Bayes Model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Step 6: Predict on Test Set
y_pred = model.predict(X_test_vec)


# Step 7: Test on New Emails
sample_emails = [
    "Congratulations! You have won a $1000 Walmart gift card. Click here to claim now!",
    "Hey, are we still meeting for lunch today?",
    "Your Amazon order has been shipped successfully."
]

sample_vec = vectorizer.transform(sample_emails)
predictions = model.predict(sample_vec)

print("\n🔍 Sample Email Predictions:")
for email, label in zip(sample_emails, predictions):
    print(f"Email: {email}\n→ {'SPAM' if label == 1 else 'HAM'}\n")
