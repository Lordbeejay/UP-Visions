## ============================================================================
## ACT 2 DIALOGUES — Exploring BOX 1 and New Admin
## KEY THEME: Security & Permits, Offices, Office Hours
## ============================================================================

## ============================================================================
## NPC 1 — ATE BEA (Upperclassman Guide)
## KEY INFO: What is BOX 1, Bus schedules, tips
## ============================================================================
label act2_npc_ate_bea:
    window show
    ate_bea "Oh, you look lost. First time sa BOX 1?"
    player_char "Is it that obvious?"
    ate_bea "Haha, everyone has that face. I'm Bea, 3rd year. I basically lived here during my freshie days."
    player_char "Why is it called BOX 1?"
    ate_bea "Good question! Nobody really knows the official reason—but the popular theory is it's because the building is literally box-shaped."
    ate_bea "Others say it's because it's the first 'box' or checkpoint you pass before entering the main campus."
    ate_bea "Either way, BOX 1 is basically the gateway. Everything admin-related starts here."
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
    jump act2_bea_end

label act2_bea_end:
    $ complete_task("talk_ate_bea")
    window hide
    return

## ============================================================================
## NPC 2 — KUYA MARK (Security Guard)
## KEY INFO: ID policies, security protocols, restricted areas
## ============================================================================
label act2_npc_kuya_mark:
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
    jump act2_mark_end

label act2_mark_end:
    kuya_mark "Any more questions, come find me at the Security Office near the main gate. I'm here 6 AM to 6 PM."
    $ complete_task("talk_kuya_mark")
    window hide
    return

## ============================================================================
## NPC 3 — MA'AM REYES (Admin Staff)
## KEY INFO: Offices in BOX 1, office hours, appointments vs walk-ins
## ============================================================================
label act2_npc_maam_reyes:
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
    jump act2_reyes_end

label act2_reyes_end:
    maam_reyes "If you have more questions, my desk is right here at the New Admin lobby. Don't hesitate!"
    $ complete_task("talk_maam_reyes")
    window hide
    return

## ============================================================================
## NPC 4 — SIR ALLAN (Faculty NPC)
## KEY INFO: CRS walkthrough, enrollment process
## ============================================================================
label act2_npc_sir_allan:
    window show
    sir_allan "Ah, a freshie! You look like you need help with the CRS."
    player_char "The CRS? I've heard it mentioned but I don't fully understand it yet."
    sir_allan "The Computerized Registration System. It's how UP manages enrollment. Let me show you."
    sir_allan "But first — do you have your student number and initial password from the Registrar?"
    menu:
        "Yes, I have them.":
            jump act2_allan_crs_demo
        "No, I don't have them yet.":
            jump act2_allan_crs_prereq

label act2_allan_crs_prereq:
    sir_allan "Then your first stop is the Registrar's window. Ask for your CRS credentials."
    sir_allan "You'll need your Notice of Admission and one valid ID."
    sir_allan "Once you have your student number and temporary password, come back and we'll go through the CRS together."
    $ complete_task("talk_sir_allan")
    window hide
    return

label act2_allan_crs_demo:
    sir_allan "Good. Let me walk you through the CRS enrollment process step by step."
    sir_allan "Pay attention — this is how you'll enroll every semester for the next four years."
    call screen crs_enrollment_ui
    $ crs_result = _return
    if crs_result == "completed":
        sir_allan "Well done! You just completed your first CRS enrollment simulation."
        sir_allan "The real CRS works exactly like that. Go to crs.upv.edu.ph when enrollment opens."
        sir_allan "Your pre-enlisted subjects will already be there — you just need to confirm and pay at the Cashier."
        sir_allan "Any questions about what you just saw?"
        menu:
            "What if a subject is closed or full?":
                jump act2_allan_closed_subject
            "What is the difference between pre-enlistment and enrollment?":
                jump act2_allan_preenlist
            "I think I understand now.":
                jump act2_allan_end
    else:
        sir_allan "Take your time. The CRS can be confusing at first but you'll get used to it."
        jump act2_allan_end

label act2_allan_closed_subject:
    sir_allan "If a subject is closed — meaning all slots are taken — you have two options."
    sir_allan "One: wait for the adjustment period. Some students drop subjects, freeing up slots."
    sir_allan "Two: ask your adviser for an overloading permit or a waitlist slot directly from the professor."
    sir_allan "Never just skip the subject and hope for the best. Coordinate with your college."
    jump act2_allan_end

label act2_allan_preenlist:
    sir_allan "Pre-enlistment happens before the official enrollment period."
    sir_allan "You log into CRS and indicate which subjects and sections you want."
    sir_allan "The system then assigns you slots based on availability and priority — freshies and graduating students get priority."
    sir_allan "Enrollment is when you officially confirm those subjects, pay your fees, and get your Form 5."
    sir_allan "Think of pre-enlistment as reserving a seat, and enrollment as actually paying for it."
    jump act2_allan_end

label act2_allan_end:
    sir_allan "You're going to be fine. The first enrollment is always the most confusing."
    sir_allan "My consultation hours are Tuesday and Thursday, 2 PM to 4 PM, Room 201 New Admin. Door's always open."
    $ complete_task("talk_sir_allan")
    window hide
    return

## ============================================================================
## ACT 2 — ENROLLMENT OFFICE ARRIVAL
## ============================================================================
label act2_enrollment_office:
    window show
    narrator_char "(You arrive at the Enrollment Window. A short queue of students waits ahead of you.)"
    narrator_char "(You take a number and wait. This is it — the official start of your UP life.)"
    play sound "task_complete.ogg"
    narrator_char "\[TASK 2 COMPLETE] — Reached the Enrollment Office."
    narrator_char "\[ACT 2 COMPLETE] — BOX 1 and New Admin explored."
    $ complete_task("reach_enrollment")
    $ complete_task("act2_complete")
    window hide
    return

## ============================================================================
## END OF ACT 2 DIALOGUES
## ============================================================================