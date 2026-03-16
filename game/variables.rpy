## ============================================================================
## GAME VARIABLES — State tracking for tasks, acts, and player position
## ============================================================================

## --- Act & Story Progression ---
default current_act = 1
default current_task_text = ""
default tasks_completed = set()
default game_complete = False

## --- Act Task Requirements ---
## Each act has a set of task IDs the player must complete to advance
define ACT1_TASKS = {"talk_jaden", "talk_manong_josh", "talk_aleng_maria", "talk_manong_chris", "talk_joseph_driver", "reach_box1"}
define ACT2_TASKS = {"talk_ate_bea", "talk_kuya_mark", "go_to_newad", "talk_maam_reyes", "complete_flip_card"}
define ACT3_TASKS = {"talk_sir_noel", "view_crs_portal", "complete_enrollment_tetris"}
define ACT4_TASKS = {"talk_dorm_manager"}

## --- Acts 5–8 Task Requirements ---
define ACT5_TASKS = {"talk_prof_lena", "talk_kuya_rico", "talk_ate_grace", "talk_classmate_dan", "attend_first_class"}
define ACT6_TASKS = {"talk_mika", "talk_kuya_tomas", "talk_ate_jenny", "talk_coach_ramon", "visit_org_fair"}
define ACT7_TASKS = {"talk_ate_rosa", "talk_kuya_neil", "talk_prof_santos", "talk_classmate_bea", "attend_study_session"}
define ACT8_TASKS = {"talk_jaden_act8", "talk_ate_linda", "talk_nanay_elena", "talk_prof_reyes", "end_of_first_week"}

## --- Player Map Position ---
default player_map_x = 640
default player_map_y = 500
default player_facing = "down"
default current_map_bg = "maps/banwa.png"

## --- Task Names (for HUD display) ---
define TASK_DESCRIPTIONS = {
    "talk_jaden": "Talk to Jaden",
    "talk_manong_josh": "Talk to Manong Josh",
    "talk_aleng_maria": "Talk to Aleng Maria",
    "talk_manong_chris": "Talk to Manong Chris",
    "talk_joseph_driver": "Talk to Joseph (Driver)",
    "reach_box1": "Head to BOX 1",
    "talk_ate_bea": "Talk to Ate Bea",
    "talk_kuya_mark": "Talk to Kuya Mark",
    "go_to_newad": "Go to New Admin",
    "talk_maam_reyes": "Talk to Ma'am Reyes",
    "complete_flip_card": "Complete the Office Match Game",
    "talk_sir_noel": "Talk to Sir Noel",
    "view_crs_portal": "View the CRS Portal",
    "complete_enrollment_tetris": "Complete Enrollment Tetris",
    "talk_dorm_manager": "Talk to the Dorm Manager",
    "talk_prof_lena": "Talk to Prof. Lena",
    "talk_kuya_rico": "Talk to Kuya Rico",
    "talk_ate_grace": "Talk to Ate Grace",
    "talk_classmate_dan": "Talk to Dan",
    "attend_first_class": "Attend First Class",
    "talk_mika": "Talk to Mika",
    "talk_kuya_tomas": "Talk to Kuya Tomas",
    "talk_ate_jenny": "Talk to Ate Jenny",
    "talk_coach_ramon": "Talk to Coach Ramon",
    "visit_org_fair": "Visit the Org Fair",
    "talk_ate_rosa": "Talk to Ate Rosa",
    "talk_kuya_neil": "Talk to Kuya Neil",
    "talk_prof_santos": "Talk to Prof. Santos",
    "talk_classmate_bea": "Talk to Bea",
    "attend_study_session": "Attend Study Session",
    "talk_jaden_act8": "Talk to Jaden",
    "talk_ate_linda": "Talk to Ate Linda",
    "talk_nanay_elena": "Talk to Nanay Elena",
    "talk_prof_reyes": "Talk to Prof. Reyes",
    "end_of_first_week": "End of First Week",
}

define ACT_TASK_ORDER = {
    1: ["talk_jaden", "talk_manong_josh", "talk_aleng_maria", "talk_manong_chris", "talk_joseph_driver", "reach_box1"],
    2: ["talk_ate_bea", "talk_kuya_mark", "go_to_newad", "talk_maam_reyes", "complete_flip_card"],
    3: ["talk_sir_noel", "view_crs_portal", "complete_enrollment_tetris"],
    4: ["talk_dorm_manager"],
    5: ["talk_prof_lena", "talk_kuya_rico", "talk_ate_grace", "talk_classmate_dan", "attend_first_class"],
    6: ["talk_mika", "talk_kuya_tomas", "talk_ate_jenny", "talk_coach_ramon", "visit_org_fair"],
    7: ["talk_ate_rosa", "talk_kuya_neil", "talk_prof_santos", "talk_classmate_bea", "attend_study_session"],
    8: ["talk_jaden_act8", "talk_ate_linda", "talk_nanay_elena", "talk_prof_reyes", "end_of_first_week"],
}

