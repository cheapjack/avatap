#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You quickly go to
your quarters to
find an empty sack.
Now go back outside
to the STABLES.
"""
    yield from render1(engine, story, box, node, card, sack)
