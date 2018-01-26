#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """He rides off to the
West, whilst you go
back to your quarters
to count your pay.
"""
    yield from render1(engine, story, box, node, card, sack)
