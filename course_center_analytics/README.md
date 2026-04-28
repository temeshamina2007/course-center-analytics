# Course Center Sales Analytics

## Project Description

This project is a sales analytics system for a small educational course center.

I created this project as a practical tool for analyzing:
- student enrollments
- course popularity
- revenue by course
- monthly revenue
- payment status
- unpaid balances

The project is connected with real business needs because course centers need to understand which courses are profitable and which students still have unpaid payments.

## Technologies Used

- Python
- CSV
- JSON
- OS module
- Regular expressions
- Matplotlib
- Object-Oriented Programming
- Unit testing with pytest

## Project Structure

```text
course_center_analytics/
│
├── main.py
├── data/
│   └── enrollments.csv
├── reports/
│   ├── sales_report.json
│   └── cleaned_enrollments.csv
├── charts/
│   ├── revenue_by_course.png
│   ├── students_by_course.png
│   ├── monthly_revenue.png
│   └── payment_status.png
├── analytics/
│   ├── models.py
│   ├── data_loader.py
│   ├── analyzer.py
│   ├── visualizer.py
│   ├── validators.py
│   ├── decorators.py
│   └── report.py
└── tests/
    └── test_analyzer.py
```
---

## Features

- Load and validate data from CSV
- Analyze total revenue, expected revenue, and debt
- Calculate average check and course popularity
- Filter and process data using lambda, map, and filter
- Generate charts using matplotlib
- Save reports in JSON and CSV formats
- Use OOP concepts like classes, inheritance, and polymorphism
- Validate emails using regular expressions
- Measure function execution time using decorators
- Read data using generators
- Test core logic with pytest

---

## Course Topics Covered

| Topic | Usage |
|------|------|
| Variables & Data Types | Prices, names, dates, status |
| Input/Output | Console menu |
| if/elif/else | Menu logic, validation |
| Logical Operators | Conditions |
| Loops (for/while) | Processing data |
| Strings | Names, emails |
| Lists | Enrollments storage |
| Tuples | Sorted results |
| Sets | Unique courses |
| Dictionaries | Statistics |
| OS Module | File/folder handling |
| File Handling | open(), read/write |
| CSV | Data input/output |
| JSON | Report saving |
| Functions | Modular logic |
| Lambda | Sorting, filtering |
| Map | Transforming data |
| Filter | Selecting data |
| Exceptions | Error handling |
| Classes & Objects | Enrollment model |
| Inheritance | Report classes |
| Polymorphism | save() method |
| Association | Analyzer uses data |
| Modules & Packages | analytics package |
| Unit Tests | tests folder |
| Decorators | Execution time |
| Generators | Reading CSV |
| Regex | Email validation |

---

## How to Run

Install requirements:

```bash
pip install -r requirements.txt
```
Run the project: python main.py
Run tests: pytest

### COURSE CENTER SALES ANALYTICS
1. Show summary
2. Show revenue by course
3. Show students by course
4. Show payment status
5. Generate charts
6. Save reports
7. Show top courses by revenue
0. Exit