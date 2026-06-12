import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("items.csv")

# User interests
user_interest = input("Enter your interests: ")

# Combine user profile with dataset
all_text = [user_interest] + data["Tags"].tolist()

# Convert text to TF-IDF vectors
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(all_text)

# Calculate similarity
similarity = cosine_similarity(vectors[0:1], vectors[1:])

# Get scores
scores = similarity.flatten()

# Add scores to dataframe
data["Score"] = scores

# Sort recommendations
recommendations = data.sort_values(by="Score", ascending=False)

print("\nRecommended Items:")
print(recommendations[["Item", "Score"]].head(5))