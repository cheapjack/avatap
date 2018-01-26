#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """It's still musty in
the storeroom.
Was that a rat?
You're a bit tired,
but can't quite finish
work yet...
"""
    yield from render1(engine, story, box, node, card, sack)
