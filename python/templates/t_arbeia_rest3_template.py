#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You share some bread &
cheese that you bought
for """
        yield str(node.change.minus['money'])
        yield """ Denarii.
Now back to work!
"""
    yield from render1(engine, story, box, node, card, sack)
