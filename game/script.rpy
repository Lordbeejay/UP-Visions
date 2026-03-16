## ============================================================================
## MIAGAO FRESHMAN GUIDE — Main Game Script
## ============================================================================
## A point-and-click adventure set in UP Visayas - Miagao campus.
## Navigate the top-down map, click locations, and experience the story
## of a freshman's first day navigating enrollment, medical exams,
## and campus life.
## ============================================================================
##
## ============================================================================
## --- Map zoom constant ---
define MAP_ZOOM = 0.144

label start:
    ## stop the fucking music when entering game
    stop music fadeout 1.0  # FUCKING STOP the main menu theme

    ## Hide the dialogue window for map exploration
    window hide

    ## --- Fade to black from main menu ---
    scene black with Dissolve(1.0)
    pause 0.3

    ## --- INTRO SEQUENCE ---
    scene bg miagao_campus with Dissolve(1.2)
    pause 0.3

    call screen act_transition("MIAGAO FRESHMAN GUIDE", "A point-and-click adventure\nNavigate your first day at UP Visayas", mode="welcome")

    ## --- ACT 4 ---
    scene expression "images/ui/UI_Miagao.png" with fade
    call screen act_transition("ACT 4", "Dorm Accommodation", mode="intro")

    $ current_act = 1
    $ tasks_completed = set()
    $ player_map_x = 2300
    $ player_map_y = 3100
    $ player_facing = "up"
    jump act2_map


## ============================================================================
## ACT 1 MAP — Banwa (Gate / HSU / Admin / Medical)
## ============================================================================
## Map features (map coords on 5000x5000 map):
## - Gate/Guard: bottom center (2500, 3200)
## - HSU: upper-left area (1800, 2000)
## - Admin/Registrar: center (2500, 2500)
## - Medical buildings: center-left (2000, 2300)
## ============================================================================

label act1_map:
    $ current_map_bg = "maps/banwa.png"
    $ act1_nodes = [
        MapNode("jaden",         1200, 1400, "act1_npc_jaden",         tooltip="Jaden",           icon_image="jaden.png",          locked=False),
        MapNode("manong_josh",   2100, 2600, "act1_npc_manong_josh",   tooltip="Manong Josh",     icon_image="manongjosh.png",    locked=True),
        MapNode("aleng_maria",   3000, 2200, "act1_npc_aleng_maria",   tooltip="Aleng Maria",     icon_image="alengmaria.png",    locked=True),
        MapNode("manong_chris",  3600, 3000, "act1_npc_manong_chris",  tooltip="Manong Chris",    icon_image="manongchris.png",   locked=True),
        MapNode("joseph_driver", 2500, 3800, "act1_npc_joseph_driver", tooltip="Joseph (Driver)", icon_image="manong_driver.png",  locked=True),
        MapNode("box1",          4200, 1800, "act1_prebox1_gate",      tooltip="BOX 1",           icon_image="box1.png",           locked=True),
    ]

    $ current_task_text = "Talk to Jaden near the Banwa entrance"

label act1_loop:
    call screen map_screen("maps/banwa.png", act1_nodes, current_task_text, 1.0)

    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node)
        call expression _node.target_label

        ## unlock logic below...
        if "talk_jaden" in tasks_completed:
            $ act1_nodes[1].locked = False
            $ act1_nodes[2].locked = False
            ## Switch Jaden's target to second talk (unlocks GC)
            $ act1_nodes[0].target_label = "act1_npc_jaden_second"

        if "talk_manong_josh" in tasks_completed or "talk_aleng_maria" in tasks_completed:
            $ act1_nodes[3].locked = False

        if "talk_manong_chris" in tasks_completed:
            $ act1_nodes[4].locked = False

        if (
            "talk_jaden"         in tasks_completed and
            "talk_manong_josh"   in tasks_completed and
            "talk_aleng_maria"   in tasks_completed and
            "talk_manong_chris"  in tasks_completed and
            "talk_joseph_driver" in tasks_completed
        ):
            $ act1_nodes[5].locked = False
            $ current_task_text = "Talk to Jaden again, then head to BOX 1"

        if is_act_complete():
            jump act1_complete

    ## Phone toggle (P key) — universal
    if _action == "phone":
        call phone_check

    ## Inventory toggle (I key) — universal
    if _action == "inventory":
        if inventory_unlocked:
            call screen inventory_screen()

    jump act1_loop



