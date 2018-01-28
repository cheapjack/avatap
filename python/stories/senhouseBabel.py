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
        "alexpoints":0,
        "hours":0,
    }
)
agnostic.collect()

with story:

    infoBox =    Box( uid="1",   label="Box I",      description="Information Books")
    localBox =   Box( uid="2",   label="Box II",     description="Local Interest")
    wowBox = Box( uid="3",   label="Box III",     description="Writing on the Wall")
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
                """You are in Toxteth
                Library. You must
                discover books and
                collections unknown""",
                """You must READ books
                you don't know about
                and explore the library""",
            ],
            missTemplate = """Your adventure is over.
            you have {{sack.dockerspoints}}
            local knowledge.
            You have {{sack.sciencepoints}} science
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
        """You are in the
        Information and children
        section.
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
            "exhibit":  """Read letters from
            the past.""",
        },
    )
    agnostic.collect()

    ThroughSequence(
        uid =   "localbooks",
        time = incrementTime,
        sequence = [
        """You are in the Local
        Interest section. You
        can see two different
        books
        """,
        ],
        goalBoxUid = localBox.uid,
        nextNodeUid = "chooseBook",
    )
    agnostic.collect()

    NodeFork(
        uid = "chooseBook",
        choices  = {
            #23456789012345678901234
            "dockers" : """Dockers, photos by
            Dave Sinclair""",
            "science"  : """science, god of war &
            also peace""",
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
        page ="""{% if node.change.triggered %}dockers protector of
        horses!
        May our mounts stay
        strong steady & fertile.
        Make an offering!
        {% else %}dockers is with us already!
        {% endif %}
        """,
        goalBoxUid = infoBox.uid,
        nextNodeUid = "dockersoffers",
    )
    agnostic.collect()

    ThroughPage(
        uid = "science",
        goalBoxUid = wowBox.uid,
        time = incrementTime,
        change = SackChange(
            trigger = "sack.science == False",
            assign = { "science":True },
        ),
        page =
        """{% if node.change.triggered %}science! MIME how
                strong you are!
                We need great warriors!
        {% else %}You feel strong!
                science is with us already!
                He also helps with the
                harvest you know...
        {% endif %}
        """,
        nextNodeUid = "scienceoffers",
    )
    agnostic.collect()

    NodeFork(
        uid =   "dockersoffers",
        choices = {
            "dockerswine": "Offer some wine",
            "dockersgrain": """Seek some ears
            of grain"""
        },
    )
    agnostic.collect()

    ThroughPage(
        uid =   "dockerswine",
        goalBoxUid = wowBox.uid,
        change = SackChange(
            trigger = "sack.dockerspoints > 1",
            assign = { "dockers":False },
            minus = { "dockerspoints":1 },
        ),
        page ="""{% if node.change.triggered %}
                    {% if node.change.completed %}
                        You leave a cup of wine
                        for her. Should she
                        drink and ride?
                    {% else %}
                    You are out of favour!
                    {% endif %}
                {% else %}
                dockers is not satisfied.
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
        """PRETEND to offer grain
        from the local harvest
        dockers is often depicted
        with grain. She also
        is a god of fertility
        """,
        nextNodeUid = "yardArrive",
    )
    agnostic.collect()

    NodeFork(
        uid =   "scienceoffers",
        choices = {
            "sciencewine": "Offer some wine",
            "sciencegrain": """Seek some ears
            of grain""",
        },
    )
    agnostic.collect()

    ThroughSequence(
        uid =   "sciencewine",
        goalBoxUid = localBox.uid,
        time = incrementTime,
        change = SackChange(
            plus = { "sciencepoints":2 }
        ),
        sequence = [
        """LEAVE a cup of wine.
        He also helps with
        the harvest you know...""",
        """...which helps us
        make more wine!"""
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
        page = """{% if node.change.triggered %}You offer grain from the
        store. What is he
        to do with this?
        He's not a horse!
        GALLOP away mortal!
        {% else %}science is bored of grain
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
        goalBoxUid = wowBox.uid,
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
            you can see a sail!""",
            """We must fight off the
            invaders and prepare
            to defend the coastal
            outpost!""",
        ],
        goalBoxUid = wowBox.uid,
        nextNodeUid = "bravery",
    )
    agnostic.collect()

    NodeFork(
        uid =   "bravery",
        choices = {
            "localbooks": """Make another visit to
            the altars""",
            "battle": """Defend the outpost!
            Get a sword!""",
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
            plus  =     { "sciencepoints":4 },
        ),
        page = """{% if node.change.triggered %}You bravely hold back
        the invaders! CHARGE
        down the coastal path!
        You kill the fleeing
        celts & take a horse
            {% else %}You HOLD back the hordes
            best you can but are
            driven back! the coastal
            path may be over run!
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
            the invaders charging
            up the coastalpath
            but are forced back!""",
            """You RUN to the wall
            and DIE! science help us!"""
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
            and science will make {{sack.sciencepoints}}
            great cavalryman for
            the wall
            Return to {{node.goalBox.label}}
            to respawn.""",
        ],
        missTemplate = finalReport,
        nextNodeUid = "landing",
    )
    agnostic.collect()