define TASK_LIST_TEXT = {
    "talk_jaden": "Talk to Jaden",
    "talk_manong_josh": "Talk to Manong Josh",
    "talk_aleng_maria": "Talk to Aleng Maria",
    "talk_manong_chris": "Talk to Manong Chris",
    "talk_joseph_driver": "Talk to Joseph (Driver)",
    "reach_box1": "Head to BOX 1",
    "talk_ate_bea": "Talk to Ate Bea at the Entrance",
    "talk_kuya_mark": "Talk to Kuya Mark about security",
    "go_to_newad": "Head to New Admin building",
    "talk_maam_reyes": "Find Ma'am Reyes inside New Admin",
    "complete_flip_card": "Complete the Office Match Game",
    "talk_sir_noel": "Talk to Sir Noel about enrollment",
    "view_crs_portal": "View the CRS Student Portal",
    "complete_enrollment_tetris": "Complete Enrollment Tetris",
    "talk_dorm_manager": "Talk to the Dorm Manager",
    "talk_prof_lena": "Talk to Prof. Lena in the classroom",
    "talk_kuya_rico": "Ask Kuya Rico about buildings",
    "talk_ate_grace": "Talk to Ate Grace about student rights",
    "talk_classmate_dan": "Chat with Dan about study tips",
    "attend_first_class": "Attend your first class",
    "talk_mika": "Talk to Mika at the org fair",
    "talk_kuya_tomas": "Ask Kuya Tomas about scholarships",
    "talk_ate_jenny": "Visit Ate Jenny at the OSA",
    "talk_coach_ramon": "Talk to Coach Ramon about sports",
    "visit_org_fair": "Walk through the org fair",
    "talk_ate_rosa": "Talk to Ate Rosa at the library",
    "talk_kuya_neil": "Visit Kuya Neil at the computer lab",
    "talk_prof_santos": "Talk to Prof. Santos about research",
    "talk_classmate_bea": "Chat with Bea about study groups",
    "attend_study_session": "Attend the study session",
    "talk_jaden_act8": "Catch up with Jaden",
    "talk_ate_linda": "Talk to Ate Linda at the canteen",
    "talk_nanay_elena": "Visit Nanay Elena at the dorm",
    "talk_prof_reyes": "Talk to Prof. Reyes",
    "end_of_first_week": "Reflect on your first week",
}

