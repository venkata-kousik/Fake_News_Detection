import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
port_stem = PorterStemmer()
vectorization = TfidfVectorizer()

vector_form = pickle.load(open('vector.pkl', 'rb'))
load_model = pickle.load(open('model.pkl', 'rb'))

def preprocess_data(content):
    con=re.sub('[^a-zA-Z]', ' ', content) # Removing special characters, punctuation, and numbers
    con=con.lower()
    word_tokens=word_tokenize(con) #Tokenization
    stemmed_tokens=[port_stem.stem(word) for word in word_tokens if not word in stopwords.words('english')] #Stemming and stop words removal
    stemmed_sentence=' '.join(stemmed_tokens)
    return stemmed_sentence


def news_prediction(news):
    news=preprocess_data(news)
    input_data=[news]
    vector_form_transformed=vector_form.transform(input_data)
    prediction = load_model.predict(vector_form_transformed)
    return prediction


if __name__ == '__main__':
    st.title('Fake News Classifier')
    st.subheader("Input the News content below")
    sentence = st.text_area("Enter your news content here", "",height=200)
    predict_btt = st.button("predict")
    if predict_btt:
        prediction_class=news_prediction(sentence)
        print(prediction_class)
        if prediction_class == [1]:
            st.warning('It is fake news')
        if prediction_class == [0]:
            st.success('It is real news')