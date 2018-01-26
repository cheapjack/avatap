#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Now PUSH the CART inside
the barracks and pretend
to BUILD a fire in one
of the fireplaces...
"""
    yield from render1(engine, story, box, node, card, sack)
