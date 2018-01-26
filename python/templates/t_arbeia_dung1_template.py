#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You quickly go to your
quarters to find your
broom. It's behind some
old animal skins.
Now head outside
to the STABLES.
"""
    yield from render1(engine, story, box, node, card, sack)
