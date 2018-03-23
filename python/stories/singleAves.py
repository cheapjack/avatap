from milecastles import Story, Box, ThroughPage, ThroughSequence, ConditionFork, NodeFork, SackChange
from stories import introText

# inspects the module to figure out the story name (e.g. corbridge)
storyName = "skeletonAves"

# create story
story = Story(
    uid=storyName,
    version="0.1.0",
    startNodeUid="firstLanding",
    startSack={
            "audubon": False,
            }
    )

with story:
    groundBox = Box( uid="1", label="Vol I", description="Ground Floor")

    entranceBox = groundBox
    incrementTime = SackChange(
            plus={ "hours":1 }
            )

    # populate with passages
    ThroughPage(
            change=SackChange(
                reset=story.startSack
                ),
            uid="firstLanding",
            goalBoxUid=entranceBox.uid,
            page=introText,
            nextNodeUid="foyerIntro",
            )


    ThroughSequence(
            uid= "foyerIntro",
            time = incrementTime,
            goalBoxUid = groundBox.uid,
            nextNodeUid = "firstLanding",
            sequence = [
             """You have stumbled upon
            the first of 4 unusual
            volumes hidden in the
            library...""",
            """This is an RFID driven
            txt adventure hidden in
            the library on William
            Brown Street...""",
            """It's made by Domestic
            Science an artist group
            that explores how we use
            science every day...""",
            """As Makers we love
            S.T.E.M & S.T.E.A.M. but
            for us A is for art
            practice & S is for
            sciencestudies...""",
            """Maker Difference asked
            DS to make a game about
            the library and so we
            thought about how the
            library came to be...""",
            """and how science worked
            in the 18th century.
            John James Audubon was
            an eccentric failed
            businessman with a
            passion for nature...""",
            """a long haired handsome
            son of a sea captain
            visits Liverpool
            seeking patronage and
            charms the 13th Earl
            of Derby in Knowsley...""",
            """Edward becomes a
            patron & donates his
            collections to the
            people of Liverpool
            over 15,000 specimens...""",
            """He also was patron of
            poet Edward Lear, who
            like audubon drew birds.
            Unlike John he would
            only draw living birds
            at Knowsley Hall...""",
            """Historically science
            views animals as simple
            mechanistic organisms
            but both audubon and
            Lear seemed to be
            precursors of modern...""",
            """science where animals
            are complex actors in
            vast complex contexts;
            blurring the difference
            of animal/human...""",
            """Audubon on horseback
            in the USA came across
            a vast flock of birds
            taking 3 days to pass
            him overhead""",
            """today this vast animal
            world is a ghost of it's
            former self; in Knowsley
            Halls hey day the scale
            of nature & knowledge
            seemed infinite...""",
            """take a tag and find
            books like this and play
            a game inspired by Lear
            and Audubon and the great
            store of knowledge in
            Liverpool...""",
            ],
            )
