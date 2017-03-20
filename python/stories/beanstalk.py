from milecastles import Story, Box, ThroughPage, ThroughSequence, ConditionFork, NodeFork, SackChange
from engines.console import ConsoleSiteEmulator
# inspects the module to figure out the story name (e.g. corbridge)
storyName = __name__.split(".")[-1]

# create story
story = Story(
    uid=storyName,
    # choose an alternative startNodeUid and startSack for debugging
    #startNodeUid = "stoneFork",
    startNodeUid = "landing",
    startSack={
        "beans":False,
        "beanstalk":False,
        "beanssewn":False,
        "evicted":False,
        "hours":0,
        "points":0,
        }
)

with story:

    homeBox =       Box( uid="1",   label="Box I",      description="at Jack's Mother's house")
    roadBox =       Box( uid="2",   label="Box II",     description="on The Road")
    gardenBox =     Box( uid="3",   label="Box III",     description="in The Garden")

    entranceBox = homeBox
# An additional var if you're doing hella SackChanges
    incrementTime = SackChange(
        plus={"hours":1}
    )

    ThroughPage(
        uid="landing",
        change=SackChange(
            reset=story.startSack
        ),
        time = incrementTime,
        #2345678901234567890123456
        page="""Times are hard in Jack's\nHouse, his Father was lost\nin the robot protests.\nJack, you need to sell\nstuff basically.\n
        """,
        missTemplate="Go to {{node.getGoalBox(story).label}} to sell something",
        goalBoxUid = homeBox.uid,
        nextNodeUid = "homeArrive"
    )

#This is a conditional
    ConditionFork(
            uid = "homeArrive",
            condition = "sack.beanstalk or sack.evicted",
            falseNodeUid = "homeIntro",
            trueNodeUid = "ending",
            )

    ThroughPage(
            uid="homeIntro",
            page = "You are at home.",
            nextNodeUid = "homechoice",
            goalBoxUid = homeBox.uid,
            )

    NodeFork(
            uid = "homechoice",
            choices = {
                "selling": "Sell some things at market",
                "watchTV": "Watch TV"
                },
            )

    ThroughPage(
            uid = "watchTV",
            page= "You watch TV, There's nothing on.",
            goalBoxUid = gardenBox.uid,
            nextNodeUid = "evicted",
            )

    ThroughPage(
            uid = "evicted",
            change = SackChange(
                #trigger = "sack.evicted == False",
                assign = { "evicted":True },
                ),
            page= "You have been evicted",
            goalBoxUid = gardenBox.uid,
            nextNodeUid = "homeArrive",
            )

    ConditionFork(
            uid = "selling",
            condition = "sack.beans",
            trueNodeUid = "home",
            falseNodeUid = "sellingstuff",
            )

    ThroughPage(
            uid="sellingstuff",
            page="What could I sell\nI wonder?",
            goalBoxUid = homeBox.uid,
            missTemplate="Go to {{node.getGoalBox(story).label}} to sell something",
            nextNodeUid = "sellingchoices"
            )

    NodeFork(
            uid= "sellingchoices",
            choices = {
                "sellcow": "to sell the cow\nat the market",
                "sewbeans": "to look for junk in the garden",
                },
            hideChoices = {
            },
            )

    ThroughPage(
        uid="sellcow",
        time=incrementTime,
        change = SackChange(
            trigger = "sack.beans == False",
            assign=     { "beans":True }
        ),
        #missTemplate="Go to {{node.getGoalBox(story).label}} to sell the cow",
        page="""
        {% if node.change.triggered %}
            {% if node.change.completed %}
            You head to the road.\nYou meet a man who\n buys the cow for some\nbeans\nWow beans!
            {% else %}
            You're on the road. Nobody around since\nthe bypass was built
            {% endif %}
        {% else %}
        You already sold the cow\nto some guy.
        {% endif %}
        """,
        goalBoxUid = roadBox.uid,
        nextNodeUid = "home"
    )

    ThroughPage(
        uid="home",
        page="""
        You are at home.
        {% if sack.beans == True %}
            You have some beans
        {% else %}
            You have nothing.
            Your mother weeps.
        {% endif %}
        """,
        missTemplate="Go to {{node.getGoalBox(story).label}} your mother needs you",
        goalBoxUid = homeBox.uid,
        nextNodeUid = "fortune"
    )

    NodeFork(
        uid =   "fortune",
        choices = {
            "sewbeans": "Get rid of the beans in the garden",
            "leavehome": "Return to the market",
            },
        hideChoices = {
            },
        )

