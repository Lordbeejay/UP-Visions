## ============================================================================
## SUBQUESTS — Optional bonus quests tied to UPV culture, handbook & services
## Reference: UP Visayas Student Handbook, UP Academic Information Bulletin
##
## Each subquest uses one of 4 interactive mini-game screens:
##   sq_quiz_game()      — 3-question multiple choice (returns score int)
##   sq_sort_game()      — click-to-categorize card sort (returns "completed"/"skip")
##   sq_timeline_game()  — chronological event ordering (returns score int)
##   sq_gwa_calc_game()  — UP grade cycling / GWA explorer (returns "completed"/"partial")
##
## Indentation rule: ALL indents must be multiples of 4 spaces.
## ============================================================================


## ============================================================================
## ACT 1 — SUBQUEST A: "The Oblation and the Iskolar ng Bayan"
## Trigger: Jaden's dialogue  |  Game: Quiz
## ============================================================================
label sq_oblation:
    window show
    jaden "Alright — quick challenge before you go. You know the Oblation statue?"
    jaden "Every UP student should know what it is, who made it, and why it matters."
    python:
        sq_quiz_state.setup(
            "The Oblation & Iskolar ng Bayan",
            "Jaden challenges your UP identity knowledge",
            "🗿",
            [
                (
                    "Who sculpted the Oblation statue?",
                    [
                        ("Guillermo Tolentino", True, "Correct! Tolentino created the Oblation in 1935. He also sculpted the Bonifacio Monument."),
                        ("Fernando Amorsolo", False, "Amorsolo was a painter — National Artist for Painting. The Oblation sculptor was Guillermo Tolentino."),
                        ("Napoleon Abueva", False, "Abueva is the National Artist for Sculpture, but the Oblation was created by Guillermo Tolentino in 1935."),
                    ]
                ),
                (
                    "What does the Oblation symbolize?",
                    [
                        ("The Filipino youth offering themselves in service to the nation", True, "Exactly. The outstretched arms represent selfless dedication to the Filipino people — not to a party or a person."),
                        ("Academic excellence and scholastic honor", False, "Those are UP values, but the Oblation symbolizes service and sacrifice — the offering of oneself for the nation."),
                        ("Freedom from colonial rule and independence", False, "It carries that spirit, but the Oblation specifically represents the youth's offering of themselves in service."),
                    ]
                ),
                (
                    "What does 'Iskolar ng Bayan' mean — and why does it matter at UP?",
                    [
                        ("Scholar of the Nation — UP students are publicly funded and owe their education in service to the Filipino people", True, "That is the heart of it. The taxes of ordinary Filipinos fund your education. That creates a moral obligation — not just to graduate, but to serve."),
                        ("A scholarship award given to the top 10 students in each college batch", False, "Iskolar ng Bayan is not a prize — it is the identity of every enrolled UP student. The Filipino people are paying for your education."),
                        ("A government subsidy program that lowers tuition through STFAP", False, "STFAP is one part of it, but Iskolar ng Bayan is the identity and obligation of every UP student as a public scholar."),
                    ]
                ),
            ]
        )
    window hide
    call screen sq_quiz_game()
    $ _sq_result = _return
    window show
    if _sq_result >= 2:
        jaden "That's the foundation. You understand where you are and why."
        jaden "When things get hard — look at the Oblation. You're not just studying for yourself."
    else:
        jaden "Keep that in mind going forward. The Oblation isn't just decoration."
    $ collect_item(ITEM_OBLATION_PLEDGE)
    show screen item_pickup_screen(ITEM_OBLATION_PLEDGE)
    pause 2.5
    hide screen item_pickup_screen
    $ persistent.encyclopedia_unlocks.add("the_oblation_sq")
    $ complete_subquest("sq_oblation")
    window hide
    return


## ============================================================================
## ACT 1 — SUBQUEST B: "Miagao Heritage Deep Dive"
## Trigger: Manong Josh's dialogue  |  Game: Timeline
## ============================================================================
label sq_miagao_heritage:
    window show
    manong_josh "You want to understand this place? Arrange its history. Earliest to latest."
    manong_josh "Five moments. Put them in order."
    python:
        sq_timeline_state.setup(
            [
                (1787, "Church Construction Begins", "Spanish colonial authorities begin building Miagao Church — a fortress church to defend against Moro raids.", "#8B4513"),
                (1797, "Miagao Church Completed", "After ten years of labor by the local community, the baroque church is completed with its unique Filipino motifs.", "#CD853F"),
                (1947, "UPV Founded as College of Fisheries", "The UP College of Fisheries is established in Iloilo. Marine science becomes UPV's founding identity.", "#2a5c2a"),
                (1979, "UPV Becomes a Constituent University", "The campus is elevated from a college to a full constituent university of the UP System under reorganization.", "#2a2a5c"),
                (1993, "UNESCO World Heritage Site", "Miagao Church is declared a UNESCO World Heritage Site — one of four Philippine baroque churches recognized.", "#5c2a5c"),
            ]
        )
    window hide
    call screen sq_timeline_game()
    $ _sq_result = _return
    window show
    if _sq_result >= 4:
        manong_josh "You have the history right. Now you know what you're standing next to."
    elif _sq_result >= 2:
        manong_josh "Almost right. But you know more than when you started. This place has layers."
    else:
        manong_josh "The order matters. History is not random. Read it again someday."
    $ collect_item(ITEM_MIAGAO_HERITAGE)
    show screen item_pickup_screen(ITEM_MIAGAO_HERITAGE)
    pause 2.5
    hide screen item_pickup_screen
    $ persistent.encyclopedia_unlocks.add("miagao_heritage_sq")
    $ complete_subquest("sq_miagao_heritage")
    window hide
    return


## ============================================================================
## ACT 2 — SUBQUEST A: "UP Jargon Decoder"
## Trigger: Ate Bea's dialogue  |  Game: Quiz
## ============================================================================
label sq_up_jargon:
    window show
    ate_bea "Before you go — let me make sure you speak the language. UP has its own vocabulary."
    ate_bea "You'll see these terms on grade reports and official documents. Three questions."
    python:
        sq_quiz_state.setup(
            "UP Academic Jargon",
            "Ate Bea tests your UP vocabulary",
            "📘",
            [
                (
                    "What does 'DRP' mean on an official grade report?",
                    [
                        ("Dropped — the student officially withdrew from the course before the deadline", True, "Correct. A DRP means you filed a dropping form before the midterm deadline. It does not count as a failing grade."),
                        ("Deferred — the grade is pending submission of additional requirements", False, "That describes an INC (Incomplete). DRP means the student formally dropped the course before the dropping deadline."),
                        ("Disqualified — the student failed for disciplinary reasons", False, "Disciplinary matters are handled separately through the OSA. DRP is simply a voluntary course drop filed before the deadline."),
                    ]
                ),
                (
                    "What is an 'INC' grade — and what happens if you don't complete it within one year?",
                    [
                        ("Incomplete — you have unfinished requirements. If not completed within one academic year, it becomes a permanent 5.0", True, "Exactly right. INC means you missed a specific requirement but your professor gave you a chance to complete it. One year — then it becomes 5.0 permanently."),
                        ("Incomplete — you must retake the entire course the following semester", False, "With an INC, you only need to complete the MISSING requirement. But ignore it for a year and it becomes a permanent 5.0."),
                        ("In-progress — the grade will be updated once final exams are graded", False, "INC means Incomplete — your professor already graded the final, but you are missing a specific requirement."),
                    ]
                ),
                (
                    "What is a 'LOA' and when might a student need one?",
                    [
                        ("Leave of Absence — a formal one-semester pause in enrollment, approved by the college", True, "Correct. LOA is not quitting — it is an official academic pause for health, family emergencies, or financial difficulty. You remain a UP student and return the following semester."),
                        ("Late Official Addition — adding a subject after the regular enlistment period has closed", False, "Adding a subject late is done during the adjustment period through CRS. LOA means Leave of Absence — a semester-long break from enrollment."),
                        ("Level of Achievement — a grade classification above the Dean's List distinction", False, "LOA is Leave of Absence — when a student takes a formal semester off from enrollment with official college approval."),
                    ]
                ),
            ]
        )
    window hide
    call screen sq_quiz_game()
    $ _sq_result = _return
    window show
    if _sq_result >= 2:
        ate_bea "You passed UP Jargon 101. These terms could save your academic record someday."
    else:
        ate_bea "Knowing these now is better than learning them the hard way at the Registrar's window."
    $ collect_item(ITEM_UP_JARGON)
    show screen item_pickup_screen(ITEM_UP_JARGON)
    pause 2.5
    hide screen item_pickup_screen
    $ persistent.encyclopedia_unlocks.add("up_jargon_sq")
    $ complete_subquest("sq_up_jargon")
    window hide
    return