## --- Helper function: mark a task complete and get next task ---
init python:
    def complete_task(task_id):
        """Mark a task as complete and update the current task text."""
        store.tasks_completed.add(task_id)
        renpy.notify("✅ Task Complete!")

    def get_current_tasks():
        """Get the set of remaining tasks for the current act."""
        act_map = {
            1: ACT1_TASKS,
            2: ACT2_TASKS,
            3: ACT3_TASKS,
            4: ACT4_TASKS,
            5: ACT5_TASKS,
            6: ACT6_TASKS,
            7: ACT7_TASKS,
            8: ACT8_TASKS,
        }
        required = act_map.get(store.current_act, set())
        return required - store.tasks_completed

    def is_task_unlocked(task_id):
        """Return whether a task is currently unlockable based on prerequisites."""
        ## Act 1 prerequisites
        if task_id in ("talk_manong_josh", "talk_aleng_maria"):
            return "talk_jaden" in store.tasks_completed
        if task_id == "talk_manong_chris":
            return ("talk_manong_josh" in store.tasks_completed or
                    "talk_aleng_maria" in store.tasks_completed)
        if task_id == "talk_joseph_driver":
            return "talk_manong_chris" in store.tasks_completed
        if task_id == "reach_box1":
            return (
                "talk_jaden" in store.tasks_completed and
                "talk_manong_josh" in store.tasks_completed and
                "talk_aleng_maria" in store.tasks_completed and
                "talk_manong_chris" in store.tasks_completed and
                "talk_joseph_driver" in store.tasks_completed
            )
        ## Act 2 prerequisites
        if task_id == "talk_kuya_mark":
            return "talk_ate_bea" in store.tasks_completed
        if task_id == "go_to_newad":
            return (
                "talk_ate_bea" in store.tasks_completed and
                "talk_kuya_mark" in store.tasks_completed
            )
        if task_id == "talk_maam_reyes":
            return "go_to_newad" in store.tasks_completed
        if task_id == "complete_flip_card":
            return "talk_maam_reyes" in store.tasks_completed
        ## Act 3 prerequisites
        if task_id == "view_crs_portal":
            return "talk_sir_noel" in store.tasks_completed
        if task_id == "complete_enrollment_tetris":
            return "view_crs_portal" in store.tasks_completed
        ## Act 5 prerequisites
        if task_id in ("talk_kuya_rico", "talk_ate_grace"):
            return "talk_prof_lena" in store.tasks_completed
        if task_id == "talk_classmate_dan":
            return ("talk_kuya_rico" in store.tasks_completed or
                    "talk_ate_grace" in store.tasks_completed)
        if task_id == "attend_first_class":
            return (
                "talk_prof_lena" in store.tasks_completed and
                "talk_kuya_rico" in store.tasks_completed and
                "talk_ate_grace" in store.tasks_completed and
                "talk_classmate_dan" in store.tasks_completed
            )
        ## Act 6 prerequisites
        if task_id in ("talk_kuya_tomas", "talk_ate_jenny"):
            return "talk_mika" in store.tasks_completed
        if task_id == "talk_coach_ramon":
            return ("talk_kuya_tomas" in store.tasks_completed or
                    "talk_ate_jenny" in store.tasks_completed)
        if task_id == "visit_org_fair":
            return (
                "talk_mika" in store.tasks_completed and
                "talk_kuya_tomas" in store.tasks_completed and
                "talk_ate_jenny" in store.tasks_completed and
                "talk_coach_ramon" in store.tasks_completed
            )
        ## Act 7 prerequisites
        if task_id in ("talk_kuya_neil", "talk_prof_santos"):
            return "talk_ate_rosa" in store.tasks_completed
        if task_id == "talk_classmate_bea":
            return ("talk_kuya_neil" in store.tasks_completed or
                    "talk_prof_santos" in store.tasks_completed)
        if task_id == "attend_study_session":
            return (
                "talk_ate_rosa" in store.tasks_completed and
                "talk_kuya_neil" in store.tasks_completed and
                "talk_prof_santos" in store.tasks_completed and
                "talk_classmate_bea" in store.tasks_completed
            )
        ## Act 8 prerequisites
        if task_id in ("talk_ate_linda", "talk_nanay_elena"):
            return "talk_jaden_act8" in store.tasks_completed
        if task_id == "talk_prof_reyes":
            return ("talk_ate_linda" in store.tasks_completed or
                    "talk_nanay_elena" in store.tasks_completed)
        if task_id == "end_of_first_week":
            return (
                "talk_jaden_act8" in store.tasks_completed and
                "talk_ate_linda" in store.tasks_completed and
                "talk_nanay_elena" in store.tasks_completed and
                "talk_prof_reyes" in store.tasks_completed
            )
        return True

    def get_act_task_items(act_num):
        """Ordered checklist rows for the gameplay HUD task panel."""
        ordered = ACT_TASK_ORDER.get(act_num, [])
        rows = []
        for task_id in ordered:
            done = task_id in store.tasks_completed
            unlocked = done or is_task_unlocked(task_id)
            label = TASK_LIST_TEXT.get(task_id, TASK_DESCRIPTIONS.get(task_id, task_id))
            rows.append((label, done, unlocked))
        return rows

    def is_act_complete():
        """Check if all tasks for the current act are done."""
        return len(get_current_tasks()) == 0

    def get_act_title(act_num):
        titles = {
            1: "ACT 1: Arrival in Miagao",
            2: "ACT 2: Entering the University",
            3: "ACT 3: Enrollment",
            4: "ACT 4: Dorm Accommodation",
            5: "ACT 5: First Day of Classes",
            6: "ACT 6: Student Orgs & Campus Life",
            7: "ACT 7: Library & Academic Resources",
            8: "ACT 8: Finding Your Place",
        }
        return titles.get(act_num, "The End")


## ============================================================================
## PHONE & INVENTORY UNLOCK FLAGS
## ============================================================================
## These are set during Act 1 but persist globally across all acts.

default phone_unlocked = False
default inventory_unlocked = False


## ============================================================================
## CLASSES — InfoItem, NotebookQuestion, GCMessage
## ============================================================================

init python:

    ## -------------------------------------------------------------------------
    ## INFO ITEM — represents a piece of knowledge dropped by an NPC
    ## -------------------------------------------------------------------------
    class InfoItem:
        def __init__(self, item_id, label, short, source, icon="📄", full=None):
            self.item_id  = item_id   # unique string key
            self.label    = label     # full display name
            self.short    = short     # 1-line description shown in inventory
            self.source   = source    # which NPC gave this
            self.icon     = icon
            self.full     = full if full else short  # encyclopedia long description

    ## -------------------------------------------------------------------------
    ## NOTEBOOK QUESTION — one question on the detective board
    ## -------------------------------------------------------------------------
    class NotebookQuestion:
        def __init__(self, qid, text, correct_item_id, hint=""):
            self.qid             = qid
            self.text            = text
            self.correct_item_id = correct_item_id
            self.hint            = hint
            self.answered        = False
            self.chosen_item_id  = None

    ## -------------------------------------------------------------------------
    ## GROUP CHAT MESSAGE
    ## -------------------------------------------------------------------------
    class GCMessage:
        def __init__(self, sender, text, avatar_color="#7C3AED", is_player=False):
            self.sender       = sender
            self.text         = text
            self.avatar_color = avatar_color
            self.is_player    = is_player


