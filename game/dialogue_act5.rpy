## ============================================================================
## ACT 5 DIALOGUES — First Day of Classes
## KEY THEME: Classrooms, Professors, Academic System, GWA
## ============================================================================

## --- ACT 5 INIT ---
label act5_start:
    # play music moved to end of previous act
    $ talked_prof_lena = False
    $ talked_kuya_rico = False
    $ talked_ate_grace = False
    $ talked_classmate_dan = False
    jump act5_map

## ============================================================================
## NPC 1 — PROF. LENA (GE Professor)
## KEY INFO: GE curriculum, class expectations, grading system
## ============================================================================
label act5_npc_prof_lena:
    window show
    prof_lena "Good morning, class. Sit down. If you're in the wrong room, now is the time to leave."
    prof_lena "..."
    prof_lena "No one left? Good. Welcome to your first General Education class at UP Visayas."
    prof_lena "I'm Professor Lena. I teach Kas 1 — Kasaysayan ng Pilipinas."
    player_char "(She seems strict. Better pay attention.)"
    menu:
        "What should I expect from GE classes?":
            jump act5_lena_ge
        "How does the grading system work?":
            jump act5_lena_grading
        "Any advice for freshmen?":
            jump act5_lena_advice

label act5_lena_ge:
    prof_lena "GE stands for General Education. These are subjects every UP student must take regardless of their degree program."
    prof_lena "You'll encounter subjects from the arts, humanities, social sciences, and natural sciences."
    prof_lena "The purpose? To develop well-rounded individuals, not just specialists."
    prof_lena "Expect a lot of reading. UP is a reading university. If you don't read, you fall behind."
    prof_lena "Class participation matters. I don't give grades to silent students."
    player_char "How many GE subjects do we need to complete?"
    prof_lena "Around 36 units total — that's roughly 12 subjects spread across your first two years."
    prof_lena "Some are prescribed. Others, you choose from an approved list. Check your curriculum flowchart."

    ## ITEM DROP
    $ collect_item(ITEM_GE_CURRICULUM)
    show screen item_pickup_screen(ITEM_GE_CURRICULUM)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "How does grading work?":
            jump act5_lena_grading
        "Any advice for freshmen?":
            jump act5_lena_advice
        "(Thank you, Ma'am.)":
            jump act5_lena_end

label act5_lena_grading:
    prof_lena "The UP grading system. This is critical, so listen well."
    prof_lena "Grades range from 1.00 — the highest — to 5.00, which means failure."
    prof_lena "1.00 is excellent. 1.25, 1.50, 1.75 — very good to good."
    prof_lena "2.00, 2.25, 2.50 — satisfactory range. 2.75 — borderline passing."
    prof_lena "3.00 — the lowest passing grade. Anything below 3.00 is a failing mark."
    prof_lena "4.00 means conditional failure — you get a chance to pass a removal exam."
    prof_lena "5.00 is outright failure. No removal. You retake the subject."
    prof_lena "INC means Incomplete — you have one year to complete missing requirements."
    prof_lena "DRP means Dropped — you officially withdrew before the deadline."
    player_char "What's a good GWA to aim for?"
    prof_lena "GWA — General Weighted Average. Below 1.75 puts you in the Dean's List."
    prof_lena "Below 1.20 makes you a University Scholar. That's the highest academic distinction."
    prof_lena "For scholarship retention, most require at least 2.00 or better. Check your specific scholarship terms."

    ## ITEM DROP
    $ collect_item(ITEM_GRADING_GUIDE)
    show screen item_pickup_screen(ITEM_GRADING_GUIDE)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "Any advice for freshmen?":
            jump act5_lena_advice
        "(That's very helpful.)":
            jump act5_lena_end

