#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Choose from :
"""
    yield from render1()
#
    def render2(*a, **d):
        if not(node.isHidden(engine, 'epona')):
            yield """Epona, god of horses
and fertility: """
            yield str(story.lookupNode('epona').getGoalBox(story).label)
            yield """
"""
        if not(node.isHidden(engine, 'mars')):
            yield """Mars, god of war &
also peace: """
            yield str(story.lookupNode('mars').getGoalBox(story).label)
            yield """
"""
    yield from render2()
