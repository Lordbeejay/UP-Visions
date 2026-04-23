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

## --- Defaults ---
default jaden_second_talk = False
default talked_jaden = False
default talked_josh = False
default talked_maria = False
default talked_chris = False
default talked_joseph = False
default gc_unlocked = False
default gc_revealed = []
default gc_open_count = 0
default collected_items = []
default quiz_score = 0


label start:

    ## Stop the main menu theme (the one from options.rpy)
    stop music fadeout 1.0

    ## You can change this to an Act 5 specific track if you have one
    play music "audio/Act1.mp3" fadein 1.0

    ## Hide the dialogue window for map exploration
    window hide

    ## --- Fade to black from main menu ---
    scene black with Dissolve(1.0)
    pause 0.3

    ## --- INTRO SEQUENCE ---
    scene bg miagao_campus with Dissolve(1.2)
    pause 0.3

    call screen act_transition("MIAGAO FRESHMAN GUIDE", "A point-and-click adventure\nNavigate your first day at UP Visayas", mode="welcome")

    # Start Act 1 transition
    call screen act_transition("ACT 1", "Arrival at Miagao", "intro") 
    
    # Start Act 1 background
    scene expression "maps/banwa.png" 
    
    # Task Testing
    $ current_act = 5
    $ tasks_completed = set()
    
    # Act 1 starting coordinates (near the gate)
    $ player_map_x = 2500 
    $ player_map_y = 3500
    $ player_facing = "up"
    
    $ inventory_unlocked = False

    ## ── Detective Notebook intro ─────────────────────────────────────────
    call screen notebook_intro_screen()
    ## ────────────────────────────────────────────────────────────────────

    # Act Testing
    jump act5_map
## ============================================================================
## ACT 1 MAP — Banwa (Gate / HSU / Admin / Medical)
## ============================================================================
## Map features (map coords on 5000x5000 map):
## - Gate/Guard: bottom center (2500, 3200)
## - HSU: upper-left area (1800, 2000)
## - Admin/Registrar: center (2500, 2500)
## - Medical buildings: center-left (2000, 2300)
## ============================================================================

## --- Navigation helper variable for multi-map Act 1 ---
default act1_nav_target = None

## --- ACT 1 PHASE 1: Banwa (center map) ---
## Jaden is here. Arrows lead to Tindahan (left) and Marillac (right).
## BOX 1 unlocks after all NPCs across all maps are talked to.
label act1_map:
    $ current_map_bg = "maps/banwa.png"
    $ act1_nav_target = None
    $ act1_nodes = [
        MapNode("jaden",         2300, 4000, "act1_npc_jaden",     tooltip="Jaden",              icon_image="jaden.png",        locked=False),
        MapNode("go_tindahan",   100,  2500, "act1_go_tindahan",   tooltip="← Tindahan",         icon_image="ArrowLeft.png",        locked=True, icon_zoom=1.5),
        MapNode("go_marillac",   4900, 2500, "act1_go_marillac",   tooltip="Marillac →",         icon_image="Arrow.png",        locked=True, icon_zoom=1.5),
        MapNode("box1",          3860, 1500, "act1_prebox1_gate",  tooltip="BOX 1",              icon_image="ArrowUp.png",        locked=True, icon_zoom=1.5),
    ]

    ## Re-apply unlock states when returning from other maps
    if "talk_jaden" in tasks_completed:
        $ act1_nodes[0].target_label = "act1_npc_jaden_second"
        $ act1_nodes[1].locked = False
        $ act1_nodes[2].locked = False

    if (
        "talk_jaden"         in tasks_completed and
        "talk_manong_josh"   in tasks_completed and
        "talk_aleng_maria"   in tasks_completed and
        "talk_manong_chris"  in tasks_completed and
        "talk_joseph_driver" in tasks_completed
    ):
        $ act1_nodes[3].locked = False

    if "talk_jaden" not in tasks_completed:
        $ current_task_text = "Talk to Jaden near the Banwa entrance"
    elif (
        "talk_manong_josh"   not in tasks_completed or
        "talk_aleng_maria"   not in tasks_completed or
        "talk_manong_chris"  not in tasks_completed or
        "talk_joseph_driver" not in tasks_completed
    ):
        $ current_task_text = "Explore Tindahan and Marillac to meet the locals"
    else:
        $ current_task_text = "Talk to Jaden again, then head to BOX 1"