label act1_complete:
    scene expression "images/ui/UI_Miagao.png" with fade
    pause 0.3
    call screen act_transition("ACT 1 COMPLETE", "You've learned the lay of the land.\nMiagao is starting to feel like home.", "complete")
    call screen act_transition("ACT 2", "Entering the University", "intro")

    $ current_act = 2
    $ player_map_x = 2500
    $ player_map_y = 2800
    $ player_facing = "up"
    jump act2_map


## ============================================================================
## ACT 2 MAP — Entrance → New Admin → Inside New Admin
## ============================================================================

## --- PHASE 1: Entrance map with Ate Bea and Kuya Mark ---
label act2_map:
    $ current_map_bg = "maps/Entrance.png"
    $ act2_entrance_nodes = [
        MapNode("ate_bea",    1600, 2600, "act2_npc_ate_bea",    tooltip="Ate Bea",     icon_image="ate_bea.png",    locked=False),
        MapNode("kuya_mark",  3200, 2200, "act2_npc_kuya_mark",  tooltip="Kuya Mark",   icon_image="kuya_mark.png",  locked=True),
        MapNode("newad_gate", 2500, 1200, "act2_go_to_newad",    tooltip="New Admin",   icon_image="box1.png",       locked=True),
    ]
    $ current_task_text = "Talk to Ate Bea at the Entrance"

label act2_entrance_loop:
    call screen map_screen("maps/Entrance.png", act2_entrance_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node)
        call expression _node.target_label

        if "talk_ate_bea" in tasks_completed:
            $ act2_entrance_nodes[1].locked = False
            $ current_task_text = "Talk to Kuya Mark about campus security"

        if "talk_ate_bea" in tasks_completed and "talk_kuya_mark" in tasks_completed:
            $ act2_entrance_nodes[2].locked = False
            $ current_task_text = "Head to New Admin building"

        ## After clicking New Admin, transition to phase 2
        if "go_to_newad" in tasks_completed:
            jump act2_newad_map

    jump act2_entrance_loop


## --- PHASE 2: New Admin exterior — enter inside ---
label act2_newad_map:
    $ current_map_bg = "maps/NewAd.png"
    $ player_map_x = 2500
    $ player_map_y = 3200
    $ player_facing = "up"

    $ act2_newad_nodes = [
        MapNode("enter_inside", 2500, 1800, "act2_enter_inside", tooltip="Enter New Admin", icon_image="box1.png", locked=False),
    ]
    $ current_task_text = "Enter the New Admin building"

label act2_newad_loop:
    call screen map_screen("maps/NewAd.png", act2_newad_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node)
        call expression _node.target_label

        ## After entering, transition to phase 3
        jump act2_inside_map

    jump act2_newad_loop


## --- PHASE 3: Inside New Admin — find Ma'am Reyes ---
label act2_inside_map:
    $ current_map_bg = "maps/NewAd_Inside.png"
    $ player_map_x = 2500
    $ player_map_y = 3500
    $ player_facing = "up"

    $ act2_inside_nodes = [
        MapNode("maam_reyes", 2500, 1800, "act2_npc_maam_reyes", tooltip="Ma'am Reyes", icon_image="maam_reyes.png", locked=False),
    ]
    $ current_task_text = "Find Ma'am Reyes inside New Admin"

label act2_inside_loop:
    call screen map_screen("maps/NewAd_Inside.png", act2_inside_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node)
        call expression _node.target_label

        if "talk_maam_reyes" in tasks_completed:
            $ current_task_text = "Complete the Office Match Game!"

        if is_act_complete():
            jump act2_complete

    jump act2_inside_loop


