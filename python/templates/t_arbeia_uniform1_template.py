#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """'Help to get me and my
horse Regalis looking
smart for the Troy Games!
Quickly! I'm late!!''
"""
    yield from render1(engine, story, box, node, card, sack)
