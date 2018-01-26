#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """YAWN!! You wake up
MUCH later. Can you
CHECK the position
of the sun to work out
the time?
"""
    yield from render1(engine, story, box, node, card, sack)
