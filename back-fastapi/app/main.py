from fastapi import FastAPI
import uvicorn  # Asynchronous ASGI web server and framework for building APIs with Python 3.6+ based on standard Python type hints
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.count_table import CountTable
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pour développement, à restreindre en prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Adapter l'URL à votre config Docker Compose
DATABASE_URL = "postgresql://postgres:postgres123@db:5432/coder_ia_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/count")
def get_count():
    with SessionLocal() as session:
        count_row = session.query(CountTable).first()
        if count_row:
            return {"count_number": count_row.count_number}
        else:
            return {"count_number": None}


@app.post("/count/increment")
def increment_count():
    with SessionLocal() as session:
        count_row = session.query(CountTable).first()
        if count_row:
            count_row.count_number += 1
            session.commit()
            return {"count_number": count_row.count_number}
        else:
            # Si aucune ligne n'existe, on en crée une à 1
            new_row = CountTable(count_number=1)
            session.add(new_row)
            session.commit()
            return {"count_number": new_row.count_number}

# Nouveau endpoint pour reset le compteur
@app.post("/count/reset")
def reset_count():
    with SessionLocal() as session:
        count_row = session.query(CountTable).first()
        if count_row:
            count_row.count_number = 0
            session.commit()
            return {"count_number": count_row.count_number}
        else:
            new_row = CountTable(count_number=0)
            session.add(new_row)
            session.commit()
            return {"count_number": new_row.count_number}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)