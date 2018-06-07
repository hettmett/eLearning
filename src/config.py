import configparser


conf = configparser.ConfigParser()
conf.read('config.ini', encoding='utf-8')

sys_conf = dict(conf.items('system'))
db_conf = dict(conf.items('database'))
sec_conf = dict(conf.items('security'))