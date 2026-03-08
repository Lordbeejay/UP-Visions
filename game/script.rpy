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

    ## --- INTRO SEQUENCE ---
    scene bg miagao_campus with fade
    pause 0.5

    centered "{size=+8}{color=#ffd700}MIAGAO FRESHMAN GUIDE{/color}{/size}"
    pause 1.0
    centered "{size=+2}{color=#ffffff}A point-and-click adventure{/color}{/size}"
    pause 1.0
    centered "{size=+2}{color=#cccccc}Navigate your first day at UP Visayas{/color}{/size}"
    pause 1.5

    ## --- ACT 1 ---
    scene bg Miagao with fade
    show text "{size=+6}{color=#ffd700}ACT 1{/color}{/size}\n{color=#ffffff}Arrival in Miagao{/color}" at truecenter
    pause 2.0
    hide text

    $ current_act = 1
    $ player_map_x = 2500
    $ player_map_y = 3200
    $ player_facing = "up"
    jump act1_map


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
    $ act1_nodes = [
        MapNode("jaden",         1200, 1400, "act1_npc_jaden",         tooltip="Jaden",           icon_image="jaden.png",          locked=False),
        MapNode("manong_josh",   2100, 2600, "act1_npc_manong_josh",   tooltip="Manong Josh",     icon_image="manongjosh.png",    locked=True),
        MapNode("aleng_maria",   3000, 2200, "act1_npc_aleng_maria",   tooltip="Aleng Maria",     icon_image="alengmaria.png",    locked=True),
        MapNode("manong_chris",  3600, 3000, "act1_npc_manong_chris",  tooltip="Manong Chris",    icon_image="manongchris.png",   locked=True),
        MapNode("joseph_driver", 2500, 3800, "act1_npc_joseph_driver", tooltip="Joseph (Driver)", icon_image="manong_driver.png",  locked=True),
        MapNode("box1",          4200, 1800, "act1_box1_arrive",       tooltip="BOX 1",           icon_image="box1.png",           locked=True),
    ]

    $ current_task_text = "Talk to Jaden near the Banwa entrance"

label act1_loop:
    call screen map_screen("maps/banwa.png", act1_nodes, current_task_text, MAP_ZOOM)

    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node)
        call expression _node.target_label

        ## --- After talking to Jaden, unlock Manong Josh and Aleng Maria ---
        if "talk_jaden" in tasks_completed:
            $ act1_nodes[1].locked = False  # Manong Josh
            $ act1_nodes[2].locked = False  # Aleng Maria
            if "talk_manong_josh" not in tasks_completed and "talk_aleng_maria" not in tasks_completed:
                $ current_task_text = "Explore the Banwa Area — talk to the locals"

        ## --- After Josh OR Maria, unlock Manong Chris ---
        if "talk_manong_josh" in tasks_completed or "talk_aleng_maria" in tasks_completed:
            $ act1_nodes[3].locked = False  # Manong Chris

        ## --- After Chris, unlock Joseph ---
        if "talk_manong_chris" in tasks_completed:
            $ act1_nodes[4].locked = False  # Joseph
            if "talk_joseph_driver" not in tasks_completed:
                $ current_task_text = "Find Joseph the tricycle driver near the plaza"

        ## --- After all 5 NPCs, unlock BOX 1 ---
        if (
            "talk_jaden"          in tasks_completed and
            "talk_manong_josh"    in tasks_completed and
            "talk_aleng_maria"    in tasks_completed and
            "talk_manong_chris"   in tasks_completed and
            "talk_joseph_driver"  in tasks_completed
        ):
            $ act1_nodes[5].locked = False  # BOX 1
            $ current_task_text = "Head to BOX 1 at the edge of the Banwa Area"

        if is_act_complete():
            jump act1_complete

    jump act1_loop


label act1_complete:
    scene black with fade
    pause 0.5
    centered "{size=+4}{color=#44cc44}✅ ACT 1 COMPLETE{/color}{/size}\n\n{color=#ffffff}You've learned the lay of the land. Miagao is starting to feel like home.{/color}"
    pause 2.5

    scene black with fade
    centered "{size=+6}{color=#ffd700}ACT 2{/color}{/size}\n{color=#ffffff}Entering the University{/color}"
    pause 2.0

    $ current_act = 2
    $ player_map_x = 2500
    $ player_map_y = 2800
    $ player_facing = "up"
    jump act2_map


## ============================================================================
## ACT 2 MAP — BOX 1 / CUB / OSA
## ============================================================================

label act2_map:
    $ act2_nodes = [
        MapNode("CUB", 1900, 1800, "npc_ms_santos", "CUB / OSA Office", False, "#cc99ff", "ms_santos.png"),
        MapNode("Enrollment", 3000, 2500, "npc_sarah", "Enrollment Line", False, "#ffcc99", "sarah.png"),
    ]

    $ current_task_text = "Visit Ms. Santos at the OSA and check the enrollment line"

label act2_loop:
    call screen map_screen("NewAd/.png", act2_nodes, current_task_text, MAP_ZOOM)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node)
        call expression _node.target_label

        if "talk_ms_santos" in tasks_completed and "talk_sarah" not in tasks_completed:
            $ current_task_text = "Talk to Sarah at the enrollment line"
        elif "talk_sarah" in tasks_completed and "talk_ms_santos" not in tasks_completed:
            $ current_task_text = "Visit Ms. Santos at the OSA"

        if is_act_complete():
            jump act2_complete

    jump act2_loop


