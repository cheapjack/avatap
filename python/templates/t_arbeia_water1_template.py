#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You walk across the
courtyard in the rain.
Pretend to FETCH the
water from the well
into a BUCKET...
"""
    yield from render1(engine, story, box, node, card, sack)
