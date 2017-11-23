#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """We must fight off the
invaders and prepare
to defend the coastal
outpost!
"""
    yield from render1(engine, story, box, node, card, sack)
