#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """The harness looks
perfect. Your master
will be amongst the
most well-dressed
at the Trojan games...
"""
    yield from render1(engine, story, box, node, card, sack)
