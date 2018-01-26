#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You let yourself into the
storeroom. It's dark and
musty in here. You find a
note with today's list of
jobs waiting for you.
"""
    yield from render1(engine, story, box, node, card, sack)
