import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    create_engine, Column, Integer, String, Date, Float
)

Base = declarative_base()


class Clients(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    adress = Column("adress", String)
    phone = Column("phone", String)
    email = Column("email", String)
    num_rccm = Column("num_rccm", String)
    num_p_id = Column("num_p_id", Integer)
    num_id = Column("num_id", Integer)
    num_inpot = Column("num_inpot", String)
    m_total = Column("m_total", Float)
    m_payer = Column("m_payer", Float)
    date = Column("date", Date)

    def __init__(
        self,
        name,
        phone,
        email,
        adress,
        num_rccm,
        num_p_id,
        num_id,
        num_inpot,
        m_total=0,
        m_payer=0.0,
        date=datetime.date.today(),
        *args, **kwargs
    ):
        self.name = name
        self.phone = phone
        self.email = email
        self.adress = adress
        self.num_id = num_id
        self.num_rccm = num_rccm
        self.num_p_id = num_p_id
        self.num_inpot = num_inpot
        self.m_total = m_total
        self.m_payer = m_payer
        self.date = date

    @property
    def m_rest(self):
        return self.m_total - self.m_payer

    def getname(self) -> str:
        return f"{self.id } {self.name}"

    def __str__(self) -> str:
        return self.getname()

    def __repr__(self):
        return self.getname()


engine = create_engine("sqlite:///db/sample.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
