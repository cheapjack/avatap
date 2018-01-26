#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Choose from :
"""
    yield from render1()
#
    def render2(*a, **d):
        if not(node.isHidden(engine, 'harness1')):
            yield """ 'Clean my harness!
Quickly!': """
            yield str(story.lookupNode('harness1').getGoalBox(story).label)
            yield """
"""
        if not(node.isHidden(engine, 'armour1')):
            yield """ 'Polish my armour!
Pronto!: """
            yield str(story.lookupNode('armour1').getGoalBox(story).label)
            yield """
"""
    yield from render2()
