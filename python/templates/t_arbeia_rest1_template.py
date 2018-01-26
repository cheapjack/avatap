#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You take a short rest in
your quarters. You think
about the """
        yield str(sack.money)
        yield """ Denarii
you've earned so far.
It's good to sit down...
"""
    yield from render1(engine, story, box, node, card, sack)
