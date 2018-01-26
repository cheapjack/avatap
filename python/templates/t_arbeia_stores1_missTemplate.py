#
def render(engine, story, box, node, card, sack):
    yield """This isn't the storeroom!
Go to """
    yield str(node.goalBox.label)
    yield """
"""
