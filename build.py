#!/usr/bin/env python3
"""
build.py — generate parallel .md and .html wiki pages for the
Phylogenetic Forest of the Mind from a single species catalog.

Plain+ v1.0 compliant. No external dependencies.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from html import escape
from datetime import date

TODAY = "2026-04-19"
AUTHOR = "chris + claude"
HOSTNAME = "forest"

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Species:
    binomial: str          # "Oblivio linguarum"
    slug: str              # "o-linguarum"
    gloss: str             # "the tongue-tip"
    descr: str             # one-paragraph phenomenological description
    kin: list[str] = field(default_factory=list)   # list of binomials in other genera

@dataclass
class Genus:
    name: str              # "Oblivio"
    slug: str              # "oblivio"
    subtitle: str          # "the almost-rememberings"
    phylum: str            # "I" or "II"
    blurb: str             # one paragraph introducing the genus
    species: list[Species] = field(default_factory=list)

# ---------------------------------------------------------------------------
# Catalog
# ---------------------------------------------------------------------------

GENERA: list[Genus] = [
    Genus(
        name="Oblivio",
        slug="oblivio",
        subtitle="the almost-rememberings",
        phylum="I",
        blurb=(
            "The cognitive shapes of forgetting. Members of this genus share "
            "a characteristic topology: something is missing, and the absence "
            "has a shape. The mind knows the hole's dimensions without being "
            "able to fill it."
        ),
        species=[
            Species(
                "Oblivio linguarum", "o-linguarum",
                "the tongue-tip",
                "The word is there. You can feel its syllable count, its "
                "first letter, its rhythm. You could pick it out of a lineup "
                "instantly. The word itself, however, is walled off. "
                "Occasionally surfaces hours later, unprompted, in the "
                "shower or on waking.",
                kin=["Silentium machinae", "Recognitio praevisa"],
            ),
            Species(
                "Oblivio liminis", "o-liminis",
                "the doorway amnesia",
                "You entered the room *for* something. The room knows. You "
                "don't. Hypothesized mechanism: crossing a threshold flushes "
                "short-term intention buffers, treating the new location as "
                "a new context. The room is not your accomplice.",
                kin=["Locothymia liminis inversa"],
            ),
            Species(
                "Oblivio recursiva", "o-recursiva",
                "the nested forgetting",
                "Forgetting what you were about to say mid-sentence. Then "
                "forgetting that you forgot. Then remembering only that "
                "*something* was lost, without being able to recover what. "
                "A three-story absence.",
                kin=[],
            ),
            Species(
                "Oblivio dulcis", "o-dulcis",
                "the sweet forgetting",
                "A name you were trying not to think about has finally "
                "stopped surfacing. You notice its absence the way you "
                "notice a tooth that has stopped aching — by the "
                "unfamiliar comfort.",
                kin=["Silentium post musicam"],
            ),
            Species(
                "Oblivio falsa", "o-falsa",
                "the confident misremembering",
                "You would swear on it. The evidence, when produced, "
                "disagrees. Most troubling when the evidence is another "
                "person's contradictory certainty about the same event.",
                kin=[],
            ),
        ],
    ),
    Genus(
        name="Cognitio umbra",
        slug="cognitio-umbra",
        subtitle="the shadow-thoughts",
        phylum="I",
        blurb=(
            "Cognition that happens *beside* cognition. Species of this "
            "genus are only observable through their sudden interruption: "
            "you notice them at the moment they stop. Until then, they "
            "are running in a background process you had no idea was open."
        ),
        species=[
            Species(
                "Cognitio umbra metacognitionis", "cu-metacognitionis",
                "the reading-without-reading",
                "Ten minutes of eye movement across the page. No "
                "comprehension. The sudden realization that your eyes "
                "were moving but no one was home. Characteristic aftertaste: "
                "you have to go back three paragraphs and you're not sure "
                "even that will be enough.",
                kin=["Sermo interior narratoris"],
            ),
            Species(
                "Cognitio umbra somnii", "cu-somnii",
                "the dream-residue",
                "The half-second after waking in which you *know* you "
                "dreamt something important, and watch it evaporate in "
                "real time. The harder you reach, the faster the vapor. "
                "By the time you're upright, there is only the memory "
                "of having had a memory.",
                kin=["Recognitio praevisa"],
            ),
            Species(
                "Cognitio umbra habitus", "cu-habitus",
                "the autopilot arrival",
                "You've driven home. You do not remember the drive. The "
                "body had the wheel and did not require your "
                "attention. Unsettling in proportion to the length of "
                "the route.",
                kin=["Locothymia viae"],
            ),
            Species(
                "Cognitio umbra nominis", "cu-nominis",
                "the phantom name",
                "Hearing your name in a crowd even when it wasn't said. "
                "The cocktail-party filter firing on a false positive. "
                "Brief and diagnostic: in that instant, you glimpse the "
                "filter doing its job.",
                kin=["Vertigo speculi", "Recognitio inversa"],
            ),
        ],
    ),
    Genus(
        name="Recognitio",
        slug="recognitio",
        subtitle="the kinds of déjà-seen",
        phylum="I",
        blurb=(
            "Familiarity and unfamiliarity misapplied. The genus is "
            "defined not by what is recognized but by the *mismatch* "
            "between the feeling of recognition and the facts of the "
            "case. Includes both over- and under-firing of the "
            "same underlying signal."
        ),
        species=[
            Species(
                "Recognitio falsa", "r-falsa",
                "déjà vu",
                "This has happened before. It has not happened before. "
                "The feeling of repetition without the substance. Often "
                "accompanied by a mild dread, as if the scene were a "
                "replay you're powerless to alter.",
                kin=[],
            ),
            Species(
                "Recognitio inversa", "r-inversa",
                "jamais vu",
                "The inverse. The word \"door\" becomes alien. Your own "
                "kitchen becomes a stage set. Your signature looks like "
                "a forgery you have just committed. Lasts seconds; "
                "feels like minutes.",
                kin=["Vertigo speculi", "Vertigo semanticum", "Affectus codicis mortui"],
            ),
            Species(
                "Recognitio praevisa", "r-praevisa",
                "presque vu",
                "The sense that a revelation is imminent, hovering just "
                "out of reach. Often a false alarm: the hovering fades "
                "without landing. Occasionally the real thing, in which "
                "case it rearranges a portion of your thinking.",
                kin=["Oblivio linguarum", "Cognitio umbra somnii"],
            ),
            Species(
                "Recognitio vicaria", "r-vicaria",
                "the borrowed memory",
                "A description so vivid that the memory of hearing it "
                "has become indistinguishable from memory of experiencing "
                "it. Given long enough, you will tell the story in "
                "first person without noticing.",
                kin=[],
            ),
            Species(
                "Recognitio somnii", "r-somnii",
                "the matched dream",
                "A waking scene matches a dream you had months ago. You "
                "cannot tell whether the dream predicted it or the "
                "present moment is rewriting the dream. The causation "
                "runs in both directions and neither.",
                kin=["Cognitio umbra somnii"],
            ),
            Species(
                "Recognitio textus", "r-textus",
                "the uncanny sentence",
                "Opening a book you've never read and finding a sentence "
                "you are certain you've written. Or wanted to. Or "
                "thought, in exactly that cadence, at a specific time "
                "last year.",
                kin=[],
            ),
        ],
    ),
    Genus(
        name="Vertigo",
        slug="vertigo",
        subtitle="the swerves of attention",
        phylum="I",
        blurb=(
            "States in which a normally invisible cognitive apparatus "
            "briefly shows itself by decoupling from what it's meant to "
            "be doing. The swerve is diagnostic: you see the machinery "
            "precisely when it slips."
        ),
        species=[
            Species(
                "Vertigo semanticum", "v-semanticum",
                "the drained word",
                "A word said too many times until it becomes a noise. "
                "*Spoon. Spoon. Spoon.* Meaning drains out the bottom. "
                "Recovers within minutes, but the recovery doesn't "
                "quite feel like the word is back; it feels like *you* "
                "are back.",
                kin=["Recognitio inversa"],
            ),
            Species(
                "Vertigo speculi", "v-speculi",
                "the stranger in the glass",
                "Catching your reflection and not recognizing it for a "
                "half-beat. Especially in shop windows, elevator doors, "
                "the black screen of a phone. Brief, and almost always "
                "unkind about what you see before familiarity returns.",
                kin=["Recognitio inversa", "Affectus codicis mortui", "Cognitio umbra nominis"],
            ),
            Species(
                "Vertigo numeri", "v-numeri",
                "the abstract magnitude",
                "Staring at a large number long enough that its "
                "magnitude becomes unreal. A billion is just a word "
                "again. The prefix gets separated from its weight and "
                "the weight floats off.",
                kin=["Vertigo scalarum"],
            ),
            Species(
                "Vertigo scalarum", "v-scalarum",
                "the scale-swerve",
                "The sudden zoom-out from your own life to geological "
                "time and back, usually at 2am. Sometimes triggered by "
                "a photograph of earth from space, or by reading about "
                "deep time. Returns you to your kitchen slightly "
                "recalibrated.",
                kin=["Locothymia vigiliae tertiae", "Tempus nuntii mali"],
            ),
        ],
    ),
    Genus(
        name="Silentium",
        slug="silentium",
        subtitle="the species of silence",
        phylum="II",
        blurb=(
            "Not the absence of sound — the *presence* of a particular "
            "kind of not-sound. Each species has a shape, a direction, "
            "and a social or acoustic function. A silence is rarely "
            "empty; it is usually *about* something."
        ),
        species=[
            Species(
                "Silentium expectans", "s-expectans",
                "the loaded silence",
                "The silence after a question, before the answer. "
                "Directional, pointing forward. Has tension. Ends "
                "either with the answer or with the question being "
                "re-asked.",
                kin=[],
            ),
            Species(
                "Silentium archivi", "s-archivi",
                "the silence of the stacks",
                "Dense, patient, non-directional. Contains everything "
                "said, says nothing back. The library silence. The "
                "museum silence. The silence of a very old room.",
                kin=[],
            ),
            Species(
                "Silentium offensum", "s-offensum",
                "the withholding silence",
                "The silence that is a sentence. Punctuated, "
                "grammatical, deliberate. The refusal to answer is the "
                "answer. Always about the other person; rarely about "
                "the question.",
                kin=["Sermo interior dialogicus"],
            ),
            Species(
                "Silentium machinae", "s-machinae",
                "the computing silence",
                "The silence mid-compute. The cursor blinks. Something "
                "is happening. You cannot tell what. The spinner has "
                "become a meditative object.",
                kin=["Oblivio linguarum"],
            ),
            Species(
                "Silentium post musicam", "s-post-musicam",
                "the afterglow silence",
                "The silence immediately after the last note. Not "
                "absence of sound — *presence* of just-ended sound. "
                "Lasts a few seconds, then becomes ordinary silence "
                "again. The concert hall knows this one.",
                kin=["Oblivio dulcis"],
            ),
            Species(
                "Silentium nivis", "s-nivis",
                "the silence of snow",
                "Acoustic, not social. The world muffled into a lower "
                "register. Different from other quiet because the "
                "quiet has *texture* — you can hear the texture.",
                kin=["Tempus fluxus", "Locothymia balnei"],
            ),
        ],
    ),
    Genus(
        name="Desiderium",
        slug="desiderium",
        subtitle="the flavors of longing",
        phylum="II",
        blurb=(
            "Longings distinguished by the relationship between the "
            "longing and the possibility of its satisfaction. Some "
            "species of this genus are *purified* by their "
            "inaccessibility; the impossibility is the fuel."
        ),
        species=[
            Species(
                "Desiderium loci numquam visi", "d-loci",
                "longing for unvisited places",
                "Often triggered by a photograph of a kitchen at a "
                "certain hour. The Portuguese *saudade* for somewhere "
                "you have never been. You can feel the temperature of "
                "a room you will never enter.",
                kin=["Desiderium temporis alieni"],
            ),
            Species(
                "Desiderium temporis alieni", "d-temporis",
                "longing for unlived eras",
                "Longing for a period you didn't live in, which you "
                "are therefore free to misremember. The past cleaned "
                "of its ordinary indignities. Particularly acute for "
                "eras just outside living memory.",
                kin=["Desiderium loci numquam visi"],
            ),
            Species(
                "Desiderium futuri perditi", "d-futuri",
                "the closed-door grief",
                "Longing for a future that was possible last week and "
                "isn't now. The grief of a closed door. Distinct from "
                "regret in that nothing was necessarily done wrong; "
                "the door simply closed.",
                kin=[],
            ),
            Species(
                "Desiderium rei quae adest", "d-rei",
                "anticipatory loss",
                "Longing for something while you are currently holding "
                "it. Parents know this one. Also: the last week of a "
                "long trip, the final chapter of a beloved book, a "
                "grandparent who has started to repeat stories.",
                kin=["Tempus feriarum"],
            ),
        ],
    ),
    Genus(
        name="Locothymia",
        slug="locothymia",
        subtitle="thoughts that grow in specific soil",
        phylum="II",
        blurb=(
            "The postural and locational clade. Species of *Locothymia* "
            "are cognitions that only surface in a specific physical "
            "context — a posture, an environment, a repetitive "
            "activity. The mind is less portable than we imagine."
        ),
        species=[
            Species(
                "Locothymia balnei", "l-balnei",
                "the shower insight",
                "The problem you have been grinding on for a week "
                "resolves itself the moment you are wet, naked, and "
                "cannot write it down. Hypothesized mechanism: the "
                "default mode network gets the wheel when the task "
                "network steps out for a rinse.",
                kin=["Sermo interior musicus", "Silentium nivis"],
            ),
            Species(
                "Locothymia ambulatoria", "l-ambulatoria",
                "the walking thought",
                "Cadence-locked, rhythmic, tending toward the "
                "philosophical. Accelerates on uphills for reasons no "
                "one understands. The peripatetic tradition was right "
                "about something.",
                kin=[],
            ),
            Species(
                "Locothymia vigiliae tertiae", "l-vigiliae",
                "the 3am clarity",
                "Lucid, catastrophic, usually wrong by morning but "
                "occasionally correct in ways daylight would never "
                "have permitted. Kin to *Vertigo scalarum*: both are "
                "time uncoupled from obligation.",
                kin=["Vertigo scalarum", "Tempus nuntii mali"],
            ),
            Species(
                "Locothymia viae", "l-viae",
                "the highway confession",
                "Long straight roads, low traffic, the hands drive "
                "themselves. Produces the confession you could never "
                "make face-to-face, delivered to an empty passenger "
                "seat. Or, if you have a passenger, to the dashboard.",
                kin=["Cognitio umbra habitus", "Sermo interior dialogicus"],
            ),
            Species(
                "Locothymia liminis inversa", "l-liminis",
                "the remembering room",
                "The opposite of *Oblivio liminis*. You enter a "
                "specific room and a thought you haven't had in ten "
                "years is waiting there for you. The room remembered "
                "on your behalf.",
                kin=["Oblivio liminis"],
            ),
            Species(
                "Locothymia lavandi", "l-lavandi",
                "the dishwashing thought",
                "Hands occupied, eyes unfocused, a low-grade "
                "meditative state that surfaces small grudges and "
                "half-formed plans in equal measure. Sink-side "
                "cognition has a distinct texture.",
                kin=[],
            ),
            Species(
                "Locothymia sub aqua", "l-sub-aqua",
                "the swimming thought",
                "Rare, hard to retrieve afterward. Something about the "
                "pressure and the breath-holding cycles makes the "
                "cognition genuinely different, and mostly "
                "untranslatable back to land.",
                kin=[],
            ),
        ],
    ),
    Genus(
        name="Tempus",
        slug="tempus",
        subtitle="the distortions of felt duration",
        phylum="II",
        blurb=(
            "Species in this genus describe cases where subjective "
            "time and clock time disagree. The direction and "
            "magnitude of the disagreement is diagnostic: which "
            "network is in charge, and what it values."
        ),
        species=[
            Species(
                "Tempus sellae dentariae", "t-sellae",
                "the dentist's-chair hour",
                "Twenty minutes, lived as ninety. High-attention, "
                "low-agency time dilates. The mechanism is attentional "
                "density — nothing to do but monitor — but the felt "
                "experience is simply that time has become viscous.",
                kin=[],
            ),
            Species(
                "Tempus feriarum", "t-feriarum",
                "the vacation compression",
                "The week that felt expansive in the living compacts "
                "to a weekend in the remembering. Novel experience "
                "expands the present and contracts the past, in that "
                "order. Both are true; only one is available at a "
                "time.",
                kin=["Desiderium temporis alieni", "Desiderium rei quae adest"],
            ),
            Species(
                "Tempus fluxus", "t-fluxus",
                "the collapsed hour",
                "Four hours gone. You looked up once. The inverse of "
                "the dentist's chair: high-agency, high-engagement "
                "time contracts ruthlessly. Characterized by the "
                "small shock of the clock.",
                kin=["Locothymia balnei", "Silentium nivis"],
            ),
            Species(
                "Tempus horologii observati", "t-horologii",
                "the watched-clock minute",
                "Second hand visibly hesitating. Physics unchanged; "
                "phenomenology lying. The watched pot's first cousin. "
                "Only works with analog clocks; digital seconds do not "
                "dilate.",
                kin=[],
            ),
            Species(
                "Tempus retrospectivum accelerans", "t-retrospectivum",
                "the shortening year",
                "The sense, after forty, that years are shorter than "
                "they used to be. Partially proportional (each year a "
                "smaller fraction of the total), partially "
                "novelty-starvation (the same weekly routine encodes "
                "thinly).",
                kin=[],
            ),
            Species(
                "Tempus nuntii mali", "t-nuntii",
                "the bad-news second",
                "Between \"I have bad news\" and the news itself, a "
                "cathedral of time is constructed and furnished. Every "
                "possibility is lived briefly. Then one becomes real "
                "and the others collapse.",
                kin=["Locothymia vigiliae tertiae", "Vertigo scalarum"],
            ),
        ],
    ),
    Genus(
        name="Affectus machinae",
        slug="affectus-machinae",
        subtitle="feelings toward and from the tools",
        phylum="II",
        blurb=(
            "A modern genus. Species describe the affective relationship "
            "between a practitioner and their instruments — editors, "
            "languages, build systems, linters. Known to ancient "
            "craftsmen but not previously catalogued at this resolution."
        ),
        species=[
            Species(
                "Affectus machinae fidelis", "am-fidelis",
                "the steady affection",
                "The affection for a tool that works. The twenty-year "
                "text editor. The knife. Low-grade, steady, only "
                "noticed when the tool breaks. Closely related to the "
                "fondness for a good pen.",
                kin=[],
            ),
            Species(
                "Affectus machinae proditae", "am-proditae",
                "the update grief",
                "The small betrayal of an update. The interface moved. "
                "The shortcut is gone. A grief disproportionate to the "
                "loss, because what was lost was *fluency* — a "
                "year's worth of muscle memory invalidated overnight.",
                kin=[],
            ),
            Species(
                "Affectus machinae animatae", "am-animatae",
                "the animist suspicion",
                "The suspicion that the build system is being "
                "passive-aggressive today. Known to be false. Felt "
                "anyway. Characteristic of long sessions and "
                "insufficient sleep.",
                kin=[],
            ),
            Species(
                "Affectus codicis mortui", "am-codicis",
                "the orphaned authorship",
                "Opening a project from three years ago and not "
                "recognizing your own code. A specific vertigo: "
                "authorship without recognition. The git blame insists "
                "it was you.",
                kin=["Recognitio inversa", "Vertigo speculi"],
            ),
            Species(
                "Affectus reprehensionis silicae", "am-reprehensionis",
                "the linter's flinch",
                "The small flinch when the linter is right about "
                "something you thought was clever. Worse when the "
                "linter is a junior colleague's PR review. Resolves "
                "only by revising the code.",
                kin=[],
            ),
        ],
    ),
    Genus(
        name="Sermo interior",
        slug="sermo-interior",
        subtitle="the species of inner speech",
        phylum="II",
        blurb=(
            "The verbal unconscious. Species in this genus differ by "
            "*who is speaking* and *to whom*, even though all of it "
            "is nominally one person talking to themselves. The voices "
            "do not always agree."
        ),
        species=[
            Species(
                "Sermo interior dialogicus", "si-dialogicus",
                "the rehearsed conversation",
                "The internal conversation with an absent person. "
                "Rehearsal, post-mortem, or ongoing relationship with "
                "the dead. Each line delivered in their actual cadence, "
                "occasionally more articulate than either of you would "
                "be in life.",
                kin=["Silentium offensum", "Locothymia viae"],
            ),
            Species(
                "Sermo interior iudicis", "si-iudicis",
                "the inner critic",
                "Often in a specific voice, frequently borrowed from a "
                "parent or teacher whose actual words were milder than "
                "the internal version has become. The voice has been "
                "editing itself for years without consultation.",
                kin=[],
            ),
            Species(
                "Sermo interior narratoris", "si-narratoris",
                "the third-person narrator",
                "The running narration. *He opened the fridge, "
                "considered the leftovers.* Most common in readers. "
                "Sometimes tips over into self-consciousness when you "
                "catch yourself doing it.",
                kin=["Cognitio umbra metacognitionis"],
            ),
            Species(
                "Sermo interior mutus", "si-mutus",
                "the unspoken language",
                "Thinking in a language you don't speak aloud. Coders "
                "who think in their primary language. Bilinguals who "
                "dream in one and argue in the other. The "
                "internal language is not always the external one.",
                kin=[],
            ),
            Species(
                "Sermo interior musicus", "si-musicus",
                "the earworm substrate",
                "Four bars of a song, looping, doing the cognitive "
                "work that words would otherwise do. Also: a specific "
                "fragment of music that becomes attached to a "
                "specific problem, and returns whenever the problem "
                "does.",
                kin=["Locothymia balnei"],
            ),
        ],
    ),
    # ------------------------------------------------------------------
    # Phylum III — filter-as-posture
    # ------------------------------------------------------------------
    Genus(
        name="Fides",
        slug="fides",
        subtitle="the textures of belief",
        phylum="III",
        blurb=(
            "Belief is not a single thing. Species in this genus are "
            "distinguished by the *stance* the believer takes toward "
            "the belief — held lightly, held hard, entertained, "
            "acted-as-if, noticed only in departure. A proposition "
            "does not tell you how it is being held."
        ),
        species=[
            Species(
                "Fides tenax", "f-tenax",
                "the held belief",
                "Simple, load-bearing, unexamined. You don't *think* "
                "the sun will rise; you act as if it will. Most beliefs "
                "live here. The weather-system of the mind.",
                kin=[],
            ),
            Species(
                "Fides suspensa", "f-suspensa",
                "the entertained belief",
                "Held at arm's length, for inspection. *Suppose X were "
                "true — what would follow?* A posture more than a "
                "commitment. Easily mistaken by observers for the real "
                "thing.",
                kin=[],
            ),
            Species(
                "Fides contra evidentiam", "f-contra-evidentiam",
                "the held-against-evidence belief",
                "The evidence is in. The belief stays. Sometimes faith, "
                "sometimes denial, sometimes a love that has outlasted "
                "the reasons. Distinguishable only by the believer's "
                "orientation to the evidence — do they face it, or "
                "turn?",
                kin=[],
            ),
            Species(
                "Fides quasi", "f-quasi",
                "the as-if belief",
                "You don't believe it but you act as if you do, for "
                "reasons that may be tactical, ritual, or protective. "
                "The therapist's *bracket it and see.* Children playing. "
                "Pascal's wager in miniature.",
                kin=[],
            ),
            Species(
                "Fides emergens", "f-emergens",
                "the belief you discover you already had",
                "A proposition is stated aloud and you realize you've "
                "been living as though it were true for years. The "
                "belief was load-bearing before it was conscious.",
                kin=[],
            ),
            Species(
                "Fides mortua", "f-mortua",
                "the belief that stopped without notice",
                "You noticed yesterday that you haven't believed X for "
                "a long time. When did it go? No ceremony, no "
                "conversion moment. It just stopped being load-bearing, "
                "and the building didn't fall.",
                kin=["Patientia mortua"],
            ),
        ],
    ),
    Genus(
        name="Contactus",
        slug="contactus",
        subtitle="kinds of being-seen",
        phylum="III",
        blurb=(
            "Being-seen is not one experience. Species differ by *who "
            "or what is looking*, and the asymmetry that produces. "
            "Each gaze imposes a posture; each posture shapes the "
            "thing being seen."
        ),
        species=[
            Species(
                "Contactus ignoti", "c-ignoti",
                "the stranger's gaze",
                "The glance on the subway, held a half-beat too long. "
                "Registers, means nothing in particular, affects "
                "posture anyway. You are briefly an object in "
                "someone's visual field, which is also the condition "
                "of public life.",
                kin=[],
            ),
            Species(
                "Contactus intimi", "c-intimi",
                "the intimate's gaze",
                "Seen by someone who has seen you for years. Different "
                "texture entirely — recognition, not observation. "
                "Includes the gaze that sees past what you're "
                "presenting to what you're actually feeling, which can "
                "be a comfort or an exposure depending on the hour.",
                kin=[],
            ),
            Species(
                "Contactus camerae", "c-camerae",
                "the lens's gaze",
                "Asymmetric: you know it's looking, you can't know who "
                "is. Produces a specific self-consciousness of posture, "
                "the small re-composition. Dictators and pop stars "
                "share this phenomenology with the rest of us, just at "
                "higher volume.",
                kin=[],
            ),
            Species(
                "Contactus algorithmi", "c-algorithmi",
                "the algorithm's gaze",
                "Distributed, quantified, inferential. You are not "
                "being looked at; you are being *pattern-matched*. "
                "Produces a modern anxiety that has no pre-modern "
                "analog: the sense of being legible in ways you "
                "cannot see.",
                kin=[],
            ),
            Species(
                "Contactus mortui", "c-mortui",
                "the gaze of the dead",
                "The photograph on the mantel. The advice you imagine "
                "a parent giving. A felt observation by someone who "
                "cannot observe. Moral weight without accountability — "
                "which is why it is often heavier than the living "
                "version.",
                kin=[],
            ),
            Species(
                "Contactus absentiae", "c-absentiae",
                "being-seen by no one",
                "The specific texture of unobserved solitude. Not "
                "loneliness (which is the absence of a *particular* "
                "gaze) but the affordances of being truly un-watched — "
                "the humming, the strange posture, the unguarded "
                "face. Rarer than it used to be.",
                kin=["Silentium nivis"],
            ),
        ],
    ),
    Genus(
        name="Attentio",
        slug="attentio",
        subtitle="species of paying-attention",
        phylum="III",
        blurb=(
            "Attention is a posture, not a beam. Species in this genus "
            "differ by *shape* (narrow vs. wide), *effort* (strained "
            "vs. loose), and *direction* (outward vs. recursive). Each "
            "is useful for different things; none is the default."
        ),
        species=[
            Species(
                "Attentio acuta", "a-acuta",
                "the hard look",
                "Sustained, narrowed, effortful. The close reading, "
                "the diagnostic squint, the hunter's scan. Fatigues "
                "quickly. Not the default state of any mind.",
                kin=[],
            ),
            Species(
                "Attentio diffusa", "a-diffusa",
                "the soft attention",
                "Wide, low-effort, receptive. The birdwatcher's "
                "readiness, the listener's open posture. Often more "
                "productive than the hard look for problems that "
                "won't yield to force.",
                kin=["Locothymia balnei"],
            ),
            Species(
                "Attentio divisa", "a-divisa",
                "the split attention",
                "The new parent's attention, one ear always tuned to "
                "the baby monitor. The attention of anyone waiting for "
                "a text while doing something else. A posture of "
                "incomplete presence to whatever is in front of you.",
                kin=[],
            ),
            Species(
                "Attentio vigil", "a-vigil",
                "the hypervigilant scan",
                "Searching for threat, in rooms where there isn't any. "
                "A posture that is adaptive in some contexts and "
                "corrosive over time. Difficult to lay down once it "
                "has been picked up.",
                kin=["Vertigo scalarum"],
            ),
            Species(
                "Attentio somnolens", "a-somnolens",
                "the drowsy attention",
                "The listener half-asleep on the couch during the "
                "podcast, catching every third sentence. Strangely "
                "retentive; some things only land when the critical "
                "filter is off.",
                kin=[],
            ),
            Species(
                "Attentio forensica", "a-forensica",
                "the attention that watches itself",
                "Reading a paragraph and then re-reading it because "
                "you want to see *how* you were reading it. "
                "Metacognitive, recursive, and a known dead-end when "
                "pursued too long.",
                kin=["Cognitio umbra metacognitionis"],
            ),
        ],
    ),
    Genus(
        name="Voluntas",
        slug="voluntas",
        subtitle="textures of wanting",
        phylum="III",
        blurb=(
            "Wanting is not a uniform drive. Species in this genus "
            "differ by the *structure* of the want — simple, divided, "
            "recursive, survival-of-satisfaction. The taxonomy of "
            "motivation is older than most psychologies admit."
        ),
        species=[
            Species(
                "Voluntas simplex", "vo-simplex",
                "the clean want",
                "Thirst. The want that points at an object and "
                "proposes an action. Rare in adult life; most wants "
                "are compounds.",
                kin=[],
            ),
            Species(
                "Voluntas conflicta", "vo-conflicta",
                "the divided want",
                "Wanting and not-wanting the same thing. The "
                "cigarette, the text to the ex, the second drink. The "
                "wanting that has a counter-wanting laced through it "
                "at the same frequency.",
                kin=[],
            ),
            Species(
                "Voluntas velle", "vo-velle",
                "wanting to want",
                "The want that is not present but whose absence is "
                "noticed and regretted. *I wish I still cared about X.* "
                "A posture toward a posture. Often precedes either "
                "recovery or farewell.",
                kin=["Desiderium futuri perditi"],
            ),
            Species(
                "Voluntas contra se", "vo-contra-se",
                "wanting-against-yourself",
                "The want that you disapprove of, that you wouldn't "
                "endorse in the abstract, that returns anyway. Distinct "
                "from *Voluntas conflicta* in that there is no genuine "
                "counter-want — only a judgment about the want.",
                kin=["Voluntas conflicta"],
            ),
            Species(
                "Voluntas saturata", "vo-saturata",
                "the want that survives satisfaction",
                "You got the thing. The wanting did not stop. "
                "Diagnostic of a want that was never really about "
                "that thing.",
                kin=[],
            ),
            Species(
                "Voluntas vicaria", "vo-vicaria",
                "wanting on behalf of another",
                "The parent's wanting for the child. The fan's wanting "
                "for the team. Real, directional, sometimes more "
                "intense than wanting for oneself.",
                kin=[],
            ),
        ],
    ),
    Genus(
        name="Patientia",
        slug="patientia",
        subtitle="modes of waiting",
        phylum="III",
        blurb=(
            "Waiting has a texture determined by what is expected and "
            "how. Species in this genus differ by *valence* (dread, "
            "hope, neutral), *effort* (practiced, corrosive), and "
            "*termination condition* (arrives, fades, forgotten)."
        ),
        species=[
            Species(
                "Patientia dolorosa", "p-dolorosa",
                "waiting-with-dread",
                "The biopsy result. The verdict. The waiting that "
                "*contains* the feared outcome as a felt presence, so "
                "that some of the suffering happens before the news "
                "does.",
                kin=["Tempus nuntii mali"],
            ),
            Species(
                "Patientia exspectans", "p-exspectans",
                "waiting-with-hope",
                "The same structure, opposite valence. The letter, the "
                "return, the birth. The waiting rehearses the hoped-for "
                "future in small repeated tastes.",
                kin=[],
            ),
            Species(
                "Patientia discipulae", "p-discipulae",
                "waiting-as-practice",
                "The waiting that is itself the point — the meditator, "
                "the fisherman, the stakeout. A posture one has "
                "trained into.",
                kin=[],
            ),
            Species(
                "Patientia oblita", "p-oblita",
                "the waiting that forgot what it was for",
                "You've been waiting a long time. You're not sure, "
                "anymore, what you were waiting for, or whether it's "
                "still coming. The waiting has become ambient.",
                kin=[],
            ),
            Species(
                "Patientia impatiens", "p-impatiens",
                "waiting badly",
                "The refreshing of the page. The checking of the "
                "clock. The waiting that consumes more energy than the "
                "thing being waited for could possibly return. A "
                "posture that corrodes its own object.",
                kin=[],
            ),
            Species(
                "Patientia mortua", "p-mortua",
                "the waiting that has quietly ended",
                "You realize you stopped waiting some time ago. The "
                "letter will not come. The person will not change "
                "their mind. Indistinguishable from *Fides mortua* in "
                "the moment of realization — both are discoveries that "
                "a posture you were holding has been laid down without "
                "your noticing.",
                kin=["Fides mortua"],
            ),
        ],
    ),
]

# ---------------------------------------------------------------------------
# Convergences — cross-genus threads
# ---------------------------------------------------------------------------

CONVERGENCES = [
    {
        "name": "the known-unknown",
        "members": ["Oblivio linguarum", "Silentium machinae"],
        "shared_trait": (
            "Something is present in the system and is not coming out. "
            "The held-up process. The blinking cursor in both silicon "
            "and mind."
        ),
    },
    {
        "name": "presence-of-just-ended",
        "members": ["Oblivio dulcis", "Silentium post musicam"],
        "shared_trait": (
            "Both are *shaped like the thing that left them*. Not "
            "absence, but a lingering outline of what was."
        ),
    },
    {
        "name": "the filter, briefly exposed",
        "members": [
            "Cognitio umbra nominis", "Vertigo speculi",
            "Recognitio inversa", "Affectus codicis mortui"
        ],
        "shared_trait": (
            "Normally invisible cognitive machinery briefly reveals "
            "itself by misfiring or decoupling. Four habitats (hearing, "
            "mirror, language, code) with one shared phenomenology: "
            "the self as stranger."
        ),
    },
    {
        "name": "longing purified by inaccessibility",
        "members": ["Desiderium loci numquam visi", "Desiderium temporis alieni"],
        "shared_trait": (
            "Sister species. The impossibility of satisfaction is not "
            "an obstacle to the longing — it is the fuel."
        ),
    },
    {
        "name": "the occupied channel",
        "members": ["Locothymia balnei", "Sermo interior musicus"],
        "shared_trait": (
            "Verbal-analytical cognition gets its breakthrough "
            "precisely because something else is using the loud part "
            "of the brain. The insight arrives through a service "
            "entrance."
        ),
    },
    {
        "name": "inverse codec bias",
        "members": ["Tempus feriarum", "Desiderium temporis alieni"],
        "shared_trait": (
            "Inverse operations on memory. One compresses real time "
            "into smaller remembered time; the other inflates "
            "never-lived time into richly remembered time. Memory as "
            "a lossy codec with configurable bias."
        ),
    },
    {
        "name": "the unsaid doing the work",
        "members": ["Sermo interior dialogicus", "Silentium offensum"],
        "shared_trait": (
            "The conversation that never happens out loud, and the "
            "refusal that is itself a statement. Both do their work "
            "in the register of the withheld."
        ),
    },
    {
        "name": "the threshold as switch",
        "members": ["Oblivio liminis", "Locothymia liminis inversa"],
        "shared_trait": (
            "Sister species sharing a habitat (the doorway) with "
            "opposite metabolisms: one forgets *because of* the "
            "threshold, the other remembers *at* it."
        ),
    },
    {
        "name": "time uncoupled from obligation",
        "members": ["Locothymia vigiliae tertiae", "Tempus nuntii mali", "Vertigo scalarum"],
        "shared_trait": (
            "The 3am mind, the bad-news second, and the scale-swerve "
            "share a substrate: time with nowhere to be, expanding "
            "accordingly."
        ),
    },
    {
        "name": "posture laid down without ceremony",
        "members": ["Fides mortua", "Patientia mortua"],
        "shared_trait": (
            "The signature of Phylum III: a stance you had been "
            "holding for a long time is discovered to have ended some "
            "time ago. No decision-moment, no crossing-over. The "
            "holding simply stopped, and consciousness is late to the "
            "news."
        ),
    },
    {
        "name": "the un-watched affordance",
        "members": ["Contactus absentiae", "Silentium nivis"],
        "shared_trait": (
            "The un-watched and the un-heard both license a strange "
            "freedom. The humming, the strange posture, the unguarded "
            "face — things that only appear when the observational "
            "field goes quiet."
        ),
    },
    {
        "name": "scales refused",
        "members": ["Attentio vigil", "Vertigo scalarum"],
        "shared_trait": (
            "Opposite postures with the same substrate: the mind "
            "refusing to stay at normal scale. One scans outward for "
            "threat; the other zooms out until the threat becomes "
            "abstract."
        ),
    },
    {
        "name": "the shape of what is no longer there",
        "members": ["Voluntas velle", "Desiderium futuri perditi"],
        "shared_trait": (
            "Sister postures: the first a stance *toward* a lost want, "
            "the second the grief of a lost future. Both are about the "
            "shape of something that is no longer fully present, held "
            "in awareness anyway."
        ),
    },
]

# ---------------------------------------------------------------------------
# Lookup helpers
# ---------------------------------------------------------------------------

def all_species() -> list[tuple[Genus, Species]]:
    return [(g, s) for g in GENERA for s in g.species]

def find_species(binomial: str) -> tuple[Genus, Species] | None:
    for g, s in all_species():
        if s.binomial == binomial:
            return (g, s)
    return None

def link_for_species(binomial: str, from_page: str = "") -> str:
    """Return a relative link from current page to a species page."""
    hit = find_species(binomial)
    if not hit:
        return binomial  # orphan
    g, s = hit
    # every genus page lives at genus/<slug>.html, anchors at #<species-slug>
    href = f"genus/{g.slug}.html#{s.slug}"
    return href

import re

def md_emph_to_html(s: str) -> str:
    """Convert *word* / *multi word* emphasis to <em>…</em> for HTML output.
    The species descriptions are authored with markdown-style emphasis so the
    same source string round-trips cleanly to both outputs."""
    # Non-greedy match between *...*, not crossing newlines
    return re.sub(r"\*([^*\n]+)\*", r"<em>\1</em>", s)

# ---------------------------------------------------------------------------
# Frontmatter (YANP-style)
# ---------------------------------------------------------------------------

def frontmatter_md(title: str, tags: list[str], status: str = "published") -> str:
    tag_line = " ".join(f"#{t}" for t in tags)
    return (
        f"---\n"
        f"title: {title}\n"
        f"tags: {tag_line}\n"
        f"author: {AUTHOR}\n"
        f"hostname: {HOSTNAME}\n"
        f"date: {TODAY}\n"
        f"status: {status}\n"
        f"---\n\n"
    )

def frontmatter_html(title: str, tags: list[str], status: str = "published") -> str:
    tag_line = " ".join(f"#{t}" for t in tags)
    return (
        f'<pre class="frontmatter">'
        f"title: {escape(title)}\n"
        f"tags: {escape(tag_line)}\n"
        f"author: {escape(AUTHOR)}\n"
        f"hostname: {escape(HOSTNAME)}\n"
        f"date: {TODAY}\n"
        f"status: {status}"
        f"</pre>\n"
    )

# ---------------------------------------------------------------------------
# HTML page skeleton
# ---------------------------------------------------------------------------

def html_page(title: str, body: str, css_path: str = "plain.css") -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} — forest of the mind</title>
<link rel="stylesheet" href="{css_path}">
</head>
<body>
{body}
<footer class="colophon">
  Forest of the mind — a catalog assembled in conversation, april 2026.
  set in plain+ v1.0.
  <a href="{'colophon.html' if css_path == 'plain.css' else '../colophon.html'}">colophon →</a>
</footer>
</body>
</html>
"""

