#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You are in your quarters.
Walk over to BOX II
on the other side of the
museum to get started.
"""
    yield from render1(engine, story, box, node, card, sack)
