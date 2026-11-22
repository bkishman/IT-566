#!/usr/bin/env bash
# Drops and recreates the Expenses database and user
# Run from database_project:  bash database/initialize_database.sh
MYSQL="/c/MAMP/bin/mysql/bin/mysql.exe"
export MYSQL_PWD=root
cd "$(dirname "$0")/db_version_1" || exit 1

for script in drop_database.sql drop_user.sql create_database.sql create_user.sql; do
    echo "Running $script..."
    "$MYSQL" -u root < "$script" || exit 1
done
echo "Done."