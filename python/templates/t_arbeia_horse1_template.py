#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You cross the courtyard.
Your master is waiting
at the barracks...
"""
    yield from render1(engine, story, box, node, card, sack)
