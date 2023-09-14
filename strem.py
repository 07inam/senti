
import pickle
import streamlit as st

# Load the model from the pickle file
with open("classifier.pickle", 'rb') as model_file:
    model = pickle.load(model_file)

# Define the Streamlit app
st.title('Sentiment Analysis App')

# Create a text input field for user input
review = st.text_area('Enter your review:')

# Create a button to trigger the analysis
analyze_button = st.button('Analyze')

# Function to perform sentiment analysis
def perform_sentiment_analysis(text):
    prediction = model.predict([text])
    sentiment = 'Positive' if prediction[0] == 1 else 'Negative'
    return sentiment

# Display the sentiment analysis result when the button is clicked
if analyze_button:
    if review:
        sentiment = perform_sentiment_analysis(review)
        st.write(f'Sentiment: {sentiment}')
    else:
        st.warning('Please enter a review before analyzing.')