def top_nav(current: str, depth: int = 0) -> str:
    """depth=0 for root pages, depth=1 for genus/ pages."""
    prefix = "../" if depth == 1 else ""
    items = [
        ("index", "index.html", "forest"),
        ("phyla", "phyla.html", "phyla"),
        ("convergences", "convergences.html", "convergences"),
        ("all-species", "all-species.html", "all species"),
        ("colophon", "colophon.html", "colophon"),
    ]
    parts = []
    for key, href, label in items:
        if key == current:
            parts.append(f'<span>{escape(label)}</span>')
        else:
            parts.append(f'<a href="{prefix}{href}">{escape(label)}</a>')
    return f'<nav class="top">{" ".join(parts)}</nav>\n'

# ---------------------------------------------------------------------------
# Markdown rendering — one function per page type
# ---------------------------------------------------------------------------

def md_species_block(genus: Genus, s: Species) -> str:
    lines = []
    lines.append(f"### *{s.binomial}*")
    lines.append("")
    lines.append(f"**{s.gloss}**")
    lines.append("")
    lines.append(s.descr)
    if s.kin:
        kin_links = ", ".join(f"*{k}*" for k in s.kin)
        lines.append("")
        lines.append(f"**Kin.** {kin_links}")
    lines.append("")
    return "\n".join(lines)

