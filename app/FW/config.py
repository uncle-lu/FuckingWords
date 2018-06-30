#coding:utf-8

class BaseConfig:
    SECRET_KEY = "use Chinese English to code"

class DebuggingConfig(BaseConfig):
    DEBUG = True
    WTF_CSRF_ENABLED = False
    MONGODB_SETTINGS = {
            'db' : 'test',
            'host': '127.0.0.1',
            'port': 27017
            }

class ProductionConfig(BaseConfig):
    MONGODB_SETTINGS = {
            'db' : 'test',
            'host': '127.0.0.1',
            'port': 27017
            }
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = 'noonewillknowwhoIam'

config = {
        'base' : BaseConfig,
        'debug' : DebuggingConfig,
        'production' : ProductionConfig
        }