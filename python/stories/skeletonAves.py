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
            "pages": 0,
            "Leared": False,
            "audubon": False,
            "bonnet": False,
            "beard": False,
            "pussy": False,
            "turkey": False,
            "owl": False,
            "lark": False,
            }
)

with story:
    groundBox = Box( uid="1", label="Vol I", description="Ground Floor")
    oakBox = Box( uid="2", label="Vol II", description="The Oak Room")
    pictonBox = Box( uid="3", label="Vol III", description="The Picton Room")
    archiveBox = Box( uid="4", label="Vol IV", description="The Archives")

    entranceBox = groundBox

    # populate with passages
    ThroughPage(
            uid="firstLanding",
            goalBoxUid=entranceBox.uid,
            page=introText,
            nextNodeUid="landing",
            )

    ConditionFork(
            uid= "tinbergenCheck",
           condition = "sack.audubon == True",
            falseNodeUid = "adventureChoice",
            trueNodeUid = "tinbergensGame",
            )

    ConditionFork(
            uid= "completeCheck",
            condition = "sack.Leared == True and sack.audubon == True",
            falseNodeUid = "pictonSecond",
            trueNodeUid = "endGame",
            )

    ThroughPage(
            uid="landing",
            goalBoxUid=entranceBox.uid,
            change = SackChange(
                reset=story.startSack
            ),
            page="""You have stumbled upon
            the first of 4 unusual
            volumes hidden in the
            library...""",
            nextNodeUid="foyerIntro",
            )


    ThroughSequence(
            uid= "foyerIntro",
            #123456789012345678901234
            goalBoxUid = groundBox.uid,
            nextNodeUid = "firstOak",
            sequence = [
            """You are on the ground
            floor beautiful levels
		    of knowledge above you.
            """,
            """Go FIND the Oak Room
            with the biggest book
            in the library to
            continue your adventure!""",
            ],
            )

    ThroughSequence(
            uid= "firstOak",
		    sequence = [
		    #23456789012345678901234
            """In front of you in the
            case is the infamous
            "Birds of America" by
            John James Audubon a
            great naturalist, artist
            and hunter""",
            """This book is the key
            to your adventure! And
            it's part of why this
            library exists...""",
            """GO to the Picton
            Reading Room QUIETLY
            to find out more...""",
            ],
            goalBoxUid = oakBox.uid,
            nextNodeUid = "pictonStart",
            )

    ThroughSequence(
            uid="pictonStart",
            goalBoxUid=pictonBox.uid,
            sequence=[
            # embellish and explain
            #23456789012345678901234
            """OK be quiet, like in
            the British Museum
            reading room it was
            modelled on, people here
            can hear you across the
            other side of the room""",
            """You are going to make
            a slim volume for the
            13th Earl of Derby,
            his collection led to
            this library being
            built...""",
            """Do you want to take the
            path of the hunter or
            a lyrical journey of
            Liverpudlian patronage?""",
            ],
            nextNodeUid="adventureChoice",
            )

    ThroughSequence(
            uid="pictonSecond",
            goalBoxUid=pictonBox.uid,
            sequence=[
            #23456789012345678901234
            """Did you know that this
            is the worlds first
            library to be lit by
            electricity?...""",
            """You could inform the
            Lord Stanley on progress
            or hurry along with
            your book...""",
            ],
            nextNodeUid="checkinChoice",
            )

    NodeFork(
            uid = "checkinChoice",
            page = "What do you want to do?",
            choices = {
                "Derby1": """Check in with
                the Earl of Derby""",
                "hurryUp": """Let's get
                this book
                finished!""",
                },
            )

    ThroughPage(
            uid="hurryUp",
            goalBoxUid = groundBox.uid,
            #23456789012345678901234
            page="""
            Let's finish this thing!
            ...""",
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
                "Lear": "sack.Leared==True",
                },
            )

    ThroughSequence(
            uid="Lear",
            goalBoxUid = groundBox.uid,
            #goalBoxUid = archiveBox.uid,
            nextNodeUid="poemChoice",
            #23456789012345678901234
            sequence=[
            """Audubon's patron, the
            13th Earl of Derby was
            also the patron of the
            poet and painter Edward
            Lear...""",
            """Lear was invited to
            Knowsley Hall to paint
            from Lord Stanley's
            collection of birds &
            animals...""",
            """Unlike Audubon, he
            would only draw from
            real live birds...
            you could say this
            might be why he was a
            poet and not a hunter..""",
            """Try to FIND 3 Lear
            poems in the library and
            write them in the
            INVENTORY in your
            booklet...""",
            """RETURN here
            once you FIND all
            of his poems.""",
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
                "bonnetGround": "Archives",
                "oldManOak": "Oak Room",
                "owlPicton": "Reading Room",
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
                plus = { "pages":1 },
                assign = {"bonnet": True},
                ),
            goalBoxUid = archiveBox.uid,
            #23456789012345678901234
            #needs logic for saying '1 page'
            sequence = [
            """There was a Young Lady
            whose bonnet,
            Came untied when the
            birds sat upon it;...""",
            """All the birds in the air
            Are welcome to sit on my
            bonnet!""",
            """You write it down in
            your booklet ready for
            your book...""",
            """You now have {{ sack.pages }} pages
            Carry on...
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
                plus = { "pages":1 },
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
            """You write it down in
            your booklet ready for
            your book...""",
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
                plus = { "pages":1 },
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
            """You write it down in
            your booklet ready for
            your book...""",
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
            goalBoxUid = groundBox.uid,
            nextNodeUid="poemChoice",
            sequence = [
            #23456789012345678901234
            """Your lyrical search
            for content continues...
		    You are doing well!
            Another page for Lear.
            {% if sack.pages < 2 %}You have {{ sack.pages }} page so far,
            keep looking!
		    {% else %}
            You have {{ sack.pages }} pages now!
            Carry on!
            {% endif %}
            """
            ],
            )

    ThroughPage(
            uid="LearSuccess",
            change = SackChange(
                trigger = "sack.Leared == False",
                assign = {"Leared": True},
                ),
            # Add logic for publishing message
            #May need changing to 2 oakBox
            #23456789012345678901234
            goalBoxUid = pictonBox.uid,
            nextNodeUid="completeCheck",
            page = """Great rhymes! You
            have {{ sack.pages }} pages toward your
            slim volume! Go get it
            published!
            {% if sack.audubon == False %}Now I think you need to
            do some twitching...{% endif %}
            """,
            )

    ThroughSequence(
            uid="Audubon",
            goalBoxUid = oakBox.uid,
            sequence=[
            #123456789012345678901234
            #elaborate
            """Audubon hunted his birds
            pinned them in place and
            drew them life size in
            the 'elephant' portfolio
            size you see in the Oak
            Room...""",
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
                "Turkey": """The Ground Floor""",
                "Owl": """The Reading Room""",
                "Lark": """Larkin about the
                archives""",
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
                plus = { "pages":1 },
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
                plus = { "pages":1 },
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
                plus = { "pages":1 },
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
		    {% if sack.pages < 3 %}You are doing ok!
            You have {{ sack.pages }} so far,
            keep looking!
		    {% endif %}
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
            page = """Congratulations!
            You have drawn {{ sack.pages }} pages
            in your notebook.
            Onwards with your book!
            {% if sack.Leared == False %}Maybe some humerous
            poems would be nice...{% endif %}
            """,
            nextNodeUid="completeCheck",
            )

    ThroughSequence(
            uid="Derby1",
            goalBoxUid = archiveBox.uid,
            change = SackChange(
                plus = { "pages":1 },
                ),
            sequence=[
                #123456789012345678901234
            """An old man in victorian
            clothes is sitting by the
            microfiche machine... he
            shakes his head...""",
             """'Why this is like the
            opposite of Audubon;
            collecting knowledge in
            tiny images!'...""",
            """I could be patron to
            thousands more books if
            we had this in my day...""",
            """I see you have the start
            of something, maybe Lear
            and Audubon together is
            a nice idea...""",
            """I'll write a preface
            if you like! I've written
            to Darwin you know...""",
            """
            {% if sack.audubon == True %}
                That's fine work. They
                are important specimens!
                Audubon would be proud
                of your tenacity...
            {% else %}
                Ah Lear, such a lover of
                drawing living animals
                at Knowsley Hall when he
                wasnt reading rhymes
                to the children!...
            {% endif %}""",
            """CARRY ON with the work
            my friend, I'm going to
            look up my descendants
            on this machine...""",
            ],
            #change to tinbergenCheck
            nextNodeUid="tinbergenCheck",
            #nextNodeUid="adventureChoice",
            )

    ThroughSequence(
            uid= "tinbergensGame",
            goalBoxUid = pictonBox.uid,
		    sequence = [
		    #23456789012345678901234
            """You see a man with
            white hair and glasses
            making a really strange
            model of a bird""",
            """It's not very realistic
            not like Audubon's work!
            The eyes are huge and
            its brightly coloured
            like a cartoon image...""",
            """You ask him what he's
            doing...it looks wrong!
            'My name's Niko
            Tinbergen and this is
            some superstimuli...""",
            """I'm an ornithologist
            I suppose like Audubon,
            but more like Edward
            Lear; I only observe
            birds in their natural
            context...""",
            """I've done this on
            Walney island & I think
            this exagerated bird
            will attract birds more
            than a realistic one...""",
            """Maybe you could use
            this for something?""",
            ],
            nextNodeUid = "stimuliChoice",
            )

    NodeFork(
            uid = "stimuliChoice",
            page = """Do you want to try
            superstimuli?""",
            choices = {
                "superStimuli": """Ok I'll try, maybe
                animals are quite
                complicated""",
                "noThanks": """No thanks I'm
                busy collecting""",
                },
            )

    ThroughSequence(
            uid="superStimuli",
            goalBoxUid = oakBox.uid,
            change = SackChange(
                plus = { "pages":1 },
                ),
            sequence=[
		    #23456789012345678901234
            """You take the odd
            bird head and place it
            on the floor...""",
            """after a while you hear
            fluttering sound and a
            gull approaches the head
            and keeps perfectly still
            striking a pose!...""",
            """You draw it in your
            notebook""",
            """A long haired man
            appears next to you...
            he looks like Audubon!
            'Whats this? a lesser
            black-backed Gull,
            Larus fuscus...""",
            """All the way from
            Walney Island let me
            get my gun!'...""",
            """But the gull is
            more complex than 19th
            century science assumes,
            out of context, it flys
            through the skylight""",
            """This will make an
            interesting extra page
            for your book but
            no kill for Audubon!
            """,
            ],
            nextNodeUid="extraBird",
            )

    ThroughPage(
            uid="extraBird",
            goalBoxUid = pictonBox.uid,
            #23456789012345678901234
            page="""
            You hear a shot in the
            distance and a shout
            Audubon must have lost
            his extra bird!""",
            nextNodeUid="adventureChoice",
            )


    ThroughPage(
            uid="noThanks",
            goalBoxUid = groundBox.uid,
            #23456789012345678901234
            page="""
            No thanks that doesn't
            seem right. Birds are
            simple mechanisms...
            I'm going to carry on
            19th century style...""",
            nextNodeUid="adventureChoice",
            )

    ThroughPage(
            uid="endGame",
            goalBoxUid = oakBox.uid,
            page="""
            Game Over! You made {{ sack.pages }}
            pages for publication!
            Lord Derby's feedback..
            {% if sack.pages == 7 %}'A Well written preface!'
            The glory of science!
            Go to Vol I to respawn{% endif %}
            {% if sack.pages == 8 %}'Amazing ethology page!
            Animals know things!'
            Go to Vol I to respawn{% endif %}
            {% if sack.pages < 7 %}'A modest collection.
            Better luck next time'
            Go to Vol I to respawn{% endif %}
            """,
            nextNodeUid="firstLanding",
            )
