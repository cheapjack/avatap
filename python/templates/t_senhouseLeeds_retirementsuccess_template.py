#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """WELL DONE! VICTORY!
The gods are with you!
"""
    yield from render1(engine, story, box, node, card, sack)
