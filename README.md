# 🏎️ Formula 1 Data Engineering Pipeline

This project builds an **end-to-end data pipeline** for Formula 1 data using the [Ergast API](http://ergast.com/mrd/).  
The goal is to ingest, transform, and visualize F1 data in a modern analytics stack.

This is completely open source and free to run!!

## 📂 Current Progress
- ✅ Week 1: Setup repo, environment, and first ingestion scripts (SQLite)
- ⬜ Week 2: Add orchestration (Airflow / GitHub Actions)
- ⬜ Week 3: Add DBT transformations
- ⬜ Week 4: Streamlit dashboard
- ⬜ Week 5: CI/CD workflows
- ⬜ Week 6: Enhancements & polish

## 🛠️ Tech Stack
- Python (requests, pandas, sqlalchemy)
- SQLite (local database for raw data)
- Ergast API (F1 data source)

## 🔧 Local Setup
1. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
