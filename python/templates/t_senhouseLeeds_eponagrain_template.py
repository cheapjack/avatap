#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        yield """PRETEND to offer grain
from the local harvest
Epona is often depicted
with grain. She also
is a god of fertility

"""
    yield from render1(engine, story, box, node, card, sack)