## ============================================================================
## ACT 2 — SUBQUEST B: "Know Your Rights"
## Trigger: Kuya Mark's dialogue  |  Game: Quiz
## ============================================================================
label sq_student_rights:
    window show
    kuya_mark "You look like you actually want to learn. Good. Do you know your rights as a UP student?"
    kuya_mark "Three scenarios. Answer carefully."
    python:
        sq_quiz_state.setup(
            "UP Student Rights",
            "Kuya Mark tests your handbook knowledge",
            "⚖️",
            [
                (
                    "A student has the 'right to quality education.' What does this mean in practical terms?",
                    [
                        ("Professors must follow the syllabus, give adequate feedback, and meet classes as scheduled", True, "Correct. The right to quality education means professors have obligations too. If a professor consistently misses class or grades unfairly, you can file a concern with the OSA."),
                        ("Students can demand easy exams and automatic extensions whenever they want", False, "The right is to QUALITY — not to ease. It means fair, consistent, professional instruction — not lowered standards on demand."),
                        ("The university must provide free textbooks and materials for all courses", False, "That is a resource matter, not a right per se. The right to quality education means instruction standards — not material provision."),
                    ]
                ),
                (
                    "You believe a professor gave you an unfairly low grade. What is the correct procedure?",
                    [
                        ("Request a consultation with the professor, then escalate to the Department Chair if unresolved, then to the Dean", True, "Exactly the correct procedure. Start with the professor. If that fails, the Department Chair. Then the Dean. Document everything — keep copies of your work and all correspondence."),
                        ("Immediately file a formal complaint with the OSA and demand a grade change", False, "That skips several steps. OSA handles student welfare issues, not grade disputes directly. Begin with the professor and work up the proper chain."),
                        ("Accept it — professors always have final say over all grades without exception", False, "While professors have academic freedom, they also have professional obligations. An unjust grade CAN be challenged through proper channels."),
                    ]
                ),
                (
                    "Does the university's right to discipline students have any limits?",
                    [
                        ("Yes — disciplinary proceedings must follow due process: the student must be informed of charges and given a chance to respond", True, "Correct. Even in cases of clear misconduct, UP must follow due process. You have the right to be heard, to see the evidence, to have representation, and to appeal any decision."),
                        ("No — the university can suspend or expel any student for any reason it considers appropriate", False, "Absolutely not. UP is bound by due process. Arbitrary punishment without proper procedure is a direct violation of student rights."),
                        ("Only if the student is paying full tuition — STFAP students have reduced procedural rights", False, "Rights apply equally to ALL enrolled students regardless of financial bracket or scholarship status."),
                    ]
                ),
            ]
        )
    window hide
    call screen sq_quiz_game()
    $ _sq_result = _return
    window show
    if _sq_result >= 2:
        kuya_mark "Good. A student who knows their rights is harder to mistreat — and harder to fool."
    else:
        kuya_mark "Read Section 3 of the UP Student Handbook when you get the chance. These rights protect you."
    $ collect_item(ITEM_STUDENT_RIGHTS)
    show screen item_pickup_screen(ITEM_STUDENT_RIGHTS)
    pause 2.5
    hide screen item_pickup_screen
    $ persistent.encyclopedia_unlocks.add("student_rights_sq")
    $ complete_subquest("sq_student_rights")
    window hide
    return


## ============================================================================
## ACT 3 — SUBQUEST A: "CRS Battle Strategy"
## Trigger: Sir Noel's dialogue  |  Game: Quiz
## ============================================================================
label sq_crs_tactics:
    window show
    sir_noel "One more thing. CRS isn't just a system — it is a skill. Three scenarios. Answer correctly."
    python:
        sq_quiz_state.setup(
            "CRS Battle Strategy",
            "Sir Noel tests your enlistment tactics",
            "💻",
            [
                (
                    "CRS enlistment opens at 8 AM. You log in at 8:02 and your top choice is already full. What do you do?",
                    [
                        ("Immediately enlist in your backup class, then check for openings during the adjustment period", True, "Correct strategy. Always have backup classes prepared. The adjustment period sometimes opens slots when other students drop."),
                        ("Wait for the professor to increase the class limit — they usually do eventually", False, "Sometimes professors increase limits, but you cannot count on it. Enlist in your backup first."),
                        ("Email the Registrar to request a forced override into the full class", False, "Overrides are only approved in specific cases — usually graduating students needing a subject to complete requirements."),
                    ]
                ),
                (
                    "You accidentally enlisted in the wrong section of the same subject — different professor. Best move?",
                    [
                        ("Use the add/drop adjustment period to switch to the correct section before the deadline", True, "Exactly. The adjustment period lets you add, drop, or switch sections. Act quickly — slots in your preferred section may fill up."),
                        ("Attend the wrong section anyway — professors rarely check the official class list", False, "They do check. Attending a class you are not officially enlisted in is irregular. You will not receive a grade."),
                        ("File a concern with the Registrar to automatically reassign you to the correct section", False, "The Registrar does not reassign students automatically. You must handle the switch yourself during the adjustment period."),
                    ]
                ),
                (
                    "You missed a prerequisite subject this semester. Can you take the upper-level course that requires it?",
                    [
                        ("No — take the prerequisite next semester. You cannot take the upper-level course without completing it first", True, "Correct. Prerequisites exist for a reason. CRS will block enrollment in the upper-level course. Plan your curriculum map from day one."),
                        ("Petition the professor of the upper-level course to waive the prerequisite requirement", False, "This is possible in exceptional cases but rarely approved for freshmen. The standard answer is: take the prerequisite first."),
                        ("Enlist in both simultaneously to complete them at the same time and save a semester", False, "CRS will block you from enlisting in the upper-level course if the prerequisite has not been completed. The system enforces this."),
                    ]
                ),
            ]
        )
    window hide
    call screen sq_quiz_game()
    $ _sq_result = _return
    window show
    if _sq_result >= 2:
        sir_noel "You're ready. You just need a fast internet connection on enlistment day."
    else:
        sir_noel "Review your answers. CRS season comes twice a year — be ready for it."
    $ collect_item(ITEM_CRS_TACTICS)
    show screen item_pickup_screen(ITEM_CRS_TACTICS)
    pause 2.5
    hide screen item_pickup_screen
    $ complete_subquest("sq_crs_tactics")
    window hide
    return


## ============================================================================
## ACT 3 — SUBQUEST B: "Academic Load Mastery"
## Trigger: Sir Noel's dialogue  |  Game: Quiz
## ============================================================================
label sq_academic_load:
    window show
    sir_noel "Before you go — one more critical area. How much is too much? How much is too little?"
    python:
        sq_quiz_state.setup(
            "Academic Load Mastery",
            "Sir Noel tests your load and NSTP knowledge",
            "📚",
            [
                (
                    "What is the standard full academic load for an undergraduate student per semester?",
                    [
                        ("15 to 18 units, with a maximum of 21 units for students in good standing with dean approval", True, "That is the standard range. 18 units is comfortable for most students. Going above 18 requires dean approval and a clean academic record."),
                        ("24 units per semester — more subjects means faster graduation", False, "24 units is an extreme overload requiring special approval. More subjects at once means more risk of failing all of them."),
                        ("10 to 12 units — UP is hard, so you should take as few subjects as possible", False, "Under 15 units is considered part-time enrollment. Many scholarships require a full load."),
                    ]
                ),
                (
                    "What is NSTP — and is it required for all first-year students?",
                    [
                        ("National Service Training Program — 3 units per semester for 2 semesters, required for all first-year college students", True, "Correct. NSTP options: CWTS or LTS. You choose one. Both fulfill the requirement. It is a government mandate under RA 9163."),
                        ("A physical education requirement — one semester of military drills and training", False, "You are thinking of ROTC, which is one NSTP option — but CWTS and LTS are more common at UPV. NSTP is not purely military."),
                        ("An optional enrichment program for students interested in community service activities", False, "NSTP is not optional. It is required by Republic Act 9163 for all first and second year students in higher education."),
                    ]
                ),
                (
                    "What happens if a student's GWA drops below 2.00 for two consecutive semesters?",
                    [
                        ("The student may be placed on academic probation — required to reduce load and seek academic counseling", True, "Correct in principle. Consistent underperformance triggers academic intervention. Continued poor performance can lead to dismissal. UP enforces academic standards seriously."),
                        ("Nothing — grades are a personal matter and the university does not intervene in academic performance", False, "That is not how UP works. The university has obligations to both the student and to the quality of its degrees."),
                        ("The student is automatically shifted to a different degree program with lower academic requirements", False, "Shifting is a voluntary process initiated by the student with the Dean's approval. It is not automatic."),
                    ]
                ),
            ]
        )
    window hide
    call screen sq_quiz_game()
    $ _sq_result = _return
    window show
    if _sq_result >= 2:
        sir_noel "Good. You understand the system. Now build your four-year curriculum map accordingly."
    else:
        sir_noel "Review your curriculum map and your college's academic regulations. The Registrar can provide a copy."
    $ collect_item(ITEM_ACADEMIC_LOAD)
    show screen item_pickup_screen(ITEM_ACADEMIC_LOAD)
    pause 2.5
    hide screen item_pickup_screen
    $ complete_subquest("sq_academic_load")
    window hide
    return


