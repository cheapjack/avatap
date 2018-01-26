#
def render(engine, story, box, node, card, sack):
    yield """This isn't your quarters
Go to """
    yield str(node.goalBox.label)
    yield """
"""