# ROUTE TO SEW beans

    ConditionFork(
        uid =           "sewbeans",
        condition =     "sack.beans == True",
        trueNodeUid=    "sewbeanSuccess",
        falseNodeUid=   "sewbeanFailure",
        )

    ThroughPage(
        uid="sewbeanSuccess",
        goalBoxUid = gardenBox.uid,
        time=incrementTime,
        change = SackChange(
            trigger =   "sack.beanssewn == False",
            assign=     { "beanssewn":True },
            plus =      { "points":1 },
        ),
        page = """
        {% if node.change.triggered %}
            {% if node.change.completed %}
                You throw the beans on the ground. Nothing happens.
            {% else %}
                There's nothing in the\ngarden
            {% endif %}
        {% else %}
            No nothing in the garden for ebay
            {% endif %}
        """,
        nextNodeUid = "bed"
    )

    ThroughPage(
        uid="sewbeanFailure",
        goalBoxUid = gardenBox.uid,
        time=incrementTime,
        change = SackChange(
            minus ={ "points":1 },
        ),
        page = """
        There's nothing in the\ngarden
        """,
        missTemplate="Go to {{node.getGoalBox(story).label}} to continue your adventure",
        nextNodeUid = "homeArrive"
    )


    ThroughPage(
        uid="bed",
        time=incrementTime,
        change = SackChange(
            assign={"slept":True},

        ),
        missTemplate="Go to {{node.getGoalBox(story).label}} to continue your adventure",
        page="You go to bed and sleep\nwith terrible dreams\nabout giant food",
        goalBoxUid = gardenBox.uid,
        nextNodeUid = "beanstalkgrow"
    )

# ROUTE TO GROW THE BEANSTALK

    ConditionFork(
        uid =           "beanstalkgrow",
        condition =     "sack.beanssewn == True",
        trueNodeUid=    "beanstalkgrowSuccess",
        falseNodeUid=   "beanstalkgrowFailure",
        )

    ThroughSequence(
        uid="beanstalkgrowSuccess",
        change = SackChange(
            trigger = "sack.beanstalk == False",
            assign={ "beanstalk":True },
            plus = { "points":10 },
            ),
        goalBoxUid = gardenBox.uid,
        sequence = [
            "You are in the garden\nThe beanstalk towers\nabove you!\nFortune smiles on Jack\n"
            "But what adventure\nAwaits him at the top?"
            ],
        missTemplate="Go to {{node.getGoalBox(story).label}} to continue your adventure",
        nextNodeUid = "homeArrive",
        )

    ThroughPage(
            uid="beanstalkgrowFailure",
            change = SackChange(
                minus = { "points":1 },
                ),
            page="There's nothing in the garden",
            goalBoxUid = gardenBox.uid,
            nextNodeUid = "home",
            )

    ThroughPage(
        uid = "leavehome",
        page = """
        You leave home for the town.
        It's abandoned.
        A chill wind blows
        """,
        goalBoxUid = roadBox.uid,
        missTemplate="Go to {{node.getGoalBox(story).label}} to continue your adventure",
        nextNodeUid = "homeArrive",
        )

    ThroughPage(
        uid="ending",
        goalBoxUid = entranceBox.uid,
        page="""
        The end.\nYou scored {{sack.points}} points\n
        TAP TO CONTINUE...
        """,
        missTemplate="The end.\nYou scored {{sack.points}} points\nReturn to {{node.goalBox.label}} to respawn.",
        nextNodeUid = "landing"
    )

if __name__ == "__main__":
    print("Loading emulator")
    emulator = ConsoleSiteEmulator(story=story)
    print("Running Emulator")
    emulator.run()