## ============================================================================
## ACT 4 — SUBQUEST A: "Dorm Code of Conduct"
## Trigger: Dorm Manager's dialogue  |  Game: Quiz
## ============================================================================
label sq_dorm_code:
    window show
    dorm_mgr "Since you're staying with us — let me make sure you actually understand the rules."
    dorm_mgr "Not to scare you. The dormitory has policies for a reason. Three scenarios."
    python:
        sq_quiz_state.setup(
            "Dorm Code of Conduct",
            "The Dorm Manager tests the house rules",
            "🏠",
            [
                (
                    "Your friend from another building wants to hang out in your room at 9 PM. Is that allowed?",
                    [
                        ("No — visitors are not allowed inside rooms after 8 PM. Guests must stay in the common area only", True, "Correct. Visitors of any gender are restricted to common areas. Both the visitor and the resident can face a dorm violation if this rule is broken."),
                        ("Yes — it is still early and the main gate curfew is at 10 PM", False, "The main gate curfew is 10 PM. But visitor-in-room restrictions begin at 8 PM — these are separate rules with separate consequences."),
                        ("Yes — as long as they leave before lights-out at the end of the evening", False, "Visitor rules are specific: common areas only, and they must leave before 8 PM applies to room areas."),
                    ]
                ),
                (
                    "A typhoon signal is raised and classes are suspended. What is your responsibility as a dormitory resident?",
                    [
                        ("Stay inside the dorm, inform the dorm manager if you plan to leave, and follow all safety announcements", True, "Exactly. During typhoons or emergencies, the dorm manager coordinates with the university. Leaving without notice puts you at risk."),
                        ("Use the free time to go to town since classes are already cancelled for the day", False, "A typhoon is not a holiday. Wandering out during signal-level weather without notice is irresponsible and dangerous."),
                        ("Nothing specific — class suspension only affects academic schedule, not dormitory rules", False, "It does. Emergency conditions activate additional dorm protocols. The manager needs to know the whereabouts of all residents."),
                    ]
                ),
                (
                    "You and your roommate have a growing conflict over cleanliness and living standards. First step?",
                    [
                        ("Talk directly with your roommate first; if unresolved, bring it to the dorm manager for mediation", True, "That is exactly the process. Direct communication first — most conflicts are resolved by simply talking. If that fails, the manager is here to mediate."),
                        ("File a formal complaint with the OSA immediately to document the situation", False, "That jumps too many steps. A roommate conflict does not require OSA involvement unless there is harassment or a serious conduct issue."),
                        ("Move your belongings to a different room informally without telling anyone", False, "Room assignments are not changed informally. You would need to formally request a room change with proper justification."),
                    ]
                ),
            ]
        )
    window hide
    call screen sq_quiz_game()
    $ _sq_result = _return
    window show
    if _sq_result >= 2:
        dorm_mgr "Good. You are a reasonable person. This dorm needs more of those."
    else:
        dorm_mgr "Review the dorm guidelines posted in your room. They exist so everyone can live here comfortably."
    $ collect_item(ITEM_DORM_CODE)
    show screen item_pickup_screen(ITEM_DORM_CODE)
    pause 2.5
    hide screen item_pickup_screen
    $ complete_subquest("sq_dorm_code")
    window hide
    return


## ============================================================================
## ACT 4 — SUBQUEST B: "Dorm Survival Kit"
## Trigger: Nanay Elena's dialogue  |  Game: Quiz
## ============================================================================
label sq_dorm_survival:
    window show
    nanay_elena "You've unpacked already? Good. But do you have EVERYTHING you actually need?"
    nanay_elena "Most freshmen arrive missing something important. Let's check your survival kit."
    python:
        sq_quiz_state.setup(
            "Dorm Survival Kit",
            "Nanay Elena checks if you are truly prepared",
            "🎒",
            [
                (
                    "You get sick at 2 AM — fever, headache. The HSU is closed. What should you have in your room?",
                    [
                        ("A basic medicine kit: paracetamol, antacid, antihistamine, oral rehydration salts, and a thermometer", True, "Good. That covers the basics. Add a flashlight for power outages and a spare phone charger. These things always fail at the worst moment."),
                        ("Nothing — just call the dorm manager, that is what they are there for", False, "The manager can get you to the HSU or call emergency services — but cannot treat you. Have basic medicines ready."),
                        ("Nothing — there are hospitals and clinics within a short distance from campus", False, "The nearest hospital is a tricycle ride away at 2 AM during a typhoon. A paracetamol in your drawer is faster."),
                    ]
                ),
                (
                    "There is a 3-day power outage during exam week — it happens here. What do you need?",
                    [
                        ("A power bank, battery lamp or candles, printed notes, and a small battery-powered fan", True, "Excellent. A large power bank keeps your phone and laptop alive for days. Print critical notes before exam week — do not depend entirely on digital files."),
                        ("Nothing special — the library has power and WiFi so I can just study there", False, "The library may also lose power during extended outages. And it closes at 7 PM. Evening study with no power becomes a problem quickly."),
                        ("Just buy everything at the nearest store once the outage happens", False, "Stores run out of candles, batteries, and power banks immediately during any power emergency. Prepare before you need it."),
                    ]
                ),
                (
                    "Homesickness hits hard at week three. What is the most effective thing in your survival kit for that?",
                    [
                        ("A connection to community — a study group, an org, or at least one person you can call a real friend here", True, "That is it. Not food. Not gadgets. People. I have seen students with the best-equipped rooms cry — and students with almost nothing thrive because they found their people."),
                        ("Calling home every day so you stay connected to your family and roots", False, "Calling home helps — but only when balanced. Calling home constantly to avoid building new connections here just delays adjustment."),
                        ("Keeping yourself busy with studies so you do not have time to feel lonely or sad", False, "Busyness masks loneliness — it does not heal it. Build real connections here. That is the real survival kit."),
                    ]
                ),
            ]
        )
    window hide
    call screen sq_quiz_game()
    $ _sq_result = _return
    window show
    if _sq_result >= 2:
        nanay_elena "You are going to be fine. You know what you need."
    else:
        nanay_elena "Write down what is missing. There is still time to prepare properly before the semester truly begins."
    $ collect_item(ITEM_SURVIVAL_KIT)
    show screen item_pickup_screen(ITEM_SURVIVAL_KIT)
    pause 2.5
    hide screen item_pickup_screen
    $ complete_subquest("sq_dorm_survival")
    window hide
    return


## ============================================================================
## ACT 5 — SUBQUEST A: "UP Grading System Mastery"
## Trigger: Prof. Lena's dialogue  |  Game: GWA Calculator
## ============================================================================
label sq_grade_mastery:
    window show
    prof_lena "Let me show you something practical about the UP grading system."
    prof_lena "This is a GWA simulator. Cycle through grades for each course and see how your standing changes."
    prof_lena "Challenge: reach University Scholar status. That means a GWA of 1.20 or better."
    $ sq_gwa_state.reset()
    window hide
    call screen sq_gwa_calc_game()
    $ _sq_result = _return
    window show
    if _sq_result == "completed":
        prof_lena "University Scholar. That means every course at 1.25 or better. Now you know what it takes."
        prof_lena "The cutoffs: 1.20 for University Scholar, 1.45 for College Scholar, 1.75 for Dean's List."
    else:
        prof_lena "The grading scale is unforgiving. 1.00 is the best. 5.00 is failing."
        prof_lena "Know the difference: 4.00 is conditional failure with a removal exam, 5.00 requires retaking the course."
    $ collect_item(ITEM_GRADING_GUIDE)
    show screen item_pickup_screen(ITEM_GRADING_GUIDE)
    pause 2.5
    hide screen item_pickup_screen
    $ persistent.encyclopedia_unlocks.add("grading_system_sq")
    $ complete_subquest("sq_grade_mastery")
    window hide
    return