label act5_lena_advice:
    prof_lena "Advice? I'll give you three things."
    prof_lena "One — attend every class. UP has a maximum allowable absences policy. Exceed it and you get a DRP or a 5.0."
    prof_lena "Two — submit on time. Late papers in my class are not accepted. Other professors may be lenient, but don't count on it."
    prof_lena "Three — use consultation hours. Every faculty member has posted hours. If you're struggling, come to us before it's too late."
    prof_lena "The biggest mistake freshmen make is suffering in silence. UP is hard. Ask for help."
    player_char "Thank you, Ma'am. I'll keep that in mind."

    ## ITEM DROP
    $ collect_item(ITEM_PROF_ADVICE)
    show screen item_pickup_screen(ITEM_PROF_ADVICE)
    pause 2.5
    hide screen item_pickup_screen

    jump act5_lena_end

label act5_lena_end:
    prof_lena "Class starts properly next meeting. Read Chapters 1 through 3 of Agoncillo. No excuses."
    $ talked_prof_lena = True
    $ complete_task("talk_prof_lena")
    if "sq_grade_mastery" not in subquests_completed:
        menu:
            "★ Can you show me how the UP grading system actually works?":
                jump sq_grade_mastery
            "(Got it, see you next class.)":
                pass
    window hide
    return

## ============================================================================
## NPC 2 — KUYA RICO (Senior Student / Class Adviser's Assistant)
## KEY INFO: Classrooms, building navigation, class schedules
## ============================================================================
label act5_npc_kuya_rico:
    window show
    kuya_rico "Hey, freshie! Lost already? I saw you walking in circles."
    player_char "I can't find Room 203. The building numbers don't make sense."
    kuya_rico "Classic. Let me help you. I'm Rico, 4th year. I've been navigating these halls for ages."
    menu:
        "How do the room numbers work?":
            jump act5_rico_rooms
        "What buildings hold classes?":
            jump act5_rico_buildings
        "How do I read my class schedule?":
            jump act5_rico_schedule

label act5_rico_rooms:
    kuya_rico "Room numbering in UPV is straightforward once you get the pattern."
    kuya_rico "First digit — the floor. Room 203 means 2nd floor, Room 03."
    kuya_rico "Room 101 to 110 — ground floor. Room 201 to 210 — second floor. And so on."
    kuya_rico "The problem is — different buildings use different numbering. CFOS rooms start with CF, CAS rooms with CAS."
    kuya_rico "So 'CAS 203' is NOT the same as 'CFOS 203.' Check the building prefix on your schedule."
    player_char "That explains why I ended up in the fisheries building looking for a history class."
    kuya_rico "Ha! Classic freshie move. Happens every year."

    ## ITEM DROP
    $ collect_item(ITEM_ROOM_NUMBERING)
    show screen item_pickup_screen(ITEM_ROOM_NUMBERING)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "What buildings hold classes?":
            jump act5_rico_buildings
        "How do I read my schedule?":
            jump act5_rico_schedule
        "(Thanks, that helps!)":
            jump act5_rico_end

label act5_rico_buildings:
    kuya_rico "The main classroom buildings on the Miagao campus:"
    kuya_rico "CAS Building — College of Arts and Sciences. Most GE classes happen here. Near the flagpole."
    kuya_rico "CFOS Building — College of Fisheries and Ocean Sciences. Specialized labs and lecture rooms."
    kuya_rico "CM Building — College of Management. Business, accounting, economics courses."
    kuya_rico "New Admin — some classes and faculty offices on the upper floors."
    kuya_rico "The Auditorium — for large lecture classes and university events."
    kuya_rico "And the wet lab area down by the coast — for practical marine science and fisheries work."
    kuya_rico "Oh — and don't forget the HSU. The Health Services Unit. It's near the admin area."
    player_char "HSU? What's that for?"
    kuya_rico "Campus clinic, basically. If you get sick, feel dizzy, need first aid — go there."
    kuya_rico "They have a doctor and a nurse on duty during weekdays. It's free for students."
    kuya_rico "They also do medical and dental check-ups at the start of each semester. Don't skip those."
    player_char "Is there a campus map I can use?"
    kuya_rico "Check the bulletin board near the flagpole. There's also one posted at each building entrance."
    kuya_rico "Pro tip — take a photo of it on your first day. You'll thank me later."

    ## ITEM DROP
    $ collect_item(ITEM_BUILDING_MAP)
    show screen item_pickup_screen(ITEM_BUILDING_MAP)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "How do I read my schedule?":
            jump act5_rico_schedule
        "(Got it, thanks!)":
            jump act5_rico_end

