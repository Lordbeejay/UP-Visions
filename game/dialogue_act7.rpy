## ============================================================================
## ACT 7 DIALOGUES — Library & Academic Resources
## KEY THEME: Library, research, study habits, academic support
## ============================================================================

## --- ACT 7 INIT ---
label act7_start:
    $ talked_ate_rosa = False
    $ talked_kuya_neil = False
    $ talked_prof_santos = False
    $ talked_classmate_bea = False
    jump act7_map

## ============================================================================
## NPC 1 — ATE ROSA (University Librarian)
## KEY INFO: Library system, borrowing, digital resources
## ============================================================================
label act7_npc_ate_rosa:
    window show
    ate_rosa "Welcome to the UPV Library! First time here?"
    player_char "Yes, Ate. It's bigger than I expected."
    ate_rosa "I'm Ate Rosa, one of the librarians. Let me show you what's available."
    menu:
        "How does the library work?":
            jump act7_rosa_library
        "What digital resources are available?":
            jump act7_rosa_digital
        "Any tips for using the library effectively?":
            jump act7_rosa_tips

label act7_rosa_library:
    ate_rosa "The UPV Library has several sections:"
    ate_rosa "General Circulation — textbooks, reference books, and general reading. Open shelves."
    ate_rosa "Filipiniana Section — materials about Philippine culture, history, and society. Important for GE courses."
    ate_rosa "Periodicals Section — journals, magazines, and newspapers. Both current and archived."
    ate_rosa "Reserve Section — books requested by professors for specific courses. Limited borrowing time."
    ate_rosa "Thesis and Dissertation Section — completed research papers from UPV graduates. Great for research ideas."
    player_char "How do I borrow books?"
    ate_rosa "You need your UPV student ID. That's your library card."
    ate_rosa "General circulation books — 3-day borrowing period. Renewable once if no one else has reserved it."
    ate_rosa "Reserve books — room use only, or overnight borrowing after 4 PM. Return by 8 AM the next day."
    ate_rosa "Overdue fines are ₱5 per day for general, ₱10 per hour for reserve. They add up fast, so return on time!"
    ate_rosa "Lost books — you'll need to replace the exact title or pay the replacement cost plus processing fee."
    menu:
        "What digital resources are available?":
            jump act7_rosa_digital
        "Any tips?":
            jump act7_rosa_tips
        "(Thank you, Ate Rosa!)":
            jump act7_rosa_end

label act7_rosa_digital:
    ate_rosa "This is where modern students have a huge advantage."
    ate_rosa "UP subscribes to several online databases that you can access for FREE as a student."
    ate_rosa "JSTOR — academic journals across all disciplines. Your best friend for research papers."
    ate_rosa "ScienceDirect — science and medical journals. Essential for CFOS and science students."
    ate_rosa "Google Scholar — not a UP subscription, but it's powerful. Link it with your UP email for better access."
    ate_rosa "Philippine E-Journals — local academic publications. Good for topics about Filipino society."
    ate_rosa "To access these from off-campus, you'll need to go through the UP Remote Access Portal."
    ate_rosa "Log in with your UP Mail credentials. The portal gives you access as if you were on campus."
    player_char "I didn't know we had all of that."
    ate_rosa "Most students don't! That's why I always tell freshmen — learn your tools early."
    menu:
        "Any tips?":
            jump act7_rosa_tips
        "(This is so helpful!)":
            jump act7_rosa_end

label act7_rosa_tips:
    ate_rosa "Here are my librarian tips for surviving academics:"
    ate_rosa "One — come to the library during off-peak hours. Early morning or late afternoon. You'll find seats and silence."
    ate_rosa "Two — use the online catalog before coming in. Search from your phone so you know the call number before you arrive."
    ate_rosa "Three — don't just Google your research. Use academic databases. Professors can tell the difference."
    ate_rosa "Four — if you can't find a book, ASK US. We know this library like the back of our hands."
    ate_rosa "Five — the library also has study rooms. You can reserve one for group study sessions. Two hours max."
    ate_rosa "Six — we have printing and photocopying services. Cheaper than the shops outside campus."
    player_char "I'll definitely be a regular here."
    ate_rosa "That's what I like to hear!"
    jump act7_rosa_end

