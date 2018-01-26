#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """The harness looks good!
you've earned """
        yield str(node.change.plus['money'])
        yield """ Denarii.
Looking closer, you
notice a split. I wonder
if I can find something
to fix it in my quarters?
"""
    yield from render1(engine, story, box, node, card, sack)
