import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

students= []
for i in range (1, 51):
    students.append('Student_' + str(i))

subjects = ['Math', 'Science', 'History', 'English', 'Art']

data = []
for s in students:
    row = {'Name': s}
    for sub in subjects:
        row[sub] = random.randint(20,100)
    data.append(row)

df = pd.DataFrame(data)
df.to_csv('students_scores.csv', index=False)
print(df.head())

df = pd.read_csv('students_scores.csv')
df.info()
df.describe()
df.isnull().sum()

df['Total'] = df[subjects].sum(axis=1)
df['Average'] = df[subjects].mean(axis=1)
topper = df.loc[df['Total'].idxmax()]

print(f"Topper: {topper['Name']} with {topper['Total']} marks and an average of {topper['Average']:.2f}")

subject_average = df[subjects].mean()

def check_pass(row):
    return 'PASS' if all(row[sub] >= 35 for sub in subjects) else 'FAIL'
df['Result'] = df.apply(check_pass, axis=1)
print(df['Result'].value_counts())

top_5 = df.sort_values('Total', ascending=False).head(5)

subject_average.plot(kind = 'bar', color  = 'skyblue')
plt.title('Average Marks per Subject')
plt.ylabel('Average Marks')
plt.show()
df['Result'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightgreen', 'salmon'])

import sqlite3
conn = sqlite3.connect('students.db')
df.to_sql('students', conn, if_exists='replace', index=False)
query1 = "SELECT Name, Total FROM students ORDER BY Total DESC LIMIT 5"
print(pd.read_sql(query1,conn))
query2 = "SELECT Name, Average FROM students WHERE Result='FAIL' ORDER BY Average ASC"
print(pd.read_sql(query2,conn))
query3 = "SELECT Name, Total FROM students WHERE Result='PASS' ORDER BY Total DESC LIMIT 5"
print(pd.read_sql(query3,conn))