#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Your bucket is now full.
Pretend to CARRY the
heavy bucket back to the
main building.
Don't spill any!
You earned """
        yield str(node.change.plus['money'])
        yield """ Denarii
"""
    yield from render1(engine, story, box, node, card, sack)
