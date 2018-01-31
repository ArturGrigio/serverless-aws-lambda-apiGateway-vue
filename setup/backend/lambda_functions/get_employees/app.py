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

    output = []

    with conn.cursor() as cur:
        cur.execute("select * from `serverless`.`employees` limit 100")
        for row in cur:
            employee_dict = {
                'id' : row[0],
                'first' : row[1],
                'last' : row[2],
                'email': row[3]
            }
            output.append(employee_dict)

    return output
