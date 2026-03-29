## ============================================================================
## GAME VARIABLES — State tracking for tasks, acts, and player position
## ============================================================================

## --- Act & Story Progression ---
default current_act = 1
default current_task_text = ""
default tasks_completed = set()
default subquests_completed = set()
default game_complete = False

## --- Act Task Requirements ---
## Each act has a set of task IDs the player must complete to advance
define ACT1_TASKS = {"talk_jaden", "talk_manong_josh", "talk_aleng_maria", "talk_manong_chris", "talk_joseph_driver", "reach_box1"}
define ACT2_TASKS = {"talk_ate_bea", "talk_kuya_mark", "go_to_newad", "talk_maam_reyes", "complete_flip_card"}
define ACT3_TASKS = {"talk_sir_noel", "view_crs_portal", "complete_enrollment_tetris"}
define ACT4_TASKS = {"talk_dorm_manager", "explore_dorm_room", "complete_room_setup"}

## --- Acts 5–8 Task Requirements ---
define ACT5_TASKS = {"talk_prof_lena", "talk_kuya_rico", "talk_ate_grace", "talk_classmate_dan", "attend_first_class", "visit_hsu"}
define ACT6_TASKS = {"talk_mika", "talk_kuya_tomas", "talk_ate_jenny", "talk_coach_ramon", "visit_org_fair", "visit_scholarship_service"}
define ACT7_TASKS = {"talk_ate_rosa", "talk_kuya_neil", "talk_prof_santos", "talk_classmate_bea", "attend_study_session", "visit_tlrc"}
define ACT8_TASKS = {"talk_jaden_act8", "talk_ate_linda", "talk_nanay_elena", "talk_prof_reyes", "end_of_first_week", "visit_gcsu"}

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
    "explore_dorm_room": "Explore Your Dorm Room",
    "complete_room_setup": "Complete Room Setup",
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
    "visit_hsu": "Visit the Health Services Unit",
    "visit_scholarship_service": "Visit the Scholarship Service",
    "visit_tlrc": "Visit the TLRC",
    "visit_gcsu": "Visit the Guidance & Counseling Office",
}