## ============================================================================
## GLOBAL STATE — collected items, GC state, quiz state
## ============================================================================

init python:

    # Collected info items (list of InfoItem objects)
    collected_items = []

    # Whether the group chat is unlocked
    gc_unlocked = False

    # Which GC messages have been revealed (index into gc_all_messages)
    gc_revealed = []

    # Track how many times player has opened GC (caps at 3 batches)
    gc_open_count = 0

    quiz_result = None   # "pass" or "fail"
    quiz_score  = 0


## ============================================================================
## HELPER FUNCTIONS — item collection, GC reveal
## ============================================================================

init python:

    def collect_item(item):
        """Add an InfoItem to the player's collection if not already there."""
        ids = [i.item_id for i in collected_items]
        if item.item_id not in ids:
            collected_items.append(item)

    def has_item(item_id):
        return any(i.item_id == item_id for i in collected_items)

    def get_item(item_id):
        for i in collected_items:
            if i.item_id == item_id:
                return i
        return None

    def reveal_gc_batch():
        """Replace current batch with the next 3 GC messages."""
        global gc_open_count, gc_revealed
        batch = gc_open_count
        if batch < len(gc_all_messages):
            start = batch * 3
            gc_revealed = [start, start + 1, start + 2]
            gc_open_count += 1

    def save_quiz_answer(q_idx, chosen_id):
        """Persist the player's quiz answer to the notebook question object."""
        if 0 <= q_idx < len(notebook_questions):
            notebook_questions[q_idx].chosen_item_id = chosen_id
            notebook_questions[q_idx].answered = True


## ============================================================================
## DEFINE ALL INFO ITEMS
## ============================================================================

