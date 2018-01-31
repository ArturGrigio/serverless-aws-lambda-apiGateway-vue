import sys
import logging
import rds_config
import pymysql
import json

#rds settings
rds_host  = rds_config.db_endpoint
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name


logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=3)
    logger.info("\nSUCCSESS: Connection Established")
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")

def handler(event, context):

    add_employee = ("INSERT INTO employees (first, last, email) VALUES (%s, %s, %s)")

    data_employee = ('Geert', 'Vanderkelen', 'asdfasdfasf@asdfasf.com')

    emp_no = None
    # Insert new employee
    with conn.cursor() as cur:
        cur.execute(add_employee, data_employee)
        emp_no = cur.lastrowid

    return emp_no
