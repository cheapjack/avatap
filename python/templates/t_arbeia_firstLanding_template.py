#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """Welcome to Milecastles!
Look for numbered boxes!
Place tag on the symbol
& keep in place to read
then lift & replace to
progress the story...
"""
    yield from render1(engine, story, box, node, card, sack)