init python:

    # --- JADEN ITEMS ---
    ITEM_MIAGAO_LOCATION = InfoItem(
        "miagao_location",
        "Miagao's Location",
        "40 km SW of Iloilo City, ~1 hr by jeepney",
        "Jaden", "🗺️",
        full="Miagao is a first-class municipality in Iloilo Province on the island of Panay. It lies 40 kilometers southwest of Iloilo City, reachable by jeepney from Tagbak Terminal in about one hour. The town sits along the Iloilo Strait, which is why you sometimes catch a sea breeze on campus."
    )
    ITEM_UPV_HISTORY = InfoItem(
        "upv_history",
        "UPV's Origin",
        "Established 1979, built for Visayas marine research",
        "Jaden", "🎓",
        full="University of the Philippines Visayas was established in 1979. The campus was deliberately placed in Miagao to serve the region's coastal communities — focusing on marine science, fisheries, and sustainable development. It is one of the few UP constituent universities with a distinct regional identity tied to the sea."
    )
    ITEM_CHURCH_UNESCO = InfoItem(
        "church_unesco",
        "Miagao Church",
        "National Cultural Treasure, UNESCO recognized",
        "Jaden", "⛪",
        full="The Santo Tomas de Villanueva Parish Church was built in 1787 and completed in 1797. It is recognized as both a National Cultural Treasure and a UNESCO World Heritage Site. Its baroque façade features uniquely Filipino motifs: coconut trees, papaya plants, and Santo Tomas de Villanueva dressed as a local — a fusion of colonial architecture and indigenous identity."
    )

    # --- JOSH ITEMS ---
    ITEM_MARKET_HOURS = InfoItem(
        "market_hours",
        "Public Market Hours",
        "Opens early, best goods gone by 10 AM",
        "Manong Josh", "🕙",
        full="The Miagao Public Market is most active from 5 to 9 AM. Fish, vegetables, and cooked food are freshest and cheapest during this early window. By 10 AM, most of the good stock is sold out. If you plan to cook for yourself, set your alarm early. The market also has cheap prepared meals for students who get there in time."
    )
    ITEM_LANDMARKS = InfoItem(
        "landmarks",
        "Town Landmarks",
        "Church → Plaza → Market → UPV Gate",
        "Manong Josh", "📍",
        full="Miagao's key landmarks are arranged along the main road. The Church sits at the center of town near the plaza — a reliable navigation anchor visible from most parts of town. The Public Market is a short walk from the plaza. Municipal Hall handles LGU documents and permits. The UPV gate is southeast of town, about 15 minutes by tricycle from the plaza."
    )
    ITEM_SAFETY_TIPS = InfoItem(
        "safety_tips",
        "Town Safety",
        "Safe daytime, greet elders properly",
        "Manong Josh", "🛡️",
        full="Miagao is generally safe during the day. Avoid wandering unfamiliar streets alone after dark, especially outside the town center. Always greet people you pass — 'Manong,' 'Manang,' 'Ate,' 'Kuya.' Locals notice who is respectful and will look out for you. The beach along the strait is accessible but always check with locals before swimming — currents vary by location."
    )

    # --- MARIA ITEMS ---
    ITEM_MEAL_COST = InfoItem(
        "meal_cost",
        "Meal Budget",
        "₱45–70 per meal, ₱150–200/day total",
        "Aleng Maria", "🍚",
        full="A standard rice meal at a carinderia costs ₱45–70 (rice + one viand). Extra rice is ₱5–10 — look for unlimited rice places near campus. A full day of meals runs ₱150–200. Water refills at 5-gallon containers cost ₱20–25, far cheaper than buying bottles. Merienda snacks like banana cue and puto cost ₱5–15. Avoid sit-down restaurants unless treating yourself."
    )
    ITEM_TRICYCLE_FARE = InfoItem(
        "tricycle_fare",
        "Tricycle Fare",
        "₱15 plaza to UPV, ₱10 short hops",
        "Aleng Maria", "🛺",
        full="The standard tricycle fare from Miagao Plaza to the UPV gate is ₱15. Short hops within town cost ₱10. Hiring the whole tricycle for yourself runs ₱50–80 depending on distance. Be wary of drivers quoting higher prices for obvious freshies. You can ask 'Pila man gid ang tama nga bayad?' (What's the correct fare?) to signal you know what it should cost."
    )
    ITEM_WEEKLY_BUDGET = InfoItem(
        "weekly_budget",
        "Weekly Budget",
        "₱1,500 minimum for food and fare",
        "Aleng Maria", "💰",
        full="A realistic minimum weekly budget: meals ₱150–200/day (₱1,050–1,400/week), tricycle fare ₱50–100/week, miscellaneous ₱200+. Total minimum: ₱1,500 per week for food and transport. Cook occasionally — instant noodles plus egg and vegetables is filling and economical. Pack meals from the market to save further. Budget more for toiletries, printing, and org fees."
    )

    # --- CHRIS ITEMS ---
    ITEM_KINARAYA = InfoItem(
        "kinaraya",
        "Kinaray-a Phrases",
        "Kamusta ka na, Salamat, Estudyante ako sa UPV",
        "Manong Chris", "🗣️",
        full="Kinaray-a is the primary language of Miagao and much of Antique Province — distinct from Hiligaynon spoken in Iloilo City. Locals also speak Hiligaynon and Filipino. Key phrases: 'Kamusta ka na?' (How are you?), 'Salamat' (Thank you), 'Wara' (None/Nothing/No). Saying 'Estudyante ako sa UPV' instantly earns goodwill. Even one phrase shows respect for their culture."
    )
    ITEM_LOCAL_CUSTOMS = InfoItem(
        "local_customs",
        "Local Customs",
        "Greet elders, pause at Angelus, no littering at church",
        "Manong Chris", "🙏",
        full="Key customs: Always address elders as 'Manong/Manang' or 'Lolo/Lola.' At 6 PM when the Angelus bells ring from the church, pause and lower your voice — locals observe this moment of prayer. The town fiesta honors Santo Tomas de Villanueva, usually in September, with street food, processions, and open homes. If invited inside someone's home, always accept the food offered — refusing is considered rude."
    )
    ITEM_MASS_SCHEDULE = InfoItem(
        "mass_schedule",
        "Church Mass Schedule",
        "Weekdays 6 AM, Sunday 5:30/7:00/9:00 AM",
        "Manong Chris", "🔔",
        full="Santo Tomas de Villanueva Parish Mass schedule: Weekdays at 6:00 AM. Sundays at 5:30 AM, 7:00 AM, 9:00 AM, and sometimes 5:30 PM. Even non-Catholics are welcome to visit the church as a UNESCO World Heritage Site and historical landmark. Observe proper dress: no shorts, cover your shoulders. Photography is allowed in the grounds but be respectful during Mass."
    )

    # --- JOSEPH ITEMS ---
    ITEM_ROUTES = InfoItem(
        "routes",
        "Tricycle Routes",
        "Route 1: Plaza↔UPV, Route 2: Plaza↔Market",
        "Tol Joseph", "🛤️",
        full="Miagao tricycles follow loose routes. Route 1 (most useful): Town Center/Plaza ↔ UPV Main Gate. Route 2: Town Center ↔ Public Market. Route 3: UPV Gate ↔ Poblacion interior streets. Route 4: Town Center ↔ outlying barangays (Kirayan, Sapa, Guibongan) — higher fare, longer trip. As a UPV student, you'll primarily use Route 1 and Route 2 for daily life."
    )
    ITEM_JEEPNEY_CITY = InfoItem(
        "jeepney_city",
        "Jeepney to Iloilo City",
        "₱50–65 from highway junction, last trip ~6:30 PM",
        "Tol Joseph", "🚌",
        full="To reach Iloilo City: take a tricycle to the highway junction (₱10–15), then board a Tagbak-bound jeepney (₱50–65 one way, 45 min–1 hour). CRITICAL: the last jeepney back to Miagao from Tagbak Terminal departs around 6:30–7:00 PM. Miss it and you'll need to arrange alternative transport or stay in the city overnight. Always check the last trip time before heading out."
    )
    ITEM_DROPOFFS = InfoItem(
        "dropoffs",
        "Drop-off Points",
        "UPV Gate, Plaza, Market, Municipal Hall, Highway",
        "Tol Joseph", "📌",
        full="Standard Miagao tricycle drop-off points: UPV Main Gate (for campus), Miagao Plaza (town center — your navigation anchor), Public Market (for groceries and cheap meals), Municipal Hall (for LGU documents), and the Highway Junction (for jeepneys to Iloilo City and other provinces). When lost or unsure: always say 'Plaza' as your destination. You can walk anywhere from there."
    )


    ## =========================================================================
    ## ACT 2 INFO ITEMS — Ate Bea, Kuya Mark, Ma'am Reyes
    ## =========================================================================

    # --- ATE BEA ITEMS ---
    ITEM_BOX1_INFO = InfoItem(
        "box1_info",
        "What is BOX 1?",
        "Gateway building — all admin offices start here",
        "Ate Bea", "🏢",
        full="BOX 1 is the main administrative building and the first checkpoint when entering campus. It houses the Registrar, Cashier, OSA, and the Chancellor's Office upstairs. The name likely comes from its box shape or its role as the first 'box' you pass. Everything enrollment-related starts here."
    )
    ITEM_UPV_BUS = InfoItem(
        "upv_bus",
        "UPV Bus Schedule",
        "Free shuttle: 5:30/6:00 AM to city, 5:00 PM back",
        "Ate Bea", "🚌",
        full="The UPV shuttle runs from Miagao to Iloilo City, departing at 5:30 AM and 6:00 AM on weekdays. Return trips leave around 5:00 PM. The bus is FREE for enrolled students — just show your validated Form 5 or UP ID. Schedules change every semester, so check the bulletin board or UPV Facebook page. Arrive 10 minutes early — the bus does not wait."
    )
    ITEM_FRESHIE_TIPS = InfoItem(
        "freshie_tips",
        "Freshie Survival Tips",
        "Form 5, office hours, CRS, be polite to staff",
        "Ate Bea", "💡",
        full="Five survival tips for freshies: (1) Always carry your Form 5 — it's your proof of enrollment. (2) Respect office hours — don't show up at closing time. (3) Be polite to staff — a 'Good morning' goes a long way. (4) Learn the CRS (Computerized Registration System) — you'll use it every semester. (5) When in doubt, ask a fellow student."
    )

    # --- KUYA MARK ITEMS ---
    ITEM_ID_POLICY = InfoItem(
        "id_policy",
        "Campus ID Policy",
        "No ID, no entry — wear UP ID at all times",
        "Kuya Mark", "🪪",
        full="Strict ID policy on campus. Once you have your UP ID, wear it at all times inside campus. No ID means no entry at the main gate and most buildings. Freshies can use their Notice of Admission or validated Form 5 as a temporary pass. Keep it in a clear sleeve. Vehicles need a separate sticker from the Security Office. Forgot your ID? Sign the logbook and leave a valid ID — but don't make it a habit."
    )
    ITEM_SECURITY_RULES = InfoItem(
        "security_rules",
        "Security Protocols",
        "Bag checks, zero tolerance, 10 PM curfew",
        "Kuya Mark", "🛡️",
        full="Campus security protocols: (1) Bags subject to inspection at building entrances, especially library and labs. (2) Zero tolerance for alcohol, weapons, illegal substances. (3) Curfew for dormers is 10 PM — need special permission after that. (4) Report incidents immediately to the Security Office near the gate. (5) During emergencies, follow evacuation signs to the open field near the flagpole. Save the security hotline number posted at every building entrance."
    )
    ITEM_RESTRICTED_AREAS = InfoItem(
        "restricted_areas",
        "Restricted Areas",
        "Fishponds, Chancellor's floor, rooftops — off limits",
        "Kuya Mark", "⛔",
        full="Restricted campus areas: Fishponds and wet labs require written permission from the College of Fisheries. The Chancellor's Office floor needs an appointment — no walk-ins. Research vessels and marine stations are for faculty and authorized researchers only. All building rooftops are off-limits with no exceptions. Parts of the beachfront are restricted after 6 PM. Violation means ID confiscation, incident report, and possible disciplinary action through OSA."
    )

    # --- MA'AM REYES ITEMS ---
    ITEM_OFFICE_DIRECTORY = InfoItem(
        "office_directory",
        "BOX 1 Office Directory",
        "Registrar, Cashier, OSA (ground), Chancellor (2F)",
        "Ma'am Reyes", "📋",
        full="BOX 1 ground floor: Office of the University Registrar (enrollment, transcripts, certifications, Form 5), Cashier's Office (fees, refunds, financial transactions), Office of Student Affairs/OSA (scholarships, student orgs, discipline). Second floor: Chancellor's Office, Vice Chancellor offices. New Admin building: College offices, faculty rooms, Conference Room. As a student, Registrar and Cashier will be your most visited offices."
    )
    ITEM_OFFICE_HOURS = InfoItem(
        "office_hours",
        "Office Hours",
        "M-F 8AM-12PM, 1PM-5PM; closed lunch 12-1",
        "Ma'am Reyes", "🕐",
        full="Office hours: Monday to Friday, 8:00 AM to 12:00 NN and 1:00 PM to 5:00 PM. Registrar and Cashier close for lunch 12-1 PM with no exceptions during peak enrollment. OSA may have extended hours during the first week of classes. Chancellor's Office is by appointment only — morning slots fill fast. Some offices operate Saturday 8 AM-12 PM only. Fully closed on holidays. Best time to avoid lines: 8 AM sharp."
    )
    ITEM_APPOINTMENTS = InfoItem(
        "appointments_info",
        "Appointments vs Walk-ins",
        "Walk-in: Registrar, Cashier, OSA. Appointment: Chancellor",
        "Ma'am Reyes", "📅",
        full="Walk-in offices (no appointment needed): Registrar for Form 5, enrollment, certifications. Cashier for payments and receipts. OSA for scholarship inquiries and org matters (expect a wait). Appointment required: Chancellor's Office (email the administrative aide), Vice Chancellor offices, faculty consultations (coordinate with professor), and non-routine Medical Certificate requests through Health Services Unit."
    )

    ## =========================================================================
    ## ACT 3 INFO ITEMS — Sir Noel (Enrollment)
    ## =========================================================================

    # --- SIR NOEL ITEMS ---
    ITEM_CRS_SYSTEM = InfoItem(
        "crs_system",
        "CRS Enrollment System",
        "Computerized Registration System — online enrollment portal",
        "Sir Noel", "💻",
        full="The Computerized Registration System (CRS) is UP's online enrollment portal at crs.upv.edu.ph. Students use it every semester to pre-enlist subjects, confirm enrollment, view grades, and check their academic records. You log in with your student number and password from the Registrar. Pre-enlistment happens before the official enrollment period — the system assigns slots based on availability and priority."
    )
    ITEM_ENROLLMENT_STEPS = InfoItem(
        "enrollment_steps",
        "Enrollment Steps",
        "Pre-enlist → Confirm → Assess → Pay → Get Form 5",
        "Sir Noel", "📝",
        full="The enrollment process: (1) Pre-enlistment — log into CRS and select desired subjects and sections. (2) Confirmation — verify your pre-enlisted subjects when enrollment opens. (3) Assessment — the system calculates your tuition and fees. (4) Payment — pay at the Cashier's Office or via online payment. (5) Form 5 — your official proof of enrollment is generated. Keep it safe — you'll need it everywhere on campus."
    )
    ITEM_UNITS_LOAD = InfoItem(
        "units_load",
        "Academic Load & Units",
        "18 units typical, 3 units per subject, plus PE and NSTP",
        "Sir Noel", "📊",
        full="A typical freshman load is 18 academic units (6 subjects at 3 units each). On top of this, you'll have PE (Physical Education) and NSTP (National Service Training Program) — these are required but carry 0 academic units. Each unit roughly equals 1 hour of class per week. When building your schedule, consider time gaps between classes and avoid back-to-back heavy subjects. The maximum load is usually 21 units with special permission."
    )
    ITEM_SCHEDULE_TIPS = InfoItem(
        "schedule_tips",
        "Schedule Building Tips",
        "Avoid conflicts, check room locations, keep buffer time",
        "Sir Noel", "📅",
        full="Tips for building your class schedule: (1) Check for time conflicts — the CRS won't allow overlapping classes. (2) Consider room locations — give yourself at least 15 minutes between classes in different buildings. (3) Avoid 7:00 AM classes if you're not a morning person — attendance matters. (4) Keep at least one lunch break slot. (5) Balance heavy and light subjects across the week. (6) PE and NSTP schedules are fixed — build around them first."
    )


