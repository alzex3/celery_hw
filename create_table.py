from sqlalchemy import create_engine

from api.models import Advert
from settings import PG_DSN

engine = create_engine(
    PG_DSN,
    echo=True,
    future=True)

if __name__ == '__main__':
    Advert.metadata.create_all(engine)
