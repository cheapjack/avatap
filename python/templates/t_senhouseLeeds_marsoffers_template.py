#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Choose from :
"""
    yield from render1()
#
    def render2(*a, **d):
        if not(node.isHidden(engine, 'marswine')):
            yield """Offer some wine: """
            yield str(story.lookupNode('marswine').getGoalBox(story).label)
            yield """
"""
        if not(node.isHidden(engine, 'marsgrain')):
            yield """Seek some ears
of grain: """
            yield str(story.lookupNode('marsgrain').getGoalBox(story).label)
            yield """
"""
    yield from render2()
