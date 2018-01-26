#
def render(engine, story, box, node, card, sack):
    yield """Stop slacking!! Go to """
    yield str(node.goalBox.label)
    yield """
"""