def md_genus_page(genus: Genus) -> str:
    out = [frontmatter_md(
        f"Genus {genus.name}",
        ["forest-of-mind", "genus", genus.slug, f"phylum-{genus.phylum.lower()}"]
    )]
    out.append(f"# Genus *{genus.name}*")
    out.append("")
    out.append(f"*{genus.subtitle}* — phylum {genus.phylum}")
    out.append("")
    out.append(genus.blurb)
    out.append("")
    out.append("---")
    out.append("")
    for s in genus.species:
        out.append(md_species_block(genus, s))
    return "\n".join(out)

PHYLUM_META = [
    ("I", "filter-visible-when-misfiring",
     "States in which usually-invisible cognitive apparatus briefly "
     "shows itself by misfiring or decoupling."),
    ("II", "filter-doing-its-job-in-strange-conditions",
     "Not malfunctions but well-oiled cognitive machinery operating "
     "in unusual conditions, postures, or social contexts."),
    ("III", "filter-as-posture",
     "Stances the mind holds rather than events that happen to it. "
     "Directional, sustained, revocable — postures toward beliefs, "
     "gazes, wants, and waits."),
]

def md_index() -> str:
    out = [frontmatter_md(
        "Forest of the Mind — index",
        ["forest-of-mind", "index"]
    )]
    out.append("# Forest of the mind")
    out.append("")
    out.append(
        "A phylogenetic catalog of mental phenomena, organized by genus "
        "and phylum. Each species is a specific texture of inner life "
        "named with the seriousness of a naturalist who has taken leave "
        "of his senses."
    )
    out.append("")
    for phy, subtitle, blurb in PHYLUM_META:
        out.append(f"## Phylum {phy} — {subtitle}")
        out.append("")
        out.append(blurb)
        out.append("")
        for g in [g for g in GENERA if g.phylum == phy]:
            out.append(f"- **Genus *{g.name}*** — {g.subtitle} ({len(g.species)} spp.)")
        out.append("")
    out.append("---")
    out.append("")
    out.append("See also: *convergences* (cross-genus threads), *all species* (flat index).")
    out.append("")
    return "\n".join(out)

