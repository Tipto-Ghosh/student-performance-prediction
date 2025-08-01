# 🔐 Environment Setup Guide

Make sure to create a `.env` file in the **same directory** as this file to configure the environment variables required to run the project.

## Database Configuration

```
host = "localhost"
user = "mySql username"
password = "password"
databaseName = "studentPerformance" # example database name
datatable = "students" # example database table
```

## DagsHub Integration

```
dagshub_url = "https://dagshub.com/yourusername/student-performance-prediction.mlflow" # your dagshub_url
dagshub_username = "your username"
dagshub_token = "your_dagshub_token"
```

---

## 📜 Instructions

1. Copy the above content into a new file named `.env` in this same directory.
2. Replace `your_dagshub_token` with your actual token.
3. Do **not** commit the `.env` file to version control. Ensure `.gitignore` includes `.env`.
4. Keep your DagsHub token safe. Regenerate it if it gets leaked or exposed.

---
