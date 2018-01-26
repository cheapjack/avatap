#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """EXPLORE the BARRACKS to
LOOK for your tools and
polish. Hmm, where did
I leave them?
"""
    yield from render1(engine, story, box, node, card, sack)
