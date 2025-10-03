from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.count_table import Base, CountTable

# Adapter l'URL à votre config Docker Compose
DATABASE_URL = "postgresql://postgres:postgres123@localhost:5432/coder_ia_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 1. Créer la base et la table
Base.metadata.create_all(bind=engine)

# 2. Vider la table et insérer une ligne avec count_number=0
with SessionLocal() as session:
    session.query(CountTable).delete()
    session.add(CountTable(count_number=0))
    session.commit()

print("Table initialisée avec une ligne count_number=0")
