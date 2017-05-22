from apistar import Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes
from project.views import welcome, create_poll, polls, polls_details, create_choices, vote

routes = [
	# Demo API
    Route('/', 'GET', welcome),
    # API to create Polls
    Route('/create_poll', 'POST', create_poll),
    # API to add choices to the polls
    Route('/create_choices', 'POST', create_choices),
    # API to show 5 latest polls
    Route('/polls', 'GET', polls),
    # API to show the details of polls
    Route('/polls_details', 'GET', polls_details),
    # API to cast the vote
    Route('/vote', 'POST', vote),
    # For demo purpose.
    Include('/docs', docs_routes),
    Include('/static', static_routes)
]
