import sqlalchemy


db=sqlalchemy.engine.url.URL.create(
    drivername='postgresql',
    username='postgres',
    password='20041014',
    host='localhost',
    port=5432,
    database='autoseller'
)