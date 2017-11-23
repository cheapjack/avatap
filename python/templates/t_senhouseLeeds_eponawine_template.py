#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        if node.change.triggered:
            if node.change.completed:
                yield """You leave a cup of wine
for her. Should she
drink and ride?
"""
            else:
                yield """You are out of favour!
"""
        else:
            yield """Epona is not satisfied.
"""
        yield """
"""
    yield from render1(engine, story, box, node, card, sack)