## ============================================================================
## ACT 5 — SUBQUEST B: "Absence Policy Challenge"
## Trigger: Kuya Rico's dialogue  |  Game: Quiz
## ============================================================================
label sq_absence_policy:
    window show
    kuya_rico "Wait — before you go. One thing you MUST know about UP attendance."
    kuya_rico "The MAO. Maximum Allowable Absence. Three questions."
    python:
        sq_quiz_state.setup(
            "Absence Policy Challenge",
            "Kuya Rico tests your MAO knowledge",
            "📅",
            [
                (
                    "You are in a 3-unit class meeting three times a week. How many total absences triggers automatic DRP under UP policy?",
                    [
                        ("More than 20% of total class meetings — roughly 10 to 11 absences across the full semester", True, "That is the UP policy: more than 20% triggers automatic DRP. BUT many professors set STRICTER limits in their syllabus. Always read the syllabus on day one."),
                        ("Exactly 3 absences total — three strikes and you are automatically dropped", False, "That is stricter than the actual UP policy. Some professors impose 3-absence rules in their own syllabus, but the UP minimum threshold is the 20% rule."),
                        ("6 absences — two absences per month across a three-month semester", False, "There is no monthly cap in UP policy. Absences are counted as a total against 20% of all scheduled class meetings for the entire semester."),
                    ]
                ),
                (
                    "You arrive 20 minutes late to class. The professor marks you tardy three times. Does this count as an absence?",
                    [
                        ("It depends entirely on the professor's syllabus policy — some count three tardies as one absence", True, "Exactly. There is no universal UP rule converting tardiness to absences. The professor's syllabus defines the tardiness policy. Know it before you assume you are fine."),
                        ("No — tardiness and absences are completely separate categories under official UP attendance rules", False, "The baseline UP policy does not convert tardiness to absences — but individual professors can and do impose their own tardiness rules. Always check the syllabus."),
                        ("Yes — any tardy automatically counts as exactly half an absence under official UP rules", False, "That is not a universal UP rule. Individual professors set tardiness policies independently. Your syllabus tells you which kind you have."),
                    ]
                ),
                (
                    "You exceed the MAO in a subject. What appears on your official academic record?",
                    [
                        ("DRP — Dropped. Not a 5.0 — but it can still affect scholarship standing if you did not file the dropping form yourself", True, "Correct. An MAO-triggered drop appears as DRP, not 5.0. BUT if you are on scholarship, a DRP can still trigger a probation review."),
                        ("5.0 — an automatic failing grade is recorded for students who exceed the absence limit", False, "MAO-triggered drops are recorded as DRP, not 5.0. The 5.0 you earn by failing examinations — that is a different situation."),
                        ("INC — you will need to make up the missed class sessions in a following semester", False, "You cannot make up physical attendance. An MAO drop is recorded as DRP. There is no makeup process for exceeding the absence limit."),
                    ]
                ),
            ]
        )
    window hide
    call screen sq_quiz_game()
    $ _sq_result = _return
    window show
    if _sq_result >= 2:
        kuya_rico "Good. You can afford exactly zero careless absences. Every one of them counts."
    else:
        kuya_rico "Reread the attendance section of every syllabus you receive. Every professor is slightly different."
    $ collect_item(ITEM_MAO_POLICY)
    show screen item_pickup_screen(ITEM_MAO_POLICY)
    pause 2.5
    hide screen item_pickup_screen
    $ complete_subquest("sq_absence_policy")
    window hide
    return


## ============================================================================
## ACT 6 — SUBQUEST A: "Org Culture & OSA Registration"
## Trigger: Mika's dialogue  |  Game: Sort
## ============================================================================
label sq_org_culture:
    window show
    mika "Before you leave — let me test the official side of org life, not just the fun part."
    mika "Sort these items into the correct categories. Take your time."
    python:
        sq_sort_state.setup(
            "Org Culture & OSA",
            "Sort each item into the correct category",
            [
                ("Need at least 15 enrolled student members", 0, "👥"),
                ("Must have an approved constitution and by-laws", 0, "📄"),
                ("Must secure a faculty adviser from the college", 0, "👨‍🏫"),
                ("Oversees official recognition of student orgs", 1, "🏛️"),
                ("Investigates harassment complaints against orgs", 1, "⚖️"),
                ("Banned by RA 8049 — the Anti-Hazing Law", 2, "🚫"),
                ("Psychological pressure during recruitment intake", 2, "⚠️"),
            ],
            [
                ("Org Requirements", "#5c1a1a", "📋"),
                ("OSA Functions", "#1a2a5c", "🏛️"),
                ("Prohibited Acts", "#2a1a00", "🚫"),
            ]
        )
    window hide
    call screen sq_sort_game()
    $ _sq_result = _return
    window show
    if _sq_result == "completed":
        mika "You understand the system. Org life is fun — but it has rules that protect everyone."
        mika "Remember: RA 8049 and RA 11053 are very clear. Report hazing and coercive recruitment to the OSA."
    else:
        mika "Review what you missed. Org life has structure — knowing it lets you enjoy it safely."
    $ collect_item(ITEM_ORG_CULTURE)
    show screen item_pickup_screen(ITEM_ORG_CULTURE)
    pause 2.5
    hide screen item_pickup_screen
    $ persistent.encyclopedia_unlocks.add("org_culture_sq")
    $ complete_subquest("sq_org_culture")
    window hide
    return


## ============================================================================
## ACT 6 — SUBQUEST B: "UPV Events Calendar"
## Trigger: Ate Jenny's dialogue  |  Game: Sort
## ============================================================================
label sq_upv_events:
    window show
    ate_jenny "Campus life is not just studying. Sort these UPV events into the right categories."
    ate_jenny "Know your calendar — these are the moments that define your UP experience."
    python:
        sq_sort_state.setup(
            "UPV Events Calendar",
            "Sort each campus event into the right category",
            [
                ("Freshie Week — orientation activities for incoming students", 0, "🎓"),
                ("Org Fair — recognized student organizations recruit members", 0, "📢"),
                ("Academic convocations and Recognition Day ceremonies", 0, "🏅"),
                ("Lantern Parade — annual pre-Christmas lantern competition", 1, "🏮"),
                ("Loyalty Day — UP founding anniversary celebration, June 18", 1, "🎗️"),
                ("Pahampang — inter-college sports festival", 2, "🏀"),
                ("College athletics tournaments across multiple sports", 2, "🏊"),
            ],
            [
                ("Academic / Orientation", "#1a3a4a", "🎓"),
                ("Cultural Traditions", "#4a1a3a", "🏮"),
                ("Sports Events", "#1a4a1a", "🏀"),
            ]
        )
    window hide
    call screen sq_sort_game()
    $ _sq_result = _return
    window show
    if _sq_result == "completed":
        ate_jenny "Now you know your campus calendar. Attend these events — they are part of your UP education."
        ate_jenny "The Lantern Parade and Pahampang especially. Do not miss your first year versions."
    else:
        ate_jenny "Keep an eye on the OSA bulletin board. These events are posted at the start of each semester."
    $ collect_item(ITEM_UPV_EVENTS)
    show screen item_pickup_screen(ITEM_UPV_EVENTS)
    pause 2.5
    hide screen item_pickup_screen
    $ persistent.encyclopedia_unlocks.add("upv_events_sq")
    $ complete_subquest("sq_upv_events")
    window hide
    return


