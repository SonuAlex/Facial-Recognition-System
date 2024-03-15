import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://facerecognitiondatabase-4bf2d-default-rtdb.asia-southeast1.firebasedatabase.app/'
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