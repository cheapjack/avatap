#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Here it is. Pretend to
SCRUB the harness.
LOOK for other CAVALRY
items in the museum,
then come back...
"""
    yield from render1(engine, story, box, node, card, sack)
