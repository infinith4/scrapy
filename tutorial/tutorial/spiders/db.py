from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import configparser

cfg = configparser.ConfigParser()
cfg.read('settings.cfg')

url = 'mysql+pymysql://{0}:{1}@{2}/infbot_db?charset=utf8'.format(cfg['mysql']['user'], cfg['mysql']['password'], cfg['mysql']['host'])
engine = create_engine(url, echo=True)
metadata = MetaData()
metadata.bind = engine

# menuテーブルの定義
dmoz = Table(
  'dmoz', metadata,
  Column('id', Integer, primary_key=True),
  Column('title', String),
  Column('link', String)
)
