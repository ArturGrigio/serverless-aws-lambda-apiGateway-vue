#!/bin/bash

# For Get
zip -X9r ./lambda_functions/get_employees/get.zip ./rds_config.py ./pymysql
zip -uj ./lambda_functions/get_employees/get.zip ./lambda_functions/get_employees/app.py

# For Delete
zip -X9r ./lambda_functions/delete_employee/delete.zip ./rds_config.py ./pymysql
zip -uj ./lambda_functions/delete_employee/delete.zip ./lambda_functions/delete_employee/app.py

# For Add
zip -X9r ./lambda_functions/add_employee/add.zip ./rds_config.py ./pymysql
zip -uj ./lambda_functions/add_employee/add.zip ./lambda_functions/add_employee/app.py

# For Update
zip -X9r ./lambda_functions/update_employee/update.zip ./rds_config.py ./pymysql
zip -uj ./lambda_functions/update_employee/update.zip ./lambda_functions/update_employee/app.py
