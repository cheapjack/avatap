#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Here they are...
Pretend to HAMMER the
dents out of the
armour. Then POLISH
the metal...
"""
    yield from render1(engine, story, box, node, card, sack)