label act2_complete:
    scene expression "images/ui/UI_Miagao.png" with fade
    pause 0.3
    call screen act_transition("ACT 2 COMPLETE", "You've navigated enrollment\nand met the campus staff!", "complete")
    call screen act_transition("ACT 3", "Social / Exploration", "intro")

    $ current_act = 3
    $ player_map_x = 2500
    $ player_map_y = 2600
    $ player_facing = "down"
    jump act3_map


## ============================================================================
## ACT 3 MAP — Social / Exploration
## ============================================================================

label act3_map:
    $ current_map_bg = "maps/banwa.png"
    $ act3_nodes = [
        MapNode("Sarah", 2600, 3000, "npc_mikhaela", "Sarah", False, "#ff99cc", "sarah.png"),
        MapNode("Jaden", 2100, 2600, "act3_npc_jaden", "Jaden", False, "#99ccff", "jaden.png"),
        MapNode("Ceazar", 1600, 1800, "npc_caezar", "Ceazar", True, "#ccff99", "caezar.png", icon_zoom=0.06),
    ]

    $ current_task_text = "Explore campus — find Sarah and Jaden"

label act3_loop:
    # Refresh node labels/tooltips for compatibility with old saves.
    if len(act3_nodes) >= 3:
        $ act3_nodes[0].name = "Sarah"
        $ act3_nodes[0].tooltip = "Sarah"
        $ act3_nodes[1].name = "Jaden"
        $ act3_nodes[1].tooltip = "Jaden"
        $ act3_nodes[2].name = "Ceazar"
        $ act3_nodes[2].tooltip = "Ceazar"

    call screen map_screen("maps/banwa.png", act3_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node)
        call expression _node.target_label

        if "talk_jaden" in tasks_completed:
            $ act3_nodes[2].locked = False
            if "talk_caezar" not in tasks_completed:
                $ current_task_text = "Meet Caezar at Ceazar"

        if is_act_complete():
            jump act3_complete

    jump act3_loop


label act3_complete:
    scene expression "images/ui/UI_Miagao.png" with fade
    pause 0.3
    call screen act_transition("ACT 3 COMPLETE", "You've made friends and explored the campus!", "complete")
    call screen act_transition("ACT 4", "Dorm Accommodation", "intro")

    $ current_act = 4
    $ player_map_x = 2500
    $ player_map_y = 2600
    $ player_facing = "up"
    jump act4_map


## ============================================================================
## ACT 4 MAP — Dorm
## ============================================================================

label act4_map:
    $ current_map_bg = "ui/Dorm.png"
    $ act4_nodes = [
        MapNode("Dorm", 2500, 2500, "npc_dorm_manager", "Dormitory Office", False, "#ffaa77", "dorm_mgr.png"),
    ]

    $ current_task_text = "Talk to the Dorm Manager"

label act4_loop:
    call screen map_screen("ui/Dorm.png", act4_nodes, current_task_text, 2.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node)
        call expression _node.target_label

        if is_act_complete():
            jump act4_complete

    jump act4_loop


label act4_complete:
    scene expression "images/ui/UI_Miagao.png" with fade
    pause 0.3
    call screen act_transition("ACT 4 COMPLETE", "You've secured your dorm room!", "complete")
    call screen act_transition("ACT 5", "First Day of Classes", "intro")

    $ current_act = 5
    $ player_map_x = 2500
    $ player_map_y = 2600
    $ player_facing = "up"
    jump act5_map


## ============================================================================
## ACT 5 MAP — First Day of Classes
## ============================================================================

label act5_map:
    $ current_map_bg = "ui/CL3.png"
    $ act5_nodes = [
        MapNode("prof_lena",     1800, 1800, "act5_npc_prof_lena",     tooltip="Prof. Lena",     icon_image="prof_lena.png",     locked=False),
        MapNode("kuya_rico",     2800, 2200, "act5_npc_kuya_rico",     tooltip="Kuya Rico",      icon_image="kuya_rico.png",     locked=True),
        MapNode("ate_grace",     3200, 2800, "act5_npc_ate_grace",     tooltip="Ate Grace",      icon_image="ate_grace.png",     locked=True),
        MapNode("classmate_dan", 2200, 3200, "act5_npc_classmate_dan", tooltip="Dan",            icon_image="classmate_dan.png", locked=True),
        MapNode("first_class",   2500, 1400, "act5_first_class",       tooltip="First Class",    icon_image="box1.png",          locked=True),
    ]
    $ current_task_text = "Talk to Prof. Lena in the classroom"

