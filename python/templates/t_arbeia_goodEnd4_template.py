#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Now you can take a rest!
LIFT and HOLD your TAG
here to play again or go
to another museum to play
as a different character!
"""
    yield from render1(engine, story, box, node, card, sack)
