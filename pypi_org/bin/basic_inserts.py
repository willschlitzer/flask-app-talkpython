import os
import pypi_org
import pypi_org.data.db_session as db_session
from pypi_org.data.package import Package
from pypi_org.data.releases import Release

def main():
    init_db()
    while True:
        insert_a_package()

def insert_a_package():
    p = Package()
    p.id = input("Package id/name: ").strip().lower()
    p.summary = input("Package summary: ").strip()
    p.author = input("Author: ").strip()
    p.license = input("License: ").strip()

    print("Release 1")
    r = Release()
    r.major_ver = int(input("Major version: "))
    r.minor_ver = int(input("Minor version: "))
    r.build_ver = int(input("Build version: "))
    r.size = int(input("Size in bytes: "))

    print("Release 2")
    r = Release()
    r.major_ver = int(input("Major version: "))
    r.minor_ver = int(input("Minor version: "))
    r.build_ver = int(input("Build version: "))
    r.size = int(input("Size in bytes: "))

    import sqlalchemy.orm
    session: sqlalchemy.orm.Session = db_session.factory()

    session.add(p)


    session.commit()

def init_db():
    top_folder = os.path.dirname(__file__)
    rel_file = os.path.join("..", 'db', 'pypi.sqlite')
    db_file = os.path.join(top_folder, rel_file)
    db_session.global_init(db_file)


if __name__ == "__main__":
    main()