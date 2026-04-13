## ============================================================================
## ACT 6 DIALOGUES — Student Support Services
## KEY THEME: HSU, GCSU, Scholarship Service
## STORY: Dan is unwell. Player navigates three support offices together.
## INTERACTIVE: Menu choices, inline quiz, breathing exercise, 3 sort mini-games
## ============================================================================

## --- ACT 6 INIT ---
label act6_start:
    jump act6_map

## --- Compatibility stubs ---
label act6_npc_mika:
    window hide
    jump act6_map

label act6_npc_coach_ramon:
    window hide
    jump act6_map

label act6_org_fair:
    window hide
    jump act6_map

## ============================================================================
## ACT 6 MAP — Phase 1: CAS Overworld — Find Dan
## ============================================================================
label act6_map:
    $ current_map_bg = "ace/OW_CAS.png"
    $ act6_nodes = [
        MapNode("dan_cas",   2800, 3200, "act6_npc_dan",
                tooltip="Dan",
                icon_image="caezar.png",
                locked=False,
                icon_zoom=0.10),
        MapNode("go_to_hsu", 2500, 1200, "act6_go_to_hsu",
                tooltip="HSU →",
                icon_image="Arrow.png",
                locked=True,
                icon_zoom=2.0),
    ]
    $ current_task_text = "Find Dan near the CAS corridor"

