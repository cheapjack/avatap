#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """The END! How did you
find life as a groom?
You made """
        yield str(sack.money)
        yield """ Denarii.
HOLD TAG to play again or
visit another museum to
play another character.
"""
    yield from render1(engine, story, box, node, card, sack)
