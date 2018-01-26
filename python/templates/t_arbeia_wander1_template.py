#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You walk around your
quarters for a while.
Kicking an old barrel,
you see something
glinting. What is it?
...
"""
    yield from render1(engine, story, box, node, card, sack)
