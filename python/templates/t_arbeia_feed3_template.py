#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Those horses should be
nice and full now.
Put your sack down down
and walk back to the
storeroom. You earned
"""
        yield str(node.change.plus['money'])
        yield """ Denarii
"""
    yield from render1(engine, story, box, node, card, sack)