define ACT_TASK_ORDER = {
    1: ["talk_jaden", "talk_manong_josh", "talk_aleng_maria", "talk_manong_chris", "talk_joseph_driver", "reach_box1"],
    2: ["talk_ate_bea", "talk_kuya_mark", "go_to_newad", "talk_maam_reyes", "complete_flip_card"],
    3: ["talk_sir_noel", "view_crs_portal", "complete_enrollment_tetris"],
    4: ["talk_dorm_manager", "explore_dorm_room", "complete_room_setup"],
    5: ["talk_prof_lena", "talk_kuya_rico", "talk_ate_grace", "talk_classmate_dan", "attend_first_class", "visit_hsu"],
    6: ["talk_mika", "talk_kuya_tomas", "talk_ate_jenny", "talk_coach_ramon", "visit_org_fair", "visit_scholarship_service"],
    7: ["talk_ate_rosa", "talk_kuya_neil", "talk_prof_santos", "talk_classmate_bea", "attend_study_session", "visit_tlrc"],
    8: ["talk_jaden_act8", "talk_ate_linda", "talk_nanay_elena", "talk_prof_reyes", "end_of_first_week", "visit_gcsu"],
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
    "talk_dorm_manager": "Talk to the Dorm Manager about check-in",
    "explore_dorm_room": "Explore your dorm room",
    "complete_room_setup": "Set up your dorm room with essentials",
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

    def complete_subquest(sq_id):
        """Mark an optional subquest as complete."""
        store.subquests_completed.add(sq_id)
        renpy.notify("★ Subquest Complete!")

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
        ## Act 4 prerequisites
        if task_id == "explore_dorm_room":
            return "talk_dorm_manager" in store.tasks_completed
        if task_id == "complete_room_setup":
            return "explore_dorm_room" in store.tasks_completed
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
            4: "ACT 4: Dorm Life",
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

    ## =========================================================================
    ## ACT 4 INFO ITEMS — Dorm Manager (Dormitory Life)
    ## =========================================================================

    ITEM_DORM_POINT_SYSTEM = InfoItem(
        "dorm_point_system",
        "Dorm Point System",
        "Priority based on distance, income bracket, and year level",
        "Dorm Manager", "📋",
        full="The UPV dormitory uses a Point System to prioritize applicants. Points are based on: (1) Distance from permanent residence — farther = more points. Luzon/Mindanao/outside Panay gets maximum points. (2) Family income bracket — lower income = higher priority. (3) Year level — freshmen and graduating students get priority. The dorm is usually at 90%% capacity. If you don't qualify, you'll need to find a boarding house in Miagao town."
    )
    ITEM_DORM_RULES = InfoItem(
        "dorm_rules",
        "Dorm Rules & Curfew",
        "10 PM curfew, no cooking appliances, visitors in lobby only",
        "Dorm Manager", "🏠",
        full="Key dormitory rules: (1) Curfew is 10:00 PM — gates are locked. First offense is a warning, second is community service, third is eviction. (2) No electric coils, heaters, or rice cookers in rooms — fire hazard. (3) Visitors are allowed in the lobby area only, never in the rooms. (4) Quiet hours are 10 PM to 6 AM. (5) Room inspections happen monthly — keep your space clean. (6) Report maintenance issues to the dorm office immediately."
    )
    ITEM_DORM_ESSENTIALS = InfoItem(
        "dorm_essentials",
        "Dorm Room Essentials",
        "What to bring: bedding, fan, toiletries, study lamp, lock",
        "Dorm Manager", "🎒",
        full="Essential items for your dorm room: (1) Bedding — pillow, blanket, bed sheet (mattress provided). (2) Electric fan — no aircon in standard rooms. (3) Toiletries — soap, shampoo, toothbrush, towel. (4) Study lamp — for late-night studying without disturbing roommates. (5) Padlock — for your personal cabinet. (6) Extension cord — limited outlets per room. (7) Hangers and storage boxes — closet space is limited. (8) First aid kit — basic medicine for common ailments. Budget tip: buy from Miagao market, not Manila prices."
    )
    ITEM_DORM_TIPS = InfoItem(
        "dorm_tips",
        "Roommate & Dorm Life Tips",
        "Communicate, share space, respect quiet hours",
        "Dorm Manager", "🤝",
        full="Tips for dorm life: (1) Introduce yourself to your roommate on day one — set expectations early. (2) Agree on shared items like cleaning supplies and snacks. (3) Use headphones after quiet hours. (4) Label your food in shared fridges. (5) Join dorm activities — movie nights, study groups, and floor events. (6) The dorm kitchen has a shared rice cooker and microwave — bring your own utensils. (7) Laundry schedule is posted on the bulletin board — don't miss your slot. (8) The dorm is your first community in UP — make the most of it."
    )


    ## --- SUBQUEST REWARD ITEMS ---

    ITEM_OBLATION_PLEDGE = InfoItem(
        "oblation_pledge",
        "The Oblation & Iskolar ng Bayan",
        "Created by Guillermo Tolentino, 1935 — symbol of service to the nation",
        "Jaden", "🗿",
        full="The Oblation was sculpted by National Artist Guillermo Tolentino in 1935. The figure with outstretched arms and upward-facing gaze symbolizes the Filipino youth's selfless offering to the nation — not to any individual or government, but to the Filipino people. Every UP campus has a replica. As an Iskolar ng Bayan (Scholar of the Nation), your education is subsidized by Philippine taxpayers. Your obligation: to use that education in service. The UP motto 'Honor and Excellence' gives that service its standard."
    )
    ITEM_MIAGAO_HERITAGE = InfoItem(
        "miagao_heritage",
        "Miagao Heritage",
        "Baroque church completed 1797 — UNESCO World Heritage Site",
        "Manong Josh", "⛪",
        full="The Santo Tomas de Villanueva Parish Church of Miagao was completed in 1797 during Spanish colonial rule. It is a UNESCO World Heritage Site and a National Cultural Treasure. Its baroque façade uniquely blends European architecture with indigenous Filipino motifs — coconut trees, papaya plants, and Santo Tomas dressed in local attire. The church survived invasions, earthquakes, and typhoons across three centuries. It is a symbol of Miagao's resilience and cultural identity. As a UPV student, you live in the shadow of this heritage. Respect it."
    )
    ITEM_UP_JARGON = InfoItem(
        "up_jargon",
        "UP Academic Jargon",
        "DRP, INC, LOA, GWA, MAO — know these before they happen to you",
        "Ate Bea", "📖",
        full="Essential UP academic terms: GWA (Grade Weighted Average) — your semester-end average weighted by units. DRP (Dropped) — official withdrawal from a course before the deadline; not a failing grade. INC (Incomplete) — unfinished requirements; you have one year to complete them or they become a 5.0. LOA (Leave of Absence) — an approved one-semester pause in enrollment; you remain a UP student. 4.00 — conditional failure; you may take a removal exam. 5.00 — outright failure; retake the subject. MAO (Maximum Allowable Absence) — more than 20% of class meetings triggers automatic DRP."
    )
    ITEM_STUDENT_RIGHTS = InfoItem(
        "student_rights",
        "UP Student Rights",
        "Quality education, due process, academic freedom — know your rights",
        "Kuya Mark", "⚖️",
        full="Under the UP Student Handbook: (1) Right to quality education — professors must follow the syllabus, hold classes, and grade fairly. (2) Right to due process in discipline — you must be informed of charges and given a chance to respond. (3) Right to academic freedom — your intellectual inquiry is protected. (4) Right to a grievance process — unjust grades or treatment can be appealed: professor → department chair → dean → OSA. (5) Right to organize — recognized student organizations are protected from arbitrary dissolution. (6) Rights apply to ALL students equally, regardless of scholarship or STFAP bracket."
    )
    ITEM_CRS_TACTICS = InfoItem(
        "crs_tactics",
        "CRS Battle Tactics",
        "Backup classes, adjustment period, prerequisites — survive enlistment",
        "Sir Noel", "💻",
        full="CRS (Computerized Registration System) survival guide: (1) Always prepare backup classes before enlistment opens. Popular subjects fill in seconds. (2) Use the adjustment period to add, drop, or switch sections after initial enlistment. (3) Prerequisites are system-enforced — you cannot enlist in an upper-level course without completing the lower one. (4) If a class is full, check again on the first day of classes — some students drop. (5) Use wired internet (ethernet) during enlistment — WiFi is unreliable under load. (6) Overrides are only for graduating students with documented curriculum needs. (7) Know your curriculum map from semester one."
    )
    ITEM_ACADEMIC_LOAD = InfoItem(
        "academic_load",
        "Academic Load Guide",
        "15–18 units standard; NSTP required; overload needs dean approval",
        "Sir Noel", "📋",
        full="Academic load rules: Standard full load is 15–18 units per semester; maximum is 21 units with dean approval for students in good standing. NSTP (National Service Training Program) is required for all first and second year students under RA 9163 — 3 units per semester for two semesters; choose CWTS (Civic Welfare Training Service) or LTS (Literacy Training Service). Taking fewer than 15 units is part-time enrollment — check if your scholarship requires full-time status. Academic probation may result from a GWA below 2.00 for two consecutive semesters. Know your curriculum flowchart from day one."
    )
    ITEM_DORM_CODE = InfoItem(
        "dorm_code",
        "Dorm Code of Conduct",
        "Visitors in common areas only, curfew 10 PM, due process for disputes",
        "Dorm Manager", "🏠",
        full="Key UPV dormitory policies: (1) Visitor rule — guests are restricted to common areas only; no visitors in rooms after 8 PM. (2) Main gate curfew — 10 PM on weekdays; inform the dorm manager if you'll be late. (3) Noise — quiet hours from 10 PM; respect shared study time. (4) Room inspection — every two weeks; keep your space clean. (5) No cooking in rooms — use the communal kitchen only (fire safety). (6) Roommate disputes — resolve directly first; escalate to dorm manager for mediation before going to OSA. (7) Emergency protocol — during typhoons or university closures, inform the dorm manager before leaving campus."
    )
    ITEM_SURVIVAL_KIT = InfoItem(
        "survival_kit",
        "Freshie Survival Kit",
        "Medicine, power bank, community — the three things you really need",
        "Nanay Elena", "🎒",
        full="The real freshman survival kit: PHYSICAL — basic medicines (paracetamol, antacid, antihistamine, ORS, thermometer), a 20,000 mAh power bank, printed backup notes before exam week, and a flashlight for outages. PRACTICAL — a padlock, extension cord, study lamp, and reusable water bottle (the heat causes more clinic visits than anything else). SOCIAL — the most important item: at least one real friend or community here in Miagao. Every physical problem has a solution. Loneliness is healed only by belonging. A dorm room full of supplies and empty of connection is not surviving — it's just existing."
    )
    ITEM_GRADING_GUIDE = InfoItem(
        "grading_guide",
        "UP Grading System",
        "1.0 highest → 3.0 passing → 4.0 conditional → 5.0 fail",
        "Prof. Lena", "📊",
        full="UP numerical grading scale: 1.00 (Excellent/Outstanding) → 1.25, 1.50, 1.75 (Very Good to Good) → 2.00, 2.25, 2.50 (Satisfactory) → 2.75 (Passing) → 3.00 (Lowest passing grade) → 4.00 (Conditional failure — removal exam allowed) → 5.00 (Failure — retake required). Special marks: INC (Incomplete — complete within one year or becomes 5.0), DRP (Dropped — official withdrawal). Academic distinctions: University Scholar (GWA ≤ 1.20), College Scholar (GWA ≤ 1.45), Dean's Lister (GWA ≤ 1.75, recognition only). Scholarship maintenance usually requires GWA ≤ 2.00 — check your specific grant conditions."
    )
    ITEM_MAO_POLICY = InfoItem(
        "mao_policy",
        "MAO — Maximum Allowable Absence",
        "More than 20% of class meetings = automatic DRP",
        "Kuya Rico", "📅",
        full="The Maximum Allowable Absence (MAO) rule: A student who incurs absences of MORE than 20% of the total prescribed class meetings shall be dropped from the course (recorded as DRP — not 5.0). For a 3-unit MWF class across 18 weeks (~54 meetings), this means approximately 10–11 absences. HOWEVER: many professors set STRICTER absence limits in their syllabus (e.g., 6 absences = DRP). Always read the syllabus. Tardiness: no universal UP tardiness-to-absence conversion exists, but individual professors may apply one. Being dropped for MAO can affect scholarship status even though it appears as DRP, not 5.0."
    )
    ITEM_ORG_CULTURE = InfoItem(
        "org_culture",
        "Student Organization Culture",
        "OSA-registered, 15 members minimum, anti-hazing laws strictly apply",
        "Mika", "🌿",
        full="Student organization requirements at UPV: Minimum 15 student members, a written constitution and by-laws, a faculty adviser, and OSA (Office of Student Affairs) approval. Unrecognized orgs cannot officially use campus facilities or collect fees. Membership fees: typically ₱50–200/semester, set in the org's constitution. HAZING: Republic Act 8049 and RA 11053 (Expanded Anti-Hazing Act) strictly prohibit physical and psychological hazing during recruitment or initiation. Violations result in criminal charges — not just school suspension. Report hazing to the OSA immediately. You have the right to join or not join any org without coercion."
    )
    ITEM_UPV_EVENTS = InfoItem(
        "upv_events",
        "UPV Events Calendar",
        "Lantern Parade, Pahampang, Arts Month, Loyalty Day — attend all of these",
        "Ate Jenny", "🗓️",
        full="Major UPV campus events every student should experience: LANTERN PARADE — pre-Christmas competition where colleges and orgs build giant lanterns and parade them across campus. PAHAMPANG — the annual inter-college sports festival; basketball, volleyball, swimming, track and field. ARTS MONTH — cultural performances, visual art exhibits, literary events; usually held in February–March. LOYALTY DAY — annual celebration of UP's founding on June 18, 1908; awards, alumni recognition, student performances. FRESHIE WEEK — your week; orientation, org fair, campus tours. GRADUATION — when all of this becomes real. Attend these events — they are not distractions. They are the education."
    )
    ITEM_APA_GUIDE = InfoItem(
        "apa_guide",
        "APA 7th Edition Quick Guide",
        "In-text: (Author, Year) | Reference: Author, I. (Year). Title. Journal, Vol, Pages.",
        "Bea", "📝",
        full="APA 7th Edition essentials: IN-TEXT CITATION — (Last Name, Year) for paraphrase; (Last Name, Year, p. #) for direct quote. REFERENCE LIST format for journal article: Last, F. (Year). Title in sentence case. Journal Name in Title Case and Italics, Volume(Issue), pages. https://doi.org/xxxxx. PLAGIARISM: includes copy-paste, too-close paraphrasing, submitting others' work, and self-plagiarism. Turnitin detects all forms. PRACTICAL RULE: If the idea is not yours, cite it. When in doubt, cite it. Always write in your own voice — summarize, don't transcribe. Get the TLRC's one-page APA cheat sheet for quick reference during paper-writing."
    )
    ITEM_UP_MANDATES = InfoItem(
        "up_mandates",
        "UP's Three Mandates",
        "Instruction, Research, Extension — all three define what UP is",
        "Prof. Santos", "🔬",
        full="Under the UP Charter (Republic Act 9500, 2008), the University of the Philippines has three core mandates: (1) INSTRUCTION — quality tertiary education across arts, sciences, and professions. (2) RESEARCH — generation of new knowledge; UP is the leading research university in the Philippines. (3) EXTENSION — applying university knowledge to benefit communities, especially marginalized ones. UPV's strength lies in marine science and fisheries research (via CFOS), directly serving Western Visayas coastal communities. As an Iskolar ng Bayan, you're expected to contribute to all three before graduation — through your coursework, thesis, and professional life."
    )
    ITEM_UPV_IDENTITY = InfoItem(
        "upv_identity",
        "UP Visayas Identity",
        "Established 1979 | Campuses: Miagao, Iloilo City, Tacloban | 4 colleges",
        "Jaden", "🎓",
        full="UP Visayas was established as a constituent university in 1979, growing from the College of Fisheries founded in 1947. Main campus: Miagao, Iloilo. Satellite campuses: UPV-Iloilo City College (UPV-ICC) and UPV Tacloban College (UPV-TC) in Leyte. Four colleges at Miagao: CAS (College of Arts and Sciences) — GE and liberal arts; CFOS (College of Fisheries and Ocean Sciences) — marine science flagship, one of Southeast Asia's leading fisheries institutes; CM (College of Management) — business, economics, management; CTE (College of Technology and Environmental Management) — engineering and environmental programs. UPV's regional identity is inseparable from the sea."
    )
    ITEM_HONOR_EXCELLENCE = InfoItem(
        "honor_excellence",
        "Honor and Excellence",
        "UP's motto: integrity in work, excellence in service — not just in grades",
        "Prof. Reyes", "🏅",
        full="UP's motto 'Honor and Excellence' defines the standard for every Iskolar ng Bayan. HONOR means academic integrity: submitting your own work, citing sources, refusing to cheat even under pressure, and speaking up when you witness injustice. It means being a person whose word means something. EXCELLENCE means the quality of your work, your character, and how you use your education in service. A 1.0 GWA with no moral backbone serves no one. Excellence is not just a grade — it is a way of living. The Oblation statue embodies both: arms raised, not grasping, but offering. That is the UP ideal."
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
