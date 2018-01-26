#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Keep going, you'll
need a lot more
than one bucket!
...
"""
    yield from render1(engine, story, box, node, card, sack)
