#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Your bed looks too
comfortable...
Maybe just a quick nap.
No one will notice...
"""
    yield from render1(engine, story, box, node, card, sack)