label act5_rico_schedule:
    kuya_rico "Your class schedule — important stuff. Let me break it down."
    kuya_rico "The format is usually: Subject Code — Section — Day/Time — Room."
    kuya_rico "Days: M = Monday, T = Tuesday, W = Wednesday, Th = Thursday, F = Friday, S = Saturday."
    kuya_rico "Time slots are in 24-hour format sometimes. 1300 means 1:00 PM."
    kuya_rico "If a class says 'TTh 1300-1430 CAS 203' — that means Tuesday and Thursday, 1 to 2:30 PM, CAS Building Room 203."
    kuya_rico "Watch out for 'TBA' — To Be Announced. It means the room or time isn't finalized yet. Check with the department."
    kuya_rico "And 'DISSOLVED' means the section was cancelled. You need to find a replacement ASAP."
    player_char "What if two of my classes overlap?"
    kuya_rico "That's a conflict. You can't enroll in both. Go to the Registrar during the adjustment period to fix it."
    kuya_rico "Always double-check your schedule the night before the first day. Changes happen."

    ## ITEM DROP
    $ collect_item(ITEM_MASS_SCHEDULE)
    $ collect_item(ITEM_MAO_POLICY)
    show screen item_pickup_screen(ITEM_MASS_SCHEDULE)
    pause 2.5
    hide screen item_pickup_screen
    show screen item_pickup_screen(ITEM_MAO_POLICY)
    pause 2.5
    hide screen item_pickup_screen

    jump act5_rico_end

label act5_rico_end:
    kuya_rico "You'll figure it out in a week. Promise. Every senior here was once as confused as you."
    kuya_rico "If you get lost again, ask any upperclassman. We don't bite. Usually."
    $ talked_kuya_rico = True
    $ complete_task("talk_kuya_rico")
    if "sq_absence_policy" not in subquests_completed:
        menu:
            "★ One more thing — quiz me on the absence policy.":
                jump sq_absence_policy
            "(Thanks, Kuya.)":
                pass
    window hide
    return

## ============================================================================
## NPC 3 — ATE GRACE (Student Council Representative)
## KEY INFO: Student rights, academic freedom, the UP Code
## ============================================================================
label act5_npc_ate_grace:
    window show
    ate_grace "Hey! I noticed you in Kas 1 earlier. First class, huh? How was it?"
    player_char "Intense. Professor Lena doesn't mess around."
    ate_grace "Ha! Classic Ma'am Lena. She's tough but fair. You'll learn a lot from her."
    ate_grace "I'm Grace, by the way. Student Council rep for the College of Arts and Sciences."
    menu:
        "What does the Student Council do?":
            jump act5_grace_council
        "What rights do students have at UP?":
            jump act5_grace_rights
        "What is academic freedom?":
            jump act5_grace_freedom

label act5_grace_council:
    ate_grace "The Student Council — or USC for University Student Council — represents the student body."
    ate_grace "We handle student concerns, negotiate with the administration, organize campus-wide events."
    ate_grace "Each college has its own council too. CAS has CASCSC, CFOS has CFOSC, CM has CMSC."
    ate_grace "We also manage the student activity fund — that's the fee you pay during enrollment for org activities and events."
    ate_grace "If you have any issues — unfair grading, harassment, facility problems — the Student Council is your first point of contact."
    player_char "Can freshmen join the Student Council?"
    ate_grace "Not yet as officers — you need to run during elections in your second semester."
    ate_grace "But you CAN attend general assemblies and voice concerns. Your voice counts from day one."

    ## ITEM DROP
    $ collect_item(ITEM_STUDENT_COUNCIL)
    show screen item_pickup_screen(ITEM_STUDENT_COUNCIL)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "What rights do students have?":
            jump act5_grace_rights
        "What is academic freedom?":
            jump act5_grace_freedom
        "(Thanks for the info!)":
            jump act5_grace_end