label act1_loop:
    call screen map_screen("maps/banwa.png", act1_nodes, current_task_text, 1.0)

    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, nodes=act1_nodes) from _call_walk_to_node_3
        call expression _node.target_label from _call_expression_3

        ## unlock logic after talking to Jaden
        if "talk_jaden" in tasks_completed:
            $ act1_nodes[1].locked = False
            $ act1_nodes[2].locked = False
            $ act1_nodes[0].target_label = "act1_npc_jaden_second"
            $ current_task_text = "Explore Tindahan and Marillac to meet the locals"

        if (
            "talk_jaden"         in tasks_completed and
            "talk_manong_josh"   in tasks_completed and
            "talk_aleng_maria"   in tasks_completed and
            "talk_manong_chris"  in tasks_completed and
            "talk_joseph_driver" in tasks_completed
        ):
            $ act1_nodes[3].locked = False
            $ current_task_text = "Talk to Jaden again, then head to BOX 1"

        ## Navigation to other maps
        if act1_nav_target == "tindahan":
            $ act1_nav_target = None
            jump act1_tindahan_map
        if act1_nav_target == "marillac":
            $ act1_nav_target = None
            jump act1_marillac_map

        if is_act_complete():
            jump act1_complete

    ## Phone toggle (P key) — universal
    if _action == "phone":
        call phone_check from _call_phone_check_3

    ## Inventory toggle (I key) — universal
    if _action == "inventory":
        if inventory_unlocked:
            call screen inventory_screen()

    jump act1_loop


## --- ACT 1 PHASE 2: Tindahan (left map) ---
## Aleng Maria (food/budget) and Joseph Driver (transport) are here.
label act1_tindahan_map:
    $ current_map_bg = "ui/overhead_tindahan.png"
    $ act1_nav_target = None
    $ act1_tindahan_nodes = [
        MapNode("aleng_maria",   1500, 3400, "act1_npc_aleng_maria",   tooltip="Aleng Maria",     icon_image="alengmaria.png",    locked=False),
        MapNode("joseph_driver", 2800, 2400, "act1_npc_joseph_driver", tooltip="Joseph (Driver)", icon_image="manong_driver.png",  locked=True),
        MapNode("go_banwa_r",    4900, 2400, "act1_go_banwa",          tooltip="Banwa →",         icon_image="Arrow.png",          locked=False, icon_zoom=1.5),
    ]

    ## Unlock Joseph after talking to Aleng Maria
    if "talk_aleng_maria" in tasks_completed:
        $ act1_tindahan_nodes[1].locked = False

    if "talk_aleng_maria" not in tasks_completed:
        $ current_task_text = "Talk to Aleng Maria at the Tindahan"
    elif "talk_joseph_driver" not in tasks_completed:
        $ current_task_text = "Talk to Joseph the tricycle driver"
    else:
        $ current_task_text = "Head back to Banwa →"

label act1_tindahan_loop:
    call screen map_screen("ui/overhead_tindahan.png", act1_tindahan_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, nodes=act1_tindahan_nodes) from _call_walk_to_node_4
        call expression _node.target_label from _call_expression_4

        if "talk_aleng_maria" in tasks_completed:
            $ act1_tindahan_nodes[1].locked = False
            $ current_task_text = "Talk to Joseph the tricycle driver"

        if "talk_aleng_maria" in tasks_completed and "talk_joseph_driver" in tasks_completed:
            $ current_task_text = "Head back to Banwa →"

        ## Navigation back to Banwa
        if act1_nav_target == "banwa":
            $ act1_nav_target = None
            jump act1_map

    ## Phone toggle (P key) — universal
    if _action == "phone":
        call phone_check from _call_phone_check_4

    ## Inventory toggle (I key) — universal
    if _action == "inventory":
        if inventory_unlocked:
            call screen inventory_screen()

    jump act1_tindahan_loop


