{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "25ed491f-de0b-4974-ae7d-6eff94d04860",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2023-09-14 13:52:25.002 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\91812\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import pickle\n",
    "import streamlit as st\n",
    "\n",
    "# Load the model from the pickle file\n",
    "with open(r\"C:\\Users\\91812\\Desktop\\Test jupyter\\lr.pickle\", 'rb') as model_file:\n",
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
   "execution_count": 5,
   "id": "37c80659-55b1-45e9-a3f2-f103186638de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting streamlit\n",
      "  Obtaining dependency information for streamlit from https://files.pythonhosted.org/packages/50/28/fdfe9711d553cfaf217cafc9b8ba21479c663b6504cc96652465b153e04b/streamlit-1.26.0-py2.py3-none-any.whl.metadata\n",
      "  Using cached streamlit-1.26.0-py2.py3-none-any.whl.metadata (8.0 kB)\n",
      "Collecting altair<6,>=4.0 (from streamlit)\n",
      "  Obtaining dependency information for altair<6,>=4.0 from https://files.pythonhosted.org/packages/f2/b4/02a0221bd1da91f6e6acdf0525528db24b4b326a670a9048da474dfe0667/altair-5.1.1-py3-none-any.whl.metadata\n",
      "  Using cached altair-5.1.1-py3-none-any.whl.metadata (8.6 kB)\n",
      "Collecting blinker<2,>=1.0.0 (from streamlit)\n",
      "  Using cached blinker-1.6.2-py3-none-any.whl (13 kB)\n",
      "Collecting cachetools<6,>=4.0 (from streamlit)\n",
      "  Obtaining dependency information for cachetools<6,>=4.0 from https://files.pythonhosted.org/packages/a9/c9/c8a7710f2cedcb1db9224fdd4d8307c9e48cbddc46c18b515fefc0f1abbe/cachetools-5.3.1-py3-none-any.whl.metadata\n",
      "  Using cached cachetools-5.3.1-py3-none-any.whl.metadata (5.2 kB)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Collecting importlib-metadata<7,>=1.4 (from streamlit)\n",
      "  Obtaining dependency information for importlib-metadata<7,>=1.4 from https://files.pythonhosted.org/packages/cc/37/db7ba97e676af155f5fcb1a35466f446eadc9104e25b83366e8088c9c926/importlib_metadata-6.8.0-py3-none-any.whl.metadata\n",
      "  Using cached importlib_metadata-6.8.0-py3-none-any.whl.metadata (5.1 kB)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (1.25.2)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (23.1)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (2.1.0)\n",
      "Requirement already satisfied: pillow<10,>=7.1.0 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (9.5.0)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (4.24.3)\n",
      "Requirement already satisfied: pyarrow>=6.0 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (13.0.0)\n",
      "Requirement already satisfied: pympler<2,>=0.9 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (1.0.1)\n",
      "Requirement already satisfied: python-dateutil<3,>=2.7.3 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: requests<3,>=2.18 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (2.31.0)\n",
      "Collecting rich<14,>=10.14.0 (from streamlit)\n",
      "  Obtaining dependency information for rich<14,>=10.14.0 from https://files.pythonhosted.org/packages/8d/5f/21a93b2ec205f4b79853ff6e838e3c99064d5dbe85ec6b05967506f14af0/rich-13.5.2-py3-none-any.whl.metadata\n",
      "  Using cached rich-13.5.2-py3-none-any.whl.metadata (18 kB)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (8.2.3)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.1.0 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (4.7.1)\n",
      "Collecting tzlocal<5,>=1.1 (from streamlit)\n",
      "  Obtaining dependency information for tzlocal<5,>=1.1 from https://files.pythonhosted.org/packages/55/a6/a75af44665e5e77e52f6789eef4f8bc056c8e039d96c804b975806942580/tzlocal-4.3.1-py3-none-any.whl.metadata\n",
      "  Using cached tzlocal-4.3.1-py3-none-any.whl.metadata (14 kB)\n",
      "Requirement already satisfied: validators<1,>=0.2 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (0.22.0)\n",
      "Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)\n",
      "  Obtaining dependency information for gitpython!=3.1.19,<4,>=3.0.7 from https://files.pythonhosted.org/packages/f9/94/1877b88fa3a0a30bedb43757a14f548c3b2719c8d83c16012f89564c0f3b/GitPython-3.1.36-py3-none-any.whl.metadata\n",
      "  Using cached GitPython-3.1.36-py3-none-any.whl.metadata (12 kB)\n",
      "Collecting pydeck<1,>=0.8 (from streamlit)\n",
      "  Using cached pydeck-0.8.0-py2.py3-none-any.whl (4.7 MB)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (6.3.3)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (3.0.0)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.19.0)\n",
      "Requirement already satisfied: toolz in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
      "  Using cached gitdb-4.0.10-py3-none-any.whl (62 kB)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from importlib-metadata<7,>=1.4->streamlit) (3.16.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from python-dateutil<3,>=2.7.3->streamlit) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from requests<3,>=2.18->streamlit) (3.2.0)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from requests<3,>=2.18->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from requests<3,>=2.18->streamlit) (2.0.4)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from requests<3,>=2.18->streamlit) (2023.7.22)\n",
      "Collecting markdown-it-py>=2.2.0 (from rich<14,>=10.14.0->streamlit)\n",
      "  Obtaining dependency information for markdown-it-py>=2.2.0 from https://files.pythonhosted.org/packages/42/d7/1ec15b46af6af88f19b8e5ffea08fa375d433c998b8a7639e76935c14f1f/markdown_it_py-3.0.0-py3-none-any.whl.metadata\n",
      "  Using cached markdown_it_py-3.0.0-py3-none-any.whl.metadata (6.9 kB)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.16.1)\n",
      "Requirement already satisfied: pytz-deprecation-shim in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from tzlocal<5,>=1.1->streamlit) (0.1.0.post0)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.0)\n",
      "Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit)\n",
      "  Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)\n",
      "Using cached streamlit-1.26.0-py2.py3-none-any.whl (8.1 MB)\n",
      "Using cached altair-5.1.1-py3-none-any.whl (520 kB)\n",
      "Using cached cachetools-5.3.1-py3-none-any.whl (9.3 kB)\n",
      "Using cached GitPython-3.1.36-py3-none-any.whl (189 kB)\n",
      "Using cached importlib_metadata-6.8.0-py3-none-any.whl (22 kB)\n",
      "Using cached rich-13.5.2-py3-none-any.whl (239 kB)\n",
      "Using cached tzlocal-4.3.1-py3-none-any.whl (20 kB)\n",
      "Using cached markdown_it_py-3.0.0-py3-none-any.whl (87 kB)\n",
      "Installing collected packages: mdurl, importlib-metadata, gitdb, cachetools, blinker, tzlocal, pydeck, markdown-it-py, gitpython, rich, altair, streamlit\n",
      "Successfully installed altair-5.1.1 blinker-1.6.2 cachetools-5.3.1 gitdb-4.0.10 gitpython-3.1.36 importlib-metadata-6.8.0 markdown-it-py-3.0.0 mdurl-0.1.2 pydeck-0.8.0 rich-13.5.2 streamlit-1.26.0 tzlocal-4.3.1\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: Ignoring invalid distribution -illow (c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -illow (c:\\users\\91812\\appdata\\local\\programs\\python\\python310\\lib\\site-packages)\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit\n"
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
