#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You find the wood store
next to the Barracks...
Pretend to GATHER the
wood into a CART...
"""
    yield from render1(engine, story, box, node, card, sack)