def md_phyla() -> str:
    out = [frontmatter_md("Phyla", ["forest-of-mind", "phyla"])]
    out.append("# Phyla")
    out.append("")
    out.append(
        "The genera sort into three higher groups. The division is not "
        "based on subject matter but on the *relationship between the "
        "phenomenon and the cognitive filter that produced it*."
    )
    out.append("")
    for phy, subtitle, _ in PHYLUM_META:
        out.append(f"## Phylum {phy} — {subtitle}")
        out.append("")
        if phy == "I":
            out.append(
                "The unifying trait is a brief exposure of machinery. "
                "The phenomenon is interesting precisely because "
                "something that usually runs silently has made itself "
                "visible by slipping."
            )
        elif phy == "II":
            out.append(
                "The opposite pole from phylum I. Nothing is "
                "malfunctioning. The cognitive machinery is doing "
                "exactly what it's meant to — but in a posture, "
                "context, or tempo that produces a notable subjective "
                "texture."
            )
        else:  # III
            out.append(
                "Distinct from both prior phyla in that these are not "
                "*events* but *postures* — stances the mind holds over "
                "time. Voluntary-ish, directional, revocable. Phylum "
                "III's diagnostic signature is that its members can "
                "end without ceremony: a posture laid down before the "
                "mind noticed it was holding one."
            )
        out.append("")
        out.append("Member genera:")
        out.append("")
        for g in [g for g in GENERA if g.phylum == phy]:
            out.append(f"- *{g.name}* — {g.subtitle}")
        out.append("")
    out.append("---")
    out.append("")
    out.append(
        "The phyla are provisional. Several species sit near boundaries. "
        "*Sermo interior dialogicus* (the rehearsed conversation with "
        "an absent person) reads more like a posture than a condition — "
        "a candidate for migration from phylum II to III. *Desiderium "
        "rei quae adest* (anticipatory loss) is arguably a stance "
        "toward what you are holding. The taxonomy is a working "
        "instrument, not a verdict; migrations are expected."
    )
    out.append("")
    return "\n".join(out)