label act5_grace_rights:
    ate_grace "Student rights. This is important — a lot of freshmen don't know these."
    ate_grace "First — the right to quality education. UP is mandated to provide it. If a professor is consistently absent, you can file a complaint."
    ate_grace "Second — the right to due process. No student can be punished without proper investigation and hearing."
    ate_grace "Third — freedom of expression. You can voice dissent, protest peacefully, publish articles. The Oblation symbolizes this."
    ate_grace "Fourth — the right to access records. You can request your grades, your Form 5, certifications."
    ate_grace "Fifth — the right to organize. You can form or join student organizations freely."
    ate_grace "All of this is enshrined in the UP Student Code. Read it. It's available at the OSA."
    player_char "I didn't know we had all these protections."
    ate_grace "Most students don't. That's why the Student Council exists — to remind everyone."

    ## ITEM DROP
    $ collect_item(ITEM_STUDENT_RIGHTS)
    show screen item_pickup_screen(ITEM_STUDENT_RIGHTS)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "What is academic freedom?":
            jump act5_grace_freedom
        "(I'll definitely read the Student Code.)":
            jump act5_grace_end

label act5_grace_freedom:
    ate_grace "Academic freedom is one of UP's core principles. It has two sides."
    ate_grace "For professors — the freedom to teach, research, and publish without interference."
    ate_grace "For students — the freedom to learn, to question, and to explore ideas without fear of retribution."
    ate_grace "This means you can disagree with a professor in class — respectfully — and not be penalized for it."
    ate_grace "It also means professors can challenge you with uncomfortable ideas. That's the point."
    ate_grace "Academic freedom isn't a free pass. It comes with responsibility — intellectual honesty, rigor, respect for evidence."
    player_char "That's what makes UP different, isn't it?"
    ate_grace "Exactly. Honor and Excellence — the UP motto. Freedom is the foundation of both."

    ## ITEM DROP
    $ collect_item(ITEM_ACADEMIC_FREEDOM)
    show screen item_pickup_screen(ITEM_ACADEMIC_FREEDOM)
    pause 2.5
    hide screen item_pickup_screen

    jump act5_grace_end

label act5_grace_end:
    ate_grace "Welcome to UP, freshie. Don't just survive — participate. The university is what you make of it."
    $ talked_ate_grace = True
    $ complete_task("talk_ate_grace")
    if "sq_rights_freedom" not in subquests_completed:
        menu:
            "★ Can you test me on rights versus academic freedom?":
                jump sq_rights_freedom
            "(Got it — see you around.)":
                pass
    window hide
    return

## ============================================================================
## NPC 4 — DAN (Classmate / Fellow Freshie)
## KEY INFO: Study tips, survival strategies, student life balance
## ============================================================================
label act5_npc_classmate_dan:
    window show
    dan "Psst. Hey. You're in Kas 1 too, right? With Professor Lena?"
    player_char "Yeah. That reading list she gave us is terrifying."
    dan "Tell me about it. Three chapters by Thursday. I'm Dan, by the way."
    player_char "Nice to meet you. How are you handling all of this?"
    dan "Barely. But I've been asking around. Want to hear what I've figured out so far?"
    menu:
        "What study tips have you picked up?":
            jump act5_dan_study
        "How do you balance everything?":
            jump act5_dan_balance
        "Where do students usually study?":
            jump act5_dan_study_spots
        "What if I get sick on campus?":
            jump act5_dan_hsu