label act5_loop:
    call screen map_screen("ui/CL3.png", act5_nodes, current_task_text, 0.7)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node)
        call expression _node.target_label

        if "talk_prof_lena" in tasks_completed:
            $ act5_nodes[1].locked = False
            $ act5_nodes[2].locked = False
            $ current_task_text = "Talk to Kuya Rico and Ate Grace"

        if "talk_kuya_rico" in tasks_completed or "talk_ate_grace" in tasks_completed:
            $ act5_nodes[3].locked = False

        if (
            "talk_prof_lena" in tasks_completed and
            "talk_kuya_rico" in tasks_completed and
            "talk_ate_grace" in tasks_completed and
            "talk_classmate_dan" in tasks_completed
        ):
            $ act5_nodes[4].locked = False
            $ current_task_text = "Attend your first class"

        if is_act_complete():
            jump act5_complete

    jump act5_loop


label act5_complete:
    scene expression "images/ui/UI_Miagao.png" with fade
    pause 0.3
    call screen act_transition("ACT 5 COMPLETE", "You survived your first day of classes!", "complete")
    call screen act_transition("ACT 6", "Student Orgs & Campus Life", "intro")

    $ current_act = 6
    $ player_map_x = 2500
    $ player_map_y = 2600
    $ player_facing = "down"
    jump act6_map


## ============================================================================
## ACT 6 MAP — Student Orgs & Campus Life
## ============================================================================

label act6_map:
    $ current_map_bg = "ui/CAS_Overworld(F).png"
    $ act6_nodes = [
        MapNode("mika",         1600, 2200, "act6_npc_mika",         tooltip="Mika",          icon_image="mika.png",         locked=False),
        MapNode("kuya_tomas",   2800, 1900, "act6_npc_kuya_tomas",   tooltip="Kuya Tomas",    icon_image="kuya_tomas.png",   locked=True),
        MapNode("ate_jenny",    2200, 2800, "act6_npc_ate_jenny",    tooltip="Ate Jenny",     icon_image="ate_jenny.png",    locked=True),
        MapNode("coach_ramon",  3400, 2600, "act6_npc_coach_ramon",  tooltip="Coach Ramon",   icon_image="coach_ramon.png",  locked=True),
        MapNode("org_fair",     2500, 1500, "act6_org_fair",         tooltip="Org Fair",      icon_image="box1.png",         locked=True),
    ]
    $ current_task_text = "Talk to Mika at the org fair"

label act6_loop:
    call screen map_screen("ui/CAS_Overworld(F).png", act6_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node)
        call expression _node.target_label

        if "talk_mika" in tasks_completed:
            $ act6_nodes[1].locked = False
            $ act6_nodes[2].locked = False
            $ current_task_text = "Learn about scholarships and the OSA"

        if "talk_kuya_tomas" in tasks_completed or "talk_ate_jenny" in tasks_completed:
            $ act6_nodes[3].locked = False

        if (
            "talk_mika" in tasks_completed and
            "talk_kuya_tomas" in tasks_completed and
            "talk_ate_jenny" in tasks_completed and
            "talk_coach_ramon" in tasks_completed
        ):
            $ act6_nodes[4].locked = False
            $ current_task_text = "Walk through the org fair"

        if is_act_complete():
            jump act6_complete

    jump act6_loop


label act6_complete:
    scene expression "images/ui/UI_Miagao.png" with fade
    pause 0.3
    call screen act_transition("ACT 6 COMPLETE", "You've explored campus life and organizations!", "complete")
    call screen act_transition("ACT 7", "Library & Academic Resources", "intro")

    $ current_act = 7
    $ player_map_x = 2500
    $ player_map_y = 2600
    $ player_facing = "up"
    jump act7_map


