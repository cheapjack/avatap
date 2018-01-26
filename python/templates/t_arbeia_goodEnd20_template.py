#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """'Did you put these fancy
beads on there?'
Answer: """
        yield str(sack.beads)
        yield """
'Did you repair my
dented old armour?'
Answer: """
        yield str(sack.polish)
        yield """
"""
    yield from render1(engine, story, box, node, card, sack)
