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
define ACT1_TASKS = {
    "talk_jaden",
    "talk_manong_josh",
    "talk_aleng_maria",
    "talk_manong_chris",
    "talk_joseph_driver",
}
define ACT2_TASKS = {"talk_ms_santos", "talk_sarah"}
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
    "talk_ms_santos": "Visit Ms. Santos at the OSA (CUB)",
    "talk_sarah": "Talk to Sarah at the enrollment line",
    "talk_mikhaela": "Find Mikhaela",
    "talk_jaden": "Talk to Jaden",
    "talk_caezar": "Meet Caezar at Lover's Lane",
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

    def is_act_complete():
        """Check if all tasks for the current act are done."""
        return len(get_current_tasks()) == 0

    def get_act_title(act_num):
        titles = {
            1: "ACT 1: Arrival in Miagao",
            2: "ACT 2: Exploring BOX 1",
            3: "ACT 3: Enrollment & CRS",
            4: "ACT 4: Dorm Accommodation",
        }
        return titles.get(act_num, "The End")
