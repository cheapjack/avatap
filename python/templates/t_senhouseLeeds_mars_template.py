#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        if node.change.triggered:
            yield """Mars! MIME how
strong you are!
We need great warriors!
"""
        else:
            yield """You feel strong!
Mars is with us already!
He also helps with the
harvest you know...
"""
        yield """
"""
    yield from render1(engine, story, box, node, card, sack)