## ============================================================================
## DEFINE NOTEBOOK QUESTIONS
## ============================================================================

init python:

    notebook_questions = [
        NotebookQuestion(
            "q1",
            "How far is Miagao from Iloilo City?",
            "miagao_location",
            "Someone who's been here before might know this..."
        ),
        NotebookQuestion(
            "q2",
            "What time does the public market close for good buys?",
            "market_hours",
            "A local who knows the town well told you this."
        ),
        NotebookQuestion(
            "q3",
            "How much should you budget for meals per day?",
            "meal_cost",
            "Someone who feeds students every day would know."
        ),
        NotebookQuestion(
            "q4",
            "What phrase do you say to locals to make them trust you?",
            "kinaraya",
            "It's in a language you haven't heard before."
        ),
        NotebookQuestion(
            "q5",
            "What is the fare from the plaza to UPV gate?",
            "tricycle_fare",
            "Two people gave you this info — one might be wrong."
        ),
        NotebookQuestion(
            "q6",
            "What time does the last jeepney leave for Iloilo City?",
            "jeepney_city",
            "Miss this and you're stranded overnight."
        ),
    ]


## ============================================================================
## GROUP CHAT MESSAGES
## ============================================================================

init python:

    gc_all_messages = [

        ## BATCH 1 — revealed on first phone open
        [
            GCMessage("Jaden 🌊",
                "guys is anyone else completely lost rn 😭",
                "#7C3AED"),
            GCMessage("Jaden 🌊",
                "i asked for the registrar and ended up in the fishpond area??",
                "#7C3AED"),
            GCMessage("Caezar ⚡",
                "HAHAHA classic freshie. the fishpond is the OPPOSITE direction",
                "#0F6E56"),
        ],

        ## BATCH 2 — revealed on second phone open
        [
            GCMessage("Unknown 👤",
                "hey does anyone know the tricycle fare to UPV? i got quoted ₱25",
                "#374151"),
            GCMessage("Jaden 🌊",
                "₱25?? no way that's too high. i heard it's ₱15",
                "#7C3AED"),
            GCMessage("Caezar ⚡",
                "depends on the driver tbh. if they see a freshie backpack you're getting freshie prices lol",
                "#0F6E56"),
        ],

        ## BATCH 3 — revealed on third phone open
        [
            GCMessage("Mikhaela 🍢",
                "pls someone tell me there is decent food near campus",
                "#B45309"),
            GCMessage("Jaden 🌊",
                "there's this aleng near the gate!! she saved my life today",
                "#7C3AED"),
            GCMessage("Caezar ⚡",
                "pinakbet + rice + fish. ₱60. don't overthink it",
                "#0F6E56"),
        ],

        ## BATCH 4
        [
            GCMessage("Anonymous 👤",
                "Hello Luis ng compscie 4. I think you're cute and I wanna approach you but I'm too shy. Can we be friends? Kahit more than friends pa sana 🥲- your secret admirer ❤️",
                "#374151"),
            GCMessage("Anonymous 👤",
                "nagawork po ba ang SOTECH x SOTECH",
                "#374151"),
            GCMessage("Anonymous 👤",
                "Hello po! Sino na gusto mag ka jowa? Yung bff ko po kasi jowang-jowa na…",
                "#374151"),
        ],

        ## BATCH 5
        [
            GCMessage("Anonymous 👤",
                "as someone na suki ng mga teleserye, fantasy ko ang San Ag x UP trope 🤩 yung burgis x aktibista trope na sasamahan ako mag rally kahit aircon humor siya",
                "#374151"),
            GCMessage("Anonymous 👤",
                "ganito pala sa economics. mahirap, calculator ang puhunan, puno ng graphs, at higit sa lahat, maraming bading.",
                "#374151"),
            GCMessage("Anonymous 👤",
                "may mga poging professor din ba sa UPV? like yung poging di nakakasawa or like kahit matanda na pero masasabi mong pogi dahip malinis siya o di kaya matalino?",
                "#374151"),
        ],

        ## BATCH 6
        [
            GCMessage("Anonymous 👤",
                "weird po ba 1st year and 4th year? what if yung 1st year po yung nakacrush??",
                "#374151"),
            GCMessage("Anonymous 👤",
                "Hii asking for a friend, anu name sang upclass nga ga smoke tambay sa may mush",
                "#374151"),
            GCMessage("Anonymous 👤",
                "bat parang chill2 lng yung mga appmath dyan, eziest degprog ba talga?",
                "#374151"),
        ],
    ]

    # Player's own GC messages (sent after reading)
    gc_player_messages = [
        "just got here too 😅 someone please explain what BOX 1 is",
        "wait ₱15 to UPV?? a driver just told me ₱20 lol",
        "the church near the plaza is INSANE btw. why did nobody tell me about this",
    ]
