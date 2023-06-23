class SystemConfig:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db-name}?charset=utf8'.format(**{
        'user': 'flaskuser',
        'password': 'flaskpass',
        'host': 'localhost',
        'db-name': 'flasktest'
    })

Config = SystemConfig