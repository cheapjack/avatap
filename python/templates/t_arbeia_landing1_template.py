#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You've even been promised
Denarii for each task!
Even though earning money
is normally out of the
question for slaves...
"""
    yield from render1(engine, story, box, node, card, sack)
