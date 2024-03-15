import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Retrieve the Firebase project ID from GitHub Secrets
project_id = os.environ.get('FIREBASE_PROJECT_ID')

# Retrieve the Firebase private key from GitHub Secrets
private_key = os.environ.get('FIREBASE_PRIVATE_KEY')

# Retrieve the Firebase client email from GitHub Secrets
client_email = os.environ.get('FIREBASE_CLIENT_EMAIL')

# Retireve the Firebase Real Time Database URL from GitHub Secrets
databaseURL = os.environ.get('FIREBASE_RL_DB_URL')

# Construct the credentials dictionary
cred_dict = {
    "type": "service_account",
    "project_id": project_id,
    "private_key": private_key.replace('\\n', '\n'),  # Replace escaped newlines
    "client_email": client_email
}

# Initialize Firebase app with credentials
cred = credentials.Certificate(cred_dict)
firebase_admin.initialize_app(cred, {
    'databaseURL' : databaseURL
})

ref = db.reference('Students')

data = {
    '21BCE10221' : {
            'name' : 'Sonu Alex Antony',
            'Major' : 'CSE Core',
            'starting_year' : 2021,
            'total_attendance' : 6,
            'standing' : 'G',
            'year' : 3,
            'last_attendance_time' : '2024-03-15 10:45:20'
    }
}

for key, value in data.items():
    ref.child(key).set(value)