## --- ACT 1 PHASE 3: Marillac (right map) ---
## Manong Josh (landmarks) and Manong Chris (culture/language) are here.
label act1_marillac_map:
    $ current_map_bg = "ui/overhead_marillac.png"
    $ act1_nav_target = None
    $ act1_marillac_nodes = [
        MapNode("manong_josh",   3650, 1500, "act1_npc_manong_josh",   tooltip="Manong Josh",     icon_image="manongjosh.png",    locked=False),
        MapNode("manong_chris",  3650, 3500, "act1_npc_manong_chris",  tooltip="Manong Chris",    icon_image="manongchris.png",   locked=True),
        MapNode("go_banwa_l",    325,  650,  "act1_go_banwa",          tooltip="← Banwa",         icon_image="ArrowLeft.png",          locked=False, icon_zoom=1.5),
    ]

    ## Unlock Manong Chris after talking to Manong Josh
    if "talk_manong_josh" in tasks_completed:
        $ act1_marillac_nodes[1].locked = False

    if "talk_manong_josh" not in tasks_completed:
        $ current_task_text = "Talk to Manong Josh near Marillac"
    elif "talk_manong_chris" not in tasks_completed:
        $ current_task_text = "Talk to Manong Chris about local culture"
    else:
        $ current_task_text = "← Head back to Banwa"

label act1_marillac_loop:
    call screen map_screen("ui/overhead_marillac.png", act1_marillac_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, nodes=act1_marillac_nodes) from _call_walk_to_node_5
        call expression _node.target_label from _call_expression_5

        if "talk_manong_josh" in tasks_completed:
            $ act1_marillac_nodes[1].locked = False
            $ current_task_text = "Talk to Manong Chris about local culture"

        if "talk_manong_josh" in tasks_completed and "talk_manong_chris" in tasks_completed:
            $ current_task_text = "← Head back to Banwa"

        ## Navigation back to Banwa
        if act1_nav_target == "banwa":
            $ act1_nav_target = None
            jump act1_map

    ## Phone toggle (P key) — universal
    if _action == "phone":
        call phone_check from _call_phone_check_5

    ## Inventory toggle (I key) — universal
    if _action == "inventory":
        if inventory_unlocked:
            call screen inventory_screen()

    jump act1_marillac_loop



label act1_complete:
    scene black
    call screen act_transition("ACT 1 COMPLETE", "You've learned the lay of the land.\nMiagao is starting to feel like home.", "complete")
    call screen act_transition("ACT 2", "Entering the University", "intro")
    scene expression "images/maps/Entrance.png"
    
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
    $ current_map_bg = "maps/Box1.png"
    $ act2_entrance_nodes = [
        MapNode("ate_bea",    2000, 2600, "act2_npc_ate_bea",    tooltip="Ate Bea",     icon_image="ate_bea.png",    locked=False),
        MapNode("kuya_mark",  2800, 3900, "act2_npc_kuya_mark",  tooltip="Kuya Mark",   icon_image="kuya_mark.png",  locked=True),
        MapNode("newad_gate", 2500, 1200, "act2_go_to_newad",    tooltip="New Admin",   icon_image="ArrowUp.png",       locked=True, icon_zoom=2.0),
    ]
    $ current_task_text = "Talk to Ate Bea at the Entrance"

label act2_entrance_loop:
    call screen map_screen("maps/Box1.png", act2_entrance_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        scene black
        call walk_to_node(_node, nodes=act2_entrance_nodes) from _call_walk_to_node_6
        call expression _node.target_label from _call_expression_6

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
        MapNode("enter_inside", 2500, 2250, "act2_enter_inside", tooltip="Enter New Admin", icon_image="ArrowUp.png", locked=False, icon_zoom=2.0),
    ]
    $ current_task_text = "Enter the New Admin building"

