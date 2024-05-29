from sqlalchemy import String, Boolean, Integer, Column, text, TIMESTAMP
from .database import Base


class Product(Base):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(String)
    at_sale = Column(Boolean, server_default=text('false'))
    inventory = Column(Integer, server_default=text('0'), nullable=False)
    created_at = Column(TIMESTAMP, server_default=text('Now()'))
    updated_at = Column(TIMESTAMP, server_default=text('Now()'), onupdate=text('Now()'))