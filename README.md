# API Star's Poll Tutorial

This tutorial is meant for those, who have basic knowledge of Django and have done Django Poll tutorial.

**Refer:** https://docs.djangoproject.com/en/1.11/intro/tutorial01/

**Note:** Use Pyhton 3+ for whole tutorial.

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


