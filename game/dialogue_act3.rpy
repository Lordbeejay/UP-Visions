## ============================================================================
## ACT 3 DIALOGUES — Enrollment (CRS Portal & Schedule Building)
## KEY THEME: How enrollment works, CRS system, building a schedule
## ============================================================================

## ============================================================================
## NPC — SIR NOEL (Faculty / Enrollment Adviser)
## KEY INFO: Enrollment process, CRS walkthrough, units & schedule
## ============================================================================
label act3_npc_sir_noel:
    window show
    sir_noel "Ah, you must be one of the freshmen. Come in, come in."
    sir_noel "I'm Sir Noel, one of the faculty advisers for enrollment. You're here to learn how enrollment works?"
    player_char "Yes, Sir. I've heard about the CRS but I don't really understand how it all works."
    sir_noel "Perfect timing. Let me walk you through the entire process."
    sir_noel "First — the big picture. Enrollment at UP is done through the CRS."
    sir_noel "CRS stands for Computerized Registration System. It's the online portal where everything happens."

    ## ITEM DROP
    $ collect_item(ITEM_CRS_SYSTEM)
    show screen item_pickup_screen(ITEM_CRS_SYSTEM)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "What are the enrollment steps?":
            jump act3_noel_steps
        "How many subjects do I take?":
            jump act3_noel_units
        "Any tips for building my schedule?":
            jump act3_noel_schedule_tips

label act3_noel_steps:
    sir_noel "The enrollment process has five key steps. Pay attention."
    sir_noel "Step 1: Pre-enlistment. You log into CRS and select the subjects and sections you want."
    sir_noel "The system assigns you slots based on availability and priority — freshies get priority."
    sir_noel "Step 2: Confirmation. When enrollment officially opens, you confirm your pre-enlisted subjects."
    sir_noel "Step 3: Assessment. The system calculates your tuition and miscellaneous fees."
    sir_noel "Step 4: Payment. You pay at the Cashier's Office or through online payment channels."
    sir_noel "Step 5: Form 5. Your official proof of enrollment is generated. Keep it safe."
    player_char "So I need to do pre-enlistment first before everything else?"
    sir_noel "Exactly. Without pre-enlistment, you won't have any subjects to confirm."
    sir_noel "And without confirmation, you're not officially enrolled."

    ## ITEM DROP
    $ collect_item(ITEM_ENROLLMENT_STEPS)
    show screen item_pickup_screen(ITEM_ENROLLMENT_STEPS)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "How many subjects do I take?":
            jump act3_noel_units
        "Tips for building my schedule?":
            jump act3_noel_schedule_tips
        "(I think I understand the steps now)":
            jump act3_noel_show_portal

label act3_noel_units:
    sir_noel "Good question. Let's talk about academic load."
    sir_noel "A typical freshman load is 18 academic units."
    sir_noel "That's 6 subjects at 3 units each."
    sir_noel "On top of that, you'll have two additional non-unit subjects: PE and NSTP."
    sir_noel "PE is Physical Education — required for all freshmen."
    sir_noel "NSTP is the National Service Training Program — also required."
    sir_noel "They don't count toward your academic units, but you MUST complete them."
    player_char "So 6 academic subjects plus PE and NSTP?"
    sir_noel "Correct. That's your standard first-semester load."
    sir_noel "Each unit roughly equals one hour of class per week. A 3-unit subject meets for about 3 hours weekly."
    sir_noel "Classes can be 60 minutes or 120 minutes depending on the schedule."

    ## ITEM DROP
    $ collect_item(ITEM_UNITS_LOAD)
    show screen item_pickup_screen(ITEM_UNITS_LOAD)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "What are the enrollment steps?":
            jump act3_noel_steps
        "Tips for building my schedule?":
            jump act3_noel_schedule_tips
        "(Got it, let's see the portal)":
            jump act3_noel_show_portal

label act3_noel_schedule_tips:
    sir_noel "Building your schedule is like solving a puzzle. Here are my tips."
    sir_noel "First — PE and NSTP have fixed schedules. Build around them."
    sir_noel "Second — check for time conflicts. The CRS won't allow overlapping classes."
    sir_noel "Third — consider room locations. Give yourself at least 15 minutes between classes in different buildings."
    sir_noel "Fourth — avoid stacking all heavy subjects on one day. Spread them out."
    sir_noel "Fifth — keep at least one lunch break. Trust me on this one."
    sir_noel "Sixth — 7 AM classes are brutal. Only take them if you're truly a morning person."
    player_char "This sounds like a game of Tetris."
    sir_noel "Ha! You're not wrong. In fact, let me show you something..."

    ## ITEM DROP
    $ collect_item(ITEM_SCHEDULE_TIPS)
    show screen item_pickup_screen(ITEM_SCHEDULE_TIPS)
    pause 2.5
    hide screen item_pickup_screen

    jump act3_noel_show_portal

