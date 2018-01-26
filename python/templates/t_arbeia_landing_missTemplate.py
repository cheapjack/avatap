#
def render(engine, story, box, node, card, sack):
    yield """Please go to """
    yield str(node.goalBox.label)
    yield """
to continue the adventure
"""