## ============================================================================
## ACT 7 — SUBQUEST A: "APA Citation Challenge"
## Trigger: Bea's dialogue  |  Game: Quiz
## ============================================================================
label sq_apa_challenge:
    window show
    bea "Since I mentioned APA format — I am actually going to test you on it."
    bea "Every UP professor uses APA 7th Edition. You will fail research papers if you get this wrong."
    python:
        sq_quiz_state.setup(
            "APA Citation Challenge",
            "Bea tests APA 7th Edition citation format",
            "📝",
            [
                (
                    "You paraphrased an idea from: dela Cruz (2022), a journal article. Correct APA 7th in-text citation?",
                    [
                        ("(dela Cruz, 2022)", True, "Correct. In-text APA for a paraphrase: (Author Last Name, Year). No page number needed unless you are directly quoting a specific passage."),
                        ("(dela Cruz, 2022, pp. 45-67)", False, "Page numbers in APA in-text citations are only required for direct quotes. For paraphrasing, just (Author, Year) is correct."),
                        ("(Juan dela Cruz, 2022)", False, "APA uses only the author's LAST NAME in in-text citations — not their full given name."),
                    ]
                ),
                (
                    "How would you format the same article in your Reference List? (dela Cruz, J., 2022, vol 14, pp.45-67, Philippine Journal of Marine Science)",
                    [
                        ("dela Cruz, J. (2022). Marine biodiversity in Iloilo Strait. Philippine Journal of Marine Science, 14, 45–67.", True, "Perfect APA 7th format. Last name + initial, year in parentheses, article title in sentence case, journal name in italics, volume number, page range."),
                        ("dela Cruz, Juan (2022). 'Marine Biodiversity in Iloilo Strait.' Philippine Journal of Marine Science. 14:45-67.", False, "Several issues: APA uses initial not full first name, article title should NOT be in quotes and uses sentence case, and volume uses a comma not a colon."),
                        ("dela Cruz (2022), Marine biodiversity in Iloilo Strait, Philippine Journal of Marine Science, Vol. 14", False, "Missing the first initial, the year needs parentheses, 'Vol.' is not used in APA — just the number — and formatting punctuation is incorrect throughout."),
                    ]
                ),
                (
                    "What is plagiarism — and what is the most common form that professors and Turnitin catch?",
                    [
                        ("Using someone else's ideas or words without proper attribution. Most common: paraphrasing too closely without citation", True, "Exactly. Plagiarism is not just copy-paste. Closely following someone's sentence structure without citation is also plagiarism. Turnitin catches both exact matches and closely paraphrased content."),
                        ("Using any published material in your paper — you must generate all ideas entirely on your own", False, "Academic writing REQUIRES you to use and cite existing sources. The issue is ATTRIBUTION — not whether you use sources."),
                        ("Plagiarism only applies when you copy-paste entire paragraphs or large blocks of text", False, "Plagiarism includes paraphrasing without citation, submitting others' work as your own, and even self-plagiarism — reusing your own previously submitted paper."),
                    ]
                ),
            ]
        )
    window hide
    call screen sq_quiz_game()
    $ _sq_result = _return
    window show
    if _sq_result >= 2:
        bea "Your first research paper will not have citation issues. Get the APA Quick Guide from the TLRC — invaluable."
    else:
        bea "Get the APA 7th Edition Quick Guide from the TLRC. One page. Do not submit a paper without checking it."
    $ collect_item(ITEM_APA_GUIDE)
    show screen item_pickup_screen(ITEM_APA_GUIDE)
    pause 2.5
    hide screen item_pickup_screen
    $ complete_subquest("sq_apa_challenge")
    window hide
    return


## ============================================================================
## ACT 7 — SUBQUEST B: "UP's Three Mandates"
## Trigger: Prof. Santos' dialogue  |  Game: Quiz
## ============================================================================
label sq_up_mandates:
    window show
    prof_santos "You said you are curious. Then let me test whether you understand why UP exists the way it does."
    prof_santos "Three questions on UP's core mandates."
    python:
        sq_quiz_state.setup(
            "UP's Three Mandates",
            "Prof. Santos tests your understanding of UP's purpose",
            "🏛️",
            [
                (
                    "What are the three formal mandates of the University of the Philippines as defined in its charter?",
                    [
                        ("Instruction, Research, and Extension (community service)", True, "Correct. These three pillars define everything UP does. Instruction is your classes. Research creates new knowledge. Extension applies that knowledge to serve communities."),
                        ("Education, Discipline, and Nation-Building", False, "Those are values associated with UP's identity, but not its formal mandates. The UP Charter specifies instruction, research, and extension."),
                        ("Teaching, Sports, and Public Service", False, "Sports and wellness are part of campus life but are not formal mandates. The three mandates are instruction, research, and extension as defined in Republic Act 9500."),
                    ]
                ),
                (
                    "UPV is particularly known for research in which area, tied directly to its coastal location?",
                    [
                        ("Marine science and fisheries — CFOS is one of the leading fisheries research institutes in Southeast Asia", True, "Exactly. The College of Fisheries and Ocean Sciences — CFOS — is UPV's flagship research unit. We have the Marine Biological Station and graduates who shape national marine policy."),
                        ("Technology and engineering — UPV has a strong engineering research and development program", False, "UPV has engineering programs, but our recognized research strength is marine science and fisheries, tied directly to our coastal Miagao location."),
                        ("Law and political science — UPV was originally established as a law college in Iloilo", False, "UPV was established as a fisheries college in 1947 — not a law school. Marine science is our founding identity and research heritage."),
                    ]
                ),
                (
                    "What is the Extension mandate in practical terms — and how do UP students participate in it?",
                    [
                        ("Applying university knowledge to benefit communities — through outreach, community research, and professional practice", True, "Precisely. Extension means the university's expertise must benefit the public, not just the academic community. You participate through NSTP, org service projects, and your professional work."),
                        ("Extending class hours to provide remedial tutorials for students who are academically struggling", False, "That is a support service, not the mandate. Extension as a formal mandate means the university engaging with and serving communities outside the campus itself."),
                        ("The extracurricular activities and community events organized by student organizations", False, "Org activities contribute to community life, but Extension as a formal mandate means organized, systematic outreach by the university as an institution."),
                    ]
                ),
            ]
        )
    window hide
    call screen sq_quiz_game()
    $ _sq_result = _return
    window show
    if _sq_result >= 2:
        prof_santos "You understand UP's purpose. Now find your role in it."
        prof_santos "Read Republic Act 9500 — the UP Charter of 2008. Short, readable, and foundational."
    else:
        prof_santos "Read Republic Act 9500 — the UP Charter of 2008. It is short, readable, and it explains why this institution exists."
    $ collect_item(ITEM_UP_MANDATES)
    show screen item_pickup_screen(ITEM_UP_MANDATES)
    pause 2.5
    hide screen item_pickup_screen
    $ persistent.encyclopedia_unlocks.add("up_mandates_sq")
    $ complete_subquest("sq_up_mandates")
    window hide
    return


## ============================================================================
## ACT 8 — SUBQUEST A: "UPV Heritage and Identity"
## Trigger: Jaden's Act 8 dialogue  |  Game: Timeline
## ============================================================================
label sq_upv_heritage:
    window show
    jaden "Before we go our separate ways — do you actually know where you ARE?"
    jaden "Not just 'UP Visayas.' The real history. Arrange these milestones from earliest to latest."
    python:
        sq_timeline_state.setup(
            [
                (1908, "UP Founded in Manila", "The University of the Philippines is established by the American colonial government. The flagship campus begins in Manila.", "#2a1a5c"),
                (1947, "UPV Founded as College of Fisheries", "The UP College of Fisheries is established in Iloilo, Panay. Marine science becomes the campus' founding identity and academic core.", "#2a5c2a"),
                (1979, "UPV Becomes a Constituent University", "The campus is elevated from a college to a full constituent university of the UP System during reorganization.", "#2a2a5c"),
                (1987, "UPV Tacloban College Established", "UPV expands to Eastern Visayas — making UPV the only UP campus spanning two island groups: Panay and Leyte.", "#5c2a1a"),
                (2008, "RA 9500 — UP Charter Enacted", "Republic Act 9500, the UP Charter of 2008, is signed into law. It formally defines UP's mandates: instruction, research, and extension.", "#1a4a4a"),
            ]
        )
    window hide
    call screen sq_timeline_game()
    $ _sq_result = _return
    window show
    if _sq_result >= 4:
        jaden "You really know where you are now. That matters more than you think."
        jaden "1947. 1979. 1987. 2008. This place has been building toward the version you inherited."
    elif _sq_result >= 2:
        jaden "Close. But you know more than when we started. Know your university — it is part of knowing yourself."
    else:
        jaden "History is not random. These events explain why UPV is what it is. Read them."
    $ collect_item(ITEM_UPV_IDENTITY)
    show screen item_pickup_screen(ITEM_UPV_IDENTITY)
    pause 2.5
    hide screen item_pickup_screen
    $ persistent.encyclopedia_unlocks.add("upv_identity_sq")
    $ complete_subquest("sq_upv_heritage")
    window hide
    return


