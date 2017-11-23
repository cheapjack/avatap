#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """...which helps us
make more wine!
"""
    yield from render1(engine, story, box, node, card, sack)
