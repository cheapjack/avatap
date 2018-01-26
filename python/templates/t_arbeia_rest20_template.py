#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """'Have you:
FED the horses?'
You answer: """
        yield str(sack.feed)
        yield """!
FETCHED the water?
You answer: """
        yield str(sack.water)
        yield """!
MADE the fire?
You answer: """
        yield str(sack.fire)
        yield """!
"""
    yield from render1(engine, story, box, node, card, sack)