label act5_dan_study:
    dan "Okay, here's what the upperclassmen told me."
    dan "One — make a schedule and STICK TO IT. Time management is the number one skill in UP."
    dan "Two — don't just read the textbook. Read supplementary materials. Professors test beyond the assigned reading."
    dan "Three — form a study group early. Shared notes, shared pain. It works."
    dan "Four — start papers and projects EARLY. Not the night before. UP deadlines are non-negotiable."
    dan "Five — use the library. Seriously. It's quiet, it has free Wi-Fi, and the reference section has books you can't find online."
    player_char "That's actually really helpful."
    dan "Right? I wish someone told me this on day one. Oh wait — it IS day one."

    ## ITEM DROP
    $ collect_item(ITEM_STUDY_TIPS)
    show screen item_pickup_screen(ITEM_STUDY_TIPS)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "How do you balance everything?":
            jump act5_dan_balance
        "Where do students study?":
            jump act5_dan_study_spots
        "(Thanks, Dan.)":
            jump act5_dan_end

label act5_dan_balance:
    dan "Balance? Honestly, I'm still figuring it out. But here's what I've heard."
    dan "The 'triad' — Academics, Organizations, Social Life. You can only pick two. That's the UP joke."
    dan "But some upperclassmen say you CAN manage all three — you just need discipline."
    dan "Sleep is important. Pulling all-nighters regularly will destroy your health and your grades."
    dan "Exercise helps too. Even just walking around campus between classes counts."
    dan "And eat proper meals. I know it's tempting to skip breakfast, but your brain needs fuel."
    player_char "Pick two out of three, huh? That's a harsh reality."
    dan "It doesn't have to be. Just don't overcommit in your first semester. Ease into it."

    ## ITEM DROP
    $ collect_item(ITEM_STUDY_BALANCE)
    show screen item_pickup_screen(ITEM_STUDY_BALANCE)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "Where do students study?":
            jump act5_dan_study_spots
        "(Good advice.)":
            jump act5_dan_end

label act5_dan_study_spots:
    dan "Study spots! I've scouted a few already."
    dan "The University Library — obvious choice. Quiet, air-conditioned sections, good reference materials."
    dan "The CAS corridor benches — outdoors, breezy. Good for light reading."
    dan "Ceazar — that open area near HSU. Nice view, calm. But can get windy."
    dan "The dorm common room — if you're a dormer, it's convenient for late-night cramming."
    dan "Some students go to the carinderias near the gate for a 'study and eat' combo."
    dan "And the church grounds — oddly peaceful for reading, especially in the late afternoon."
    player_char "I didn't think of the church grounds."
    dan "Right? The benches there are shaded and nobody bothers you. Secret freshie hack."

    ## ITEM DROP
    $ collect_item(ITEM_STUDY_SPOTS)
    show screen item_pickup_screen(ITEM_STUDY_SPOTS)
    pause 2.5
    hide screen item_pickup_screen

    jump act5_dan_end

label act5_dan_hsu:
    dan "Oh — the HSU. Health Services Unit. I heard about it from a senior during orientation."
    dan "It's the campus clinic near the admin area. Doctor and dentist on duty, all free for students."
    dan "Consultations, first aid, basic checkups, dental services — you just show your student ID."
    dan "If it's serious, they refer you to the district hospital in Miagao or Western Visayas Medical Center in Iloilo."
    player_char "That's good to know. Maybe we should find out exactly where it is."
    dan "Good idea — better to know before you actually need it. Let's go check it out."
    menu:
        "(Visit the HSU with Dan right now.)":
            jump act5_visit_hsu
        "What study tips have you picked up?":
            jump act5_dan_study
        "How do you balance everything?":
            jump act5_dan_balance
        "Where do students study?":
            jump act5_dan_study_spots

label act5_dan_end:
    dan "Hey, if you want to study together sometime, I'm usually at the library after lunch."
    dan "Strength in numbers, right? See you in Kas 1!"
    $ talked_classmate_dan = True
    $ complete_task("talk_classmate_dan")
    window hide
    return

