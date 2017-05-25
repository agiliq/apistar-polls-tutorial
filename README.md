# API Star's Poll Tutorial

This tutorial is meant for those, who have basic knowledge of Django and have done Django Poll tutorial.

**Refer:** https://docs.djangoproject.com/en/1.11/intro/tutorial01/

**Note:** Use Python 3+ for whole tutorial.

**Apistar:** https://github.com/tomchristie/apistar
 
---
# Features

Why should you consider using API Star for your next Web API project?

* **API documentation** - Interactive API documentation, that's guaranteed to always
be in sync with your codebase.
* **Client libraries** - JavaScript and Python client libraries, driven by the schemas that API Star generates.
* **Schema generation** - Support for generating Swagger or RAML API schemas.
* **Expressive** - Type annotated views, that make for expressive, testable code.
* **Performance** - Dynamic behavior for determining how to run each view makes API Star incredibly efficient.

---

# Table of Contents

- [Apistar Installation](#apistar)
- [Create new Project](#newproject)
- [Apistar Architecture](#apistar_architecture)
- [Run Project](#runproject)
- [Database configuration](#database)
- [First Poll](#firstpoll)

# Apistar Installation

    $ pip3 install apistar

If its not working, then check your python version. It works with Python 3 and higher.

Check Installation:

    $ apistar --version
    0.1.17

# Create new project

    $ mkdir apistar_demo
    $ cd apistar_demo
    $ apistar new .

This will create a new project directory in your current working directory.
The directory looks like:

![ScreenShot](https://raw.githubusercontent.com/agiliq/apistar-polls-tutorial/master/screenshots/dir.png)

# Apistar Architecture

You get few files when you start a new project using Apistar namely:

**app.py:** Present in the same directory as of your project, you need to write all settings related stuff here.

**routes.py:** Similar to urls.py in django we have routes in Apistar, any request coming to the application goes via., routes.

**views.py:** All the logical implementation is being done in this file. 

**test_app.py:** Apistar comes well equipped with the TDD (Test Driven Development)

**Note** We will be creating some new files as per our requirement further. Like models.py for db related stuff.

# Run Project

    $ apistar run
    Starting up...
    * Running on http://localhost:8080/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 325-680-236

![ScreenShot](https://raw.githubusercontent.com/agiliq/apistar-polls-tutorial/master/screenshots/screen1.png)

For running project in different port and host use
    
    $ apistar run --port <someport> --host <somehost>
    
# Database Configuration

For doing database related stuff, you need to install sqlalchemy.

    $ pip install sqlalchemy

We will be using, SQLite for our tutorial, though apistar supports postgres and MySQL as well.

Step 1: Create a new file in your project directory and name it as models.py and paste the code present below:
    
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

Step 2: In your app.py file paste the code to configure your database as below:

    from apistar import App
    from project.routes import routes
    from project.models import Base

    settings = {
        "DATABASE": {
    	    "URL": "sqlite:///db.sqlite3",
                "METADATA": Base.metadata
        }
    }
    app = App(routes=routes, settings=settings)
    
Step 3: Now that you have written all the code for your database, execute the command from your terminal.

    $ apistar create_tables
    Tables created
    

# First Poll

Now that you have done your database configuration , the time comes to create your first poll. As we are not using django which gives us the flexibility of Django Admin so we depend on creating an endpoint for creating a Poll.

We will be dealing with routes and views.

**Views**

For creating first poll, add the code snnipet in views.py

    from apistar.backends import SQLAlchemy
    from .models import Poll, Choice
    
    def create_poll(db: SQLAlchemy, question: str):
	    session = db.session_class()
	    poll = Poll(question=question)
	    session.add(poll)
	    session.commit()
	    return {'question': question}
	    
	def create_choices(db: SQLAlchemy, poll_id: int, choice_text: str):
	    session = db.session_class()
	    poll = session.query(Poll).get(poll_id)
	    choice = Choice(poll=poll.id, choice_text=choice_text, votes=0)
	    session.add(choice)
	    session.commit()
	    return {'choice_text': choice_text}

**Routes**

For providing the route for the function, first we call the create_poll in routes.py and create a route related to  as shown in the snnipet below

    from apistar import Include, Route
    from project.views import  create_poll, create_choices
    
    routes = [
        # API to create Polls
        Route('/create_poll', 'POST', create_poll)
        # API to add choices to the polls
        Route('/create_choices', 'POST', create_choices),
        ]

**Run Code**

    $ apistar run

You may use any REST client to test the API, created here.

![ScreenShot](https://raw.githubusercontent.com/agiliq/apistar-polls-tutorial/master/screenshots/screen2.png)


With every poll you create, you need to add choices with respect to it.

![ScreenShot](https://raw.githubusercontent.com/agiliq/apistar-polls-tutorial/master/screenshots/screen3.png)



    


     


    
