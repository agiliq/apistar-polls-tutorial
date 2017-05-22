import datetime
from apistar import http
from apistar.backends import SQLAlchemy
from .models import Poll, Choice

def welcome(name=None):
	if name is None:
		return {'message': 'Welcome to API Star, django poll example!'}
	return {'message': 'Welcome to API Star django poll example!, %s!' % name}

def create_poll(db: SQLAlchemy, question: str):
	session = db.session_class()
	poll = Poll(question=question)
	session.add(poll)
	session.commit()
	return {'question': question}

def polls(db: SQLAlchemy):
	data = []
	current_time = datetime.datetime.utcnow()
	session = db.session_class()
	polls = session.query(Poll).filter(Poll.pub_date < current_time)[:5]
	for poll in polls:
		poll_data = {}
		poll_data['question'] = poll.question
		poll_data['pub_date'] = str(poll.pub_date)
		data.append(poll_data)
	return {'polls': data}

def polls_details(db: SQLAlchemy):
	data = []
	cdata = []
	session = db.session_class()
	polls = session.query(Poll).all()
	for poll in polls:
		poll_data = {}
		poll_data['question'] = poll.question
		poll_data['pub_date'] = str(poll.pub_date)
		if poll.choice:
			for choice in poll.choice:
				choice_data = {}
				choice_data['id'] = choice.id
				choice_data['choice_text'] = choice.choice_text
				choice_data['votes'] = choice.votes
				cdata.append(choice_data)
			poll_data['choice'] = cdata
		data.append(poll_data)
	return {'polls': data}

def create_choices(db: SQLAlchemy, poll_id: int, choice_text: str):
	session = db.session_class()
	poll = session.query(Poll).get(poll_id)
	choice = Choice(poll=poll.id, choice_text=choice_text, votes=0)
	session.add(choice)
	session.commit()
	return {'choice_text': choice_text}

def vote(db: SQLAlchemy, poll_id: int, choice_id: int):
	session = db.session_class()
	poll = session.query(Poll).get(poll_id)
	for option in poll.choice:
		if option.id == choice_id:
			choice = session.query(Choice).get(choice_id)
			temp = int(choice.votes)
			temp += 1
			choice.votes = temp
			session.add(choice)
			result = 'Vote Added'
		else:
			result = 'Wrong Choice'
		session.commit()
	return {'result': result}