label act7_rosa_end:
    ate_rosa "The library is open Monday to Friday, 8 AM to 7 PM. Saturdays, 8 AM to 12 noon."
    ate_rosa "Closed on Sundays and holidays. Plan your study schedule accordingly."
    ate_rosa "Happy reading!"
    $ talked_ate_rosa = True
    $ complete_task("talk_ate_rosa")
    window hide
    return

## ============================================================================
## NPC 2 — KUYA NEIL (Computer Lab Attendant)
## KEY INFO: Computer labs, UP Mail, CRS tips, campus WiFi
## ============================================================================
label act7_npc_kuya_neil:
    window show
    kuya_neil "Oh, freshie? Come in, come in. Welcome to the computer lab."
    player_char "Hi, Kuya. Can I use the computers here?"
    kuya_neil "Of course! I'm Kuya Neil, the lab attendant. Just sign the logbook."
    menu:
        "How does the computer lab work?":
            jump act7_neil_lab
        "Tell me about UP Mail and online tools.":
            jump act7_neil_tools
        "Any tips for campus WiFi?":
            jump act7_neil_wifi

label act7_neil_lab:
    kuya_neil "We have 30 desktop computers available on a first-come, first-served basis."
    kuya_neil "Maximum usage time is 2 hours per session. If no one's waiting, you can extend."
    kuya_neil "The computers have Microsoft Office, LibreOffice, browsers, and basic software."
    kuya_neil "For specialized software — GIS, statistical tools, design software — check your college's dedicated lab."
    kuya_neil "USB drives are allowed, but always scan for viruses first. We have antivirus installed."
    kuya_neil "Printing is ₱3 per page for black-and-white, ₱10 for colored."
    player_char "Can I bring my own laptop?"
    kuya_neil "Yes! We have power outlets and WiFi. Many students prefer their own device."
    menu:
        "Tell me about UP Mail and tools.":
            jump act7_neil_tools
        "Campus WiFi tips?":
            jump act7_neil_wifi
        "(Thanks, Kuya Neil!)":
            jump act7_neil_end

label act7_neil_tools:
    kuya_neil "Your UP Mail is your gateway to everything digital at UP. It's a Google Workspace account."
    kuya_neil "Format is usually firstname.lastname@up.edu.ph. You should have received it during enrollment."
    kuya_neil "With UP Mail, you get:"
    kuya_neil "Google Drive — unlimited storage. Back up EVERYTHING there. Don't lose your thesis to a broken laptop."
    kuya_neil "Google Docs, Sheets, Slides — free alternatives to Microsoft Office. Great for group work."
    kuya_neil "Google Meet — for online consultations with professors."
    kuya_neil "Access to UP databases — library resources, JSTOR, and other academic tools."
    kuya_neil "CRS access — the Computerized Registration System. That's where you enlist in classes."
    player_char "Any tips for CRS?"
    kuya_neil "CRS enlistment is... an experience. Here's what I tell every freshie:"
    kuya_neil "Know your schedule BEFORE enlistment opens. Have backup classes ready."
    kuya_neil "Log in the MOMENT it opens. Slots fill up in minutes."
    kuya_neil "Have a stable internet connection. Use ethernet if possible, not WiFi."
    kuya_neil "If a class is full, check again on the first day of classes. Some students drop."
    menu:
        "Campus WiFi tips?":
            jump act7_neil_wifi
        "(Very helpful!)":
            jump act7_neil_end

label act7_neil_wifi:
    kuya_neil "Campus WiFi — eduroam and UPV-Guest are the main networks."
    kuya_neil "eduroam is the more reliable one. Use your UP Mail credentials to connect."
    kuya_neil "UPV-Guest requires you to register through a portal. It resets every 24 hours."
    kuya_neil "WiFi can be slow during peak hours — lunch time, between classes. Everyone's online."
    kuya_neil "Pro tip: if WiFi is weak in your building, try the library or the admin building."
    kuya_neil "Some dorms also have their own WiFi routers, but those are usually contributed by residents."
    kuya_neil "For heavy downloads — software, videos for class, large files — use the computer lab. Wired connection is faster."
    player_char "Good to know. I'll keep that in mind."
    jump act7_neil_end

