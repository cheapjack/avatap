#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """'Are you done yet?
I have to get riding!
Let me take a look...
Did you clean my Harness?
Answer: """
        yield str(sack.harness)
        yield """
...
"""
    yield from render1(engine, story, box, node, card, sack)