label act2_newad_loop:
    call screen map_screen("maps/NewAd.png", act2_newad_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, nodes=act2_newad_nodes) from _call_walk_to_node_7
        call expression _node.target_label from _call_expression_7

        ## After entering, transition to phase 3
        jump act2_inside_map

    jump act2_newad_loop


## --- PHASE 3: Inside New Admin — find Ma'am Reyes ---
label act2_inside_map:
    $ current_map_bg = "maps/NewAd_Lobby.png"
    $ player_map_x = 2500
    $ player_map_y = 4200
    $ player_facing = "up"

    $ act2_inside_nodes = [
        MapNode("maam_reyes", 4700, 3200, "act2_npc_maam_reyes", tooltip="Ma'am Reyes", icon_image="maam_reyes.png", locked=False, icon_zoom=0.1),
    ]
    $ current_task_text = "Find Ma'am Reyes inside New Admin"

label act2_inside_loop:
    call screen map_screen("maps/NewAd_Lobby.png", act2_inside_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, nodes=act2_inside_nodes) from _call_walk_to_node_8
        call expression _node.target_label from _call_expression_8

        if "talk_maam_reyes" in tasks_completed:
            $ current_task_text = "Complete the Office Match Game!"

        if is_act_complete():
            jump act2_complete

    jump act2_inside_loop


label act2_complete:
    scene black
    call screen act_transition("ACT 2 COMPLETE", "You've navigated enrollment\nand met the campus staff!", "complete")
    call screen act_transition("ACT 3", "Enrollment", "intro")

    $ current_act = 3
    $ player_map_x = 2500
    $ player_map_y = 2600
    $ player_facing = "down"
    jump act3_map


## ============================================================================
## ACT 3 MAP — Enrollment (CRS Portal & Schedule Building)
## ============================================================================

## ============================================================================
## ACT 3 MAP — Enrollment
## Phase 1: New Admin Office  →  Sir Noel
## Phase 2: Box 1 Area        →  Mikhaela, Jaden
## Phase 3: Lover's Lane      →  Jaden, Caezar
## ============================================================================

## --- Phase 1: New Admin Office — Sir Noel ---
label act3_map:
    $ current_map_bg = "maps/NewAd_Office.png"
    $ act3_noel_nodes = [
        MapNode("sir_noel", 4500, 2500, "act3_npc_sir_noel", tooltip="Sir Noel",   icon_image="sir_allan.png",  locked=False, icon_zoom=0.25),
        MapNode("go_box1",  300,  3200, "act3_go_box1",      tooltip="← Box 1",   icon_image="ArrowLeft.png",  locked=True,  icon_zoom=2),
    ]
    $ current_task_text = "Talk to Sir Noel about enrollment"

label act3_noel_loop:
    call screen map_screen("maps/NewAd_Office.png", act3_noel_nodes, current_task_text, 1.0, player_zoom=6)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, nodes=act3_noel_nodes, player_zoom=4) from _call_walk_to_node_9
        call expression _node.target_label from _call_expression_9

        python:
            for _n in act3_noel_nodes:
                if _n.name == "go_box1" and "complete_enrollment_tetris" in tasks_completed:
                    _n.locked = False

        if "talk_sir_noel" in tasks_completed:
            $ current_task_text = "View the CRS Student Portal"
        if "view_crs_portal" in tasks_completed:
            $ current_task_text = "Complete Enrollment Tetris!"
        if "complete_enrollment_tetris" in tasks_completed:
            $ current_task_text = "Head to Box 1 (← left arrow)"

        if _node.name == "go_box1":
            jump act3_box1_map

    jump act3_noel_loop


