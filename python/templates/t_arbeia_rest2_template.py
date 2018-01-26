#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You take a another rest
in your quarters and
talk to your friend
Victor. 'You look
REALLY tired!!...
"""
    yield from render1(engine, story, box, node, card, sack)