## ============================================================================
## ACT 7 MAP — Library & Academic Resources
## ============================================================================

label act7_map:
    $ current_map_bg = "ui/Diwata.png"
    $ act7_nodes = [
        MapNode("ate_rosa",      1800, 2000, "act7_npc_ate_rosa",      tooltip="Ate Rosa",      icon_image="ate_rosa.png",      locked=False),
        MapNode("kuya_neil",     2800, 2400, "act7_npc_kuya_neil",     tooltip="Kuya Neil",     icon_image="kuya_neil.png",     locked=True),
        MapNode("prof_santos",   3200, 1800, "act7_npc_prof_santos",   tooltip="Prof. Santos",  icon_image="prof_santos.png",   locked=True),
        MapNode("classmate_bea", 2200, 3000, "act7_npc_classmate_bea", tooltip="Bea",           icon_image="classmate_bea.png", locked=True),
        MapNode("study_session", 2500, 1400, "act7_study_session",     tooltip="Study Session",  icon_image="box1.png",          locked=True),
    ]
    $ current_task_text = "Talk to Ate Rosa at the library"

label act7_loop:
    call screen map_screen("ui/Diwata.png", act7_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node)
        call expression _node.target_label

        if "talk_ate_rosa" in tasks_completed:
            $ act7_nodes[1].locked = False
            $ act7_nodes[2].locked = False
            $ current_task_text = "Explore the computer lab and talk to professors"

        if "talk_kuya_neil" in tasks_completed or "talk_prof_santos" in tasks_completed:
            $ act7_nodes[3].locked = False

        if (
            "talk_ate_rosa" in tasks_completed and
            "talk_kuya_neil" in tasks_completed and
            "talk_prof_santos" in tasks_completed and
            "talk_classmate_bea" in tasks_completed
        ):
            $ act7_nodes[4].locked = False
            $ current_task_text = "Attend the study session"

        if is_act_complete():
            jump act7_complete

    jump act7_loop


label act7_complete:
    scene expression "images/ui/UI_Miagao.png" with fade
    pause 0.3
    call screen act_transition("ACT 7 COMPLETE", "You've discovered the library and academic resources!", "complete")
    call screen act_transition("ACT 8", "Finding Your Place", "intro")

    $ current_act = 8
    $ player_map_x = 2500
    $ player_map_y = 2600
    $ player_facing = "down"
    jump act8_map


## ============================================================================
## ACT 8 MAP — End of First Week: Finding Your Place
## ============================================================================

label act8_map:
    $ current_map_bg = "ui/dormRoom.png"
    $ act8_nodes = [
        MapNode("jaden_act8",    2100, 2600, "act8_npc_jaden",       tooltip="Jaden",         icon_image="jaden.png",        locked=False),
        MapNode("ate_linda",     1600, 3200, "act8_npc_ate_linda",   tooltip="Ate Linda",     icon_image="ate_linda.png",    locked=True),
        MapNode("nanay_elena",   3300, 1900, "act8_npc_nanay_elena", tooltip="Nanay Elena",   icon_image="nanay_elena.png",  locked=True),
        MapNode("prof_reyes",    2800, 1600, "act8_npc_prof_reyes",  tooltip="Prof. Reyes",   icon_image="prof_reyes.png",   locked=True),
        MapNode("end_of_week",   2500, 2200, "act8_end_of_week",     tooltip="Campus Oval",   icon_image="box1.png",         locked=True),
    ]
    $ current_task_text = "Catch up with Jaden"

label act8_loop:
    call screen map_screen("ui/dormRoom.png", act8_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node)
        call expression _node.target_label

        if "talk_jaden_act8" in tasks_completed:
            $ act8_nodes[1].locked = False
            $ act8_nodes[2].locked = False
            $ current_task_text = "Talk to Ate Linda and Nanay Elena"

        if "talk_ate_linda" in tasks_completed or "talk_nanay_elena" in tasks_completed:
            $ act8_nodes[3].locked = False

        if (
            "talk_jaden_act8" in tasks_completed and
            "talk_ate_linda" in tasks_completed and
            "talk_nanay_elena" in tasks_completed and
            "talk_prof_reyes" in tasks_completed
        ):
            $ act8_nodes[4].locked = False
            $ current_task_text = "Reflect on your first week at the campus oval"

        if is_act_complete():
            jump act8_complete

    jump act8_loop


