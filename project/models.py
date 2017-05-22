from sqlalchemy.sql import func
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

Base = declarative_base()

class Poll(Base):
	__tablename__ = "Poll"
	id = Column(Integer, primary_key=True)
	question = Column(String)
	pub_date = Column(DateTime(timezone=True), default=func.now())
	# Gives the flexibilty to access child table's object.
	choice = relationship("Choice")

class Choice(Base):
	__tablename__ = "Choice"
	id = Column(Integer, primary_key=True)
	poll = Column(Integer, ForeignKey("Poll.id"), nullable=False)
	choice_text = Column(String)
	votes = Column(Integer)
