#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Choose from :
"""
    yield from render1()
#
    def render2(*a, **d):
        if not(node.isHidden(engine, 'water1')):
            yield """ Collect water from
the well: """
            yield str(story.lookupNode('water1').getGoalBox(story).label)
            yield """
"""
        if not(node.isHidden(engine, 'dung1')):
            yield """ Get your broom and clean
the stables: """
            yield str(story.lookupNode('dung1').getGoalBox(story).label)
            yield """
"""
    yield from render2()
