#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You are in the courtyard
by the wall.
"""
        if sack.hours <= 4:
            yield """It's early in the
morning and you can
smell the sea air.
"""
        if sack.hours > 4 and sack.hours < 12:
            yield """It's midday and people
hurry by."""
        if sack.hours == 12:
            yield """It's raining """
        if sack.hours > 12:
            yield """The night is closing in"""
        yield """
"""
    yield from render1(engine, story, box, node, card, sack)
