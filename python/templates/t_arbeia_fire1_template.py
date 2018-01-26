#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """You walk across the
courtyard in the mud.
You need to SCRAPE your
boots before carrying
on...
"""
    yield from render1(engine, story, box, node, card, sack)
