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
        ),

        # --- SUPPORT SERVICES ---
        "health_services_unit": EncyEntry(
            "health_services_unit",
            "Health Services Unit (HSU)",
            "PROCESS",
            "The UPV campus clinic providing FREE outpatient medical and dental care for all enrolled students. Services include consultations, first aid, basic laboratory tests, tooth extraction and cleaning, and issuance of medical certificates. Open Mon–Fri, 8 AM–5 PM. Serious cases are referred to Miagao District Hospital or Western Visayas Medical Center. Bring your student ID.",
        ),
        "scholarship_service": EncyEntry(
            "scholarship_service",
            "Scholarship Service",
            "PROCESS",
            "The UPV office that administers all student financial assistance. Programs: STFAP (Socialized Tuition and Financial Assistance Program) — brackets A to E9 based on family income; E5 to E9 include monthly living allowances of ₱1,000 to ₱4,000. TES (Tertiary Education Subsidy, RA 10931) — CHED national grant covering full tuition and fees plus a monthly allowance for qualifying students; coordinated through this office. GIAP (Grants-in-Aid Program) — UP System monthly cash allowance for low-income undergraduates, separate from STFAP; applications open each semester. University Scholar requires GWA of 1.20 or better. Emergency Fund: up to ₱1,500, processed in 24–48 hours. These programs are not mutually exclusive — a student can receive STFAP, TES, and GIAP simultaneously. Submit documents within the first two weeks of each semester. Deadlines are absolute.",
        ),
        "tlrc": EncyEntry(
            "tlrc",
            "TLRC — Teaching and Learning Resource Center",
            "PROCESS",
            "UPV's FREE academic support center for all enrolled students. Offers peer tutoring (matched by subject), Supplemental Instruction for high-failure courses, academic writing workshops (APA format, paper structure, anti-plagiarism), and study skills seminars. Writing consultations are available for draft review. Request a tutor via the Tutoring Request Form at the TLRC office. Come early — don't wait until you're already failing.",
        ),
        "gcsu": EncyEntry(
            "gcsu",
            "GCSU — Guidance and Counseling Services Unit",
            "PROCESS",
            "UPV's professional counseling unit providing FREE, strictly confidential services under Republic Act 9258. Services: individual counseling, group counseling, psychological assessments (RIASEC and aptitude tests), career guidance, crisis intervention, and academic counseling — including study habits, time management, and learning strategies for students who struggle not from lack of ability but from how they work. Access: walk-in Mon–Fri 8AM–5PM (no appointment needed), or pre-schedule a specific slot through the GCSU office for less waiting time. The Peer Facilitators Program — trained student volunteers who lead group psychosocial activities for college adjustment — operates under this office. The GCSU is not a last resort. Use it before the crisis.",
        ),
        "tes_giap": EncyEntry(
            "tes_giap",
            "TES & GIAP — Government and UP Grants",
            "PROCESS",
            "Two financial assistance programs distinct from STFAP. TES (Tertiary Education Subsidy) — a CHED national grant under Republic Act 10931 (Universal Access to Quality Education Act). Covers full tuition and other school fees plus a monthly cash allowance calibrated to financial need. Applied through CHED's portal; enrollment certification is done at the UPV Scholarship Office. GIAP (Grants-in-Aid Program) — a UP System monthly cash allowance for low-income undergraduate students. Applied at the Scholarship Office each semester; requires proof of income and a brief application letter. Both programs can be received simultaneously with STFAP — they are not mutually exclusive. Ask the Scholarship Office which combination applies to your bracket and situation.",
        ),
        "slas": EncyEntry(
            "slas",
            "SLAS — Student Learning Assistance System",
            "PROCESS",
            "The overarching framework coordinating student financial, academic, and welfare support at UPV. SLAS integrates the Scholarship Service (STFAP, TES, GIAP, Emergency Fund), the GCSU (counseling and psychosocial support), and the HSU (health services). Students identified as at-risk — through academic performance, financial difficulty, or health concerns — are routed through SLAS to the appropriate combination of services. STFAP is one component of SLAS, not its entirety. A GCSU referral to the Scholarship Service, or a Scholarship Office flag to the GCSU, is SLAS working as designed. Students do not apply to SLAS — the system activates on their behalf when offices communicate. No student should fall through the gap between offices.",
        ),
        "peer_facilitators": EncyEntry(
            "peer_facilitators",
            "Peer Facilitators Program",
            "PROCESS",
            "A GCSU-run program staffed by trained student volunteers who facilitate group psychosocial support activities for fellow students adjusting to college life. Peer Facilitators are not licensed counselors — they lead structured group activities: journaling circles, reflection workshops, coping exercises, and community-building sessions. The program bridges the gap between 'struggling but not in crisis' and 'ready for individual counseling.' Operating under direct GCSU supervision. Applications open each semester at the GCSU office — no psychology background required, training is provided. Joining develops the facilitator's own adjustment skills alongside their capacity to support others. Attending as a participant: check the GCSU bulletin board for scheduled sessions, free and open to all enrolled students.",
        ),
    }

    # Initialize persistent unlocks (keeps entries unlocked across save files)
    if persistent.encyclopedia_unlocks is None:
        persistent.encyclopedia_unlocks = set()