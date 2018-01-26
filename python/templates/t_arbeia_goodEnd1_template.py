#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Your master is waiting
outside of the storeroom.
"""
    yield from render1(engine, story, box, node, card, sack)
