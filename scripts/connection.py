
from sqlalchemy import create_engine


def Sql_Engine():
    
    engine = create_engine('mysql+pymysql://root:Enjoy101$@127.0.0.1/world_x', pool_recycle='3306')

    return engine