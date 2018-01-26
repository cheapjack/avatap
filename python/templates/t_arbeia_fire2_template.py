#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """When the fire is hot,
head back to the
storeroom. You earned
"""
        yield str(node.change.plus['money'])
        yield """ Denarii.
"""
    yield from render1(engine, story, box, node, card, sack)
