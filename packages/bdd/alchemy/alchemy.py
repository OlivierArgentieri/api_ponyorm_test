from sqlalchemy import create_engine

#engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('postgresql+psycopg2://postgres:toor@192.168.30.131/postgres')
print("zob")