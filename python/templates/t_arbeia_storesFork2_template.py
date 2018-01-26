#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Choose from :
"""
    yield from render1()
#
    def render2(*a, **d):
        if not(node.isHidden(engine, 'fire1')):
            yield """ Make up a fire in the
barracks: """
            yield str(story.lookupNode('fire1').getGoalBox(story).label)
            yield """
"""
        if not(node.isHidden(engine, 'feed1')):
            yield """ Collect feed for the
cavalry horses: """
            yield str(story.lookupNode('feed1').getGoalBox(story).label)
            yield """
"""
    yield from render2()
