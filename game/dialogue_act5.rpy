## ============================================================================
## ACT 5 DIALOGUES — First Day of Classes
## KEY THEME: Classrooms, Professors, Academic System, GWA
## ============================================================================

## --- ACT 5 INIT ---
label act5_start:
    $ talked_prof_lena = False
    $ talked_kuya_rico = False
    $ talked_ate_grace = False
    $ talked_classmate_dan = False
    $ talked_ria_hsu = False
    $ talked_hsu_services = False
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
    jump act5_lena_end

label act5_lena_end:
    prof_lena "Class starts properly next meeting. Read Chapters 1 through 3 of Agoncillo. No excuses."
    $ talked_prof_lena = True
    $ complete_task("talk_prof_lena")
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
    player_char "Is there a campus map I can use?"
    kuya_rico "Check the bulletin board near the flagpole. There's also one posted at each building entrance."
    kuya_rico "Pro tip — take a photo of it on your first day. You'll thank me later."
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
    jump act5_rico_end

label act5_rico_end:
    kuya_rico "You'll figure it out in a week. Promise. Every senior here was once as confused as you."
    kuya_rico "If you get lost again, ask any upperclassman. We don't bite. Usually."
    $ talked_kuya_rico = True
    $ complete_task("talk_kuya_rico")
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
    jump act5_grace_end

label act5_grace_end:
    ate_grace "Welcome to UP, freshie. Don't just survive — participate. The university is what you make of it."
    $ talked_ate_grace = True
    $ complete_task("talk_ate_grace")
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

label act5_dan_study:
    dan "Okay, here's what the upperclassmen told me."
    dan "One — make a schedule and STICK TO IT. Time management is the number one skill in UP."
    dan "Two — don't just read the textbook. Read supplementary materials. Professors test beyond the assigned reading."
    dan "Three — form a study group early. Shared notes, shared pain. It works."
    dan "Four — start papers and projects EARLY. Not the night before. UP deadlines are non-negotiable."
    dan "Five — use the library. Seriously. It's quiet, it has free Wi-Fi, and the reference section has books you can't find online."
    player_char "That's actually really helpful."
    dan "Right? I wish someone told me this on day one. Oh wait — it IS day one."
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
    jump act5_dan_end

label act5_dan_end:
    dan "Hey, if you want to study together sometime, I'm usually at the library after lunch."
    dan "Strength in numbers, right? See you in Kas 1!"
    $ talked_classmate_dan = True
    $ complete_task("talk_classmate_dan")
    window hide
    return

## ============================================================================
## NPC 5 — RIA (Dormmate) & NURSE SANTOS (HSU)
## KEY INFO: Health Services Unit, campus health resources, when to visit HSU
## STORY: Ria (your dormmate from Act 4) isn't feeling well. You help her
##        get to the HSU and learn about the campus health services.
## ============================================================================
label act5_npc_ria_hsu:
    window show
    narrator_char "(You're walking back from class when you spot a familiar face sitting on a bench near the CAS corridor.)"
    narrator_char "(It's your dormmate from Room 207 — Ria. She doesn't look well.)"
    player_char "Ria? Hey, are you okay?"
    ria "Oh... hey, roomie. I'm fine, I just..."
    narrator_char "(She presses her hand to her forehead. She's pale and sweating.)"
    ria "I've had this headache since last night. And I feel really dizzy."
    ria "I think it's the heat. Or maybe I haven't been eating right since I got here."

    menu:
        "You should go to the Health Services Unit.":
            jump act5_ria_suggest_hsu
        "Have you eaten anything today?":
            jump act5_ria_eaten
        "Do you want me to get you water first?":
            jump act5_ria_water

label act5_ria_eaten:
    ria "I had crackers this morning... I didn't want to spend on breakfast."
    ria "Back home, my mom always cooked. Here, I keep forgetting to eat properly."
    player_char "Ria, you can't skip meals like that. Especially in this heat."
    ria "I know, I know. I just didn't expect adjusting to be this hard."
    player_char "Come on. Let's get you to the Health Services Unit. They can check on you."
    jump act5_ria_go_hsu

label act5_ria_water:
    player_char "Wait here. I'll get you some water."
    narrator_char "(You grab a bottle of water from a nearby store and bring it back.)"
    ria "Thanks... you didn't have to do that."
    player_char "We're roommates. Of course I do."
    ria "I've been feeling off since yesterday. I thought it would pass."
    player_char "It's been a whole day? You need to see a doctor. Let's go to the HSU."
    jump act5_ria_go_hsu

label act5_ria_suggest_hsu:
    ria "The HSU? Where even is that?"
    player_char "The Health Services Unit — it's inside the campus. I saw it on the map during orientation."
    ria "I don't know... maybe I'll just rest in the dorm."
    player_char "Ria, you look really pale. What if it's something serious? Let me take you there."
    ria "..."
    ria "Okay. Thanks, roomie. I don't think I can walk there alone anyway."
    jump act5_ria_go_hsu

