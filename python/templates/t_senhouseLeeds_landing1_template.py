#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You must also care for
and breed horses for the
cavalry and pay tribute
to the gods with
offerings & libations

"""
    yield from render1(engine, story, box, node, card, sack)