label act7_neil_end:
    kuya_neil "Lab hours are Monday to Friday, 8 AM to 6 PM. Closed weekends."
    kuya_neil "If you have any tech issues, just ask me. I've seen it all."
    $ talked_kuya_neil = True
    $ complete_task("talk_kuya_neil")
    window hide
    return

## ============================================================================
## NPC 3 — PROF. SANTOS (Research Mentor / GE Professor)
## KEY INFO: Research culture, thesis awareness, critical thinking
## ============================================================================
label act7_npc_prof_santos:
    window show
    prof_santos "Ah, a curious freshie approaches. Are you here about my class, or just exploring?"
    player_char "Just exploring, Prof. I heard you're a research professor?"
    prof_santos "I am. Prof. Santos. I teach GE classes but my heart is in marine biology research."
    prof_santos "But research isn't just for scientists. Every UP student should understand it."
    menu:
        "Why is research important?":
            jump act7_santos_research
        "How does research work at UPV?":
            jump act7_santos_how
        "Any advice for a freshman?":
            jump act7_santos_advice

label act7_santos_research:
    prof_santos "UP's mandate has three pillars: instruction, research, and extension."
    prof_santos "Instruction is your classes. Extension is community service. Research is the creation of new knowledge."
    prof_santos "As a UP student, you're expected to contribute to all three before you graduate."
    prof_santos "Your thesis or special problem in senior year will be a research output."
    prof_santos "But more broadly — research is about critical thinking, evidence-based reasoning, and intellectual curiosity."
    prof_santos "Don't just accept information. Question it. Verify it. Test it."
    prof_santos "That's the UP way of thinking."
    player_char "That sounds intimidating."
    prof_santos "It is at first. But it becomes natural. You'll see."
    menu:
        "How does research work at UPV?":
            jump act7_santos_how
        "Advice for a freshman?":
            jump act7_santos_advice
        "(Thank you, Prof.)":
            jump act7_santos_end

label act7_santos_how:
    prof_santos "UPV is especially strong in marine science and fisheries research."
    prof_santos "We have the Marine Biological Station, the Fish World Museum, and partnerships with international marine institutes."
    prof_santos "But other colleges do excellent work too — management research, social science studies, local governance analysis."
    prof_santos "As a student, you can get involved in research as early as second year."
    prof_santos "How? Approach a professor whose work interests you. Ask to volunteer as a research assistant."
    prof_santos "You'll learn methodology, data collection, analysis — skills that are invaluable after graduation."
    prof_santos "Some professors also have funded projects and can provide a small stipend for student assistants."
    player_char "I didn't know freshmen could get involved."
    prof_santos "You can. It's rare, but the professors who see initiative will appreciate it."
    menu:
        "Advice for a freshman?":
            jump act7_santos_advice
        "(That's inspiring.)":
            jump act7_santos_end

label act7_santos_advice:
    prof_santos "Here's my advice for your first year:"
    prof_santos "Read beyond the assigned materials. Professors give minimums. Go beyond them."
    prof_santos "Learn proper citation. APA format — learn it now, thank me later. Plagiarism can get you expelled."
    prof_santos "Start building your academic vocabulary. Read journals, not just textbooks."
    prof_santos "Form study groups. Discussion sharpens understanding better than solo reading."
    prof_santos "Visit your professors during consultation hours. They WANT to help. Most are lonely in their offices."
    prof_santos "And most importantly — don't be afraid to not know. Ignorance is temporary. Apathy is the real enemy."
    player_char "That's really inspiring, Prof."
    prof_santos "You're at the University of the Philippines. You've earned your place. Now grow into it."
    jump act7_santos_end

label act7_santos_end:
    prof_santos "My office is at the CAS building, Room 204. Consultation hours are Tuesday and Thursday, 3-5 PM."
    prof_santos "Don't be a stranger."
    $ talked_prof_santos = True
    $ complete_task("talk_prof_santos")
    window hide
    return

