# -*- coding: utf-8 -*-
# AWS RDS MSSQL
# @author =__Uluç Furkan Vardar__

import pyodbc

rds_host = "Your host"
name = "your db user name"
password = "your password"
db_name = "your db name"

connection = pyodbc.connect("DRIVER={SQL Server};server="+rds_host+";database="+db_name+";uid="+name+";pwd="+password)
 
def save_New(new_URL,header,resource,New_before_time,topic):
    global connection
    cur= connection.cursor()
    query="exec [Crawled News].[dbo].[createNew]@url = \""+str(new_URL)+"\" , @header = \""+conv(header)+"\", @resource =\""+conv(resource)+"\", @beforeTime =\""+conv(New_before_time)+ "\", @topic =\""+conv(topic)+"\", @webCite =\"news.google\""
    try:
        cur.execute(query.encode('utf-8'))
        connection.commit()
    except Exception as e:
        print("New Insert Error"+str(e))
    cur.close()


def create_update():
    global connection
    cur= connection.cursor()
    try:
        cur.execute("exec [Crawled News].[dbo].[createUpdateTime]; ")
        connection.commit()
    except Exception as e:
        print("Update Creation Error"+str(e))
    cur.close()