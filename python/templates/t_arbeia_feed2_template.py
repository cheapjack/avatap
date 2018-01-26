#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You walk across the
courtyard again.
(Aren't your feet
getting sore?) and go
into the stables in
front of the Barracks...
"""
    yield from render1(engine, story, box, node, card, sack)
