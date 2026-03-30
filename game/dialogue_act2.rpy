## ============================================================================
## ACT 2 DIALOGUES — Entrance → New Admin → Inside New Admin
## KEY THEME: Security & Permits, Offices, Office Hours
## ============================================================================

## ============================================================================
## NPC 1 — ATE BEA (Upperclassman Guide) — at Entrance
## KEY INFO: What is BOX 1, Bus schedules, tips
## ============================================================================
label act2_npc_ate_bea:
    ## Play Act 2 music
    play music "audio/Something Wrong with my Dog.mp3"
    scene expression "images/maps/Entrance.png"
    window show
    ate_bea "Oh, you look lost. First time sa BOX 1?"
    player_char "Is it that obvious?"
    ate_bea "Haha, everyone has that face. I'm Bea, 3rd year. I basically lived here during my freshie days."
    player_char "Why is it called BOX 1?"
    ate_bea "Good question! Nobody really knows the official reason—but the popular theory is it's because the building is literally box-shaped."
    ate_bea "Others say it's because it's the first 'box' or checkpoint you pass before entering the main campus."
    ate_bea "Either way, BOX 1 is basically the gateway. Everything admin-related starts here."

    ## ITEM DROP
    $ collect_item(ITEM_BOX1_INFO)
    show screen item_pickup_screen(ITEM_BOX1_INFO)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "What offices are here?":
            jump act2_bea_offices
        "What about the bus schedules?":
            jump act2_bea_bus
        "Any tips for a freshie?":
            jump act2_bea_tips

label act2_bea_offices:
    ate_bea "BOX 1 has the important admin offices — Registrar, Cashier, OSA, and the Chancellor's office is upstairs."
    ate_bea "The New Admin building beside it has more faculty offices and the College offices."
    ate_bea "Rule of thumb: anything about your enrollment, grades, or official documents — BOX 1 first."
    menu:
        "What about bus schedules?":
            jump act2_bea_bus
        "Any tips?":
            jump act2_bea_tips
        "(That's helpful, thanks)":
            jump act2_bea_end

label act2_bea_bus:
    ate_bea "The UPV Bus! Lifesaver for students without a ride."
    ate_bea "There's a shuttle that goes from UPV Miagao to Iloilo City — usually departs 5:30 AM and 6:00 AM on weekdays."
    ate_bea "Afternoon trips back to Miagao leave around 5:00 PM from the Iloilo City campus or designated stops."
    ate_bea "Schedules change every semester though, so always check the bulletin board near the gate or the UPV Facebook page."
    ate_bea "Pro tip: arrive 10 minutes early. The bus doesn't wait."
    player_char "Good to know. I was wondering how to get to the city."
    ate_bea "Also — the bus is FREE for enrolled UPV students. Just show your validated Form 5 or UP ID."

    ## ITEM DROP
    $ collect_item(ITEM_UPV_BUS)
    show screen item_pickup_screen(ITEM_UPV_BUS)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "Any general tips?":
            jump act2_bea_tips
        "(That's enough, thanks)":
            jump act2_bea_end

label act2_bea_tips:
    ate_bea "Okay, freshie tips from someone who survived. Listen carefully."
    ate_bea "One — always bring your Form 5 everywhere. It's your proof of enrollment until you get your UP ID."
    ate_bea "Two — office hours are NOT suggestions. If the sign says 8 AM to 12 PM, don't show up at 11:55."
    ate_bea "Three — be polite to the staff. They process hundreds of students. A simple 'Good morning' goes a long way."
    ate_bea "Four — the CRS. That's the Computerized Registration System. You'll use it for everything — adding subjects, dropping, viewing grades."
    ate_bea "Five — when in doubt, ask a fellow student. We're not scary, I promise."
    player_char "This is really helpful. Thank you, Ate Bea."
    ate_bea "No problem! That's what upperclassmen are for. Good luck sa enrollment!"

    ## ITEM DROP
    $ collect_item(ITEM_FRESHIE_TIPS)
    show screen item_pickup_screen(ITEM_FRESHIE_TIPS)
    pause 2.5
    hide screen item_pickup_screen

    jump act2_bea_end

label act2_bea_end:
    ate_bea "By the way, you should also talk to Kuya Mark — the guard near the gate. He knows all the security rules."
    if "sq_up_jargon" not in subquests_completed:
        menu:
            "★ Before you go — can you quiz me on UP academic jargon? DRP, INC, LOA...":
                jump sq_up_jargon
            "(Alright, thanks Ate Bea!)":
                jump act2_bea_complete
    else:
        jump act2_bea_complete

label act2_bea_complete:
    $ complete_task("talk_ate_bea")
    window hide
    return

## ============================================================================
## NPC 2 — KUYA MARK (Security Guard) — at Entrance
## KEY INFO: ID policies, security protocols, restricted areas
## ============================================================================
label act2_npc_kuya_mark:
    scene expression "images/maps/Entrance.png"
    window show
    kuya_mark "Good morning. Transaction?"
    player_char "Good morning, Kuya. I'm a freshie — I wanted to ask about the campus rules."
    kuya_mark "Smart. Most students just walk in without knowing. Okay, sit down. This is important."
    menu:
        "What are the ID policies?":
            jump act2_mark_id
        "What are the security protocols?":
            jump act2_mark_security
        "Are there restricted areas?":
            jump act2_mark_restricted

