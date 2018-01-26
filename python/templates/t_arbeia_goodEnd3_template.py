#
def render(engine, story, box, node, card, sack):
    #
    def render1(*a, **d):
        if node.change.triggered:
            if node.change.completed:
                yield """With the bonus, I now
have """
                yield str(sack.money)
                yield """ Denarii.
Enough to buy my own
pony and harness!
That was the best
day's work ever!
"""
            else:
                yield """OK, I've now got
"""
                yield str(sack.money)
                yield """ Denarii!
Enough to buy some of
new clothes and food.
Not very exciting...
"""
        else:
            yield """OK, I've now got
"""
            yield str(sack.money)
            yield """ Denarii!
Enough to buy some of
new clothes and food.
Not very exciting...
"""
        yield """
"""
    yield from render1(engine, story, box, node, card, sack)