label act3_noel_show_portal:
    sir_noel "Let me show you the actual CRS Student Portal. This is what you'll be using."
    $ complete_task("talk_sir_noel")

    mikhaela "Did you survive Sir Ruel?"
    mikhaela "Want some? It's isaw from the kiosk near the gate. Best post-enrollment reward."

    menu:
        "Sure, thanks.":
            jump npc_mikhaela_eat
        "No thanks, I'm good.":
            jump npc_mikhaela_decline

label npc_mikhaela_eat:
    narrator_char "(You take a stick of isaw. It's perfectly grilled.)"
    mikhaela "See? Instant morale boost."
    $ complete_task("talk_mikhaela")
    window hide
    return

label npc_mikhaela_decline:
    mikhaela "Your loss! I'll save you one if you change your mind."
    $ complete_task("talk_mikhaela")
    window hide
    return

## --- Jaden ---
label act3_npc_jaden:
    jump Act3_npc_jaden

label Act3_npc_jaden:
    window show

    jaden "Hey! You survived Sir Ruel."

    menu:
        "Barely. He's intense.":
            jump npc_jaden_intense
        "It was easy.":
            jump npc_jaden_easy
        "I need food. Now.":
            jump npc_jaden_hungry

label npc_jaden_intense:
    jaden "Same. I came from CUB and got my stipend papers tagged."
    jaden "That line took forever."
    jump npc_jaden_invite

label npc_jaden_easy:
    jaden "Wow, confident freshie."
    jaden "I came from CUB too and got my stipend papers tagged."
    jump npc_jaden_invite

label npc_jaden_hungry:
    jaden "Real. Enrollment burns more energy than PE."
    jaden "I just finished at CUB too."
    jump npc_jaden_invite

label npc_jaden_invite:
    jaden "I'm heading to Lover's Lane to meet some friends. Want to walk with me?"

    menu:
        "Sure, let's go.":
            jump npc_jaden_go
        "Where is Lover's Lane?":
            jump npc_jaden_explain

label npc_jaden_explain:
    jaden "It's near HSU, just past the dormitory road."
    jaden "It's breezy there, and the sunset is good. It's walking distance."
    jump npc_jaden_go

label npc_jaden_go:
    jaden "All settled?"
    jaden "Come on, let's walk it off. My friends are waiting at Lover's Lane."
    $ complete_task("talk_jaden")
    window hide

    ## Show the CRS portal screen
    call screen crs_enrollment_ui()

    window show
    sir_noel "That's the portal. You'll get familiar with it quickly."
    sir_noel "Now — let's put what you learned into practice."
    sir_noel "I have a little challenge for you. Think of it as... Enrollment Tetris."
    sir_noel "You need to fit your subjects into a weekly schedule grid."
    sir_noel "18 units of academic subjects — 6 subjects at 3 units each."
    sir_noel "Plus PE and NSTP as non-unit subjects."
    sir_noel "Each class block is 60 to 120 minutes. No overlaps allowed!"
    player_char "Enrollment Tetris? Sounds fun. Let's do it."
    $ complete_task("view_crs_portal")
    window hide

    ## Launch enrollment tetris mini-game
    call screen enrollment_tetris_game()
    $ _tetris_result = _return

    if _tetris_result == "completed":
        window show
        sir_noel "Excellent work! You've built a complete schedule."
        sir_noel "All 18 units plus PE and NSTP — no conflicts."
        sir_noel "You're going to do great this semester."
        player_char "Thanks, Sir Noel! That really helped me understand how scheduling works."
        sir_noel "Anytime. My office is Room 203, New Admin. Door's always open during consultation hours."
        $ complete_task("complete_enrollment_tetris")
        if "sq_crs_tactics" not in subquests_completed or "sq_academic_load" not in subquests_completed:
            sir_noel "One more thing — while you're here, do you want to test what you've really learned?"
            menu:
                "★ CRS tactics — quiz me on survival strategies for enlistment." if "sq_crs_tactics" not in subquests_completed:
                    jump sq_crs_tactics
                "★ Academic load — quiz me on units, NSTP, and standing." if "sq_academic_load" not in subquests_completed:
                    jump sq_academic_load
                "(I'm good, thanks Sir Noel.)":
                    pass
        window hide

    caezar "Oy, Jaden! Finally."
    caezar "Welcome to UPV. First-day survival rate is still 100%%, I see."
    caezar "So, freshie, what's the plan? Honors, org life, or just survive semester one?"

    menu:
        "I need to maintain my scholarship. Grades are priority.":
            jump npc_caezar_response
        "I want to meet people. Join orgs.":
            jump npc_caezar_response
        "I just want to graduate on time.":
            jump npc_caezar_response

label npc_caezar_response:
    caezar "Good answer."
    caezar "Just remember: UP isn't just about the classroom."
    narrator_char "(He gestures to the field and the trees.)"
    caezar "Look around once in a while. That's part of learning too."
    $ complete_task("talk_caezar")
    window hide
    return

## ============================================================================
## END OF ACT 3 DIALOGUES
## ============================================================================