## ============================================================================
## ACT 8 — SUBQUEST B: "Honor and Excellence — The UP Pledge"
## Trigger: Prof. Reyes' dialogue  |  Game: Quiz
## ============================================================================
label sq_honor_excellence:
    window show
    prof_reyes "Since you came back — I have a final challenge for you."
    prof_reyes "Not just trivia. A reflection. But with right and wrong answers."
    python:
        sq_quiz_state.setup(
            "Honor and Excellence",
            "Prof. Reyes — a final reckoning on UP's values",
            "⭐",
            [
                (
                    "UP's motto is 'Honor and Excellence.' What does HONOR mean in an academic context?",
                    [
                        ("Academic integrity — honest work, no cheating, standing up for what is right even at personal cost", True, "Yes. Honor is not decoration. In UP, it means submitting your own work, citing your sources, refusing to copy even under pressure. It means being the kind of person whose word means something."),
                        ("Being polite to professors and following all rules to avoid getting into trouble", False, "That is compliance, not honor. Honor is internal. It is doing the right thing even when no one is watching."),
                        ("Graduating with Latin honors — summa, magna, or cum laude distinction", False, "That is Excellence, not Honor. Honor is integrity. A student can graduate with honors dishonestly. That is not what UP means."),
                    ]
                ),
                (
                    "A classmate shows you their answer sheet during an exam. You do not copy — but you also do not report it. Are you honoring the code?",
                    [
                        ("No — staying silent when you witness academic dishonesty makes you complicit in it", True, "That is the uncomfortable truth. UP's honor code is not just about what you do — it is about what you allow. A university built on integrity requires everyone to uphold it."),
                        ("Yes — it is not your business. You did not cheat yourself, so you have no obligation", False, "But someone else did — with your silent permission. Academic institutions survive on mutual trust. Silent tolerance of cheating degrades that trust for everyone."),
                        ("It depends on whether the professor finds out — if no one knows, there is no harm", False, "Honor cannot be contingent on getting caught. If your decision depends on whether someone is watching, it is not honor — it is calculation."),
                    ]
                ),
                (
                    "What does EXCELLENCE mean for an Iskolar ng Bayan — beyond grades alone?",
                    [
                        ("The quality of your work, your character, and how you apply your education in service to others", True, "That is the complete answer. Excellence in grades matters. But UP's definition is broader: excellence in character, in purpose, and in service. A student with a 1.00 GWA who hoards their knowledge serves no one."),
                        ("Being the highest-ranked student in your class — outperforming all your peers academically", False, "Relative ranking is not excellence. Excellence is absolute — being the best version of yourself and directing it toward something larger than personal advancement."),
                        ("Publishing research papers and academic outputs before graduation", False, "Research is one expression of excellence. But the full meaning goes beyond output: it is character, integrity, and service — all together."),
                    ]
                ),
            ]
        )
    window hide
    call screen sq_quiz_game()
    $ _sq_result = _return
    window show
    if _sq_result >= 2:
        prof_reyes "(He pauses and looks at you for a moment.)"
        prof_reyes "You understand it. Not everyone does when they first arrive."
        prof_reyes "That understanding will guide you through everything — the good semesters and the hard ones."
    else:
        prof_reyes "Think about your answers. Not because you failed — but because this question follows you for four years."
    narrator_char "(He hands you a folded card — the UP Oblation on one side, the words 'Iskolar ng Bayan' on the other.)"
    prof_reyes "Welcome — truly — to the University of the Philippines."
    $ collect_item(ITEM_HONOR_EXCELLENCE)
    show screen item_pickup_screen(ITEM_HONOR_EXCELLENCE)
    pause 2.5
    hide screen item_pickup_screen
    $ persistent.encyclopedia_unlocks.add("honor_excellence_sq")
    $ complete_subquest("sq_honor_excellence")
    window hide
    return


## ============================================================================
## ACT 5 — SUBQUEST C: "Rights vs. Freedom — Sort It Out"
## Trigger: Ate Grace's dialogue end  |  Game: Sort (3 bins)
## Sort student scenarios into: Student Right / Faculty Academic Freedom /
## Student Responsibility
## ============================================================================
label sq_rights_freedom:
    window show
    ate_grace "One more thing before you go. You said you understand your rights and academic freedom."
    ate_grace "Prove it. Sort these situations into the right category."
    python:
        sq_sort_state.setup(
            "Rights vs. Freedom",
            "Sort each situation into the correct category",
            [
                ("Requesting your official grade sheet from the Registrar", 0, "📄"),
                ("A professor teaching from an unconventional or controversial theory", 1, "📖"),
                ("Filing a formal complaint when a professor is absent more than 20% of classes", 0, "📢"),
                ("A professor deciding which readings to assign in their own syllabus", 1, "📚"),
                ("Submitting your own original work — no plagiarism, no ghostwriting", 2, "✏️"),
                ("Appealing an unfair grade through the department chair or dean", 0, "⚖️"),
                ("Attending class prepared after completing the assigned readings", 2, "📓"),
            ],
            [
                ("Your Student Right", "#1a3a1a", "🎓"),
                ("Faculty Academic Freedom", "#1a1a3a", "📚"),
                ("Your Responsibility", "#2a1a00", "⚡"),
            ]
        )
    window hide
    call screen sq_sort_game()
    $ _sq_result = _return
    window show
    if _sq_result == "completed":
        ate_grace "Good. You know the difference. Rights protect you. Academic freedom protects inquiry. Responsibility holds both together."
        ate_grace "Use all three — and understand which one applies before you act."
    else:
        ate_grace "Review what you missed. Knowing the difference between a right, a freedom, and a duty keeps you from misusing all three."
    $ collect_item(ITEM_RIGHTS_FREEDOM_GUIDE)
    show screen item_pickup_screen(ITEM_RIGHTS_FREEDOM_GUIDE)
    pause 2.5
    hide screen item_pickup_screen
    $ persistent.encyclopedia_unlocks.add("rights_freedom_sq")
    $ complete_subquest("sq_rights_freedom")
    window hide
    return


## ============================================================================
## ACT 5 — SUBQUEST D: "Campus Health Triage"
## Trigger: Physician at act5_hsu_end  |  Game: Sort (3 bins)
## Sort health scenarios into: Visit HSU / Refer to Hospital / Self-manage
## ============================================================================
label sq_hsu_triage:
    window show
    physician "Before you go — one practical exercise. Different situations call for different responses."
    physician "Sort these cases into what you would do. It will serve you better than any pamphlet."
    python:
        sq_sort_state.setup(
            "Campus Health Triage",
            "Sort each health situation into the right response",
            [
                ("Mild fever and headache — first onset today", 0, "🤒"),
                ("Severe toothache — needs extraction", 0, "🦷"),
                ("Suspected fracture after a fall — severe swelling, cannot move limb", 1, "🦴"),
                ("Common cold, runny nose only — no fever", 2, "🤧"),
                ("Need an official Medical Certificate for missed classes", 0, "📄"),
                ("High fever persisting three or more days — not improving", 1, "🌡️"),
                ("Dehydrated after vomiting — needs oral rehydration salts", 0, "💧"),
            ],
            [
                ("Visit HSU — free on campus", "#1a3a2a", "🏥"),
                ("Referral to hospital needed", "#1a2a3a", "🚑"),
                ("Self-manage — rest or pharmacy", "#2a2a1a", "💊"),
            ]
        )
    window hide
    call screen sq_sort_game()
    $ _sq_result = _return
    window show
    if _sq_result == "completed":
        physician "Correct on all. The HSU is your first stop — not last resort. We handle far more than most students expect."
        physician "And when we cannot, we refer you immediately. You are never left to figure it out alone."
    else:
        physician "Review the cases you missed. The key rule: when uncertain, come here first. We will tell you if you need to go further."
    $ collect_item(ITEM_HSU_TRIAGE_GUIDE)
    show screen item_pickup_screen(ITEM_HSU_TRIAGE_GUIDE)
    pause 2.5
    hide screen item_pickup_screen
    $ persistent.encyclopedia_unlocks.add("hsu_triage_sq")
    $ complete_subquest("sq_hsu_triage")
    window hide
    return


