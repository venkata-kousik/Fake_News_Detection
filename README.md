# Fake News Detection Using Machine Learning

## 1. Overview
Misinformation spreads rapidly in today's digital landscape, making fake news detection a critical challenge. This project uses Machine Learning and Natural Language Processing techniques to build a classifier that distinguishes between real and fake news articles. By analyzing linguistic patterns and textual features, the model aims to reduce misinformation and enhance informed decision-making.

## 2. Project Workflow

### a. Exploratory Data Analysis (EDA)
- Analyzed the dataset to understand real vs. fake news distribution.
- Used visualizations like histograms and keyword frequency analysis to detect patterns.

### b. Data Preprocessing
- Cleaned text by removing special characters, punctuation, and stop words.
- Applied stemming and lemmatization to standardize text.
- Converted text into numerical features using TF-IDF vectorization.

### c. Model Training & Evaluation
- Implemented Logistic Regression, Decision Tree, and Random Forest classifiers.
- Evaluated models using accuracy, precision, recall, and F1-score.
- Logistic Regression performed best with an accuracy of 91.47%.

### d. Web Interface (UI)
- Built a user-friendly web application using Streamlit.
- Users can input news content, and the model predicts whether it is real or fake.

## 3. Results
- Logistic Regression achieved the highest accuracy (91.47%), making it the final model for deployment.
- Successfully developed a functional web app that provides real-time fake news classification.

## 4. Limitations & Future Enhancements
- The model relies only on textual features, which may overlook contextual cues from metadata and images.
- Potential biases in the dataset could affect generalization in real-world scenarios.

### Future improvements include:
- Incorporating metadata and user engagement metrics to enhance classification accuracy.
- Extending the dataset to include multilingual and cross-domain fake news articles.

## 5. Installation & Usage

### Ensure the following dependencies are installed:
pip install numpy pandas scikit-learn streamlit nltk

### Run the Web App:
Clone the repository and execute the following command:
streamlit run app.py
