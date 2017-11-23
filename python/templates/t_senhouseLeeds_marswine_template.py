#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """LEAVE a cup of wine.
He also helps with
the harvest you know...
"""
    yield from render1(engine, story, box, node, card, sack)