label act2_mark_id:
    kuya_mark "ID policy — very strict here. Once you have your UP ID, you wear it at all times inside campus."
    kuya_mark "No ID, no entry — that's the rule at the main gate and at most buildings."
    kuya_mark "As a freshie, your temporary pass is your Notice of Admission or validated Form 5."
    kuya_mark "Keep it in a clear sleeve, not crumpled in your bag. Guards will ask for it."
    kuya_mark "For vehicles — cars, motorcycles — they need a separate vehicle sticker from the Security Office."
    kuya_mark "No sticker, no entry for vehicles. Visitors park outside and walk in."
    player_char "What if I forget my ID one day?"
    kuya_mark "You write in the logbook and leave a valid ID. We return it when you exit."
    kuya_mark "But don't make it a habit. Repeat offenders get flagged."

    ## ITEM DROP
    $ collect_item(ITEM_ID_POLICY)
    show screen item_pickup_screen(ITEM_ID_POLICY)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "What about security protocols?":
            jump act2_mark_security
        "Any restricted areas?":
            jump act2_mark_restricted
        "(Understood, thank you)":
            jump act2_mark_end

label act2_mark_security:
    kuya_mark "Security protocols. Simple rules that students often ignore."
    kuya_mark "First — bags are subject to inspection at building entrances, especially the library and labs."
    kuya_mark "Second — no alcohol, no weapons, no illegal substances anywhere on campus. Zero tolerance."
    kuya_mark "Third — curfew for dormers is 10 PM. After that, you need special permission from the Dorm Manager."
    kuya_mark "Fourth — any incident — theft, harassment, accidents — report immediately to the Security Office near the gate."
    kuya_mark "Fifth — during emergencies, follow the evacuation signs. Assembly area is the open field near the flagpole."
    player_char "Is there a security hotline?"
    kuya_mark "Yes. The number is posted at every building entrance and at the gate. Save it on your phone."
    kuya_mark "Better to have it and not need it than need it and not have it."

    ## ITEM DROP
    $ collect_item(ITEM_SECURITY_RULES)
    show screen item_pickup_screen(ITEM_SECURITY_RULES)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "Are there restricted areas?":
            jump act2_mark_restricted
        "(That's clear, thank you)":
            jump act2_mark_end

label act2_mark_restricted:
    kuya_mark "Restricted areas. Pay attention to this."
    kuya_mark "The fishponds and wet lab areas require written permission from the College of Fisheries and Ocean Sciences."
    kuya_mark "The Chancellor's Office floor — you need an appointment. You can't just walk in."
    kuya_mark "Research vessels and marine stations — strictly faculty and authorized researchers only."
    kuya_mark "The rooftops of any building — off limits. No exceptions."
    kuya_mark "Some parts of the beachfront are also restricted after 6 PM for safety reasons."
    player_char "What happens if someone enters a restricted area without permission?"
    kuya_mark "Confiscation of ID, incident report, possible disciplinary action through the OSA."
    kuya_mark "It's not worth it. Just follow the rules."

    ## ITEM DROP
    $ collect_item(ITEM_RESTRICTED_AREAS)
    show screen item_pickup_screen(ITEM_RESTRICTED_AREAS)
    pause 2.5
    hide screen item_pickup_screen

    jump act2_mark_end

label act2_mark_end:
    kuya_mark "Any more questions, come find me at the Security Office near the main gate. I'm here 6 AM to 6 PM."
    kuya_mark "If you need to process anything admin-related, head to the New Admin building. Ma'am Reyes can help you there."
    if "sq_student_rights" not in subquests_completed:
        menu:
            "★ Kuya Mark — do you know the student rights under the UP handbook?":
                jump sq_student_rights
            "(Noted, thanks Kuya Mark.)":
                jump act2_mark_complete
    else:
        jump act2_mark_complete

label act2_mark_complete:
    $ complete_task("talk_kuya_mark")
    window hide
    return

## ============================================================================
## NAVIGATION — Go to New Admin (from Entrance map)
## ============================================================================
label act2_go_to_newad:
    window show
    narrator_char "(You walk toward the New Admin building. It's a short path from the Entrance.)"
    narrator_char "(Ate Bea and Kuya Mark mentioned Ma'am Reyes can be found inside.)"
    narrator_char "(Time to head in and learn about the offices.)"
    $ complete_task("go_to_newad")
    window hide
    return

## ============================================================================
## NAVIGATION — Enter Inside New Admin (from NewAd exterior map)
## ============================================================================
label act2_enter_inside:
    window show
    narrator_char "(You push open the glass doors of the New Admin building.)"
    narrator_char "(Inside, the hallway stretches out with doors on either side — each one labeled with an office name.)"
    narrator_char "(You spot a reception desk at the far end. That must be where Ma'am Reyes is.)"
    window hide
    return

