#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Pretend to SWEEP the
horse droppings into
a corner. HOLD YOUR NOSE
with the other hand...
"""
    yield from render1(engine, story, box, node, card, sack)
