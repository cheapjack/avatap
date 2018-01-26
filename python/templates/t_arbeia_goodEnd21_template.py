#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """'Well, I'm certainly
going to be the toast
of the Troy games!
Please take this
20 Denarii as a bonus!'
"""
    yield from render1(engine, story, box, node, card, sack)
