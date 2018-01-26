#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """What's next?
Go to """
        yield str(node.goalBox.label)
        yield """
...
"""
    yield from render1(engine, story, box, node, card, sack)
