## ============================================================================
## ACT 4 DIALOGUES — Dorm Life
## KEY THEME: Dormitory check-in, dorm rules, room setup essentials
## ============================================================================

## ============================================================================
## NPC — DORM MANAGER (Check-in & Rules)
## KEY INFO: Point system, curfew, dorm rules, room assignment
## ============================================================================
label act4_npc_dorm_manager:
    # play music moved to end of previous act
    window show

    dorm_mgr "Good afternoon. You're one of the new freshmen?"
    player_char "Yes, Ma'am. I'm here to check in to the dormitory."
    dorm_mgr "Alright. Let me pull up your file."
    dorm_mgr "We use a Point System here. Priority is based on three factors."
    dorm_mgr "First — distance. How far is your permanent residence?"

    menu:
        "Luzon / Mindanao / Outside Panay.":
            jump act4_dorm_far
        "Aklan / Capiz / Antique (3-4 hours away).":
            jump act4_dorm_mid
        "Iloilo City / Oton (1-2 hours away).":
            jump act4_dorm_near

label act4_dorm_far:
    dorm_mgr "That gives you maximum points for Distance. Good."
    jump act4_dorm_income

label act4_dorm_mid:
    dorm_mgr "That gives you good points for Distance."
    jump act4_dorm_income

label act4_dorm_near:
    dorm_mgr "Hmm. That's close. You're currently Waitlist #5."
    dorm_mgr "But don't worry — slots usually open up within the first week."
    dorm_mgr "For now, let me still walk you through the process in case you get in."
    jump act4_dorm_income

label act4_dorm_income:
    dorm_mgr "Second factor — family income bracket. Lower income means higher priority."
    dorm_mgr "Third — year level. Freshmen and graduating students get priority."
    dorm_mgr "We're currently at 90%% capacity. But you qualify for a slot."

    ## ITEM DROP
    $ collect_item(ITEM_DORM_POINT_SYSTEM)
    show screen item_pickup_screen(ITEM_DORM_POINT_SYSTEM)
    pause 2.5
    hide screen item_pickup_screen

    dorm_mgr "Now — the rules. Pay close attention."
    dorm_mgr "Rule 1: Curfew is 10:00 PM. The gates are locked. No exceptions."

    menu:
        "What happens if I miss curfew?":
            jump act4_dorm_curfew_q
        "Understood. What else?":
            jump act4_dorm_more_rules

label act4_dorm_curfew_q:
    dorm_mgr "First offense — warning. Second offense — community service."
    dorm_mgr "Third offense — eviction. I don't make the rules, but I do enforce them."
    jump act4_dorm_more_rules

label act4_dorm_more_rules:
    dorm_mgr "Rule 2: No electric coils, heaters, or rice cookers inside your room."
    dorm_mgr "Fire hazard. We've had incidents before."
    dorm_mgr "Rule 3: Visitors are allowed in the lobby only. Never in the rooms."
    dorm_mgr "Rule 4: Quiet hours are 10 PM to 6 AM. Your roommates will thank you."
    dorm_mgr "Rule 5: Room inspections happen monthly. Keep your space clean."

    ## ITEM DROP
    $ collect_item(ITEM_DORM_RULES)
    show screen item_pickup_screen(ITEM_DORM_RULES)
    pause 2.5
    hide screen item_pickup_screen

    dorm_mgr "Any questions before I hand you your key?"

    menu:
        "What should I bring to my room?":
            jump act4_dorm_essentials
        "Any tips for dorm life?":
            jump act4_dorm_life_tips
        "I think I'm ready.":
            jump act4_dorm_key

label act4_dorm_essentials:
    dorm_mgr "Good question. Let me give you the essentials list."
    dorm_mgr "Bedding — we provide the mattress, you bring pillow, blanket, and sheets."
    dorm_mgr "Electric fan — no aircon in standard rooms."
    dorm_mgr "Toiletries, study lamp, padlock for your cabinet, and an extension cord."
    dorm_mgr "Buy from the Miagao market — much cheaper than Manila prices."

    ## ITEM DROP
    $ collect_item(ITEM_DORM_ESSENTIALS)
    show screen item_pickup_screen(ITEM_DORM_ESSENTIALS)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "Any tips for dorm life?":
            jump act4_dorm_life_tips
        "Got it. I'm ready for my key.":
            jump act4_dorm_key

