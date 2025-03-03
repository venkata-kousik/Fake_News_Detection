<b>1.Overview</b>
Misinformation spreads rapidly in today's digital landscape, making fake news detection a critical challenge. This project uses Machine Learning (ML) and Natural Language Processing (NLP) techniques to build a classifier that distinguishes between real and fake news articles. By analyzing linguistic patterns and textual features, the model aims to reduce misinformation and enhance informed decision-making.

<b>2.Project Workflow</b>
<b>a.Exploratory Data Analysis (EDA)</b>
Analyzed the dataset to understand real vs. fake news distribution.
Used visualizations like histograms and keyword frequency analysis to detect patterns.

<b>b.Data Preprocessing</b>
Cleaned text by removing special characters, punctuation, and stop words.
Applied stemming and lemmatization to standardize text.
Converted text into numerical features using TF-IDF vectorization.

<b>c.Model Training & Evaluation</b>
Implemented Logistic Regression, Decision Tree, and Random Forest classifiers.
Evaluated models using accuracy, precision, recall, and F1-score.
Logistic Regression performed best with an accuracy of 91.47%.

<b>Web Interface (UI)</b>
Built a user-friendly web application using Streamlit.
Users can input news content, and the model predicts whether it is real or fake.

<b>3.Results</b>
Logistic Regression achieved the highest accuracy (91.47%), making it the final model for deployment.
Successfully developed a functional web app that provides real-time fake news classification.

<b>4.Limitations & Future Enhancements</b>
The model relies only on textual features, which may overlook contextual cues from metadata and images. Additionally, potential biases in the dataset could affect generalization in real-world scenarios.

<b>Future improvements include:<b>
Incorporating metadata and user engagement metrics to enhance classification accuracy.
Exploring deep learning models for better feature extraction.
Extending the dataset to include multilingual and cross-domain fake news articles.

<b>5.Installation & Usage</b>
Ensure the following dependencies installed:
pip install numpy pandas scikit-learn streamlit nltk

<b>Run the Web App:</b>
Clone the repository and execute the following command:
streamlit run app.py
