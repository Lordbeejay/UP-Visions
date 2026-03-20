# Caller
default persistent.encyclopedia_unlocks = set()

init python:

    #Base class for entries
    class EncyEntry:
        def __init__(self, id, name, category, desc, icon=None, locked_desc="???"):
            self.id = id
            self.name = name
            self.category = category # e.g., "CULTURE", "PERSONALITY"
            self.desc = desc
            self.icon = icon
            self.locked_desc = locked_desc

    # Entries (Last updated 3/19)
    all_entries = {
        # --- CULTURE ---
        "bahay_kubo": EncyEntry(
            "bahay_kubo", 
            "Bahay Kubo", 
            "CULTURE", 
            "A traditional Filipino 'Nipa Hut' made of bamboo and cogon grass, symbolizing local resilience and architectural heritage.",
            #icon="gui/icons/kubo.png"
        ),
        "freshie": EncyEntry(
            "freshie",
            "Freshie",
            "CULTURE",
            "A campus term for first-year students. They are often spotted looking at maps with a mix of excitement and profound confusion.",
            #icon="gui/icons/freshie.png"
        ),
        "enrollment_blues": EncyEntry(
            "enrollment_blues",
            "Enrollment Blues",
            "CULTURE",
            "The collective stress experienced by students during the registration period, involving long queues and the fight for slots.",
            #icon="gui/icons/blues.png"
        ),

        # --- PERSONALITY ---
        "jaden": EncyEntry(
            "jaden", 
            "Jaden", 
            "PERSONALITY", 
            "A helpful fellow freshie from Iloilo City. He knows his way around Miagao better than most and carries a tablet for his digital art.",
            #icon="gui/icons/jaden.png"
        ),
        "prof_reyes": EncyEntry(
            "prof_reyes",
            "Professor Reyes",
            "PERSONALITY",
            "A faculty member known for a strict exterior but a deep dedication to the academic growth of their students.",
            #icon="gui/icons/prof_reyes.png"
        ),
        "lara": EncyEntry(
            "lara",
            "Lara",
            "PERSONALITY",
            "A proactive student leader often found at the CAS building, always ready to lend a hand to struggling newcomers.",
            #icon="gui/icons/lara.png"
        ),

        # --- LOCATION ---
        "upv_entrance": EncyEntry(
            "upv_entrance",
            "University Entrance",
            "LOCATION",
            "The main gate of the UPV Miagao campus, featuring the iconic archway where many students begin their college journey.",
            #icon="gui/icons/entrance.png"
        ),
        "cas_building": EncyEntry(
            "cas_building",
            "CAS Building",
            "LOCATION",
            "The College of Arts and Sciences. It is the academic heart of the campus where most general education classes are held.",
            #icon="gui/icons/cas.png"
        ),
        "the_oblation": EncyEntry(
            "the_oblation",
            "The Oblation",
            "LOCATION",
            "The iconic statue symbolizing selfless offering of oneself to the country. A central landmark for every UP campus.",
            #icon="gui/icons/oblation.png"
        ),
        "diwata_shore": EncyEntry(
            "diwata_shore",
            "Diwata Shore",
            "LOCATION",
            "A scenic coastal area near the campus where students go to reflect, relax, or watch the sunset after a long day of classes.",
            #icon="gui/icons/shore.png"
        ),

        # --- PROCESS/MISC ---
        "id_validation": EncyEntry(
            "id_validation",
            "ID Validation",
            "PROCESS",
            "The necessary task of getting your student ID stamped. Skipping this usually leads to trouble at the library or the gate.",
            #icon="gui/icons/id.png"
        ),
        "visions_quest": EncyEntry(
            "visions_quest",
            "The Vision",
            "MISC",
            "The internal drive and academic goal that keeps a student moving forward despite the 'shitty' challenges of college life.",
            #icon="gui/icons/vision.png"
        )
    }

    # Initialize persistent unlocks (keeps entries unlocked across save files)
    if persistent.encyclopedia_unlocks is None:
        persistent.encyclopedia_unlocks = set()