#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Your adventure is over.
Epona favours """
        yield str(sack.eponapoints)
        yield """ horses
and Mars will make """
        yield str(sack.marspoints)
        yield """
great cavalryman for
the wall
Return to """
        yield str(node.goalBox.label)
        yield """
to respawn.
"""
    yield from render1(engine, story, box, node, card, sack)
