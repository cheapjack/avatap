#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You are in the temple
There are many altars
Each belongs to a great
warrior or nobleman

"""
    yield from render1(engine, story, box, node, card, sack)
