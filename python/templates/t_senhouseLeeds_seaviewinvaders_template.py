#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You can see the sea
On the horizon
you can see a sail!
"""
    yield from render1(engine, story, box, node, card, sack)
