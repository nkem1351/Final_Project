import csv
from pymongo import MongoClient

class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses

    def to_dict(self):
        return {
            'age': self.age,
            'gender': self.gender,
            'total_income': self.total_income,
            'expenses': self.expenses
        }

# Fetch data from MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['survey_db']
collection = db['users']

users = []
for record in collection.find():
    user = User(
        age=record['age'],
        gender=record['gender'],
        total_income=record['total_income'],
        expenses=record['expenses']
    )
    users.append(user.to_dict())

# Save to CSV
with open('user_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['age', 'gender', 'total_income', 'expenses']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for user in users:
        writer.writerow(user)