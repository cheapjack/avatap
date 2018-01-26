#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Your master has left
the fort! You will lose
"""
        yield str(node.change.minus['money'])
        yield """ Denarii
of your pay, but at least
you won't have to cross
the courtyard again!
"""
    yield from render1(engine, story, box, node, card, sack)
