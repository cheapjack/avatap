#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """The stable is now clean!
Put your brush down and
walk back to the main
building. You earned
"""
        yield str(node.change.plus['money'])
        yield """ Denarii.
"""
    yield from render1(engine, story, box, node, card, sack)
