#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        if node.change.triggered:
            yield """You bravely hold back
the invaders! CHARGE
down the coastal path!
You kill the fleeing
celts & take a horse
"""
        else:
            yield """You HOLD back the hordes
best you can but are
driven back! the coastal
path may be over run!
"""
        yield """
"""
    yield from render1(engine, story, box, node, card, sack)