## ============================================================================
## ACT 6 — SUBQUEST C: "Which Support Office?"
## Trigger: Dan — after act6_dan_resolution  |  Game: Sort (4 bins)
## Sort student problems into: HSU / GCSU / Scholarship Service / OSA
## ============================================================================
label sq_support_router:
    window show
    dan "Hey — now that I know all three of these offices... let's see if you really do too."
    dan "Where would you send someone with each of these problems?"
    python:
        sq_sort_state.setup(
            "Which Support Office?",
            "Route each student situation to the correct campus office",
            [
                ("Dizzy and pale — hasn't eaten properly in days", 0, "🤒"),
                ("Persistent sadness and inability to leave the dorm for a week", 1, "💙"),
                ("Parents' income dropped — needs STFAP bracket re-assessed", 2, "📋"),
                ("Wants to register a new student organization", 3, "🏛️"),
                ("Anxious about career path — unsure which degree to finish", 1, "🤔"),
                ("Applying for the Emergency Assistance Fund after a family crisis", 2, "🆘"),
                ("Org activity permit and venue reservation for a campus event", 3, "📢"),
                ("Needs a Medical Certificate for two missed class days", 0, "📄"),
            ],
            [
                ("Health Services Unit (HSU)", "#1a3a2a", "🏥"),
                ("Guidance & Counseling (GCSU)", "#3a1a3a", "💙"),
                ("Scholarship Service", "#1a3a10", "📋"),
                ("Office of Student Affairs (OSA)", "#2a1a10", "🏛️"),
            ]
        )
    window hide
    call screen sq_sort_game()
    $ _sq_result = _return
    window show
    if _sq_result == "completed":
        dan "You got it. HSU for the body. GCSU for the mind. Scholarship Service for the wallet. OSA for everything else."
        dan "I'll remember this. I should have known it before today."
    else:
        dan "Review the ones you missed. I only learned this the hard way — don't wait until you actually need it."
    $ collect_item(ITEM_SUPPORT_ROUTE_MAP)
    show screen item_pickup_screen(ITEM_SUPPORT_ROUTE_MAP)
    pause 2.5
    hide screen item_pickup_screen
    $ persistent.encyclopedia_unlocks.add("support_router_sq")
    $ complete_subquest("sq_support_router")
    window hide
    return


## ============================================================================
## ACT 6 — SUBQUEST D: "Documents Checklist"
## Trigger: Kuya Tomas — end of scholarship scene  |  Game: Sort (3 bins)
## Sort documents into: STFAP Re-bracketing / Emergency Fund / Scholarship App
## ============================================================================
label sq_stfap_docs:
    window show
    kuya_tomas "One last thing. You need to know which document goes where."
    kuya_tomas "Students lose opportunities because they prepare the wrong documents for the wrong application."
    kuya_tomas "Sort these. I've seen this mistake too many times."
    python:
        sq_sort_state.setup(
            "Documents Checklist",
            "Sort each document into the correct application",
            [
                ("Sworn Affidavit of Income — notarized, signed by parent or guardian", 0, "📜"),
                ("Brief letter explaining the sudden change in family financial circumstances", 0, "✉️"),
                ("Filled Emergency Fund request form from the Scholarship Office", 1, "📝"),
                ("Written description of the specific urgent need — meals, transport, photocopying", 1, "🗒️"),
                ("Latest grades transcript — current semester GWA on record", 2, "📊"),
                ("Personal essay on financial need and long-term academic goals", 2, "✍️"),
                ("Recommendation letter from a faculty member or department chair", 2, "👨‍🏫"),
            ],
            [
                ("STFAP Re-bracketing", "#1a2a3a", "📋"),
                ("Emergency Fund Application", "#3a2a1a", "🆘"),
                ("Scholarship Application", "#1a3a1a", "🎓"),
            ]
        )
    window hide
    call screen sq_sort_game()
    $ _sq_result = _return
    window show
    if _sq_result == "completed":
        kuya_tomas "Good. Keep those categories clear in your head. Deadlines are absolute — the right document submitted late is the same as no document at all."
        kuya_tomas "Build your folder now. Don't wait until you need it."
    else:
        kuya_tomas "Review what you missed. The Scholarship Office posts guides on the bulletin board — read them before your next application."
    $ collect_item(ITEM_STFAP_DOCS_LIST)
    show screen item_pickup_screen(ITEM_STFAP_DOCS_LIST)
    pause 2.5
    hide screen item_pickup_screen
    $ persistent.encyclopedia_unlocks.add("stfap_docs_sq")
    $ complete_subquest("sq_stfap_docs")
    window hide
    return

## ============================================================================
## ACT 6 — SUBQUEST E: "Fund the Student — Financial Safety Net"
## Trigger: Kuya Tomas — after sq_stfap_docs  |  Game: Funding bar fill
## Three students, each with budget gaps. Player clicks programs to fill gaps.
## Each program lights up its specific segment with an animation.
## Teaches: TES vs GIAP vs STFAP — what each covers, and that they stack.
## ============================================================================
label sq_financial_assistance:
    window show
    kuya_tomas "Last thing. Three students. Each one has budget gaps."
    kuya_tomas "You have three programs to work with. Click each one. See what it covers."
    python:
        sq_funding_state.setup(
            "Fund the Student",
            "💰",
            [
                (
                    "👩‍🎓", "Maya",
                    "Freshman. Zero financial support yet. Needs everything — tuition covered, a monthly allowance from CHED, and UP's own cash support.",
                    [
                        ("UP Tuition Adjustment",     0, "#1e5c2a"),
                        ("CHED Tuition + Allowance",  1, "#1a3a5c"),
                        ("UP System Cash Allowance",  2, "#5c3a1a"),
                    ]
                ),
                (
                    "👨‍🎓", "Ben",
                    "STFAP re-bracketing approved. But tuition-free isn't the same as rent-free. Two more programs still to go.",
                    [
                        ("Re-bracketing (STFAP)",         0, "#1e5c2a"),
                        ("Government Subsidy (TES)",      1, "#1a3a5c"),
                        ("Grants-in-Aid Allowance (GIAP)", 2, "#5c3a1a"),
                    ]
                ),
                (
                    "👩", "Ana",
                    "On STFAP E9 already — zero tuition. But two programs she didn't know existed can still give her monthly cash.",
                    [
                        ("STFAP Bracket (E9)",           0, "#1e5c2a"),
                        ("RA 10931 National Grant (TES)", 1, "#1a3a5c"),
                        ("UP Monthly Cash (GIAP)",        2, "#5c3a1a"),
                    ]
                ),
            ],
            [
                ("STFAP", "📊", "#2a9a4a", "UP's internal tuition bracket"),
                ("TES",   "🏛️", "#2a6aaa", "CHED national grant — RA 10931"),
                ("GIAP",  "💵", "#c89218", "UP System monthly cash allowance"),
            ]
        )
    window hide
    call screen sq_funding_game()
    window show
    kuya_tomas "You saw it. All three programs running at the same time. None of them cancelling the others."
    kuya_tomas "STFAP handles tuition inside UP. TES is the government's coverage layer on top. GIAP is UP's cash for living costs."
    kuya_tomas "SLAS is what makes sure a student finds all three instead of only the one they happened to ask about."
    $ collect_item(ITEM_FINANCIAL_PROGRAMS)
    show screen item_pickup_screen(ITEM_FINANCIAL_PROGRAMS)
    pause 2.5
    hide screen item_pickup_screen
    $ persistent.encyclopedia_unlocks.add("slas")
    $ persistent.encyclopedia_unlocks.add("tes_giap")
    $ complete_subquest("sq_financial_assistance")
    window hide
    return


