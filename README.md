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

**Note** We will be making some new files as per our requirement further. Like models.py for db related stuff.

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


    