## --- Phase 2: Box 1 Area — Mikhaela, Jaden ---
label act3_box1_map:
    $ current_map_bg = "maps/Box1.png"
    $ player_map_x = 2450
    $ player_map_y = 2500
    $ player_facing = "right"
    $ act3_box1_nodes = [
        MapNode("mikhaela",  1500, 3500, "npc_mikhaela_eat", tooltip="Mikhaela",        icon_image="sarah.png",     locked=False, icon_zoom=0.15),
        MapNode("jaden",     3000, 2500, "act3_npc_jaden",   tooltip="Jaden",            icon_image="jaden.png",     locked=False, icon_zoom=0.15),
        MapNode("go_lovers", 2450, 1400, "act3_go_lovers",   tooltip="Lover's Lane →",   icon_image="ArrowUp.png",     locked=True,  icon_zoom=2.5),
    ]
    $ current_task_text = "Talk to Jaden"

label act3_box1_loop:
    call screen map_screen("maps/Box1.png", act3_box1_nodes, current_task_text, 1.0, player_zoom=3)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, nodes=act3_box1_nodes, player_zoom=4.5) from _call_walk_to_node_10
        call expression _node.target_label from _call_expression_10

        python:
            for _n in act3_box1_nodes:
                if _n.name == "go_lovers" and "talk_jaden" in tasks_completed:
                    _n.locked = False

        if "talk_jaden" in tasks_completed:
            $ current_task_text = "Head to Lover's Lane (→ right arrow)"

    jump act3_box1_loop


label act3_complete:
    scene black
    call screen act_transition("ACT 3 COMPLETE", "You've completed enrollment\nand built your class schedule!", "complete")
    call screen act_transition("ACT 4", "Dorm Life", "intro")

    $ current_act = 4
    $ player_map_x = 4800
    $ player_map_y = 4800
    $ player_facing = "up"
    jump act4_map


## ============================================================================
## ACT 4 MAP — Dorm Life (Check-in → Room Exploration → Room Setup Game)
## ============================================================================

label act4_map:
    $ current_map_bg = "maps/Dorm_Lobby.png"
    $ act4_nodes = [
        MapNode("dorm_office", 2500, 2000, "act4_npc_dorm_manager", tooltip="Dormitory Office", icon_image="dorm_mgr.png", locked=False, icon_zoom=0.25),
    ]

    $ current_task_text = "Talk to the Dorm Manager"

label act4_loop:
    ## After check-in, switch to room interior map
    if "talk_dorm_manager" in tasks_completed and "explore_dorm_room" not in tasks_completed:
        $ current_map_bg = "maps/Dorm_Lobby.png"
        $ player_map_x = 2500
        $ player_map_y = 3800
        $ player_facing = "up"
        $ act4_nodes = [
            MapNode("your_room", 1200, 4400, "act4_explore_room", tooltip="Your Room #207", icon_image="ArrowLeft.png", locked=False, icon_zoom=3),
        ]
        $ current_task_text = "Explore your dorm room"

    if "explore_dorm_room" in tasks_completed and "complete_room_setup" not in tasks_completed:
        $ current_task_text = "Set up your dorm room!"

    call screen map_screen(current_map_bg, act4_nodes, current_task_text, 1.0, player_zoom=6)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, nodes=act4_nodes, player_zoom=6) from _call_walk_to_node_11
        call expression _node.target_label from _call_expression_11

        if is_act_complete():
            jump act4_complete

    jump act4_loop


label act4_complete:
    scene black
    call screen act_transition("ACT 4 COMPLETE", "You've settled into your dorm\nand set up your room!", "complete")
    call screen act_transition("ACT 5", "First Day of Classes", "intro")

    $ current_act = 5
    $ player_map_x = 2500
    $ player_map_y = 2600
    $ player_facing = "up"
    jump act5_map


## ============================================================================
## ACT 5 MAP — First Day of Classes
## Phase 1: OW_CAS  →  Kuya Rico
## Phase 2: CL3     →  Prof. Lena
## Phase 3: OW_CAS  →  Ate Grace, Dan, HSU, First Class
## ============================================================================

