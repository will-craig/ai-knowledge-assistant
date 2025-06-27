import os
from sqlalchemy import create_engine, Column, Integer, String, Text, text, bindparam
from sqlalchemy.orm import declarative_base, sessionmaker
from pgvector.sqlalchemy import Vector

Base = declarative_base()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class Document(Base):
    __tablename__ = "documents"
    id        = Column(Integer, primary_key=True, index=True)
    filename  = Column(String, nullable=False)
    content   = Column(Text, nullable=False)
    embedding = Column(Vector(1536), nullable=False)

def init_db():
    print("Initializing database...")
    # Open a connection in autocommit (so CREATE EXTENSION takes effect)
    with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
    # Now that the extension is in place, create your tables
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully.")


def search_similar_documents(session, query_embedding, top_k=5):
    sql = build_query_search()
    sql = sql.bindparams(
        bindparam("query_embedding", type_=Vector(1536)),
        bindparam("top_k", type_=Integer),
    )

    result = session.execute(sql, {
        "query_embedding": query_embedding,
        "top_k": top_k
    })
    return result.fetchall()

def build_query_search():
    sql = text("""
        SELECT id, filename, content,
               1 - (embedding <#> :query_embedding) AS score
        FROM documents
        ORDER BY embedding <#> :query_embedding
        LIMIT :top_k
    """)
      
    return sql