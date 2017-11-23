#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You are stationed at
Leeds Becket Uni,
the coal face of game
design
"""
    yield from render1(engine, story, box, node, card, sack)