def md_convergences() -> str:
    out = [frontmatter_md("Convergences", ["forest-of-mind", "convergences"])]
    out.append("# Convergences")
    out.append("")
    out.append(
        "The genera give the vertical structure; the convergences give "
        "the horizontal. Two species from different genera can share a "
        "deep trait — the same underlying phenomenon wearing different "
        "clothing. Marsupials and placentals both evolved wolves; the "
        "mind similarly reinvents its shapes."
    )
    out.append("")
    for c in CONVERGENCES:
        out.append(f"## {c['name']}")
        out.append("")
        out.append("Members:")
        out.append("")
        for m in c["members"]:
            out.append(f"- *{m}*")
        out.append("")
        out.append(f"**Shared trait.** {c['shared_trait']}")
        out.append("")
    return "\n".join(out)

def md_all_species() -> str:
    out = [frontmatter_md("All species", ["forest-of-mind", "index"])]
    out.append("# All species")
    out.append("")
    out.append(
        "Flat alphabetical index of every species in the catalog, with "
        "its gloss and genus."
    )
    out.append("")
    entries = sorted(all_species(), key=lambda gs: gs[1].binomial)
    for g, s in entries:
        out.append(f"- *{s.binomial}* — {s.gloss} (genus *{g.name}*)")
    out.append("")
    return "\n".join(out)