## ============================================================================
## SUPPORT SERVICE VISIT — Health Services Unit (HSU)
## Reference: UP Visayas Student Handbook — Student Welfare Services
## ============================================================================
label act5_visit_hsu:
    window show
    narrator_char "(Dan leads you down a shaded path toward the administration area. A low building with a green cross sign comes into view.)"
    narrator_char "(A handwritten notice on the door: 'HSU — Health Services Unit. Open Mon–Fri, 8:00 AM to 5:00 PM. All UPV students served FREE.')"
    narrator_char "(Inside: the smell of antiseptic, a row of plastic chairs, a small triage desk. It feels calm and clinical.)"
    dan "See? Easy to find once you know where it is."
    physician "Good afternoon! First visit here?"
    player_char "Yes, doc. I wanted to familiarize myself with the clinic."
    physician "Smart move. I'm the University Physician. Every student should know where we are before they need us."
    physician "The HSU is your primary health care unit here on campus. What would you like to know?"
    menu:
        "What medical services do you offer?":
            jump act5_hsu_medical
        "Do you have a dentist here too?":
            jump act5_hsu_dental
        "How do I get a medical certificate for missed classes?":
            jump act5_hsu_medcert
        "What medicines are available for free?":
            jump act5_hsu_medicines

label act5_hsu_medical:
    physician "We provide primary outpatient medical care — free for all enrolled UPV students."
    physician "We handle common illnesses: fever, colds, cough, headache, stomach upsets, minor injuries."
    physician "We also do wound care, basic vital signs monitoring, and injection of prescribed vaccines."
    physician "For laboratory services — we do basic diagnostics: urinalysis, fecalysis, CBC, blood typing."
    physician "The Annual Physical Examination is conducted every start of the school year — height, weight, vision, blood pressure, and a general health screening."
    player_char "Is the annual physical exam a requirement?"
    physician "Yes. It's part of your enrollment clearance — you'll see 'Medical Clearance' on your checklist."
    physician "We also conduct pre-employment medical examinations for graduating students applying for government positions or jobs that require a health certificate."
    physician "And if your college requires a fit-to-work or fitness-for-laboratory certification, we issue that too."
    menu:
        "What about dental services?":
            jump act5_hsu_dental
        "How do I get a medical certificate?":
            jump act5_hsu_medcert
        "What medicines are free?":
            jump act5_hsu_medicines
        "(This is very helpful. Thank you.)":
            jump act5_hsu_end

label act5_hsu_dental:
    physician "Yes — the dental clinic is right next door. Let me introduce you."
    dentist "Welcome! I'm the University Dentist. Glad you're visiting before a toothache forces you to."
    dentist "Dental services at the HSU are completely FREE for enrolled UPV students."
    dentist "We offer: oral examination and consultation, tooth extraction, temporary and permanent fillings, and oral prophylaxis — that's dental cleaning."
    dentist "We also do tooth scaling for students with calculus buildup, and basic dental x-rays when needed."
    player_char "Do I need an appointment?"
    dentist "Walk-ins are welcome during regular hours — Monday to Friday, 8 AM to 5 PM."
    dentist "But if you want a specific time, you can schedule ahead — especially for procedures that take longer, like multiple extractions."
    dentist "Just bring your student ID. That's all. No co-pay, no fees."
    dentist "One advice: don't wait for the pain to become unbearable. Dental problems only get worse when ignored."
    dentist "Come in for a routine check at least once a semester. Prevention is always better than treatment."
    menu:
        "How do I get a medical certificate?":
            jump act5_hsu_medcert
        "What medicines are free?":
            jump act5_hsu_medicines
        "(Thank you, Doc!)":
            jump act5_hsu_end

