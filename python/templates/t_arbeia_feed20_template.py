#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Pretend to SHOVEL the
horse feed into a sack.
COUNT to 15 in Roman
numerals to make sure
that you have enough...
"""
    yield from render1(engine, story, box, node, card, sack)