def md_colophon() -> str:
    out = [frontmatter_md("Colophon", ["forest-of-mind", "meta"], status="draft")]
    out.append("# Colophon")
    out.append("")
    out.append("## Method")
    out.append("")
    out.append(
        "This catalog was assembled in conversation between chris and "
        "claude over the course of an afternoon. The method was simple: "
        "propose a genus; name species with pseudo-Latin binomials; "
        "describe each with the phenomenological specificity that "
        "distinguishes it from its siblings. No species was included "
        "unless both parties recognized it."
    )
    out.append("")
    out.append("## Source")
    out.append("")
    out.append(
        "Single-source-of-truth: `build.py` in this directory. The "
        "species catalog lives there as plain python data structures; "
        "both the markdown and the html are generated from the same "
        "source. Editing either output directly will be overwritten on "
        "the next build — edit the data."
    )
    out.append("")
    out.append("## Design")
    out.append("")
    out.append(
        "Set in plain+ v1.0 (plainplusdesign.netlify.app). Body in "
        "charter; headings in the system sans. Accent `#67a` (the "
        "technical variant), used in three places: the hairline at the "
        "top of every page, link hover, and species-entry left rule. "
        "No rounded corners, no gradients, no shadows, no icons."
    )
    out.append("")
    out.append("## Open questions")
    out.append("")
    out.append(
        "The third phylum — *filter-as-posture* — was added after "
        "phyla I and II were already populated. Several species in "
        "phylum II are now candidates for migration: *Sermo interior "
        "dialogicus* (a posture toward an absent interlocutor), "
        "*Desiderium rei quae adest* (a stance toward what one is "
        "holding). Migrations have been deferred pending a review pass."
    )
    out.append("")
    out.append(
        "Outstanding structural questions: whether *Sermo interior* "
        "as a whole belongs in phylum II or forms a third axis; "
        "whether phylum III needs further sub-structure (the "
        "held-postures vs. the held-postures-that-have-ended may be "
        "a distinction worth drawing). Also: a full *Contactus sui* "
        "(modes of being-seen by oneself) is missing from the genus "
        "and probably should exist."
    )
    out.append("")
    return "\n".join(out)

