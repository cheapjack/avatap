#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Choose from :
"""
    yield from render1()
#
    def render2(*a, **d):
        if not(node.isHidden(engine, 'horse1')):
            yield """ Find your master at the
barracks: """
            yield str(story.lookupNode('horse1').getGoalBox(story).label)
            yield """
"""
        if not(node.isHidden(engine, 'sleep1')):
            yield """ I'm tired!! Go to bed
and end the game: """
            yield str(story.lookupNode('sleep1').getGoalBox(story).label)
            yield """
"""
    yield from render2()
