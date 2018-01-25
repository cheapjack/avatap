#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Choose from :
"""
    yield from render1()
#
    def render2(*a, **d):
        if not(node.isHidden(engine, 'altars')):
            yield """Make another visit to
the altars: """
            yield str(story.lookupNode('altars').getGoalBox(story).label)
            yield """
"""
        if not(node.isHidden(engine, 'battle')):
            yield """Defend the outpost!
Get a sword!: """
            yield str(story.lookupNode('battle').getGoalBox(story).label)
            yield """
"""
    yield from render2()
