#
def render(engine, story, box, node, card, sack):
    yield """You completed your
adventure! Epona will
favour """
    yield str(sack.eponapoints)
    yield """ horses for
you when you die!
Return to """
    yield str(node.goalBox.label)
    yield """
to respawn & try again!
"""
