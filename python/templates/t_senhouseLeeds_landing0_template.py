#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You must WATCH for
attacks & hacks from
the sea & internet!
"""
    yield from render1(engine, story, box, node, card, sack)