## ============================================================================
## ACT 6 — SUBQUEST F: "Handle the Inbox — GCSU Routing"
## Trigger: Ma'am Garcia — after act6_at_gcsu  |  Game: Inbox routing
## 5 student cases arrive. Player routes each to the right GCSU resource.
## Teaches: walk-in vs. scheduled appointment, academic counseling,
##          Peer Facilitators vs. individual counseling.
## ============================================================================
label sq_gcsu_services:
    window show
    guidance_counselor "Before you go — one more exercise."
    guidance_counselor "Five students. Each one needs something specific from this office. You tell me where to send them."
    python:
        sq_inbox_state.setup(
            "GCSU Intake",
            "📬",
            [
                (
                    "😓", "Renz",
                    "Can't make himself study even with notes open in front of him. Been staring at the same page for an hour every night. Not in crisis — more like a broken system.",
                    3,
                    "GCSU academic counseling addresses exactly this — study habits, time management, and the patterns behind procrastination. This isn't a TLRC tutoring issue. TLRC helps you do the task. GCSU helps you understand why you're stuck doing it."
                ),
                (
                    "😢", "Bea",
                    "First week. Just arrived from Palawan. Cries every night, doesn't know anyone, eats alone. Not in crisis — just really struggling with the transition.",
                    2,
                    "The Peer Facilitators group is the ideal first step here. It's low-stakes, student-led, and specifically designed for adjustment — homesickness, isolation, first-year transition. Group activities help students realize they're not alone before individual counseling feels necessary."
                ),
                (
                    "🤔", "Carlo",
                    "Two months in and unsure if his degree is the right choice. Wants to understand what careers actually match his skills and personality. Not urgent — but important.",
                    1,
                    "Career guidance at GCSU (RIASEC testing, aptitude assessment, one-on-one career counseling) works best with a pre-scheduled appointment — it needs adequate time. Walk-in is available, but scheduling gets Carlo a dedicated slot without the wait."
                ),
                (
                    "😰", "Maya",
                    "Overwhelmed for weeks. Hasn't told anyone. Wants support but is scared of sitting one-on-one with a counselor. Doesn't know where to start.",
                    2,
                    "The Peer Facilitators group is the natural entry point when individual counseling feels intimidating. Group sessions are student-led, lower-stakes, and often help students feel ready for one-on-one sessions later. It's designed for this exact situation."
                ),
                (
                    "📱", "Dan",
                    "Had his first GCSU session after everything this week. Ma'am Garcia said to come back. He wants a regular slot — same time, every week, no waiting in line.",
                    1,
                    "Pre-scheduling is exactly for ongoing or recurring sessions — Dan gets a confirmed time slot, no wait, and consistency across weeks. Walk-in is best for first visits or urgent needs. For regular sessions, scheduling is the right choice."
                ),
            ],
            [
                ("Walk-in Now",     "🚪", "#1a2a4a"),
                ("Schedule Ahead",  "📅", "#1a3a2a"),
                ("Peer Facilitators Group", "🤝", "#2a1a3a"),
                ("Academic Counseling (GCSU)", "📖", "#2a2a1a"),
            ]
        )
    window hide
    call screen sq_inbox_game()
    window show
    guidance_counselor "Good. Knowing which door to open for which problem — that's half the work."
    guidance_counselor "The other half is actually walking through it."
    $ collect_item(ITEM_GCSU_SERVICES_GUIDE)
    show screen item_pickup_screen(ITEM_GCSU_SERVICES_GUIDE)
    pause 2.5
    hide screen item_pickup_screen
    $ persistent.encyclopedia_unlocks.add("gcsu")
    $ persistent.encyclopedia_unlocks.add("peer_facilitators")
    $ complete_subquest("sq_gcsu_services")
    window hide
    return


## ============================================================================
## ACT 8 — SUBQUEST A: "The Week in Review" (MANDATORY FINALE QUIZ)
## Trigger: Prof. Reyes' dialogue — mandatory before oval ending
## Game: Quiz — 3 questions spanning Acts 1–7
## Tests whether the player retained the most critical knowledge of the week.
## ============================================================================
label sq_week_review:
    window show
    prof_reyes "Seven days. A lot of people, a lot of places, a lot of information."
    prof_reyes "Before you leave these steps — three questions. One for the campus you arrived in. One for the systems you navigated. One for the person you helped."
    prof_reyes "Show me it stayed with you."
    python:
        sq_quiz_state.setup(
            "The Week in Review",
            "Prof. Reyes — everything you learned, tested in three",
            "🏛️",
            [
                (
                    "You're a freshman who just arrived in Miagao. You need to get from the Plaza to the UPV gate — you have no car. What's the correct information?",
                    [
                        ("Take a tricycle — the fare from Miagao Plaza to the UPV gate is ₱15. The UPV Bus to Iloilo City is free with a validated Form 5, and leaves around 5:30 AM on weekdays.", True, "Correct. Tol Joseph's lessons stayed with you. The tricycle is the standard route: ₱15 from Plaza to the gate. And the UPV Bus is free — just show your Form 5. Miss the last trip back at 6:30 PM and you're sleeping in the city."),
                        ("Take the jeepney from the gate — ₱50 to ₱65 gets you from the campus gate to the Plaza and back.", False, "That fare is for the Iloilo City jeepney route. For short hops within Miagao — Plaza to UPV gate — you take a tricycle at ₱15. The Iloilo City jeepney is a different route from the highway junction."),
                        ("Walk — the campus is close to the plaza and there are no public transport options between them.", False, "There are tricycle routes throughout Miagao. Route 1 goes from Town Center to the UPV Gate — the standard student route. Walking the full distance is impractical, especially under the Miagao sun."),
                    ]
                ),
                (
                    "Dan's family income has changed significantly since he enrolled, and he's been going without food for two days. Which office do you bring him to FIRST — and why?",
                    [
                        ("The HSU first — he needs immediate medical attention for dehydration and hypoglycemia, then GCSU for the emotional and mental health component, then the Scholarship Service for the financial root cause.", True, "Exactly the sequence. You saw it happen this week. Treat the physical emergency first — the body needs to be stabilized before any other support can be effective. Then the mind. Then the financial structure. The HSU, GCSU, and Scholarship Service are three interconnected pieces."),
                        ("The Scholarship Service first — the financial problem is the root cause, so solving money solves everything else.", False, "The financial problem IS the root cause — but Dan needs food and medical attention before he can even fill out a form. You treat the immediate crisis first: HSU for the physical emergency. Then GCSU. Then the scholarship office for the financial solution."),
                        ("The OSA first — they coordinate everything and will know which office to send him to.", False, "The OSA is a good coordinator, but when someone hasn't eaten in two days and is medically distressed, you go directly to the HSU. Speed matters in a health emergency. Route him yourself — don't add extra steps."),
                    ]
                ),
                (
                    "Jaden submits his Kas 1 paper. One paragraph closely paraphrases two sources without any citation. He changed all the words, so he believes it's original. What is the correct assessment?",
                    [
                        ("This is plagiarism — closely paraphrasing a source without attribution violates academic integrity, even if the exact words are different. Prof. Santos and the TLRC both warned about this.", True, "Exactly. Plagiarism is not only copy-paste. Taking someone else's ideas, structure, or argument and restating them without citation is still plagiarism. Prof. Santos called it clearly: 'closely paraphrasing without citation is a violation.' It goes on the academic record. It is not a small thing."),
                        ("It is not plagiarism — he changed the words, so the content is now his own original work.", False, "Changing the words does not make an idea original. If the argument, structure, or insight belongs to a source, that source must be credited. The test is not 'did I rephrase it?' The test is 'did I credit the mind whose thinking I used?'"),
                        ("Whether it counts as plagiarism depends on the professor — some accept paraphrasing without citation if the ideas are widely known.", False, "UP's academic integrity policy does not vary by professor or how 'widely known' an idea is. All source material — books, journals, articles — must be cited. The institution's policy is clear and the TLRC's APA workshop covered this specifically."),
                    ]
                ),
            ]
        )
    window hide
    call screen sq_quiz_game()
    $ _sq_result = _return
    window show

    if _sq_result >= 2:
        prof_reyes "Good."
        prof_reyes "You absorbed it. Not just the facts — the pattern."
        prof_reyes "The tricycle fare, the support offices, the definition of original work."
        prof_reyes "These are not trivia. They are the grammar of this place."
        prof_reyes "A student who knows the grammar can say something real."
    else:
        prof_reyes "Some of it slipped. That is honest."
        prof_reyes "The first week puts a lot through you quickly. Review what you missed."
        prof_reyes "The offices will still be there. The library will still be there."
        prof_reyes "Come back to what you don't yet know. That is also studying."

    narrator_char "(He hands you a small card — the UP Oblation on one side, the words 'Iskolar ng Bayan' on the other.)"
    prof_reyes "For the road ahead."
    prof_reyes "Welcome — truly — to UP Visayas."
    narrator_char "(Encyclopedia unlocked: The First Week — What You Now Know.)"
    $ persistent.encyclopedia_unlocks.add("first_week_complete")
    $ complete_subquest("sq_week_review")
    window hide
    return


## ============================================================================
## END OF SUBQUESTS
## ============================================================================
