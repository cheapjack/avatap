#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You walk back to the
stores. Aren't your feet
getting tired yet?
You need to find the
scrubbing brush...
"""
    yield from render1(engine, story, box, node, card, sack)
