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
define ACT2_TASKS = {"talk_ate_bea", "talk_kuya_mark", "talk_maam_reyes", "talk_sir_allan", "reach_enrollment"}
define ACT3_TASKS = {"talk_mikhaela", "talk_jaden", "talk_caezar"}
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
    "talk_maam_reyes": "Talk to Ma'am Reyes",
    "talk_sir_allan": "Talk to Sir Allan",
    "reach_enrollment": "Go to Enrollment Office",
    "talk_mikhaela": "Find Sarah",
    "talk_caezar": "Meet Caezar at Ceazar",
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
    2: ["talk_ate_bea", "talk_kuya_mark", "talk_maam_reyes", "talk_sir_allan", "reach_enrollment"],
    3: ["talk_jaden", "talk_mikhaela", "talk_caezar"],
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
    "talk_ate_bea": "Talk to Ate Bea at BOX 1 entrance",
    "talk_kuya_mark": "Talk to Kuya Mark about security",
    "talk_maam_reyes": "Talk to Ma'am Reyes about offices",
    "talk_sir_allan": "Talk to Sir Allan",
    "reach_enrollment": "Go to the Enrollment Office",
    "talk_mikhaela": "Talk to Sarah",
    "talk_caezar": "Meet Caezar after talking to Jaden and Sarah",
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
        if task_id in ("talk_kuya_mark", "talk_maam_reyes"):
            return "talk_ate_bea" in store.tasks_completed
        if task_id == "talk_sir_allan":
            return ("talk_kuya_mark" in store.tasks_completed or
                    "talk_maam_reyes" in store.tasks_completed)
        if task_id == "reach_enrollment":
            return (
                "talk_ate_bea" in store.tasks_completed and
                "talk_kuya_mark" in store.tasks_completed and
                "talk_maam_reyes" in store.tasks_completed and
                "talk_sir_allan" in store.tasks_completed
            )
        ## Act 3 prerequisites
        if task_id == "talk_caezar":
            return (
                "talk_jaden" in store.tasks_completed and
                "talk_mikhaela" in store.tasks_completed
            )
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
            2: "ACT 2: Exploring BOX 1",
            3: "ACT 3: Social / Exploration",
            4: "ACT 4: Dorm Accommodation",
            5: "ACT 5: First Day of Classes",
            6: "ACT 6: Student Orgs & Campus Life",
            7: "ACT 7: Library & Academic Resources",
            8: "ACT 8: Finding Your Place",
        }
        return titles.get(act_num, "The End")
