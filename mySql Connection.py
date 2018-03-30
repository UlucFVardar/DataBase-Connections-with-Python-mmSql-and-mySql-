# -*- coding: utf-8 -*-
# AWS RDS MySQL
# @author =__Uluç Furkan Vardar__

import pymysql

rds_host = "Your host"
name = "your db user name"
password = "your password"
db_name = "your db name"


def save_New(url, header, resource, before_time, update_id, label):
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("""call innodb.createNew("%s","%s","%s","%s",%s,"%s");""" % (
        conv(url), conv(header), conv(resource), conv(before_time), conv(update_id), conv(label)))
        conn.commit()
        cur.close()

def get_something():
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("""SELECT * From table as t ;""")
        conn.commit()
        cur.close()
        for row in cur:
            return str(row[0]) 