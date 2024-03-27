from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
import pickle
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')

# Loading models
clf = pickle.load(open('clf.pkl', 'rb'))
tfidfd = pickle.load(open('tfidf.pkl', 'rb'))

def clean_resume(resume_text):
    clean_text = re.sub('http\S+\s*', ' ', resume_text)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+', '', clean_text)
    clean_text = re.sub('@\S+', '  ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)
    return clean_text

# Initialize Flask app
app = Flask(__name__)

# Set up basic authentication
app.config['BASIC_AUTH_USERNAME'] = 'username'  # Set your desired username
app.config['BASIC_AUTH_PASSWORD'] = 'password'  # Set your desired password
basic_auth = BasicAuth(app)

@app.route('/', methods=['GET'])
def home_page():
    return "Welcome to Resume Screening API!"

@app.route('/home', methods=['POST'])
@basic_auth.required  # Require authentication for this route
def predict_job_title():
    # Get resume data from the request
    resume_text = request.json.get('resume_text', '')

    # Clean the resume text
    cleaned_resume = clean_resume(resume_text)

    # Transform the cleaned resume text
    input_features = tfidfd.transform([cleaned_resume])

    # Predict job title
    prediction_id = clf.predict(input_features)[0]

    # Map category ID to category name
    category_mapping = {
        15: "Java Developer",
        23: "Testing",
        8: "DevOps Engineer",
        20: "Python Developer",
        24: "Web Designing",
        12: "HR",
        13: "Hadoop",
        3: "Blockchain",
        10: "ETL Developer",
        18: "Operations Manager",
        6: "Data Science",
        22: "Sales",
        16: "Mechanical Engineer",
        1: "Arts",
        7: "Database",
        11: "Electrical Engineering",
        14: "Health and fitness",
        19: "PMO",
        4: "Business Analyst",
        9: "DotNet Developer",
        2: "Automation Testing",
        17: "Network Security Engineer",
        21: "SAP Developer",
        5: "Civil Engineer",
        0: "Advocate",
    }

    category_name = category_mapping.get(prediction_id, "Unknown")

    # Return the predicted job title as JSON
    return jsonify({'predicted_job_title': category_name})

if __name__ == "__main__":
    app.run(debug=True)
