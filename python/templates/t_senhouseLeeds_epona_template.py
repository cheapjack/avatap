#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        if node.change.triggered:
            yield """Epona protector of
horses!
May our mounts stay
strong steady & fertile.
Make an offering!
"""
        else:
            yield """Epona is with us already!
"""
        yield """
"""
    yield from render1(engine, story, box, node, card, sack)
