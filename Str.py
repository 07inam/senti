{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "25ed491f-de0b-4974-ae7d-6eff94d04860",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "import streamlit as st\n",
    "\n",
    "# Load the model from the pickle file\n",
    "with open("classifier1.pickle", 'rb') as model_file:\n",
    "    model = pickle.load(model_file)\n",
    "\n",
    "# Define the Streamlit app\n",
    "st.title('Sentiment Analysis App')\n",
    "\n",
    "# Create a text input field for user input\n",
    "review = st.text_area('Enter your review:')\n",
    "\n",
    "# Create a button to trigger the analysis\n",
    "analyze_button = st.button('Analyze')\n",
    "\n",
    "# Function to perform sentiment analysis\n",
    "def perform_sentiment_analysis(text):\n",
    "    prediction = model.predict([text])\n",
    "    sentiment = 'Positive' if prediction[0] == 1 else 'Negative'\n",
    "    return sentiment\n",
    "\n",
    "# Display the sentiment analysis result when the button is clicked\n",
    "if analyze_button:\n",
    "    if review:\n",
    "        sentiment = perform_sentiment_analysis(review)\n",
    "        st.write(f'Sentiment: {sentiment}')\n",
    "    else:\n",
    "        st.warning('Please enter a review before analyzing.')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0534049a-6831-4472-92ae-6c6c03502a96",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
