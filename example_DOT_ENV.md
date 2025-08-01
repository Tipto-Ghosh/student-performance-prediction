### Make the .env file in the same location where this file is.

## Database Configuration
host = "your_database_host"             # e.g., "localhost" </br>
user = "your_database_user"             # e.g., "root" </br>
password = "your_database_password"     # e.g., "your_db_password" </br>
databaseName = "your_database_name"     # e.g., "studentPerformance" </br>
datatable = "your_table_name"           # e.g., "students" </br>

## DagsHub Integration
dagshub_url = "your_dagshub_repo_url"   # e.g., "https://dagshub.com/username/repo-name.mlflow" </br>
dagshub_username = "your_dagshub_username" </br>
dagshub_token = "your_dagshub_token" </br>


**Instructions**
1. Copy this content into a new file named .env at the root of your project directory.

2. Replace all placeholder values with your actual credentials.

3. Never commit your .env file to version control (it’s already listed in .gitignore by default).

4. Keep your dagshub_token secure and regenerate it if it gets exposed.

5. Replace all the lines that i gave here just keep `Database Configuration` and `## DagsHub Integration` with proper values.