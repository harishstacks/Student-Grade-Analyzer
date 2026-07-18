# Student-Grade-Analyzer
A Python + Pandas + SQL project analyzing student performance data — computes toppers, subject averages, and pass/fail stats using both approaches.

# 📊 Student Grade Analyzer

A beginner-friendly data analysis project that processes student performance data and extracts meaningful insights using **Pandas** and **SQL** — built to practice core data handling skills required for AI/DS and Data Analyst roles.

## 🔍 What This Project Does

- Generates/loads a dataset of 50 students with marks in 5 subjects (Math, Science, History, English, Art)
- Performs Exploratory Data Analysis (EDA) — checks data types, missing values, and summary statistics
- Calculates each student's **Total** and **Average** marks
- Identifies the **class topper** and **top 5 performers**
- Computes **subject-wise average marks**
- Determines **Pass/Fail status** per student (pass mark: 35 per subject)
- Visualizes results with bar charts and pie charts using Matplotlib
- Reproduces the **same analysis using SQL queries** (via SQLite) to demonstrate both Pandas and SQL approaches to the same problem

## 🛠️ Tech Stack

- **Python 3**
- **Pandas** – data manipulation
- **NumPy** – numerical operations
- **Matplotlib** – data visualization
- **SQLite3** – SQL querying

## 📁 Project Structure

```
student-grade-analyzer/
│
├── main.py              # Full project code
├── students.csv         # Generated dataset
└── README.md            # Project documentation
```

## 🚀 How to Run

1. Clone this repository
   ```bash
   git clone https://github.com/harishstacks/Student-Grade-Analyzer.git
   cd student-grade-analyzer
   ```

2. Install dependencies
   ```bash
   pip install pandas numpy matplotlib
   ```

3. Run the script
   ```bash
   python main.py
   ```

## 📈 Sample Output

- **Topper identification** based on total marks across all subjects
- **Subject-wise average** bar chart
- **Pass/Fail distribution** pie chart
- Console output comparing results computed via Pandas vs SQL queries

## 💡 Key Learnings

- Row-wise vs column-wise operations in Pandas (`axis=1` vs `axis=0`)
- Writing and applying custom functions across a DataFrame
- Basic EDA techniques (`.info()`, `.describe()`, `.isnull()`)
- Translating Pandas logic into equivalent SQL queries (`ORDER BY`, `GROUP BY`, `COUNT`, `AVG`)
- Data visualization fundamentals

## 🔮 Future Improvements

- Add a Streamlit web interface to upload custom CSV files
- Support dynamic subject lists instead of hardcoded columns
- Add grade classification (A/B/C/D) instead of just Pass/Fail
- Export analysis results to a PDF report

## 👤 Author

Built by M.Harish
as part of a personal learning roadmap for AI & Data Science skills.

---
⭐ If you found this useful, feel free to star the repo!
