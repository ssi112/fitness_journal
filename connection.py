import configparser
appConfig = configparser.ConfigParser()
appConfig.read("app.ini")
DBMS = appConfig.get("CoreContext", "dbms")
USER = appConfig.get("CoreContext", "user")
PWD = appConfig.get("CoreContext", "password")
HOST = appConfig.get("CoreContext", "host")
DB = appConfig.get("CoreContext", "database")

db_connect = DBMS + USER + PWD + HOST + DB

