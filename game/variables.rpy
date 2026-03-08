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
}

define ACT_TASK_ORDER = {
    1: ["talk_jaden", "talk_manong_josh", "talk_aleng_maria", "talk_manong_chris", "talk_joseph_driver", "reach_box1"],
    2: ["talk_ate_bea", "talk_kuya_mark", "talk_maam_reyes", "talk_sir_allan", "reach_enrollment"],
    3: ["talk_jaden", "talk_mikhaela", "talk_caezar"],
    4: ["talk_dorm_manager"],
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
        }
        return titles.get(act_num, "The End")
