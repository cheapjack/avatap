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
        "epona":False,
        "mars":False,
        "superhorse":False,
        "eponapoints":0,
        "marspoints":0,
        "hours":0,
    }
)
agnostic.collect()

with story:

    paddockBox =    Box( uid="1",   label="Box I",      description="in the paddock breeding horses")
    altarBox =   Box( uid="2",   label="Box II",     description="Before the altars of the gods")
    seaBox = Box( uid="3",   label="Box III",     description="Looking out to sea")
    agnostic.collect()

    entranceBox = paddockBox
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
            goalBoxUid =    paddockBox.uid,
            nextNodeUid =   "yardArrive",
                #23456789012345678901234
            sequence = [
                """You are stationed at
                Leeds Becket Uni,
                the coal face of game
                design""",
                """You must WATCH for
                attacks & hacks from
                the sea & internet!""",
                """You must also care for
                and breed horses for the
                cavalry and pay tribute
                to the gods with
                offerings & libations
                """,
            ],
            missTemplate = """Your adventure is over.
            Epona will favour {{sack.eponapoints}}
            of your horses.
            Mars awards {{sack.marspoints}} gold pieces
            for the afterlife.
            Return to {{node.goalBox.label}}
            to respawn.""",
    )
    agnostic.collect()

    ConditionFork(
            uid=            "yardArrive",
            condition =     "sack.superhorse == True",
            falseNodeUid =  "yardIntro",
            trueNodeUid =   "retirementsuccess",
    )
    agnostic.collect()

    ThroughPage(
        uid=            "yardIntro",
        time = incrementTime,
        page =
        """You are in the courtyard
        by the wall.
        {% if sack.hours <= 4 %}It's early in the
        morning and you can
        smell the sea air.
        {% endif %}
        {% if sack.hours > 4 and sack.hours < 12 %}It's midday and people
        hurry by.{% endif %}
        {% if sack.hours == 12 %}It's raining {% endif %}
        {% if sack.hours > 12 %}The night is closing in{% endif %}
        """,
        goalBoxUid =    paddockBox.uid,
        nextNodeUid =   "work",
    )
    agnostic.collect()

    NodeFork(
        uid = "work",
                #23456789012345678901234
        page = "What do you want to do?",
        choices = {
            "altars":   """Make a spiritual visit
            to the altars""",
            "seaview":  """Look out for attack
            from the Northern
            Sea!""",
        },
    )
    agnostic.collect()

    ThroughSequence(
        uid =   "altars",
        time = incrementTime,
        sequence = [
        """You are in the temple
        There are many altars
        Each belongs to a great
        warrior or nobleman
        """,
        """We must pay tribute to
        the gods!
        But who in your heart
        do you seek favour?""",
        ],
        goalBoxUid = altarBox.uid,
        nextNodeUid = "chooseGod",
    )
    agnostic.collect()

    NodeFork(
        uid = "chooseGod",
        choices  = {
            #23456789012345678901234
            "epona" : """Epona, god of horses
            and fertility""",
            "mars"  : """Mars, god of war &
            also peace""",
        },
    )
    agnostic.collect()

    ThroughPage(
        uid = "epona",
        time = incrementTime,
        change = SackChange(
            trigger = "sack.epona == False",
            assign = { "epona":True },
            plus = { "eponapoints":2 },
            ),
        page ="""{% if node.change.triggered %}Epona protector of
        horses!
        May our mounts stay
        strong steady & fertile.
        Make an offering!
        {% else %}Epona is with us already!
        {% endif %}
        """,
        goalBoxUid = paddockBox.uid,
        nextNodeUid = "eponaoffers",
    )
    agnostic.collect()

    ThroughPage(
        uid = "mars",
        goalBoxUid = seaBox.uid,
        time = incrementTime,
        change = SackChange(
            trigger = "sack.mars == False",
            assign = { "mars":True },
        ),
        page =
        """{% if node.change.triggered %}Mars! MIME how
                strong you are!
                We need great warriors!
        {% else %}You feel strong!
                Mars is with us already!
                He also helps with the
                harvest you know...
        {% endif %}
        """,
        nextNodeUid = "marsoffers",
    )
    agnostic.collect()

    NodeFork(
        uid =   "eponaoffers",
        choices = {
            "eponawine": "Offer some wine",
            "eponagrain": """Seek some ears
            of grain"""
        },
    )
    agnostic.collect()

    ThroughPage(
        uid =   "eponawine",
        goalBoxUid = seaBox.uid,
        change = SackChange(
            trigger = "sack.eponapoints > 1",
            assign = { "epona":False },
            minus = { "eponapoints":1 },
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
                Epona is not satisfied.
                {% endif %}
        """,
        nextNodeUid = "yardArrive",
    )
    agnostic.collect()

    ThroughPage(
        uid =   "eponagrain",
        goalBoxUid = altarBox.uid,
        change = SackChange(
            assign = { "epona":True },
            plus = { "eponapoints":10 },
        ),
        page =
        """PRETEND to offer grain
        from the local harvest
        Epona is often depicted
        with grain. She also
        is a god of fertility
        """,
        nextNodeUid = "yardArrive",
    )
    agnostic.collect()

    NodeFork(
        uid =   "marsoffers",
        choices = {
            "marswine": "Offer some wine",
            "marsgrain": """Seek some ears
            of grain""",
        },
    )
    agnostic.collect()

    ThroughSequence(
        uid =   "marswine",
        goalBoxUid = altarBox.uid,
        time = incrementTime,
        change = SackChange(
            plus = { "marspoints":2 }
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
        uid =   "marsgrain",
        goalBoxUid = paddockBox.uid,
        change = SackChange(
            trigger = "sack.mars == True",
            assign = {"mars":False},
        ),
        page = """{% if node.change.triggered %}You offer grain from the
        store. What is he
        to do with this?
        He's not a horse!
        GALLOP away mortal!
        {% else %}Mars is bored of grain
        {% endif %}
        """,
        nextNodeUid = "yardArrive",
    )
    agnostic.collect()

    # ROUTE TO SPOTTING invaders
    ConditionFork(
        uid =       "seaview",
        condition = "sack.hours >= 10",
        falseNodeUid =  "seaviewclear",
        trueNodeUid =   "seaviewinvaders",
    )
    agnostic.collect()

    ThroughPage(
        uid =   "seaviewclear",
        time = incrementTime,
        page = """You can see the sea""",
        goalBoxUid = seaBox.uid,
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
        goalBoxUid = seaBox.uid,
        nextNodeUid = "bravery",
    )
    agnostic.collect()

    NodeFork(
        uid =   "bravery",
        choices = {
            "altars": """Make another visit to
            the altars""",
            "battle": """Defend the outpost!
            Get a sword!""",
        },
    )
    agnostic.collect()

    # ROUTE TO SUCCESSFUL BATTLE
    ConditionFork(
        uid=           "battle",
        condition =    "sack.mars == True",
        trueNodeUid=   "battleSuccess",
        falseNodeUid=  "battleFailure",
    )
    agnostic.collect()

    # battle win
    ThroughPage(
        uid =           "battleSuccess",
        time = incrementTime,
        goalBoxUid =    paddockBox.uid,
        change = SackChange(
            trigger =   "sack.superhorse == False",
            assign =    { "superhorse":True},
            plus  =     { "marspoints":4 },
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
            and DIE! Mars help us!"""
        ],
        goalBoxUid =    paddockBox.uid,
        nextNodeUid =   "retirement",
    )
    agnostic.collect()

    finalReport = (
        """You completed your
        adventure! Epona will
        favour {{sack.eponapoints}} horses for
        you when you die!
        Return to {{node.goalBox.label}}
        to respawn & try again!"""
    )

    ThroughPage(
        uid = "retirement",
        goalBoxUid = entranceBox.uid,
        page = """Bad luck. Respawned.
        Begin your adventure
        again! Epona will
        favour {{sack.eponapoints}} horses for
        you when you die!
        """,
        missTemplate = finalReport,
        nextNodeUid = "landing",
    )

    agnostic.collect()

    ThroughSequence(
        uid = "retirementsuccess",
        goalBoxUid = paddockBox.uid,
        sequence = [
            #234567889012345678901234
            """WELL DONE! VICTORY!
            The gods are with you!""",
            """{% if sack.eponapoints < 10 %}You've driven back
            the hordes but will
            you manage next time?
            Will we have the
            right horses?
            {% endif %}{% if sack.eponapoints >= 10 %}With this horse
            we can breed horses
            for the next generation
            of Hadrian's cavalry!
            {% endif %}
            """,
            """Your adventure is over.
            Epona favours {{sack.eponapoints}} horses
            and Mars will make {{sack.marspoints}}
            great cavalryman for
            the wall
            Return to {{node.goalBox.label}}
            to respawn.""",
        ],
        missTemplate = finalReport,
        nextNodeUid = "landing",
    )
    agnostic.collect()
