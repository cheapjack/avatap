#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You missed a bit!
Sweep some more!
The horses must have
been eating a lot...
"""
    yield from render1(engine, story, box, node, card, sack)