label act2_complete:
    scene black with fade
    pause 0.5
    centered "{size=+4}{color=#44cc44}✅ ACT 2 COMPLETE{/color}{/size}\n\n{color=#ffffff}Scholarship tagged and enrollment confirmed!{/color}"
    pause 2.5

    scene black with fade
    centered "{size=+6}{color=#ffd700}ACT 3{/color}{/size}\n{color=#ffffff}Campus Life{/color}"
    pause 2.0

    $ current_act = 3
    $ player_map_x = 2500
    $ player_map_y = 2800
    $ player_facing = "down"
    jump act3_map


## ============================================================================
## ACT 3 MAP — Social / Exploration
## ============================================================================

label act3_map:
    $ act3_nodes = [
        MapNode("Kiosk", 2300, 3100, "npc_mikhaela", "Kiosk (Mikhaela)", False, "#ff99cc", "mikhaela.png"),
        MapNode("Path", 2100, 2600, "act1_npc_jaden", "Main Path (Jaden)", False, "#99ccff", "jaden.png"),
        MapNode("Lover's", 1600, 1800, "npc_caezar", "Lover's Lane", True, "#ccff99", "caezar.png"),
    ]

    $ current_task_text = "Explore campus — find Mikhaela and Jaden"

label act3_loop:
    call screen map_screen("maps/banwa.png", act3_nodes, current_task_text, MAP_ZOOM)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node)
        call expression _node.target_label

        if "talk_jaden" in tasks_completed:
            $ act3_nodes[2].locked = False
            if "talk_caezar" not in tasks_completed:
                $ current_task_text = "Meet Caezar at Lover's Lane"

        if is_act_complete():
            jump act3_complete

    jump act3_loop


label act3_complete:
    scene black with fade
    pause 0.5
    centered "{size=+4}{color=#44cc44}✅ ACT 3 COMPLETE{/color}{/size}\n\n{color=#ffffff}You've made friends and explored the campus!{/color}"
    pause 2.5

    scene black with fade
    centered "{size=+6}{color=#ffd700}ACT 4{/color}{/size}\n{color=#ffffff}Dorm Accommodation{/color}"
    pause 2.0

    $ current_act = 4
    $ player_map_x = 2500
    $ player_map_y = 2600
    $ player_facing = "up"
    jump act4_map


## ============================================================================
## ACT 4 MAP — Dorm
## ============================================================================

label act4_map:
    $ act4_nodes = [
        MapNode("Dorm", 3300, 1900, "npc_dorm_manager", "Dormitory Office", False, "#ffaa77", "dorm_mgr.png"),
    ]

    $ current_task_text = "Talk to the Dorm Manager"

label act4_loop:
    call screen map_screen("maps/banwa.png", act4_nodes, current_task_text, MAP_ZOOM)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node)
        call expression _node.target_label

        if is_act_complete():
            jump act4_complete

    jump act4_loop


label act4_complete:
    scene black with fade
    pause 0.5
    centered "{size=+4}{color=#44cc44}✅ ACT 4 COMPLETE{/color}{/size}\n\n{color=#ffffff}You've secured your dorm room!{/color}"
    pause 2.5

    jump open_world


## ============================================================================
## OPEN WORLD — Free Exploration (Endgame)
## ============================================================================

label open_world:
    scene black with fade
    centered "{size=+6}{color=#ffd700}OPEN WORLD{/color}{/size}\n{color=#ffffff}Classes start next week. Explore freely!{/color}"
    pause 2.0

    $ current_act = 5
    $ player_map_x = 2500
    $ player_map_y = 2600
    $ player_facing = "down"

    $ openworld_nodes = [
        MapNode("Gate", 2500, 3200, "ow_gate", "Banwa Gate", False, "#44cc44", "manong_guard.png"),
        MapNode("HSU", 1800, 2000, "ow_hsu", "Health Services", False, "#4499ff", "hsu_nurse.png"),
        MapNode("Admin", 2500, 2500, "ow_admin", "New Admin Building", False, "#ff8844", "sir_ruel.png"),
        MapNode("CUB", 1900, 1800, "ow_cub", "CUB / OSA", False, "#cc99ff", "ms_santos.png"),
        MapNode("Kiosk", 2300, 3100, "ow_kiosk", "Food Kiosks", False, "#ff99cc", "mikhaela.png"),
        MapNode("Lover's", 1600, 1800, "ow_lovers", "Lover's Lane", False, "#ccff99", "caezar.png"),
        MapNode("Dorm", 3300, 1900, "ow_dorm", "Dormitory", False, "#ffaa77", "dorm_mgr.png"),
    ]

    $ current_task_text = "Explore freely! Click anywhere to revisit."

label open_world_loop:
    call screen map_screen("maps/banwa.png", openworld_nodes, current_task_text, MAP_ZOOM)
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
    narrator_char "Lover's Lane. The wind is strong here, carrying the scent of the sea."
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

    centered "{size=+6}{color=#ffd700}MIAGAO FRESHMAN GUIDE{/color}{/size}"
    pause 1.0
    centered "{color=#ffffff}You survived your first day.{/color}"
    pause 1.5
    centered "{color=#cccccc}Classes start next week.{/color}\n{color=#cccccc}But for now, breathe.{/color}"
    pause 2.0
    centered "{color=#ffd700}Welcome to UP Visayas.{/color}"
    pause 2.0

    centered "{size=-2}{color=#888888}Made with Ren'Py{/color}{/size}"
    pause 1.0

    return
