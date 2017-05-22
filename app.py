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
