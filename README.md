# 🏎️ Formula 1 Database Assignment

A MySQL database project analyzing historical Formula 1 racing data including drivers, teams, races, and lap times.

## 📋 Overview

This project is part of a Database Systems course (Semester A 2025/2026) that explores SQL queries using Formula 1 data provided by the course. The assignment consists of setting up a MySQL database and writing Python scripts to execute various SQL queries.

## 🗄️ Database Schema

The database `f1_data` contains the following tables loaded from the `CSV Files` directory:

### drivers_updated.csv (1,661 rows)
- **Pos** - Position/ranking
- **Driver** - Driver name
- **Nationality** - Driver nationality code
- **Car** - Team/car name
- **PTS** - Points earned
- **year** - Season year
- **Code** - Driver code

### teams_updated.csv (695 rows)
- **Pos** - Position/ranking
- **Car** - Team/car name
- **PTS** - Points earned
- **year** - Season year

### winners.csv (1,110 rows)
- **Grand Prix** - Race name
- **Date** - Race date
- **Winner** - Winner name
- **Car** - Team/car name
- **Laps** - Number of laps
- **Time** - Race time
- **Name Code** - Race code

### fastest_laps_updated.csv (1,108 rows)
- **Grand Prix** - Race name
- **Driver** - Driver name
- **Car** - Team/car name
- **Time** - Lap time
- **year** - Season year
- **Code** - Race code

## 🛠️ Setup

### Prerequisites
- Docker
- MySQL Workbench
- Python 3.x
- MySQL Connector/Python package

### Installation
1. Download CSV files from course materials (Lemida)
2. Create schema named `f1_data` in MySQL Workbench
3. Import all CSV files from the `CSV Files` directory into the schema:
   - `drivers_updated.csv`
   - `teams_updated.csv`
   - `winners.csv`
   - `fastest_laps_updated.csv`


## 🐍 Python Files

Each query is implemented as a standalone Python file:

| File | Description |
|------|-------------|
| `q1.py` | 🇧🇷 List all Brazilian Formula 1 drivers |
| `q2.py` | 🇮🇹 List all Italian Formula 1 drivers |
| `q3.py` | 🏆 Find 2000 winner with most laps and best time |
| `q4.py` | 📊 Count 2001 wins by 1999's top team |
| `q5.py` | ⚡ Average points for cars with sub-2-minute laps |
| `q6.py` | 🔄 Find Grand Prix pairs with matching lap counts (80+) |
| `q7.py` | 🏁 Drivers who won for Ferrari or are from Argentina |
| `q8.py` | 📈 Point difference between Ferrari and Maserati |
| `q9.py` | 🌍 Statistics by driver nationality (avg points, fastest lap, latest win) |

## 🚀 Running the Queries

Execute any query using:
```bash
python q1.py
```

## 💡 Key SQL Concepts Used

- ✅ **SELECT DISTINCT** - Remove duplicates
- 🔗 **JOIN** - Combine data from multiple tables
- 📦 **GROUP BY** - Aggregate data
- 🎯 **HAVING** - Filter aggregated results
- 📝 **WITH (CTE)** - Common Table Expressions for complex queries
- 🔀 **UNION** - Combine result sets
- 📅 **YEAR()** - Extract year from dates
- ⏱️ **Time functions** - Parse and compare lap times


## 🎓 Learning Objectives

- Understanding SQL query construction
- Working with relational databases
- Joining multiple tables
- Aggregating and filtering data
- Using Common Table Expressions (CTEs)
- Connecting Python to MySQL databases

---

*Homework Assignment #1 - Database Systems, Semester A 2025/2026*