label act5_map:
    ## Phase 1 — Outside CAS Building
    $ current_map_bg = "ace/OW_CAS.png"
    $ player_map_x = 2500
    $ player_map_y = 3200
    $ player_facing = "up"
    $ act5_nodes = [
        MapNode("kuya_rico", 3350, 2550, "act5_npc_kuya_rico", tooltip="Kuya Rico", icon_image="manong_guard.png", locked=False, icon_zoom=0.11),
    ]
    $ current_task_text = "Find Kuya Rico outside CAS"

label act5_ow_cas_loop:
    call screen map_screen("ace/OW_CAS.png", act5_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, nodes=act5_nodes) from _call_walk_to_node_12
        call expression _node.target_label from _call_expression_12

        if "talk_kuya_rico" in tasks_completed:
            jump act5_transition_to_cl3

        if is_act_complete():
            jump act5_complete

    jump act5_ow_cas_loop


label act5_transition_to_cl3:
    window show
    narrator_char "(Kuya Rico gives you a wave as you head into the building.)"
    narrator_char "(You follow the hallway signs. CL3 — ground floor, CAS Building.)"
    narrator_char "(You arrived in CL3.)"
    window hide
    jump act5_cl3_map


label act5_cl3_map:
    ## Phase 2 — CL3 Classroom
    $ current_map_bg = "maps/CL3.png"
    $ player_map_x = 2500
    $ player_map_y = 3500
    $ player_facing = "up"
    $ act5_nodes = [
        MapNode("prof_lena", 2475, 2100, "act5_npc_prof_lena", tooltip="Prof. Lena", icon_image="prof_lena.png", locked=False, icon_zoom=0.30),
    ]
    $ current_task_text = "Talk to Prof. Lena in CL3"


label act5_cl3_loop:
    call screen map_screen("maps/CL3.png", act5_nodes, current_task_text, 0.5, 3)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, map_bg="maps/CL3.png", nodes=act5_nodes, player_zoom=3) from _call_walk_to_node_13
        call expression _node.target_label from _call_expression_13

        if "talk_prof_lena" in tasks_completed:
            jump act5_transition_back_to_ow_cas

        if is_act_complete():
            jump act5_complete

    jump act5_cl3_loop


label act5_transition_back_to_ow_cas:
    window show
    narrator_char "(Class is done for now. You step back outside into the CAS corridor.)"
    window hide
    jump act5_ow_cas2_map


label act5_ow_cas2_map:
    ## Phase 3 — Back outside CAS: Ate Grace, Dan, HSU, First Class
    $ current_map_bg = "ace/OW_CAS.png"
    $ player_map_x = 2500
    $ player_map_y = 3200
    $ player_facing = "up"
    $ act5_nodes = [
        MapNode("ate_grace",     1250, 3000, "act5_npc_ate_grace",     tooltip="Ate Grace", icon_image="ate_grace.png",     locked=False, icon_zoom=0.15),
        MapNode("classmate_dan", 3250, 3200, "act5_npc_classmate_dan", tooltip="Dan",       icon_image="caezar.png", locked=True,  icon_zoom=0.1),
        MapNode("first_class",   3400, 2450, "act5_first_class",       tooltip="Enter CL3", icon_image="Arrow.png",    locked=True, icon_zoom=3),
        MapNode("hsu_trigger",   1500, 2000, "act5_transition_to_hsu", tooltip="Health Services (HSU)", icon_image="Arrow.png", locked=True, icon_zoom=3),
        MapNode("first_class",   3400, 2450, "act5_first_class",       tooltip="Enter CL3", icon_image="Arrow.png",     locked=True,  icon_zoom=3),
    ]
    $ current_task_text = "Talk to Ate Grace"

