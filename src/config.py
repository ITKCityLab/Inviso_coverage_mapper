from os import environ
#dbapi/dialect      ://username  :password    @hostname :port/database name
#'postgresql+psycopg2://inviso_adm:1234password@inviso_db:5432/inviso_adm'
INVISO_DB_CONN = environ['INVISO_DB_CONN']