label act5_ria_go_hsu:
    narrator_char "(You help Ria up and walk with her toward the Health Services Unit.)"
    narrator_char "(It's a short walk, but Ria leans on your shoulder the whole way.)"
    narrator_char "(You arrive at the HSU — a small, clean building with a waiting area outside.)"

    player_char "We're here. Let's get you inside."

    narrator_char "(Inside, a nurse in a white uniform greets you at the front desk.)"

    hsu_nurse "Good afternoon. What seems to be the problem?"
    player_char "My dormmate hasn't been feeling well. Headache, dizziness, she hasn't been eating properly."
    hsu_nurse "Come sit down, dear. Let me take your temperature and blood pressure."

    narrator_char "(Nurse Santos guides Ria to a chair and begins checking her vitals.)"

    hsu_nurse "Temperature is slightly elevated — 37.8. Blood pressure is a bit low."
    hsu_nurse "When was the last time you had a full meal?"
    ria "Um... yesterday lunch, I think."
    hsu_nurse "That explains a lot. You're likely dehydrated and your blood sugar is low."
    hsu_nurse "This is very common with freshmen. The stress of adjusting, the heat, irregular meals."

    menu:
        "What services does the HSU offer?":
            jump act5_hsu_services
        "Is she going to be okay?":
            jump act5_hsu_ria_okay
        "How can students avoid this?":
            jump act5_hsu_prevention

label act5_hsu_services:
    hsu_nurse "The Health Services Unit provides free basic medical services to all enrolled UP students."
    hsu_nurse "We handle consultations, first aid, blood pressure monitoring, and basic lab tests."
    hsu_nurse "We also issue medical certificates — you'll need one for PE classes and certain scholarship requirements."
    hsu_nurse "Our services include dental checkups too. The dentist is available on specific days."
    hsu_nurse "For emergencies, we stabilize the patient here and coordinate transfer to the Miagao District Hospital or Western Visayas Medical Center in Iloilo City."
    player_char "So students can just walk in anytime?"
    hsu_nurse "Yes. Walk-in basis, Monday to Friday, 8 AM to 5 PM. No appointment needed for basic consultations."
    hsu_nurse "Just bring your student ID and your Form 5 as proof of enrollment."
    hsu_nurse "We also keep records from your entrance medical exam, so we already have your baseline health data."
    menu:
        "Is Ria going to be okay?":
            jump act5_hsu_ria_okay
        "How can students avoid getting sick like this?":
            jump act5_hsu_prevention
        "(Thank you, Ma'am.)":
            jump act5_hsu_treatment

label act5_hsu_ria_okay:
    hsu_nurse "She'll be fine. It's not serious — but it could have been if she waited longer."
    hsu_nurse "Dehydration and low blood sugar can lead to fainting, and in this heat, that's dangerous."
    hsu_nurse "I'm going to give her an oral rehydration solution and some crackers for now."
    hsu_nurse "She needs to rest here for about 30 minutes while we monitor her."
    ria "I'm sorry for the trouble..."
    hsu_nurse "Don't apologize. That's what we're here for."
    hsu_nurse "The worst thing a student can do is ignore symptoms and tough it out alone."
    menu:
        "What services does the HSU offer?":
            jump act5_hsu_services
        "How can students avoid this?":
            jump act5_hsu_prevention
        "(I'm glad she's okay.)":
            jump act5_hsu_treatment

label act5_hsu_prevention:
    hsu_nurse "Prevention is simple but students always forget."
    hsu_nurse "One — eat three meals a day. I know budgeting is hard, but the carinderias near campus sell affordable meals."
    hsu_nurse "Two — drink water. Not just softdrinks or coffee. Actual water. At least 8 glasses a day, more in this heat."
    hsu_nurse "Three — sleep. I know dorm life is exciting, but your body needs 7 to 8 hours."
    hsu_nurse "Four — don't skip your medical exam. The entrance physical isn't just paperwork. It catches conditions early."
    hsu_nurse "Five — if something feels wrong, come here. Don't wait for it to get worse."
    hsu_nurse "I've seen students collapse during flag ceremony because they skipped breakfast. Don't be that student."
    player_char "That's really good advice. I'll make sure we both follow it."
    menu:
        "What services does the HSU offer?" if not talked_hsu_services:
            $ talked_hsu_services = True
            jump act5_hsu_services
        "(Thank you for everything.)":
            jump act5_hsu_treatment

label act5_hsu_treatment:
    narrator_char "(Nurse Santos gives Ria an oral rehydration drink and some biscuits.)"
    narrator_char "(After about 30 minutes, the color returns to Ria's face.)"

    hsu_nurse "Feeling better?"
    ria "Much better. Thank you, Ma'am."
    hsu_nurse "Good. Make sure you eat dinner tonight — a proper meal, not just crackers."
    hsu_nurse "And if you feel dizzy again, come back immediately. Don't hesitate."

    narrator_char "(You and Ria step outside the HSU.)"

    ria "Hey... thanks for bringing me here. I was going to just sleep it off in the dorm."
    player_char "That's what dormmates are for, right?"
    ria "I didn't even know the HSU existed. I thought you had to go all the way to Iloilo for a doctor."
    player_char "Nope. It's right here on campus. Free consultations too."
    ria "I'll remember that. And... I'll try to eat properly from now on."
    ria "Maybe we can go to the carinderia together? I don't really know anyone else here yet."
    player_char "Deal. Breakfast and dinner — no more skipping meals."
    ria "Deal."

    narrator_char "(You walk back toward the dorms together. It's a small moment, but it feels important.)"
    narrator_char "(Looking out for each other — that's how you survive freshman year.)"

    $ talked_ria_hsu = True
    $ complete_task("help_ria_hsu")
    window hide
    return

## ============================================================================
## ACT 5 COMPLETION — First Class Attended
## ============================================================================
label act5_first_class:
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
