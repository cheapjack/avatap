#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Welcome to Milecastles!
Look for numbered boxes
and hold your tag to
progress the story...
"""
    yield from render1(engine, story, box, node, card, sack)
