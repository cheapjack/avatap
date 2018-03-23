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
            "birdpoints": 0,
            "poempoints":  0,
            "lyricedLear": False,
            "audubon": False,
            "bonnet": False,
            "beard": False,
            "pussy": False,
            "owl": False,
            "turkey": False,
            "lark": False,
            "hours": 0,
            "complete": False,
            }
)

with story:
    groundBox = Box( uid="1", label="Vol I", description="Ground Floor")
    oakBox = Box( uid="2", label="Vol II", description="The Oak Room")
    pictonBox = Box( uid="3", label="Vol III", description="The Picton Room")
    archiveBox = Box( uid="4", label="Vol IV", description="The Archives")

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


    ConditionFork(
            uid= "completeCheck",
            condition = "sack.lyricedLear == True and sack.audubon == True",
            falseNodeUid = "foyerIntro",
            trueNodeUid = "endGame",
            )

    ThroughSequence(
            uid= "foyerIntro",
            time = incrementTime,
            #123456789012345678901234
            goalBoxUid = groundBox.uid,
            nextNodeUid = "firstOak",
            sequence = [
             """You have stumbled upon
            the first of 4 unusual
            volumes hidden in the
            library...""",
            """You are on the ground
            floor beautiful levels
		    of knowledge above you.
		    {% if sack.hours < 4 %}It's early in the
		    morning and some people
		    are using computers.
		    {% endif %}
            {% if sack.hours > 4 and sack.hours <= 12 %}It's midday & time for
            lunch{% endif %}
            {% if sack.hours == 13 %}It's raining {% endif %}
		    {% if sack.hours > 16 %}The library is closing!{% endif %}
            """,
            """GO FIND the OAK ROOM
            with the biggest book
            in the library to
            begin your journey""",
            ],
            )

    ThroughSequence(
            uid= "firstOak",
		    time = incrementTime,
		    sequence = [
		    #23456789012345678901234
            """In front of you in the
            case is the "Wild Birds
            of America" by
            John James Audubon a
            great naturalist, artist
            and hunter""",
            """This book is the key
            to your adventure! And
            it's part of why this
            library exists...""",
            """GO to the Picton Room
            QUIETLY to find out more""",
            ],
            goalBoxUid = oakBox.uid,
            nextNodeUid = "pictonStart",
            )

    ThroughSequence(
            uid="pictonStart",
            goalBoxUid=pictonBox.uid,
            sequence=[
            #23456789012345678901234
            """OK be quiet, like in
            the British Museum
            reading room it was
            modelled on, people here
            can hear you across the
            other side of the room""",
            """Do you want to take the
            path of the hunter or
            a lyrical journey of
            Liverpudlian patronage?""",
            ],
            nextNodeUid="adventureChoice",
            )

    NodeFork(
            uid = "adventureChoice",
            page = "What do you want to do?",
            choices = {
                "Audubon": """Audubon's Aviary
                Adventure""",
                "Lear": """Lear's Lyrical
                Listings""",
                },
            hideChoices = {
                "Audubon": "sack.audubon==True",
                "Lear": "sack.lyricedLear==True",
                },
)

    ThroughSequence(
            uid="Lear",
            goalBoxUid = archiveBox.uid,
            nextNodeUid="poemChoice",
            #23456789012345678901234
            sequence=[
            """Try to FIND 3 Lear
            poems in the library and
            mark it down in the
            INVENTORY in your
            leaflet...""",
            """RETURN here
            floor once you FIND all
            3 of his poems.""",
            ],
            missTemplate = """This isn't
            {{node.goalBox.description}}!
            Go to {{node.goalBox.label}}
            """,
            )

    NodeFork(
            uid="poemChoice",
            page="""
            Where to look?
            """,
            choices = {
                "bonnetGround": "Someone's Hat",
                "oldManOak": "Beards",
                "owlPicton": "Owls and cats",
                },
            hideChoices = {
                "bonnetGround": "sack.bonnet==True",
                "oldManOak": "sack.beard==True",
                "owlPicton": "sack.pussy==True",
                },
            )

    ThroughSequence(
            uid="bonnetGround",
            change = SackChange(
                trigger = "sack.bonnet == False",
                plus = { "poempoints":1 },
                assign = {"bonnet": True},
                ),
            goalBoxUid = groundBox.uid,
            #23456789012345678901234
            sequence = [
            """There was a Young Lady
            whose bonnet,
            Came untied when the
            birds sat upon it;...""",
            """All the birds in the air
            Are welcome to sit on my
            bonnet!""",
            """
            {% if sack.bonnet == True %}
                You now have {{ sack.poempoints }} poem!
                Return to the archives!
            {% else %}
                You now have {{ sack.poempoints }} poems!
                Keep looking!
            {% endif %}
            """,
            ],
            missTemplate = """This isn't
            {{node.goalBox.description}}!
            Go to {{node.goalBox.label}}
            """,
            nextNodeUid="LearCheck",
            )

    ThroughSequence(
            uid="oldManOak",
            change = SackChange(
                trigger = "sack.beard == False",
                plus = { "poempoints":1 },
                assign = { "beard":True },
                ),
            goalBoxUid = oakBox.uid,
            sequence = [
            #23456789012345678901234
            """There was an Old Man
            with a beard,
            Who said, It is just as
            I feared!...""",
            """Two Owls and a Hen,
            Four Larks and a Wren,
            Have all built their
            nests in my beard!""",
            ],
            nextNodeUid="LearCheck",
            missTemplate = """This isn't
            {{node.goalBox.description}}!
            Go to {{node.goalBox.label}}
            """,
            )

    ThroughSequence(
            uid="owlPicton",
            change = SackChange(
                trigger = "sack.pussy == False",
                plus = { "poempoints":1 },
                assign = { "pussy":True },
                ),
            goalBoxUid = pictonBox.uid,
            sequence = [
            #23456789012345678901234
            """The Owl and the
            Pussy-Cat went to sea
            In a beautiful pea-green
            boat,""",
            """They took some honey,
            and plenty of money,...""",
            """Wrapped in a five pound
            note.""",
            """You now have {{ sack.poempoints }} poems!
            """,
            ],
            nextNodeUid="LearCheck",
            missTemplate = """This isn't
            {{node.goalBox.description}}!
            Go to {{node.goalBox.label}}
            """,
            )

    #  condition Fork so 3 poems triggers complete
    ConditionFork(
            uid="LearCheck",
            condition = "sack.bonnet==True and sack.beard==True and sack.pussy==True",
            falseNodeUid = "morePoems",
            trueNodeUid =   "LearSuccess",
            )

    ThroughSequence(
            uid="morePoems",
            goalBoxUid = archiveBox.uid,
            nextNodeUid="poemChoice",
            sequence = [
            #23456789012345678901234
            """You are looking for poems
		    {% if sack.poempoints < 3 %}You are doing well!
            You have {{ sack.poempoints }} so far,
            keep looking!
		    {% endif %}
            {% if sack.poempoints > 1 %}Just one more
            poem to find
            {% endif %}
            {% if sack.poempoints == 3 or sack.poempoints >= 3 %}Well Done!
            {% endif %}
            """
            ],
            )

    ThroughPage(
            uid="LearSuccess",
            change = SackChange(
                trigger = "sack.lyricedLear == False",
                assign = {"lyricedLear": True},
                ),
            goalBoxUid = pictonBox.uid,
            nextNodeUid="completeCheck",
            page = """You have done it!
            You have {{ sack.poempoints }} poems
            enough for a slim volume!
            Go get it published!
            """,
            )

    ThroughSequence(
            uid="Audubon",
            goalBoxUid = oakBox.uid,
            sequence=[
            #123456789012345678901234
            #elaborate
            """The pages magically
            turn to a different page
            every week so of course
            some of these birds
            escape...""",
            """Can you look for the
            birds in the library?
            and maybe the spirit
            of John is still here.""",
            ],
            missTemplate = """This isn't
            {{node.goalBox.description}}!
            Go to {{node.goalBox.label}}
            """,
            nextNodeUid="birdChoices",
            )

    NodeFork(
            uid = "birdChoices",
            page = "Where could they be?",
            choices = {
                "Turkey": """Thanksgiving""",
                "Owl": """The Bird
                who reads""",
                "Lark": """Larkin about""",
                },
            hideChoices = {
                "Turkey": "sack.turkey==True",
                "Owl": "sack.owl==True",
                "Lark": "sack.lark==True",
                },
            )

    ThroughSequence(
            uid="Turkey",
            goalBoxUid = groundBox.uid,
            change = SackChange(
                trigger = "sack.turkey == False",
                plus = { "birdpoints":1 },
                assign = { "turkey":True },
                ),
            sequence=[
            #123456789012345678901234
            """In front of you is
            a wild turkey,
            Meleagris gallopavo
            """,
            """You draw it in your
            notebook""",
            ],
            nextNodeUid="birdCheck",
            )

    ThroughSequence(
            uid="Owl",
            goalBoxUid = pictonBox.uid,
            change = SackChange(
                trigger = "sack.owl == False",
                plus = { "birdpoints":1 },
                assign = { "owl":True },
                ),
            sequence=[
            #123456789012345678901234
            """In front of you is
            a snowy owl, Strix nectea""",
             """You draw it in your
            notebook""",
            ],
            nextNodeUid="birdCheck",
            )

    ThroughSequence(
            uid="Lark",
            goalBoxUid = archiveBox.uid,
            change = SackChange(
                trigger = "sack.lark == False",
                plus = { "birdpoints":1 },
                assign = { "lark":True },
                ),
            sequence=[
            #123456789012345678901234
            """In front of you is
            a Meadow Lark,
            Sturnus ludovicianus""",
             """You draw it in your
            notebook""",
            ],
            nextNodeUid="birdCheck",
            )

    # condition Fork so 3 bird triggers complete
    ConditionFork(
            uid="birdCheck",
            condition = "sack.turkey==True and sack.owl==True and sack.lark==True",
            falseNodeUid = "moreBirds",
            trueNodeUid =   "AudubonSuccess",
            )

    ThroughPage(
            uid="moreBirds",
            goalBoxUid = oakBox.uid,
            page = """FIND Audubon's birds!
		    {% if sack.birdpoints < 3 %}You are doing ok!
            You have {{ sack.birdpoints }} so far,
            keep looking!
		    {% endif %}
            {% if sack.birdpoints > 1 %}You have {{ sack.birdpoints }} hunt points!
            Just one more
            bird to find{% endif %}
            {% if sack.birdpoints == 3 or sack.birdpoints >= 3 %}Well Done!{% endif %}
            """,
            nextNodeUid="birdChoices",
            )

    ThroughPage(
            uid="AudubonSuccess",
            change = SackChange(
                trigger = "sack.audubon == False",
                assign = {"audubon": True},
                ),
            goalBoxUid = pictonBox.uid,
            #23456789012345678901234
            page = """You have done it!
            You have {{ sack.birdpoints }} birdpoints.
            Onwards to get a patron!
            """,
            nextNodeUid="completeCheck",
            )

    ThroughPage(
            uid="endGame",
            goalBoxUid = pictonBox.uid,
            page="""Game Over!
            You found {{ sack.birdpoints }} birds and
            {{ sack.poempoints }} poems for your book!
            Go to the ground floor
            to respawn""",
            nextNodeUid="firstLanding",
            )
# Bonus"""Can you FIND the only book in here that looks back at you and RETURN...""",
