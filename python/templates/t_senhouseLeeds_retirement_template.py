#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Bad luck. Respawned.
Begin your adventure
again! Epona will
favour """
        yield str(sack.eponapoints)
        yield """ horses for
you when you die!

"""
    yield from render1(engine, story, box, node, card, sack)