label act8_complete:
    scene expression "images/ui/UI_Miagao.png" with fade
    pause 0.3
    call screen act_transition("ACT 8 COMPLETE", "You've found your place at UP Visayas.", "complete")

    jump open_world


## ============================================================================
## OPEN WORLD — Free Exploration (Endgame)
## ============================================================================

label open_world:
    scene expression "images/ui/UI_Miagao.png" with fade
    pause 0.3
    call screen act_transition("OPEN WORLD", "Classes start next week. Explore freely!", "intro")

    $ current_act = 9
    $ player_map_x = 2500
    $ player_map_y = 2600
    $ player_facing = "down"

    $ current_map_bg = "maps/banwa.png"
    $ openworld_nodes = [
        MapNode("Gate", 2500, 3200, "ow_gate", "Banwa Gate", False, "#44cc44", "manong_guard.png"),
        MapNode("HSU", 1800, 2000, "ow_hsu", "Health Services", False, "#4499ff", "hsu_nurse.png"),
        MapNode("Admin", 2500, 2500, "ow_admin", "New Admin Building", False, "#ff8844", "sir_ruel.png"),
        MapNode("CUB", 1900, 1800, "ow_cub", "CUB / OSA", False, "#cc99ff", "ms_santos.png"),
        MapNode("Kiosk", 2600, 3000, "ow_kiosk", "Food Kiosks", False, "#ff99cc", "sarah.png"),
        MapNode("Ceazar", 1600, 1800, "ow_lovers", "Ceazar", False, "#ccff99", "caezar.png", icon_zoom=0.06),
        MapNode("Dorm", 3300, 1900, "ow_dorm", "Dormitory", False, "#ffaa77", "dorm_mgr.png"),
    ]

    $ current_task_text = "Explore freely! Click anywhere to revisit."

label open_world_loop:
    call screen map_screen("maps/banwa.png", openworld_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node)
        call expression _node.target_label

    jump open_world_loop

## --- Open World location labels ---
label ow_gate:
    window show
    narrator_char "The university gate. This is where your journey began this morning."
    narrator_char "Manong Guard waves at you as you pass by."
    window hide
    return

label ow_hsu:
    window show
    narrator_char "The Health Services Unit. You can still smell the antiseptic from your checkup."
    window hide
    return

label ow_admin:
    window show
    narrator_char "New Administration Building. Sir Ruel is probably processing the next batch of freshmen."
    narrator_char "You clutch your Form 5 a little tighter."
    window hide
    return

label ow_cub:
    window show
    narrator_char "The College Union Building. Ms. Santos' office is upstairs."
    narrator_char "You notice a bulletin board full of org announcements and scholarship postings."
    window hide
    return

label ow_kiosk:
    window show
    narrator_char "The food kiosks near the gate. The smell of grilled isaw fills the air."
    narrator_char "Students gather here between classes, swapping stories."
    window hide
    return

label ow_lovers:
    window show
    narrator_char "Ceazar. The wind is strong here, carrying the scent of the sea."
    narrator_char "You can see the open field stretching out. The world is still big."
    caezar "Just remember: Don't forget to look up once in a while."
    window hide
    return

label ow_dorm:
    window show
    narrator_char "Your dormitory. Room #207."
    narrator_char "It's small, but it's yours. Four walls, a bed, a desk, and the start of something new."
    window hide
    return


## ============================================================================
## ENDING
## ============================================================================

label game_ending:
    scene black with fade
    pause 1.0

    call screen act_transition("MIAGAO FRESHMAN GUIDE", "You survived your first day.", mode="ending")

    call screen act_transition("Welcome to UP Visayas", "Classes start next week.\nBut for now, breathe.", mode="ending")

    call screen act_transition("Made with Ren'Py", "", mode="credits")

    return
