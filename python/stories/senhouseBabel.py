import agnostic
from milecastles import Story, Box, ThroughPage, ThroughSequence, ConditionFork, NodeFork, SackChange
from stories import introText

# inspects the module to figure out the story name (e.g. corbridge)
storyName = __name__.split(".")[-1]

# create story
story = Story(
    uid=storyName,
    version="0.1.0",
    #startNodeUid = "landing",
    startNodeUid="firstLanding",
    startSack={
        "dockers":False,
        "science":False,
        "archive":False,
        "readpoints":0,
        "searchpoints":0,
        "hours":0,
    }
)
agnostic.collect()

with story:

    infoBox =    Box( uid="1",   label="Box I",      description="Fiction Section")
    localBox =   Box( uid="2",   label="Box II",     description="Liverpool Archives")
    pictonBox = Box( uid="3",   label="Box III",     description="Picton Reading Room")
    agnostic.collect()

    entranceBox = infoBox
    incrementTime = SackChange(
        plus={ "hours":1 }
    )

    # populate with passages

    ThroughPage(
        uid="firstLanding",
        goalBoxUid=entranceBox.uid,
        page=introText,
        nextNodeUid="landing",
        )

    ThroughSequence(
            uid =           "landing",
            change =        SackChange(
                reset=story.startSack
            ),
            goalBoxUid =    infoBox.uid,
            nextNodeUid =   "yardArrive",
                #23456789012345678901234
            sequence = [
                """You are in Liverpool
                Central Library. You
                must discover books and
                collections unknown!""",
                """You must READ books
                you don't know about
                and explore the library""",
            ],
            missTemplate = """Your adventure is over.
            You have {{sack.dockerspoints}}
            local knowledge.
            You have {{sack.searchpoints}} science
            points.
            Return to {{node.goalBox.label}}
            to respawn.""",
    )
    agnostic.collect()

    ConditionFork(
            uid=            "yardArrive",
            condition =     "sack.archive == True",
            falseNodeUid =  "yardIntro",
            trueNodeUid =   "retirementsuccess",
    )
    agnostic.collect()

    ThroughPage(
        uid=            "yardIntro",
        time = incrementTime,
        #123456789012345678901234
        page =
        """You are on the ground
        floor a beautiful spiral
        of knowledge above you.
        {% if sack.hours <= 4 %}It's early in the
        morning and some people
        are using computers.
        {% endif %}
        {% if sack.hours > 4 and sack.hours < 12 %}It's midday & time for
        lunch{% endif %}
        {% if sack.hours == 12 %}It's raining {% endif %}
        {% if sack.hours > 12 %}The library is closing!{% endif %}
        """,
        goalBoxUid =    infoBox.uid,
        nextNodeUid =   "work",
    )
    agnostic.collect()

    NodeFork(
        uid = "work",
                #23456789012345678901234
        page = "What do you want to do?",
        choices = {
            "localbooks":   """Find out about
            liverpool.""",
            "exhibit":  """Read letters
            from the past.""",
        },
    )
    agnostic.collect()

    ThroughSequence(
        uid =   "localbooks",
        time = incrementTime,
        sequence = [
        #23456789012345678901234
        """You are in the Search
        Room. You can see two
        different books
        """,
        ],
        goalBoxUid = localBox.uid,
        nextNodeUid = "chooseBook",
    )
    agnostic.collect()

    NodeFork(
        uid = "chooseBook",
        choices  = {
            "dockers" : """Dockers, photos by
            Dave Sinclair""",
            "science"  : """Science about
            products""",
        },
    )
    agnostic.collect()

    ThroughPage(
        uid = "dockers",
        time = incrementTime,
        change = SackChange(
            trigger = "sack.dockers == False",
            assign = { "dockers":True },
            plus = { "dockerspoints":2 },
            ),
        page ="""{% if node.change.triggered %}The history of
        dockers is important
        to Liverpool the
        great city of docks
        Read it!
        {% else %}You read dockers already!
        {% endif %}
        """,
        goalBoxUid = infoBox.uid,
        nextNodeUid = "dockersoffers",
    )
    agnostic.collect()

    ThroughPage(
        uid = "science",
        goalBoxUid = pictonBox.uid,
        time = incrementTime,
        change = SackChange(
            trigger = "sack.science == False",
            assign = { "science":True },
        ),
        page =
        """{% if node.change.triggered %}science! MIME how
                clever you are!
                We need scientists!
        {% else %}You feel clever!
                science is with us already!
        {% endif %}
        """,
        nextNodeUid = "scienceoffers",
    )
    agnostic.collect()

    NodeFork(
        uid =   "dockersoffers",
        choices = {
            "dockerswine": "Discover economics",
            "dockersgrain": """Discover work
            today"""
        },
    )
    agnostic.collect()

    ThroughPage(
        uid =   "dockerswine",
        goalBoxUid = pictonBox.uid,
        change = SackChange(
            trigger = "sack.dockerspoints > 1",
            assign = { "dockers":False },
            minus = { "dockerspoints":1 },
        ),
        page ="""{% if node.change.triggered %}
                    {% if node.change.completed %}
                        Economic policy changed
                        Liverpool forever.
                        For Good and Bad
                    {% else %}
                    You are out of favour!
                    {% endif %}
                {% else %}
                dockers are not satisfied.
                {% endif %}
        """,
        nextNodeUid = "yardArrive",
    )
    agnostic.collect()

    ThroughPage(
        uid =   "dockersgrain",
        goalBoxUid = localBox.uid,
        change = SackChange(
            assign = { "dockers":True },
            plus = { "dockerspoints":10 },
        ),
        page =
        """PRETEND tourism
        is a good alternative
        to industry
        and 3d printing
        will help employment
        """,
        nextNodeUid = "yardArrive",
    )
    agnostic.collect()

    NodeFork(
        uid =   "scienceoffers",
        choices = {
            "sciencewine": "Offer some IoT",
            "sciencegrain": """Build some
            cars""",
        },
    )
    agnostic.collect()

    ThroughSequence(
        uid =   "sciencewine",
        goalBoxUid = localBox.uid,
        time = incrementTime,
        change = SackChange(
            plus = { "searchpoints":2 }
        ),
        sequence = [
        """DO CODING using
        IoT""",
        """...with microbits"""
        ],
        nextNodeUid = "yardArrive",
    )
    agnostic.collect()

    ThroughPage(
        uid =   "sciencegrain",
        goalBoxUid = infoBox.uid,
        change = SackChange(
            trigger = "sack.science == True",
            assign = {"science":False},
        ),
        page = """{% if node.change.triggered %}You offer to make
        more cars. Are you
        serious?
        Land Rover make
        Liverpools Cars!
        {% else %}science is bored of cars
        {% endif %}
        """,
        nextNodeUid = "yardArrive",
    )
    agnostic.collect()

    # ROUTE TO SPOTTING invaders
    ConditionFork(
        uid =       "exhibit",
        condition = "sack.hours >= 10",
        falseNodeUid =  "seaviewclear",
        trueNodeUid =   "seaviewinvaders",
    )
    agnostic.collect()

    ThroughPage(
        uid =   "seaviewclear",
        time = incrementTime,
        page = """You can see the sea""",
        goalBoxUid = pictonBox.uid,
        nextNodeUid = "yardArrive",
    )
    agnostic.collect()

    # ROUTE TO COASTAL BATTLE
    ThroughSequence(
        uid =   "seaviewinvaders",
        time = incrementTime,
        sequence = [
            """You can see the sea
            On the horizon
            you can see a container""",
            """We must fight off
            supercontainerisation
            to defend docks from
            Peele Holdings""",
        ],
        goalBoxUid = pictonBox.uid,
        nextNodeUid = "bravery",
    )
    agnostic.collect()

    NodeFork(
        uid =   "bravery",
        choices = {
            "localbooks": """Make another visit to
            the search room""",
            "battle": """Fight globalisation!
            Get a laptop!""",
        },
    )
    agnostic.collect()

    # ROUTE TO SUCCESSFUL BATTLE
    ConditionFork(
        uid=           "battle",
        condition =    "sack.science == True",
        trueNodeUid=   "battleSuccess",
        falseNodeUid=  "battleFailure",
    )
    agnostic.collect()

    # battle win
    ThroughPage(
        uid =           "battleSuccess",
        time = incrementTime,
        goalBoxUid =    infoBox.uid,
        change = SackChange(
            trigger =   "sack.archive == False",
            assign =    { "archive":True},
            plus  =     { "searchpoints":4 },
        ),
        page = """{% if node.change.triggered %}You bravely hold back
        supercontainerisation
        down the estuary!
        You kill the fleeing
        Peele Holdings
            {% else %}You HOLD back
            globalisation but are
            driven back!
            {% endif %}
        """,
        nextNodeUid = "yardArrive"
    )
    agnostic.collect()

    ThroughSequence(
        uid =           "battleFailure",
        time = incrementTime,
        sequence = [
            """You bravely HOLD back
            supercontainerisation
            for a while but
            are forced back!""",
            """You RUN to the wall
            and are UNEMPLOYED!"""
        ],
        goalBoxUid =    infoBox.uid,
        nextNodeUid =   "retirement",
    )
    agnostic.collect()

    finalReport = (
        """You completed your
        adventure! dockers will
        favour {{sack.dockerspoints}} horses for
        you when you die!
        Return to {{node.goalBox.label}}
        to respawn & try again!"""
    )

    ThroughPage(
        uid = "retirement",
        goalBoxUid = entranceBox.uid,
        page = """Bad luck. Respawned.
        Begin your adventure
        again! dockers will
        favour {{sack.dockerspoints}} horses for
        you when you die!
        """,
        missTemplate = finalReport,
        nextNodeUid = "landing",
    )

    agnostic.collect()

    ThroughSequence(
        uid = "retirementsuccess",
        goalBoxUid = infoBox.uid,
        sequence = [
            #234567889012345678901234
            """WELL DONE! VICTORY!
            The gods are with you!""",
            """{% if sack.dockerspoints < 10 %}You've driven back
            the hordes but will
            you manage next time?
            Will we have the
            right horses?
            {% endif %}{% if sack.dockerspoints >= 10 %}With this horse
            we can breed horses
            for the next generation
            of Hadrian's cavalry!
            {% endif %}
            """,
            """Your adventure is over.
            dockers favours {{sack.dockerspoints}} horses
            and science will make {{sack.searchpoints}}
            great cavalryman for
            the wall
            Return to {{node.goalBox.label}}
            to respawn.""",
        ],
        missTemplate = finalReport,
        nextNodeUid = "landing",
    )
    agnostic.collect()
