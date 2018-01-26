#
def render(engine, story, box, node, card, sack):
    yield """Time for a break - go to
your quarters at """
    yield str(node.goalBox.label)
    yield """
"""
