#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Glass beads! Those
will be perfect for
covering the harness!
"""
    yield from render1(engine, story, box, node, card, sack)
