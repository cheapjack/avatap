#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You let yourself back
into the storeroom.
It's still dark and musty
in here (and there are
spiders). You find a new
list of jobs to complete.
"""
    yield from render1(engine, story, box, node, card, sack)
