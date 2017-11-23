#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """We must pay tribute to
the gods!
But who in your heart
do you seek favour?
"""
    yield from render1(engine, story, box, node, card, sack)
