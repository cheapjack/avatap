#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """What do you want to do?
"""
    yield from render1()
#
    def render2(*a, **d):
        if not(node.isHidden(engine, 'seaview')):
            yield """Look out for attack
from the Northern
Sea!: """
            yield str(story.lookupNode('seaview').getGoalBox(story).label)
            yield """
"""
        if not(node.isHidden(engine, 'altars')):
            yield """Make a spiritual visit
to the altars: """
            yield str(story.lookupNode('altars').getGoalBox(story).label)
            yield """
"""
    yield from render2()
