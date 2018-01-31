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


def handler(event, context):

    try:
        conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=3)
        logger.info("\nSUCCSESS: Connection Established")
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()


    add_employee = ("UPDATE `employees` set first = %s, last = %s, email = %s where id = %s")

    data_employee = (event['first'], event['last'], event['email'], event['id'])

    emp_no = None
    # Insert new employee
    with conn.cursor() as cur:
        ret = cur.execute(add_employee, data_employee)
        conn.commit()


    return ret
