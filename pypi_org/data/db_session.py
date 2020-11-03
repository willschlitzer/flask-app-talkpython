import sqlalchemy as sa
import sqlalchemy.orm as orm

from pypi_org.data.modelbase import SqlAlchemyBase

factory = None

def global_init(db_file: str):
    global factory
    if factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file")

    conn_str = 'sqlite:///' +db_file.strip()

    engine = sa.create_engine(conn_str, echo=False)

    factory = orm.sessionmaker(bind=engine)

    # no inspection
    from pypi_org.data.package import Package
    SqlAlchemyBase.metadata.create_all(engine)