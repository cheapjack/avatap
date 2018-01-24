#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You bravely HOLD back
the invaders charging
up the coastalpath
but are forced back!
"""
    yield from render1(engine, story, box, node, card, sack)
