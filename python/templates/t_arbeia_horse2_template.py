#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Your master is happy!!
'What a great job you've
done! Here's a bonus of
"""
        yield str(node.change.plus['money'])
        yield """ Denarii!'
...'
"""
    yield from render1(engine, story, box, node, card, sack)