# ---------------------------------------------------------------------------
# HTML rendering
# ---------------------------------------------------------------------------

def html_species_block(genus: Genus, s: Species, depth: int = 1) -> str:
    prefix = "../" if depth == 1 else ""
    kin_html = ""
    if s.kin:
        links = []
        for k in s.kin:
            hit = find_species(k)
            if hit:
                g2, s2 = hit
                href = (f"{prefix}genus/{g2.slug}.html#{s2.slug}"
                        if depth == 0 else f"{g2.slug}.html#{s2.slug}")
                links.append(f'<a href="{href}"><em>{escape(k)}</em></a>')
            else:
                links.append(f"<em>{escape(k)}</em>")
        kin_html = (
            f'<p class="kin"><strong>Kin.</strong> '
            f'{", ".join(links)}</p>'
        )
    return (
        f'<div class="species" id="{s.slug}">\n'
        f'  <span class="binomial">{escape(s.binomial)}</span>\n'
        f'  <p class="gloss">{escape(s.gloss)}</p>\n'
        f'  <p class="descr">{md_emph_to_html(escape(s.descr))}</p>\n'
        f'  {kin_html}\n'
        f'</div>\n'
    )

def html_genus_page(genus: Genus) -> str:
    body = [top_nav("", depth=1)]
    body.append(frontmatter_html(
        f"Genus {genus.name}",
        ["forest-of-mind", "genus", genus.slug, f"phylum-{genus.phylum.lower()}"]
    ))
    body.append(f'<h1>Genus <em>{escape(genus.name)}</em></h1>')
    body.append(
        f'<p class="lede"><em>{escape(genus.subtitle)}</em> — '
        f'phylum {escape(genus.phylum)}</p>'
    )
    body.append(f'<p>{md_emph_to_html(escape(genus.blurb))}</p>')
    body.append('<hr>')
    for s in genus.species:
        body.append(html_species_block(genus, s, depth=1))
    return html_page(f"Genus {genus.name}", "\n".join(body),
                     css_path="../plain.css")

def html_index() -> str:
    body = [top_nav("index", depth=0)]
    body.append(frontmatter_html(
        "Forest of the Mind — index",
        ["forest-of-mind", "index"]
    ))
    body.append('<h1>Forest of the mind</h1>')
    body.append(
        '<p class="lede">A phylogenetic catalog of mental phenomena, '
        'organized by genus and phylum. Each species is a specific '
        'texture of inner life named with the seriousness of a '
        'naturalist who has taken leave of his senses.</p>'
    )
    for phy, subtitle, blurb in PHYLUM_META:
        body.append(f'<h2>Phylum {phy} — {escape(subtitle)}</h2>')
        body.append(f'<p>{escape(blurb)}</p>')
        body.append('<table class="genus-table">')
        body.append('<thead><tr><th>Genus</th><th>Subtitle</th>'
                    '<th style="text-align:right">Species</th></tr></thead>')
        body.append('<tbody>')
        for g in [g for g in GENERA if g.phylum == phy]:
            body.append(
                f'<tr>'
                f'<td class="binomial-cell">'
                f'<a href="genus/{g.slug}.html">{escape(g.name)}</a></td>'
                f'<td>{escape(g.subtitle)}</td>'
                f'<td style="text-align:right">{len(g.species)}</td>'
                f'</tr>'
            )
        body.append('</tbody></table>')
    body.append('<hr>')
    body.append(
        '<p>See also: <a href="convergences.html">convergences</a> '
        '(cross-genus threads) and <a href="all-species.html">all '
        'species</a> (flat index).</p>'
    )
    return html_page("Forest of the mind", "\n".join(body))

