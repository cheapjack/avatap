#
def render(engine, story, box, node, card, sack):
    yield """Your adventure is over.
Epona will favour """
    yield str(sack.eponapoints)
    yield """
of your horses.
Mars awards """
    yield str(sack.marspoints)
    yield """ gold pieces
for the afterlife.
Return to """
    yield str(node.goalBox.label)
    yield """
to respawn.
"""