label act6_cas_loop:
    call screen map_screen("ace/OW_CAS.png", act6_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        scene black
        call walk_to_node(_node, nodes=act6_nodes)
        call expression _node.target_label

        if "talk_dan_cas" in tasks_completed:
            $ act6_nodes[1].locked = False
            $ current_task_text = "Bring Dan to the HSU"

        if "go_to_hsu" in tasks_completed:
            jump act6_hsu_map

    if _action == "phone":
        call phone_check

    if _action == "inventory":
        if inventory_unlocked:
            call screen inventory_screen()

    jump act6_cas_loop


## ============================================================================
## ACT 6 MAP — Phase 2: HSU
## ============================================================================
label act6_hsu_map:
    $ current_map_bg = "ui/hsu_placeholder.png"
    $ player_map_x = 2500
    $ player_map_y = 3200
    $ player_facing = "up"

    $ act6_hsu_nodes = [
        MapNode("enter_hsu", 2500, 1800, "act6_enter_hsu",
                tooltip="Enter HSU",
                icon_image="ArrowUp.png",
                locked=False,
                icon_zoom=2.0),
    ]
    $ current_task_text = "Bring Dan inside the HSU"

label act6_hsu_loop:
    call screen map_screen("ui/hsu_placeholder.png", act6_hsu_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, nodes=act6_hsu_nodes)
        call expression _node.target_label

        if "visit_hsu_annual" in tasks_completed:
            jump act6_osa_map

    if _action == "phone":
        call phone_check

    if _action == "inventory":
        if inventory_unlocked:
            call screen inventory_screen()

    jump act6_hsu_loop


## ============================================================================
## ACT 6 MAP — Phase 3: OSA Corridor — find Ate Jenny
## ============================================================================
label act6_osa_map:
    $ current_map_bg = "maps/OSA.png"
    $ player_map_x = 2500
    $ player_map_y = 3200
    $ player_facing = "up"

    $ act6_osa_nodes = [
        MapNode("ate_jenny_osa", 2500, 2000, "act6_enter_osa",
                tooltip="Ate Jenny",
                icon_image="Osa.png",
                locked=False,
                icon_zoom=0.25),
    ]
    $ current_task_text = "Meet Ate Jenny in the OSA corridor"

label act6_osa_loop:
    call screen map_screen("maps/OSA.png", act6_osa_nodes, current_task_text, 1.0)
    $ _action, _node = _return

    if _action == "walk":
        call walk_to_node(_node, nodes=act6_osa_nodes)
        call expression _node.target_label

        if "talk_ate_jenny" in tasks_completed:
            jump act6_complete

    if _action == "phone":
        call phone_check

    if _action == "inventory":
        if inventory_unlocked:
            call screen inventory_screen()

    jump act6_osa_loop


## ============================================================================
## ACT 6 NAVIGATION NODE LABELS
## ============================================================================
label act6_go_to_hsu:
    $ complete_task("go_to_hsu")
    return

label act6_enter_hsu:
    jump act6_at_hsu

label act6_enter_osa:
    jump act6_corridor_jenny


## ============================================================================
## SCENE 1 — Find Dan (CAS Corridor)
## INTERACTIVE: Player chooses how to approach Dan
## ============================================================================
label act6_npc_dan:
    window show
    narrator_char "(Dan is on a bench near the water fountain. Pale. Hunched. Staring at nothing.)"
    player_char "Dan."
    dan "Oh. Hey."
    player_char "You look terrible."
    dan "I'm fine."

    menu:
        "You're getting checked out. Right now.":
            jump act6_dan_direct
        "When did you last eat?":
            jump act6_dan_gentle
        "You don't look fine. Talk to me.":
            jump act6_dan_talk

label act6_dan_direct:
    dan "It's not that serious—"
    player_char "You're gray and you can barely sit straight. It's that serious."
    dan "..."
    dan "Okay."
    jump act6_dan_convinced

label act6_dan_gentle:
    dan "..."
    dan "Yesterday. I think."
    player_char "You think."
    dan "Maybe the day before."
    player_char "HSU. Now."
    dan "I don't want to make it a big deal."
    player_char "Not eating for two days IS the big deal."
    jump act6_dan_convinced

label act6_dan_talk:
    dan "I just haven't been sleeping. Or eating much."
    dan "My parents couldn't send my allowance. I didn't want anyone to know."
    player_char "Dan. That's what the campus clinics are for. Come on."
    jump act6_dan_convinced

label act6_dan_convinced:
    narrator_char "(He doesn't argue. That tells you everything.)"
    $ complete_task("talk_dan_cas")
    window hide
    return


## ============================================================================
## SCENE 2 — HSU Visit
## INTERACTIVE: Menu-driven consultation + sq_hsu_triage sort game
## ============================================================================
label act6_at_hsu:
    window show
    narrator_char "(The Health Services Unit. Green cross above the door. A nurse logs Dan in before he even finishes handing over his ID.)"
    hsu_nurse "Student ID. Sit. When did you last eat?"
    dan "Day before yesterday."
    hsu_nurse "Blood pressure's low. You're dehydrated and hypoglycemic."
    narrator_char "(The physician steps out and looks at the chart, then at Dan.)"
    physician "This has been going on how long?"
    dan "A week."
    physician "And you waited because...?"
    dan "I thought I could get through it."
    narrator_char "(She sets down her pen. Looks at you.)"
    physician "You have questions. Ask them."

    $ act6_hsu_asked = []

label act6_hsu_question_loop:
    menu:
        "What can the HSU actually treat on campus?" if "treat" not in act6_hsu_asked:
            $ act6_hsu_asked.append("treat")
            jump act6_hsu_q_treat
        "What if it's something more serious?" if "serious" not in act6_hsu_asked:
            $ act6_hsu_asked.append("serious")
            jump act6_hsu_q_serious
        "What's the Annual Physical Exam?" if "ape" not in act6_hsu_asked:
            $ act6_hsu_asked.append("ape")
            jump act6_hsu_q_ape
        "That's enough. What happens next?":
            jump act6_hsu_next

label act6_hsu_q_treat:
    physician "Consultations, medicines, wound care, dental extraction, vitamins, ORS — all free with your student ID."
    physician "We also issue Medical Certificates if you miss class due to illness."
    jump act6_hsu_question_loop

label act6_hsu_q_serious:
    physician "We refer. Miagao District Hospital for emergencies. WVMC in Iloilo City for specialists."
    physician "You are never left to navigate that alone — we write the referral letter and coordinate."
    jump act6_hsu_question_loop

label act6_hsu_q_ape:
    physician "Required for your enrollment clearance every year. Height, weight, blood pressure, vision, general screening."
    physician "Done here, free of charge. Don't skip it — it flags issues before they become crises. Like this one."
    jump act6_hsu_question_loop

label act6_hsu_next:
    physician "I'm treating the immediate problem — ORS, glucose drink, vitamin B complex."
    physician "But the root cause is financial stress. I'm writing a referral to the GCSU."
    dan "I don't need a counselor—"
    physician "You haven't eaten in two days because you have no money. That is not a personal failing. That is a circumstance the GCSU can help address."
    dan "...Okay."
    narrator_char "(She hands over the medication pack and the referral envelope.)"
    physician "Before you go — let me make sure you know how to use the HSU correctly."
    narrator_char "(Encyclopedia unlocked: HSU — Health Services Unit.)"
    $ persistent.encyclopedia_unlocks.add("hsu_ape")

    ## ── Sort mini-game: Campus Health Triage ──────────────────────────────────
    if "sq_hsu_triage" not in subquests_completed:
        jump sq_hsu_triage
    else:
        physician "Good. The HSU is your first stop — not your last resort."

    $ complete_task("visit_hsu_annual")
    window hide
    return


## ============================================================================
## SCENE 3 — OSA Corridor (Ate Jenny)
## INTERACTIVE: Player asks about confidentiality or OSA role
## ============================================================================
label act6_corridor_jenny:
    window show
    narrator_char "(Outside the HSU. Dan's got his glucose drink. A little color back in his face.)"
    narrator_char "(Ate Jenny is posting announcements on the OSA bulletin board. She spots you.)"
    ate_jenny "Dan — from the freshman batch?"
    dan "Yeah."
    ate_jenny "GCSU referral?"
    narrator_char "(Dan holds up the envelope.)"
    ate_jenny "Good. I'm Ate Jenny, Office of Student Affairs. Walk with me."
    ate_jenny "Three offices. HSU — physical. GCSU — mental and emotional. Scholarship Service — financial."
    ate_jenny "These three problems are connected. You can't fix one while ignoring the others."
    player_char "Dan's worried about confidentiality."

    menu:
        "Is the GCSU session actually private?":
            jump act6_jenny_confidentiality
        "What exactly does the OSA do?":
            jump act6_jenny_osa_role
        "Can a counselor contact his parents?":
            jump act6_jenny_parents

label act6_jenny_confidentiality:
    ate_jenny "Protected under Republic Act 9258 — the Guidance and Counseling Act of 2004."
    ate_jenny "Nothing leaves that room without your written consent. Professors, parents, the dean — nobody."
    ate_jenny "The only exceptions: imminent harm to yourself or others, or a court order."
    jump act6_jenny_continue

label act6_jenny_osa_role:
    ate_jenny "We're the coordinating hub. If you don't know which office handles your problem, you come here first."
    ate_jenny "We also handle student org registration, activity permits, and student welfare cases."
    ate_jenny "Think of us as the router. We direct you to the right place."
    jump act6_jenny_continue

label act6_jenny_parents:
    ate_jenny "The law says no. RA 9258 means the counselor cannot disclose anything to anyone without your written consent."
    ate_jenny "Dan is the client. The counselor is on his side."
    dan "Even if I'm a minor?"
    ate_jenny "Even then. The law is clear."
    jump act6_jenny_continue

label act6_jenny_continue:
    narrator_char "(She stops at the GCSU door and holds it open.)"
    ate_jenny "Ma'am Garcia. She's been here twelve years. Just be honest with her."
    ate_jenny "My door's always open after."
    $ complete_task("talk_ate_jenny")
    jump act6_at_gcsu


## ============================================================================
## SCENE 4 — GCSU Counseling Session
## INTERACTIVE: Player helps Dan open up + inline GCSU quiz + breathing exercise
## ============================================================================
label act6_at_gcsu:
    window show
    narrator_char "(The GCSU. Calm lighting. Plants on the windowsill. Ma'am Garcia closes her notebook.)"
    guidance_counselor "Come in. Take a seat. I'm Ma'am Garcia."
    guidance_counselor "No rush. Start wherever you want."
    narrator_char "(Dan looks at the floor. He's still holding the referral.)"
    guidance_counselor "You look like you have a lot on your mind. What's the biggest thing right now?"

    menu:
        "Tell her about the not eating.":
            jump act6_gcsu_physical
        "Tell her about the money situation.":
            jump act6_gcsu_financial
        "Tell her everything.":
            jump act6_gcsu_everything

label act6_gcsu_physical:
    dan "I've been... not eating properly. For about a week."
    guidance_counselor "And before the food — what was happening?"
    dan "I can't sleep. I keep thinking about whether I should just go home."
    guidance_counselor "What's pulling you home?"
    jump act6_gcsu_core

label act6_gcsu_financial:
    dan "My parents can't send my allowance. Probably not next month either."
    guidance_counselor "How long have you been carrying that alone?"
    dan "Since the semester started."
    guidance_counselor "That's a long time to go without telling anyone."
    jump act6_gcsu_core

label act6_gcsu_everything:
    dan "I haven't eaten in two days. My parents have no money to send. I can't sleep. I zone out in class."
    dan "I keep thinking I don't belong here."
    guidance_counselor "Thank you for saying all of that at once. That takes courage."
    jump act6_gcsu_core

label act6_gcsu_core:
    guidance_counselor "What you're describing — the exhaustion, the isolation, the feeling of being behind — that's adjustment difficulty."
    guidance_counselor "It's the most common thing I see in first-semester freshmen. You are not unusual. You are not weak."
    guidance_counselor "The UPCAT doesn't make mistakes. You earned your place here."
    dan "It doesn't feel that way right now."
    guidance_counselor "It rarely does in the first month."
    guidance_counselor "And people come here for more than crisis support. Study habits, time management — why you freeze before exams even when you studied."
    guidance_counselor "If the TLRC helps you with the paper, we help with why you can't start the paper."
    guidance_counselor "Academic counseling is part of what we do. Not just when something breaks — but before it does."
    guidance_counselor "Let's try something. Follow my lead."

    ## ── Breathing exercise ────────────────────────────────────────────────────
    window hide
    call screen breathing_exercise_screen
    window show

    guidance_counselor "Good. Now — let me make sure you both know what this office actually provides."
    guidance_counselor "Quick check — three questions."

    ## ── Inline GCSU knowledge quiz ────────────────────────────────────────────
    python:
        sq_quiz_state.setup(
            "GCSU — Know Your Rights",
            "Three questions about the Guidance and Counseling Services Unit",
            "💙",
            [
                (
                    "Under RA 9258, can Ma'am Garcia tell Dan's parents about this session?",
                    [
                        ("No — only if there is imminent harm or a court order", True, "Correct. RA 9258 protects everything said in this room. Parents, professors, the dean — none of them have access without Dan's written consent."),
                        ("Yes — parents are legal guardians and have the right to know", False, "RA 9258 is clear: the student is the client. Guardian rights do not override the confidentiality of counseling sessions."),
                        ("Yes, but only if Dan is failing academically", False, "Academic performance is not an exception under RA 9258. The law protects counseling disclosures regardless of grades."),
                    ]
                ),
                (
                    "Which of these is NOT a GCSU service?",
                    [
                        ("Annual Physical Examination (APE)", True, "Correct — the APE is an HSU service. The GCSU handles counseling, psychological testing, career guidance, and crisis intervention."),
                        ("Individual Counseling sessions", False, "Individual Counseling is one of the GCSU's core services — one-on-one, confidential, free for enrolled students."),
                        ("Crisis Intervention for students in acute distress", False, "Crisis Intervention is a GCSU service. They also coordinate referrals to licensed psychiatrists in Iloilo."),
                    ]
                ),
                (
                    "Dan skips his follow-up GCSU session. What happens?",
                    [
                        ("Nothing is enforced — counseling is voluntary, but the door stays open", True, "Exactly. The GCSU cannot compel attendance. The invitation stays open. Showing up again is always an option."),
                        ("It gets flagged on his academic record", False, "GCSU sessions are confidential. Attendance or absence does not appear on any academic record."),
                        ("His scholarship application gets blocked", False, "GCSU attendance has no connection to scholarship processing. These offices coordinate, but they don't penalize non-attendance."),
                    ]
                ),
            ]
        )
    window hide
    call screen sq_quiz_game()
    $ _gcsu_quiz = _return
    window show

    if _gcsu_quiz >= 2:
        guidance_counselor "Good. You know your rights. That matters."
    else:
        guidance_counselor "Review what you missed. Knowing what this office can and cannot do — that's part of using it correctly."

    guidance_counselor "One more thing before the referral. The Peer Facilitators Program — it runs under this office."
    guidance_counselor "Trained student volunteers. They lead group sessions: journaling, coping workshops, reflection circles."
    guidance_counselor "Not therapy. But the kind of peer support that makes walking through that door feel less impossible."
    guidance_counselor "Check the bulletin board outside. The schedule is posted every semester."
    guidance_counselor "Dan — I'm writing a referral to the Scholarship Service. GCSU-referred cases are prioritized."
    guidance_counselor "Come back after. Not because something is wrong with you. Because adjustment is a process."
    dan "...Yes, Ma'am."
    narrator_char "(She hands Dan a small card.)"
    guidance_counselor "Two ways to reach us: walk-in, Mon–Fri 8AM–5PM — no appointment needed, just come."
    guidance_counselor "Or pre-schedule through the GCSU office to get a specific time slot with less waiting."
    guidance_counselor "For crisis visits, walk-ins are always prioritized. For ongoing sessions, scheduling helps."
    dan "I didn't know you could just walk in."
    guidance_counselor "Most students don't find out until it's too late. Now you know."
    narrator_char "(Encyclopedia unlocked: GCSU — Guidance and Counseling Services Unit.)"
    $ persistent.encyclopedia_unlocks.add("gcsu")
    $ complete_task("talk_dan_gcsu")

    if "sq_gcsu_services" not in subquests_completed:
        jump sq_gcsu_services
    else:
        guidance_counselor "You already know what this office offers. Use it."

    jump act6_at_scholarship


## ============================================================================
## SCENE 5 — Scholarship Service
## INTERACTIVE: Menu-driven consultation + sq_stfap_docs sort game
## ============================================================================
label act6_at_scholarship:
    window show
    narrator_char "(New Admin Building. Bulletin boards dense with scholarship deadlines and STFAP notices.)"
    narrator_char "(Kuya Tomas reads the GCSU referral. Sets it face-down. Opens a folder.)"
    kuya_tomas "Flagged urgent. Sit down."
    kuya_tomas "Three things that can help you. Ask me about whichever one you need first."

    $ act6_scholarship_asked = []

label act6_scholarship_loop:
    menu:
        "Emergency Assistance Fund" if "emergency" not in act6_scholarship_asked:
            $ act6_scholarship_asked.append("emergency")
            jump act6_schol_emergency
        "STFAP re-bracketing" if "stfap" not in act6_scholarship_asked:
            $ act6_scholarship_asked.append("stfap")
            jump act6_schol_stfap
        "Scholarships with stipends" if "scholarships" not in act6_scholarship_asked:
            $ act6_scholarship_asked.append("scholarships")
            jump act6_schol_scholarships
        "What do we do right now?":
            jump act6_schol_action

label act6_schol_emergency:
    kuya_tomas "Student Emergency Assistance Fund. Covers immediate needs — meals, photocopying, basic transport."
    kuya_tomas "Maximum ₱1,500 per application. Processing: 24 to 48 hours."
    kuya_tomas "GCSU-referred cases — like yours — get prioritized. You could have something by end of week."
    dan "That would get me through this."
    jump act6_scholarship_loop

label act6_schol_stfap:
    kuya_tomas "STFAP — Socialized Tuition and Financial Assistance Program. UP's equity mechanism."
    kuya_tomas "Brackets A down to E9. Lower brackets mean reduced tuition. E5 to E9 also include a monthly living allowance — ₱1,000 to ₱4,000."
    player_char "So lower-bracket students get money every month?"
    kuya_tomas "Yes. That's the financial assistance component. Not just tuition — actual living support."
    kuya_tomas "If your family's situation changed since you enrolled, you can request re-bracketing."
    player_char "Is STFAP the only part of the system, or is there something bigger?"
    kuya_tomas "SLAS — Student Learning Assistance System. That is the full framework."
    kuya_tomas "STFAP is the bracketing mechanism inside SLAS. But SLAS also coordinates how the university identifies students who need financial, academic, and welfare intervention."
    kuya_tomas "The Scholarship Office, the GCSU, and the HSU all feed into SLAS. A student flagged for financial difficulty gets routed through it automatically."
    player_char "So the GCSU referral to you just now — that was SLAS in action."
    kuya_tomas "Exactly. You just watched the system work."
    narrator_char "(Encyclopedia unlocked: SLAS — Student Learning Assistance System.)"
    $ persistent.encyclopedia_unlocks.add("slas")
    jump act6_scholarship_loop

label act6_schol_scholarships:
    kuya_tomas "University Scholar — GWA of 1.20 or better. Full tuition and miscellaneous fee exemption. Automatic, no application."
    kuya_tomas "DOST-SEI — for STEM students. Full tuition plus ₱7,000 monthly stipend."
    kuya_tomas "CHED Merit — based on entrance scores. Full tuition and allowance."
    kuya_tomas "TES — Tertiary Education Subsidy. This is not a UP program. It comes from CHED under Republic Act 10931."
    kuya_tomas "It covers full tuition and school fees, plus a monthly allowance calibrated to financial need. You apply through CHED's portal — we certify your enrollment here."
    kuya_tomas "GIAP — Grants-in-Aid Program. This is a UP System grant. A monthly cash allowance specifically for low-income undergraduates."
    kuya_tomas "Separate from STFAP. You apply here at the Scholarship Office each semester."
    dan "So STFAP reduces tuition, TES covers tuition and gives an allowance, and GIAP gives a monthly allowance on top?"
    kuya_tomas "All three address different parts of the same problem. A student can receive all three — they are not mutually exclusive."
    kuya_tomas "The mistake students make is waiting too long to ask. Deadlines are absolute."
    narrator_char "(Encyclopedia unlocked: Scholarship Service — TES and GIAP added.)"
    $ persistent.encyclopedia_unlocks.add("tes_giap")
    kuya_tomas "UPV Foundation scholarships — mix of need-based and merit-based. Applications open each semester."
    dan "Some of these give ₱3,000 a month?"
    kuya_tomas "Some give more. Maintain your GWA and watch this bulletin board. Deadlines are absolute."
    jump act6_scholarship_loop

label act6_schol_action:
    kuya_tomas "Emergency Fund form — fill it out now. I'll flag it."
    narrator_char "(Dan picks up the pen. His handwriting is small and careful.)"
    kuya_tomas "Students always think there's nothing they can do. That's the most common thing I hear in this office."
    kuya_tomas "UP has been doing this for a hundred years. No Filipino should be denied education because of poverty."
    kuya_tomas "STFAP, the emergency fund, the scholarships — that's the mechanism. You just have to find the door."
    narrator_char "(Dan sets the pen down. Form complete.)"
    narrator_char "(Encyclopedia unlocked: Scholarship Service — STFAP & Financial Assistance.)"
    $ persistent.encyclopedia_unlocks.add("scholarship_service")
    $ complete_task("talk_kuya_tomas")

    ## ── Sort mini-game: Documents Checklist ──────────────────────────────────
    if "sq_stfap_docs" not in subquests_completed:
        jump sq_stfap_docs
    else:
        kuya_tomas "Keep your document folder ready. Deadlines wait for no one."

    if "sq_financial_assistance" not in subquests_completed:
        jump sq_financial_assistance
    else:
        kuya_tomas "TES, GIAP, STFAP — three different instruments. Use all of them."

    jump act6_dan_resolution


## ============================================================================
## SCENE 6 — Resolution (Outside New Admin)
## INTERACTIVE: Dan quizzes player → sq_support_router sort game
## ============================================================================
label act6_dan_resolution:
    window show
    narrator_char "(Outside the New Admin Building. Late afternoon. Campus has gone quiet.)"
    dan "That was... a lot."
    player_char "How do you feel?"
    dan "Tired. But lighter."
    player_char "You know where to go now."
    dan "HSU for the body. GCSU for the mind. Scholarship Service for the money. Three offices."
    dan "I didn't know any of them existed two hours ago."
    player_char "Now you do. And you know which one to hit first for any problem."
    dan "Hey. You didn't have to do any of this."
    player_char "You looked like you needed someone to say 'let's go.' So I said it."
    dan "..."
    dan "Thank you."
    narrator_char "(He almost smiles. It's small — but it's real.)"

    ## ── Sort mini-game: Which Support Office? ────────────────────────────────
    if "sq_support_router" not in subquests_completed:
        jump sq_support_router
    else:
        player_char "(HSU. GCSU. Scholarship Service. OSA. You know the map now.)"

    window hide
    jump act6_complete


## ============================================================================
## ACT 6 COMPLETE
## ============================================================================
label act6_complete:
    scene black
    call screen act_transition("ACT 6 COMPLETE",
        "Dan is no longer alone.\nYou know the three offices now.", "complete")
    call screen act_transition("ACT 7", "Library & Academic Resources", "intro")

    $ current_act = 7
    $ player_map_x = 2500
    $ player_map_y = 2600
    $ player_facing = "up"
    jump act7_map

## ============================================================================
## END OF ACT 6 DIALOGUES
## ============================================================================
play music "audio/Act7.mp3" fadein 1.0
