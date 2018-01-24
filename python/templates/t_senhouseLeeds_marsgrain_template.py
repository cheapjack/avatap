#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        if node.change.triggered:
            yield """You offer grain from the
store. What is he
to do with this?
He's not a horse!
GALLOP away mortal!
"""
        else:
            yield """Mars is bored of grain
"""
        yield """
"""
    yield from render1(engine, story, box, node, card, sack)
