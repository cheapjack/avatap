#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You are a slave to
the commanding officer
at Arbeia fort. The
fort is under-staffed
& your quest is to fill
in for a sick groom....
"""
    yield from render1(engine, story, box, node, card, sack)