## ============================================================================
## NPC 3 — MA'AM REYES (Admin Staff) — Inside New Admin
## KEY INFO: Offices in BOX 1, office hours, appointments vs walk-ins
## ============================================================================
label act2_npc_maam_reyes:
    scene expression "images/maps/Entrance.png"
    window show
    maam_reyes "Good morning! How can I help you?"
    player_char "Good morning, Ma'am. I'm a freshie. I wanted to know more about the offices here."
    maam_reyes "Of course! Let me walk you through everything. BOX 1 and New Admin can be confusing at first."
    menu:
        "What offices are inside BOX 1?":
            jump act2_reyes_offices
        "What are the office hours?":
            jump act2_reyes_hours
        "Which offices need appointments?":
            jump act2_reyes_appointments

label act2_reyes_offices:
    maam_reyes "Let me list them for you. Ground floor of BOX 1:"
    maam_reyes "The Office of the University Registrar — enrollment, official transcripts, certifications, Form 5."
    maam_reyes "The Cashier's Office — payment of fees, refunds, and financial transactions."
    maam_reyes "The Office of Student Affairs, or OSA — scholarships, student organizations, discipline cases."
    maam_reyes "Second floor — the Chancellor's Office and the Vice Chancellor offices."
    maam_reyes "In the New Admin building beside BOX 1 — College offices, faculty rooms, and the Conference Room."
    player_char "That's a lot of offices."
    maam_reyes "It can feel overwhelming at first! But you'll only need two or three regularly as a student."
    maam_reyes "Registrar and Cashier will be your most visited."

    ## ITEM DROP
    $ collect_item(ITEM_OFFICE_DIRECTORY)
    show screen item_pickup_screen(ITEM_OFFICE_DIRECTORY)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "What are the office hours?":
            jump act2_reyes_hours
        "Which need appointments?":
            jump act2_reyes_appointments
        "(That's helpful, thanks)":
            jump act2_reyes_end

label act2_reyes_hours:
    maam_reyes "Office hours — write these down!"
    maam_reyes "Monday to Friday. Morning: 8:00 AM to 12:00 NN. Afternoon: 1:00 PM to 5:00 PM."
    maam_reyes "The Registrar and Cashier close for lunch from 12 to 1 — no exceptions during peak enrollment."
    maam_reyes "The OSA sometimes has extended hours during the first week of classes for org registrations."
    maam_reyes "Chancellor's Office — by appointment only, and usually morning slots go fast."
    maam_reyes "On Saturdays — some offices operate 8 AM to 12 PM only. Check the bulletin board to confirm."
    maam_reyes "Holidays — fully closed. Don't show up on holidays expecting service."
    player_char "What's the best time to go to avoid long lines?"
    maam_reyes "First thing in the morning — 8 AM sharp. Lines at the Registrar can get very long by 9:30."

    ## ITEM DROP
    $ collect_item(ITEM_OFFICE_HOURS)
    show screen item_pickup_screen(ITEM_OFFICE_HOURS)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "Which offices need appointments?":
            jump act2_reyes_appointments
        "(Got it, thank you)":
            jump act2_reyes_end

label act2_reyes_appointments:
    maam_reyes "Great question. Let me separate them for you."
    maam_reyes "WALK-IN offices — no appointment needed:"
    maam_reyes "Registrar for Form 5, enrollment validation, and basic certifications."
    maam_reyes "Cashier for payments and official receipts."
    maam_reyes "OSA for scholarship inquiries and org matters — though expect a wait."
    maam_reyes "APPOINTMENT REQUIRED:"
    maam_reyes "Chancellor's Office — email or call ahead. Walk-ins are almost never accommodated."
    maam_reyes "Vice Chancellor offices — same rule, appointment first."
    maam_reyes "Faculty consultations — coordinate directly with your professor for their consultation hours."
    maam_reyes "Medical Certificate requests beyond routine — schedule with the Health Services Unit."
    player_char "How do I make an appointment with the Chancellor's Office?"
    maam_reyes "Email the administrative aide — the address is posted on the door of the office."
    maam_reyes "State your purpose clearly and include your student number. They respond within one to two working days."

    ## ITEM DROP
    $ collect_item(ITEM_APPOINTMENTS)
    show screen item_pickup_screen(ITEM_APPOINTMENTS)
    pause 2.5
    hide screen item_pickup_screen

    jump act2_reyes_end

label act2_reyes_end:
    maam_reyes "If you have more questions, my desk is right here at the New Admin lobby. Don't hesitate!"
    maam_reyes "Oh, before you go — let me test if you remember which office does what."
    maam_reyes "I have a little matching game here. It'll help you remember the offices better!"
    $ complete_task("talk_maam_reyes")
    window hide

    ## Launch the flip card mini-game
    call screen flip_card_game()
    $ _flip_result = _return

    if _flip_result == "completed":
        window show
        maam_reyes "Excellent! You matched them all correctly. You'll do just fine navigating the offices!"
        player_char "Thanks, Ma'am Reyes! That really helped me remember."
        maam_reyes "Good luck with your enrollment!"
        $ complete_task("complete_flip_card")
        window hide

    return

## ============================================================================
## END OF ACT 2 DIALOGUES
## ============================================================================