label act5_ow_cas2_loop:
    call screen map_screen("ace/OW_CAS.png", act5_nodes, current_task_text, 1.0, player_zoom=3)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, nodes=act5_nodes, player_zoom=3) from _call_walk_to_node_14
        call expression _node.target_label from _call_expression_14

        if "talk_ate_grace" in tasks_completed:
            $ act5_nodes[1].locked = False
            $ current_task_text = "Talk to Dan"

        if "talk_classmate_dan" in tasks_completed:
            # HSU Unlock
            $ act5_nodes[2].locked = False 
            $ current_task_text = "Visit the HSU with Dan"
        if (
            "talk_ate_grace" in tasks_completed and
            "talk_classmate_dan" in tasks_completed and
            "visit_hsu" in tasks_completed
        ):
            $ act5_nodes[2].locked = False
            $ current_task_text = "Attend your first class"

        if is_act_complete():
            jump act5_complete

    jump act5_ow_cas2_loop

label act5_transition_to_hsu:
    window show
    dan "The HSU is just along the road to the dorms. We need to submit our medical clearance."
    narrator_char "(You and Dan walk towards the Health Services Unit.)"
    window hide
    jump act5_hsu_map

label act5_hsu_map:
    $ current_map_bg = "maps/ow_hsu.png"
    $ player_map_x = 2000
    $ player_map_y = 3000
    $ act5_hsu_nodes = [
        MapNode("hsu_nurse", 2000, 1500, "act5_hsu_interaction", tooltip="Submit Clearance", icon_image="nurse.png", locked=False, icon_zoom=0.2)
    ]
    
    call screen map_screen("maps/HSU_Interior.png", act5_hsu_nodes, "Submit your clearance at the counter", 0.8, 3)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, map_bg="maps/ow_hsu.png", nodes=act5_hsu_nodes, player_zoom=3)
        call expression _node.target_label

    # After interaction, return to the main CAS map
    jump act5_ow_cas2_map

label act5_hsu_interaction:
    window show
    nurse "Everything looks in order. Welcome to the university, students!"
    $ tasks_completed.append("visit_hsu")
    narrator_char "(Medical clearance submitted successfully.)"
    window hide
    return # Returns to the act5_hsu_map logic which then jumps back to CAS


label act5_complete:
    scene black
    call screen act_transition("ACT 5 COMPLETE", "You survived your first day of classes!", "complete")
    call screen act_transition("ACT 6", "Student Orgs & Campus Life", "intro")

    $ current_act = 6
    $ player_map_x = 2500
    $ player_map_y = 2600
    $ player_facing = "down"
    jump act6_map


## ============================================================================
## ACT 7 MAP — Library & Academic Resources
## ============================================================================

## ============================================================================
## ACT 7 MAP — Two-map flow:
##   Library (Diwata.png)  →  ArrowUp  →  CAS Overworld (CAS_Overworld(F).png)
## ============================================================================

## --- MAP 1: Library ---
label act7_map:
    python:
        global act7_lib_nodes
    $ current_map_bg = "ui/Diwata.png"
    $ player_map_x = 2500
    $ player_map_y = 3200
    $ player_facing = "up"
    $ act7_lib_nodes = [
        MapNode("ate_rosa", 1750, 1900, "act7_npc_ate_rosa", tooltip="Ate Rosa", icon_image="ow_cub.png", locked=False),
        MapNode("to_cas",   2500, 1200,  "act7_to_cas",       tooltip="Head to CAS", icon_image="ArrowUp.png", locked=True, icon_zoom=2.0),
    ]
    $ current_task_text = "Talk to Ate Rosa at the library"

label act7_lib_loop:

    # Always unlock the arrow if Ate Rosa is done
    if "talk_ate_rosa" in tasks_completed:
        $ act7_lib_nodes[1].locked = False
        $ current_task_text = "Head to the CAS building"

    call screen map_screen("ui/Diwata.png", act7_lib_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, nodes=act7_lib_nodes) from _call_walk_to_node_15

        if _node.target_label == "act7_to_cas":
            jump act7_cas_map
        else:
            call expression _node.target_label from _call_expression_15

    jump act7_lib_loop

label act7_to_cas:
    ## This label is never called directly — Arrow node jumps to act7_cas_map.
    return

