#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        if sack.eponapoints < 10:
            yield """You've driven back
the hordes but will
you manage next time?
Will we have the
right horses?
"""
        if sack.eponapoints >= 10:
            yield """With this horse
we can breed horses
for the next generation
of Hadrian's cavalry!
"""
        yield """
"""
    yield from render1(engine, story, box, node, card, sack)