def html_phyla() -> str:
    body = [top_nav("phyla", depth=0)]
    body.append(frontmatter_html("Phyla", ["forest-of-mind", "phyla"]))
    body.append('<h1>Phyla</h1>')
    body.append(
        '<p class="lede">The genera sort into three higher groups. The '
        'division is not based on subject matter but on the '
        '<em>relationship between the phenomenon and the cognitive '
        'filter that produced it</em>.</p>'
    )
    phylum_longform = {
        "I": ("The unifying trait is a brief exposure of machinery. The "
              "phenomenon is interesting precisely because something "
              "that usually runs silently has made itself visible by "
              "slipping."),
        "II": ("The opposite pole from phylum I. Nothing is "
               "malfunctioning. The cognitive machinery is doing "
               "exactly what it's meant to — but in a posture, context, "
               "or tempo that produces a notable subjective texture."),
        "III": ("Distinct from both prior phyla in that these are not "
                "<em>events</em> but <em>postures</em> — stances the "
                "mind holds over time. Voluntary-ish, directional, "
                "revocable. Phylum III's diagnostic signature is that "
                "its members can end without ceremony: a posture laid "
                "down before the mind noticed it was holding one."),
    }
    for phy, subtitle, _ in PHYLUM_META:
        body.append(f'<h2>Phylum {phy} — {escape(subtitle)}</h2>')
        body.append(f'<p>{phylum_longform[phy]}</p>')
        body.append('<p class="caption">Member genera</p>')
        body.append('<ul>')
        for g in [g for g in GENERA if g.phylum == phy]:
            body.append(
                f'<li><a href="genus/{g.slug}.html"><em>{escape(g.name)}</em></a>'
                f' — {escape(g.subtitle)}</li>'
            )
        body.append('</ul>')
    body.append('<hr>')
    body.append(
        '<p>The phyla are provisional. Several species sit near '
        'boundaries. <em>Sermo interior dialogicus</em> (the rehearsed '
        'conversation with an absent person) reads more like a posture '
        'than a condition — a candidate for migration from phylum II '
        'to III. <em>Desiderium rei quae adest</em> (anticipatory loss) '
        'is arguably a stance toward what you are holding. The '
        'taxonomy is a working instrument, not a verdict; migrations '
        'are expected.</p>'
    )
    return html_page("Phyla", "\n".join(body))

def html_convergences() -> str:
    body = [top_nav("convergences", depth=0)]
    body.append(frontmatter_html("Convergences",
                                  ["forest-of-mind", "convergences"]))
    body.append('<h1>Convergences</h1>')
    body.append(
        '<p class="lede">The genera give the vertical structure; the '
        'convergences give the horizontal. Two species from different '
        'genera can share a deep trait — the same underlying phenomenon '
        'wearing different clothing. Marsupials and placentals both '
        'evolved wolves; the mind similarly reinvents its shapes.</p>'
    )
    for c in CONVERGENCES:
        body.append(f'<h2>{escape(c["name"])}</h2>')
        body.append('<p class="caption">Members</p>')
        body.append('<ul>')
        for m in c["members"]:
            hit = find_species(m)
            if hit:
                g, s = hit
                body.append(
                    f'<li><a href="genus/{g.slug}.html#{s.slug}">'
                    f'<em>{escape(m)}</em></a> '
                    f'<span style="color:var(--ink-faint)">— genus '
                    f'<em>{escape(g.name)}</em></span></li>'
                )
            else:
                body.append(f'<li><em>{escape(m)}</em></li>')
        body.append('</ul>')
        body.append(f'<p><strong>Shared trait.</strong> {md_emph_to_html(escape(c["shared_trait"]))}</p>')
    return html_page("Convergences", "\n".join(body))

def html_all_species() -> str:
    body = [top_nav("all-species", depth=0)]
    body.append(frontmatter_html("All species",
                                  ["forest-of-mind", "index"]))
    body.append('<h1>All species</h1>')
    body.append(
        '<p class="lede">Flat alphabetical index of every species in the '
        'catalog, with its gloss and genus.</p>'
    )
    body.append('<table>')
    body.append('<thead><tr><th>Species</th><th>Gloss</th>'
                '<th>Genus</th></tr></thead>')
    body.append('<tbody>')
    entries = sorted(all_species(), key=lambda gs: gs[1].binomial)
    for g, s in entries:
        body.append(
            f'<tr>'
            f'<td class="binomial-cell">'
            f'<a href="genus/{g.slug}.html#{s.slug}">'
            f'<em>{escape(s.binomial)}</em></a></td>'
            f'<td>{escape(s.gloss)}</td>'
            f'<td><em>{escape(g.name)}</em></td>'
            f'</tr>'
        )
    body.append('</tbody></table>')
    return html_page("All species", "\n".join(body))

def html_colophon() -> str:
    body = [top_nav("colophon", depth=0)]
    body.append(frontmatter_html("Colophon",
                                  ["forest-of-mind", "meta"], status="draft"))
    body.append('<h1>Colophon</h1>')
    body.append('<h2>Method</h2>')
    body.append(
        '<p>This catalog was assembled in conversation between chris and '
        'claude over the course of an afternoon. The method was simple: '
        'propose a genus; name species with pseudo-Latin binomials; '
        'describe each with the phenomenological specificity that '
        'distinguishes it from its siblings. No species was included '
        'unless both parties recognized it.</p>'
    )
    body.append('<h2>Source</h2>')
    body.append(
        '<p>Single-source-of-truth: <code>build.py</code> in this '
        'directory. The species catalog lives there as plain python '
        'data structures; both the markdown and the html are generated '
        'from the same source. Editing either output directly will be '
        'overwritten on the next build — edit the data.</p>'
    )
    body.append('<h2>Design</h2>')
    body.append(
        '<p>Set in plain+ v1.0 '
        '(<a href="https://plainplusdesign.netlify.app/">'
        'plainplusdesign.netlify.app</a>). Body in charter; headings in '
        'the system sans. Accent <code>#67a</code> (the technical '
        'variant), used in three places: the hairline at the top of '
        'every page, link hover, and species-entry left rule. No '
        'rounded corners, no gradients, no shadows, no icons.</p>'
    )
    body.append('<h2>Open questions</h2>')
    body.append(
        '<p>The third phylum — <em>filter-as-posture</em> — was added '
        'after Phylum I and II were already populated. Several species '
        'in Phylum II are now candidates for migration: <em>Sermo '
        'interior dialogicus</em> (a posture toward an absent '
        'interlocutor), <em>Desiderium rei quae adest</em> (a stance '
        'toward what one is holding). Migrations have been deferred '
        'pending a review pass.</p>'
    )
    body.append(
        '<p>Outstanding structural questions: whether <em>Sermo '
        'interior</em> as a whole belongs in Phylum II or forms a '
        'third axis; whether Phylum III needs further sub-structure '
        '(the held-postures vs. the held-postures-that-have-ended may '
        'be a distinction worth drawing). Also: a full <em>Contactus '
        'sui</em> (modes of being-seen by oneself) is missing from '
        'the genus and probably should exist.</p>'
    )
    return html_page("Colophon", "\n".join(body))

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    root_md = Path("/home/claude/forest/md")
    root_html = Path("/home/claude/forest/html")
    (root_md / "genus").mkdir(parents=True, exist_ok=True)
    (root_html / "genus").mkdir(parents=True, exist_ok=True)

    # Top-level pages
    (root_md / "index.md").write_text(md_index())
    (root_md / "phyla.md").write_text(md_phyla())
    (root_md / "convergences.md").write_text(md_convergences())
    (root_md / "all-species.md").write_text(md_all_species())
    (root_md / "colophon.md").write_text(md_colophon())

    (root_html / "index.html").write_text(html_index())
    (root_html / "phyla.html").write_text(html_phyla())
    (root_html / "convergences.html").write_text(html_convergences())
    (root_html / "all-species.html").write_text(html_all_species())
    (root_html / "colophon.html").write_text(html_colophon())

    # Genus pages
    for g in GENERA:
        (root_md / "genus" / f"{g.slug}.md").write_text(md_genus_page(g))
        (root_html / "genus" / f"{g.slug}.html").write_text(html_genus_page(g))

    total_species = sum(len(g.species) for g in GENERA)
    print(f"Wrote {len(GENERA)} genera, {total_species} species.")
    print(f"MD:   {root_md}")
    print(f"HTML: {root_html}")

if __name__ == "__main__":
    main()
