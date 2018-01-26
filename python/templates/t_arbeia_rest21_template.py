#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """'SWEPT the stables?'
You answer: """
        yield str(sack.dung)
        yield """!
'And how much have you
earned?'
I've earned an amazing
"""
        yield str(sack.money)
        yield """ Denarii!
"""
    yield from render1(engine, story, box, node, card, sack)
