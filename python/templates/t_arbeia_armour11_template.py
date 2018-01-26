#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Keep going, it's not
clean yet! That's it!
...
"""
    yield from render1(engine, story, box, node, card, sack)
