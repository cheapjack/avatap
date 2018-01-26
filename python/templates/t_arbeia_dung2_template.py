#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You walk across the
courtyard, saying hello
to other slaves on your
way. You head to the
front of the barracks
where the stables are
found...
"""
    yield from render1(engine, story, box, node, card, sack)