## ============================================================================
## NPC 4 — CLASSMATE BEA (Study Group Organizer)
## KEY INFO: Study groups, exam tips, academic survival
## ============================================================================
label act7_npc_classmate_bea:
    window show
    bea "Hey! Are you in the GE 1 class with Prof. Ramos? I keep seeing you around."
    player_char "Yeah, I am! I'm still trying to figure out how to study for college."
    bea "Same! I'm Bea, by the way. Some of us are forming a study group — want to join?"
    menu:
        "Sure! How does the study group work?":
            jump act7_bea_group
        "Any study tips for college?":
            jump act7_bea_tips
        "How are college exams different from high school?":
            jump act7_bea_exams

label act7_bea_group:
    bea "We meet twice a week — Tuesdays and Thursdays after last class."
    bea "Usually in a library study room or at the canteen if the library's full."
    bea "The deal is — each person summarizes one topic and presents it to the group."
    bea "That way, we all benefit from everyone's work. Plus, explaining a topic helps you understand it better."
    bea "We also share notes, reviewers, and past exam questions when we can find them."
    player_char "That sounds really organized."
    bea "It has to be! College is no joke. Working alone is possible, but working smart is better."
    bea "We've got 6 members so far. One more would be perfect."
    menu:
        "Any study tips?":
            jump act7_bea_tips
        "How are exams different?":
            jump act7_bea_exams
        "(Count me in!)":
            jump act7_bea_end

label act7_bea_tips:
    bea "I've been doing research on study techniques. Here's what actually works:"
    bea "Active recall — don't just re-read notes. Close the book and try to explain the topic from memory."
    bea "Spaced repetition — review material at intervals. Day 1, Day 3, Day 7, Day 14."
    bea "Pomodoro technique — 25 minutes of focused study, 5-minute break. Repeat 4 times, then take a longer break."
    bea "Don't highlight everything — only key concepts and unfamiliar terms. Your notes should be mostly in your own words."
    bea "Teach someone else — if you can explain it simply, you understand it deeply."
    bea "And SLEEP. Pulling all-nighters actually hurts your performance. 7-8 hours of sleep before an exam is non-negotiable."
    player_char "All-nighters don't work?"
    bea "They feel productive, but science says your retention drops. Study early, sleep well, perform better."
    menu:
        "How are exams different?":
            jump act7_bea_exams
        "(Great advice!)":
            jump act7_bea_end

label act7_bea_exams:
    bea "Oh boy, where do I start."
    bea "High school exams were mostly memorization. College exams are about APPLICATION."
    bea "Professors will give you scenarios and ask you to analyze, evaluate, and argue."
    bea "Expect essay-type questions. Not 'define photosynthesis' but 'explain why photosynthesis matters in the context of marine ecology.'"
    bea "Multiple choice exists, but the options are designed to trick you. They test understanding, not recall."
    bea "Some professors use take-home exams — longer, more in-depth, open-book but harder."
    bea "And papers. So many papers. Learn to write clear, structured academic essays NOW."
    bea "APA citation, proper bibliography, no plagiarism — professors run everything through plagiarism checkers."
    player_char "That's intense."
    bea "It is. But once you adjust, it actually makes you smarter. You'll notice the difference within a semester."
    jump act7_bea_end

label act7_bea_end:
    bea "So, study group? Tuesday, 4 PM, library study room 2?"
    bea "I'll add you to the group chat."
    bea "Together, we survive!"
    $ talked_classmate_bea = True
    $ complete_task("talk_classmate_bea")
    window hide
    return

## ============================================================================
## ACT 7 COMPLETION — Study Session
## ============================================================================
label act7_study_session:
    window show
    narrator_char "(You sit in the library study room, surrounded by new friends and stacks of books.)"
    narrator_char "(For the first time since arriving, the academic mountain ahead feels climbable.)"
    narrator_char "(You have the tools, the resources, and the people. Time to put them to use.)"
    narrator_char "\[ACT 7 COMPLETE] — Library & Academic Resources."
    $ complete_task("attend_study_session")
    window hide
    return

## ============================================================================
## END OF ACT 7 DIALOGUES
## ============================================================================