label act5_hsu_medcert:
    physician "Medical certificates. Very important — this is one of the most common reasons students come here."
    physician "If you're sick and miss class, come to the HSU AS SOON AS POSSIBLE."
    physician "We examine you, document your condition, and issue an official Medical Certificate."
    physician "That certificate is your proof of illness — you present it to your professor as documentation of your absence."
    player_char "Does it automatically excuse my absences?"
    physician "Not automatically. UP policy says a medical certificate SUPPORTS your request for an excused absence."
    physician "But each professor applies their own attendance policy as stated in their course syllabus."
    physician "Some professors excuse all medically documented absences. Others count them against you regardless."
    physician "Read your syllabus carefully on day one. Know your professor's policy before you need it."
    physician "For hospitalization — we can also issue a referral letter that your attending hospital doctor can use."
    physician "Keep a copy of all your medical certificates. Some scholarship sponsors require them in case of grade drops."
    player_char "What about emergency cases?"
    physician "For emergencies, we provide immediate first aid and stabilization — then refer to the Miagao District Hospital."
    physician "For serious cases requiring specialist care, we coordinate transport to Western Visayas Medical Center in Iloilo City."
    physician "You are not alone in a health crisis. The HSU stays with you until you're in safe hands."
    menu:
        "What medicines are free?":
            jump act5_hsu_medicines
        "(I understand. Thank you.)":
            jump act5_hsu_end

label act5_hsu_medicines:
    physician "The HSU maintains a stock of essential medicines under the DOH's Essential Medicines List."
    physician "Available free of charge for students:"
    physician "Analgesics — paracetamol, ibuprofen. For fever, pain, and headaches."
    physician "Antihistamines — for allergic reactions, rashes, and itching."
    physician "Antacids — for stomach acid and hyperacidity."
    physician "Oral rehydration salts — for dehydration, especially after episodes of diarrhea or vomiting."
    physician "Wound care supplies — antiseptic solution, bandages, cotton, gauze."
    physician "Vitamins — we dispense multivitamins and iron supplements, particularly for students showing signs of anemia or nutritional deficiency."
    player_char "What if I need something stronger, like antibiotics?"
    physician "For prescription drugs, we issue a doctor's prescription. You purchase it at the nearest pharmacy."
    physician "There's a pharmacy in Miagao town, and some over-the-counter items are available at the campus cooperative."
    physician "If you're on a maintenance medication — for hypertension, diabetes, asthma — please inform us during your physical exam."
    physician "We keep that on file so we can assist you appropriately in case of an episode on campus."
    dan "That's actually useful to know. I have mild asthma."
    physician "Then please come see me this week. We'll document it so your professors and the dorm staff are aware."
    physician "Being proactive about your health is not a weakness — it's wisdom."
    jump act5_hsu_end

label act5_hsu_end:
    physician "Before you go — here are two things to remember:"
    physician "First: we are here Monday to Friday, 8 AM to 5 PM. For after-hours emergencies, contact the campus security and they will coordinate with us."
    physician "Second: there is no shame in coming here. Your health matters as much as your grades."
    dan "Thanks, Doc. I feel better knowing this is here."
    narrator_char "(You step out into the afternoon sun, more at ease than when you arrived.)"
    narrator_char "(Knowing where to go when you're sick — even far from home — is its own kind of comfort.)"

    ## ITEM DROP
    $ collect_item(ITEM_HSU_SERVICES)
    show screen item_pickup_screen(ITEM_HSU_SERVICES)
    pause 2.5
    hide screen item_pickup_screen

    $ complete_task("visit_hsu")
    if "sq_hsu_triage" not in subquests_completed:
        menu:
            "★ Doc, can you give me a quick triage exercise?":
                jump sq_hsu_triage
            "(Thanks — we'll head out now.)":
                pass
    window hide
    jump act5_dan_end

## ============================================================================
## ACT 5 COMPLETION — First Class Attended
## ============================================================================
label act5_first_class:
    window show
    narrator_char "(You check your schedule one last time before heading out. Three classes today. Time to find them.)"
    window hide
    $ classroom_finder_state.reset()
    call screen classroom_finder_screen
    window show
    narrator_char "(The bell rings. Your first class at UP Visayas is officially over.)"
    narrator_char "(Your notebook is already half-full. The reading list is daunting. But something feels different.)"
    narrator_char "(For the first time since arriving, you feel like a real UP student.)"
    narrator_char "\[ACT 5 COMPLETE] — First Day of Classes."
    $ complete_task("attend_first_class")
    window hide
    return

## ============================================================================
## END OF ACT 5 DIALOGUES
## ============================================================================
play music "audio/Act6.mp3" fadein 1.0