label act4_dorm_life_tips:
    dorm_mgr "Introduce yourself to your roommate on day one. Set expectations early."
    dorm_mgr "Use headphones after quiet hours. Label your food in shared fridges."
    dorm_mgr "The dorm kitchen has a shared rice cooker and microwave — bring your own utensils."
    dorm_mgr "And join dorm activities. Movie nights, study groups, floor events."
    dorm_mgr "The dorm is your first community in UP. Make the most of it."

    ## ITEM DROP
    $ collect_item(ITEM_DORM_TIPS)
    show screen item_pickup_screen(ITEM_DORM_TIPS)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "What should I bring to my room?":
            if "dorm_essentials" not in [item.item_id for item in collected_items]:
                jump act4_dorm_essentials
        "I'm ready for my key.":
            jump act4_dorm_key

label act4_dorm_key:
    dorm_mgr "Sign here."
    narrator_char "(You sign the dormitory agreement form.)"
    dorm_mgr "Your room is #207. Second floor, end of the hall."
    dorm_mgr "Here's your key. Welcome to the dorm."
    player_char "Thank you, Ma'am."
    dorm_mgr "One more thing — you'll want to set up your room before it gets dark."
    dorm_mgr "Head to your room and get settled in."

    $ complete_task("talk_dorm_manager")
    if "sq_dorm_code" not in subquests_completed or "sq_dorm_survival" not in subquests_completed:
        $ _flip = renpy.random.randint(0, 1)
        if "sq_dorm_code" not in subquests_completed and "sq_dorm_survival" not in subquests_completed:
            if _flip == 0:
                menu:
                    "★ Walk me through the dorm rules properly.":
                        jump sq_dorm_code
                    "★ Help me check if I have everything I need.":
                        jump sq_dorm_survival
                    "(Okay, heading to my room now.)":
                        pass
            else:
                menu:
                    "★ Help me check if I have everything I need.":
                        jump sq_dorm_survival
                    "★ Walk me through the dorm rules properly.":
                        jump sq_dorm_code
                    "(Okay, heading to my room now.)":
                        pass
        elif "sq_dorm_code" not in subquests_completed:
            if _flip == 0:
                menu:
                    "★ Walk me through the dorm rules properly.":
                        jump sq_dorm_code
                    "(Okay, heading to my room now.)":
                        pass
            else:
                menu:
                    "(Okay, heading to my room now.)":
                        pass
                    "★ Walk me through the dorm rules properly.":
                        jump sq_dorm_code
        else:
            if _flip == 0:
                menu:
                    "★ Help me check if I have everything I need.":
                        jump sq_dorm_survival
                    "(Okay, heading to my room now.)":
                        pass
            else:
                menu:
                    "(Okay, heading to my room now.)":
                        pass
                    "★ Help me check if I have everything I need.":
                        jump sq_dorm_survival
    window hide
    return


## ============================================================================
## ROOM EXPLORATION — Enter the dorm room
## ============================================================================
label act4_explore_room:
    scene expression "images/maps/Dorm_Room.png" with fade
    window show

    narrator_char "(You open the door to Room 207.)"
    narrator_char "(It's a small room with two beds, two desks, two cabinets, and a window.)"
    narrator_char "(One side is already occupied — your roommate has set up their things.)"
    narrator_char "(Your side is bare. Just a mattress on a wooden bed frame and an empty cabinet.)"

    player_char "This is it. Home for the next year."
    narrator_char "(You set down your bag and look around.)"
    narrator_char "(You need to set up your space. Time to unpack and arrange your essentials.)"
    player_char "Let's see what I can do with this room..."

    $ complete_task("explore_dorm_room")
    window hide

    ## Launch the room setup mini-game
    call screen dorm_room_setup_game()
    $ _setup_result = _return

    if _setup_result == "completed":
        window show
        narrator_char "(Your side of the room is now set up. It's not much, but it feels like yours.)"
        narrator_char "(Bed made. Lamp on the desk. Fan plugged in. Essentials in the cabinet.)"
        player_char "Not bad for a first setup."
        narrator_char "(You sit on your bed and take a deep breath.)"
        narrator_char "(This is really happening. You're a UP student. You have a room. You're here.)"
        $ complete_task("complete_room_setup")
        window hide

    return

## ============================================================================
## END OF ACT 4 DIALOGUES
## ============================================================================
play music "audio/Act5.mp3" fadein 1.0