## --- MAP 2: CAS Overworld ---
label act7_cas_map:
    python:
        global act7_cas_nodes
    $ current_map_bg = "ui/CAS_Overworld(F).png"
    $ player_map_x = 2500
    $ player_map_y = 3500
    $ player_facing = "up"
    $ act7_cas_nodes = [
        MapNode("to_cl3",      900, 2700, "act7_cl3_map", tooltip="Head to Computer Lab", icon_image="ArrowUp.png", locked=False, icon_zoom=1.5),
        MapNode("prof_santos", 3200, 2900, "act7_npc_prof_santos", tooltip="Prof. Santos", icon_image="ow_hsu.png", locked=False, icon_zoom=0.15),
        MapNode("classmate_bea", 1500, 2900, "act7_npc_classmate_bea", tooltip="Bea", icon_image="ate_bea.png", locked=True),
        MapNode("study_session", 2260, 5000, "act7_study_session", tooltip="Study Session", icon_image="ArrowDown.png", locked=True, icon_zoom=2.0),
    ]
    $ current_task_text = "Visit the computer lab and talk to the professors"

label act7_cas_loop:

    # Always check unlocks for Bea and Study Session
    if "talk_kuya_neil" in tasks_completed and "talk_prof_santos" in tasks_completed:
        $ act7_cas_nodes[2].locked = False

    if (
        "talk_kuya_neil" in tasks_completed and
        "talk_prof_santos" in tasks_completed and
        "talk_classmate_bea" in tasks_completed
    ):
        $ act7_cas_nodes[3].locked = False
        $ current_task_text = "Attend the study session"

    call screen map_screen("ui/CAS_Overworld(F).png", act7_cas_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, map_bg="ui/CAS_Overworld(F).png", nodes=act7_cas_nodes, player_zoom=2.5) from _call_walk_to_node_16
        if _node.target_label == "act7_cl3_map":
            jump act7_cl3_map
        else:
            call expression _node.target_label from _call_expression_16

        if is_act_complete():
            jump act7_complete

    jump act7_cas_loop

## --- MAP 3: CL3 Computer Lab ---
label act7_cl3_map:
    python:
        global act7_cl3_nodes
    $ current_map_bg = "maps/CL3.png"
    $ player_map_x = 2500
    $ player_map_y = 3500
    $ player_facing = "up"
    $ act7_cl3_nodes = [
        MapNode("kuya_neil", 2475, 1775, "act7_npc_kuya_neil", tooltip="Kuya Neil", icon_image="ow_lovers.png", locked=False, icon_zoom=0.16),
        MapNode("to_cas", 4000, 1600, "act7_cas_map", tooltip="CAS Front", icon_image="Arrow.png", locked=False, icon_zoom=1.5),
    ]
    $ current_task_text = "Visit Kuya Neil in the Computer Lab"

label act7_cl3_loop:
    call screen map_screen("maps/CL3.png", act7_cl3_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, map_bg="maps/CL3.png", nodes=act7_cl3_nodes, player_zoom=2.5) from _call_walk_to_node_17
        if _node.target_label == "act7_cas_map":
            jump act7_cas_map
        else:
            call expression _node.target_label from _call_expression_17

    jump act7_cl3_loop


label act7_complete:
    scene black
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
        MapNode("end_of_week",   2500, 2200, "act8_end_of_week",     tooltip="Campus Oval",   icon_image="npcs/Arrow.png",         locked=True),
    ]
    $ current_task_text = "Catch up with Jaden"

label act8_loop:
    call screen map_screen("ui/dormRoom.png", act8_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, nodes=act8_nodes) from _call_walk_to_node_18
        call expression _node.target_label from _call_expression_18

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
    scene black
    call screen act_transition("ACT 8 COMPLETE", "You've found your place at UP Visayas.", "complete")

    jump open_world


## ============================================================================
## OPEN WORLD — Free Exploration (Endgame)
## ============================================================================

label open_world:
    scene black
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
        call walk_to_node(_node, nodes=openworld_nodes) from _call_walk_to_node_19
        call expression _node.target_label from _call_expression_19

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
