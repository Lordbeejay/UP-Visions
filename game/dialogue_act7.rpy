## ============================================================================
## ACT 7 DIALOGUES — Library & Academic Resources
## KEY THEME: UPV Library, Computer Lab, Research Writing, TLRC peer tutoring
## STORY: Jaden is panicking about a paper. Player helps him through 4 stops.
## INTERACTIVE: Menu choices, inline quizzes, mandatory sq_apa_challenge &
##              sq_up_mandates mini-games
## ============================================================================

## --- ACT 7 INIT ---
label act7_start:
    jump act7_map


## ============================================================================
## SCENE 1 — Ate Rosa / Library
## INTERACTIVE: Menu-driven tour + inline library quiz
## ============================================================================
label act7_npc_ate_rosa:
    scene expression "images/ui/old_ad.png"
    window show
    narrator_char "(Jaden is on the library steps, notebook open, writing nothing. He spots you and looks relieved.)"
    jaden "You're here. Good. I have a Kas 1 paper due Friday. Three sources, APA, five pages."
    jaden "I've never written an academic paper. I don't even know what JSTOR is."
    player_char "Have you been inside the library yet?"
    jaden "I've walked past it."
    player_char "Come on."
    scene expression "images/ui/Library_Interior.png"
    narrator_char "(Ate Rosa catches you both at the entrance the way librarians catch every lost freshie — quietly, calmly, like she's seen it a thousand times.)"
    ate_rosa "First time?"
    jaden "Is it that obvious?"
    ate_rosa "You're standing at the door like you need permission to enter. You don't. What do you need?"
    player_char "Research paper, due Friday. He doesn't know where to start."
    ate_rosa "Okay. Ask me what you need to know."

    $ act7_library_asked = []

label act7_library_loop:
    menu:
        "Where do I find Philippine history sources?" if "ph_sources" not in act7_library_asked:
            $ act7_library_asked.append("ph_sources")
            jump act7_lib_ph
        "How does borrowing books work?" if "borrow" not in act7_library_asked:
            $ act7_library_asked.append("borrow")
            jump act7_lib_borrow
        "What about online journals like JSTOR?" if "jstor" not in act7_library_asked:
            $ act7_library_asked.append("jstor")
            jump act7_lib_jstor
        "I think we have what we need.":
            jump act7_library_end

label act7_lib_ph:
    ate_rosa "Two places. The Filipiniana Section — books and materials specific to Philippine history and culture."
    ate_rosa "And the Thesis and Dissertation Section — past UPV research papers. Use their reference lists as a map to find your own sources."
    jaden "That's allowed?"
    ate_rosa "It's not just allowed — it's how research works. You build on what came before."
    jump act7_library_loop

label act7_lib_borrow:
    ate_rosa "Your student ID is your library card. General books — three days. Reserve books — room use only, or overnight after 4 PM."
    ate_rosa "Overdue fines: ₱5 per day for general books, ₱10 per hour for reserve. Return on time."
    ate_rosa "Can't find something? Ask us. We know every shelf."
    jump act7_library_loop

label act7_lib_jstor:
    ate_rosa "JSTOR needs UP Mail credentials. Once you're connected, JSTOR, ScienceDirect, and Philippine E-Journals are all free."
    ate_rosa "For setting that up — Kuya Neil at the computer lab. Room down the hall."
    jaden "I have UP Mail but I've never actually used it."
    ate_rosa "He'll fix that in ten minutes."
    jump act7_library_loop

label act7_library_end:
    narrator_char "(She pulls Agoncillo's 'History of the Filipino People' from the Filipiniana shelf and hands it to Jaden.)"
    ate_rosa "For Kas 1, this is your foundation. Library hours: Monday to Friday, 8 AM to 7 PM. Saturdays until noon."
    ate_rosa "One quick check before you go. To make sure this sticks."

    ## ── Inline library quiz ───────────────────────────────────────────────────
    python:
        sq_quiz_state.setup(
            "Know Your Library",
            "Ate Rosa checks if you'll actually find what you need",
            "📚",
            [
                (
                    "Jaden needs a 1960s book on Filipino nationalist movements. Which section first?",
                    [
                        ("Filipiniana Section — materials specific to Philippine culture and history", True, "Correct. Filipiniana is the starting point for Philippine-specific topics. General shelves carry broader, often non-local content."),
                        ("General Circulation — all books are mixed together alphabetically", False, "The library separates collections by type. Philippine-specific materials are in the Filipiniana Section — looking in General Circulation will waste your time."),
                        ("Thesis and Dissertation Section — that is where all old academic texts go", False, "Theses and dissertations are student research papers, not published books. For published books on Philippine topics, Filipiniana Section is correct."),
                    ]
                ),
                (
                    "Jaden forgets to return a Reserve Book for two hours. How much is the fine?",
                    [
                        ("₱20 — reserve books are ₱10 per hour overdue", True, "Correct. Reserve books carry a steeper fine than general books because they're high-demand limited copies. Return them on time."),
                        ("₱10 — same rate as general books at ₱5 per day", False, "General books are ₱5 per day. Reserve books are ₱10 per HOUR — a much higher rate because they're limited, in-demand copies."),
                        ("No fine — reserve books can be kept overnight for free", False, "Reserve books can only be taken overnight after 4 PM, and they still carry overdue fines of ₱10 per hour if kept past the agreed return time."),
                    ]
                ),
                (
                    "Jaden wants to access JSTOR from his dorm room. What does he need?",
                    [
                        ("UP Mail login through the UP Remote Access Portal — gives database access from anywhere", True, "Correct. UP Mail credentials unlock the Remote Access Portal, which gives full off-campus database access as if you're on campus."),
                        ("A separate application to the library, approved within three working days", False, "No separate application is needed. Your UP Mail account automatically qualifies you for database access through the Remote Access Portal."),
                        ("A physical library card issued at the circulation desk — different from the student ID", False, "Your student ID IS your library card. No separate card is needed. Database access uses your UP Mail, not a physical card."),
                    ]
                ),
            ]
        )
    window hide
    call screen sq_quiz_game()
    $ _lib_quiz = _return
    window show

    if _lib_quiz >= 2:
        ate_rosa "Good. You won't be lost in here. Come back whenever you need help."
    else:
        ate_rosa "Review what you missed. The library is only useful if you know how to use it."

    narrator_char "(Encyclopedia unlocked: UPV Library.)"
    $ persistent.encyclopedia_unlocks.add("upv_library")
    $ complete_task("talk_ate_rosa")
    window hide
    return


## ============================================================================
## SCENE 2 — Kuya Neil / Computer Lab
## INTERACTIVE: Menu-driven setup + UP Mail knowledge check
## ============================================================================
label act7_npc_kuya_neil:
    scene expression "images/ui/classroom.png"
    window show
    narrator_char "(Computer lab. Rows of desktops. Kuya Neil at the sign-in desk.)"
    kuya_neil "Freshies. Sign the logbook. What do you need?"
    player_char "UP Mail setup and JSTOR access. Research paper due Friday."
    kuya_neil "Perfect. Come here."
    narrator_char "(He pulls up a chair and opens a browser without ceremony.)"
    kuya_neil "Your UP Mail is firstname.lastname@up.edu.ph — Google Workspace account. What do you want to know about it?"

    $ act7_lab_asked = []

label act7_lab_loop:
    menu:
        "What can UP Mail actually do besides email?" if "upmail" not in act7_lab_asked:
            $ act7_lab_asked.append("upmail")
            jump act7_lab_upmail
        "How do I access JSTOR from home?" if "jstor" not in act7_lab_asked:
            $ act7_lab_asked.append("jstor")
            jump act7_lab_jstor
        "What about the campus WiFi?" if "wifi" not in act7_lab_asked:
            $ act7_lab_asked.append("wifi")
            jump act7_lab_wifi
        "We're good. Set him up.":
            jump act7_lab_end

label act7_lab_upmail:
    kuya_neil "Drive, Docs, Sheets, Meet — full Google Workspace, unlimited storage."
    kuya_neil "Back up everything there. Don't lose a paper because your laptop died."
    jump act7_lab_loop

label act7_lab_jstor:
    kuya_neil "UP Remote Access Portal — log in with UP Mail. Full database access from anywhere, as if you're on campus."
    kuya_neil "JSTOR for humanities and social sciences. ScienceDirect for sciences. Philippine E-Journals for local research."
    kuya_neil "On JSTOR: filter by date and discipline, peer-reviewed only. Professors notice the difference."
    jump act7_lab_loop

label act7_lab_wifi:
    kuya_neil "eduroam — reliable, uses your UP Mail credentials. UPV-Guest resets every 24 hours, not great for sustained work."
    kuya_neil "For heavy downloads and multiple tabs, come here. Wired is faster and stable."
    kuya_neil "Lab hours: Monday to Friday, 8 AM to 6 PM. Printing — ₱3 per page, black-and-white."
    jump act7_lab_loop

label act7_lab_end:
    narrator_char "(Kuya Neil navigates to JSTOR, logs Jaden in with his UP Mail, and types in the search topic.)"
    narrator_char "(Forty-seven results. Jaden stares at the screen.)"
    jaden "There's actually a lot here."
    kuya_neil "There's always a lot. The skill is narrowing it down. For that — Prof. Santos. Room 204, office hours now."
    player_char "Quick question before we go."
    kuya_neil "Go ahead."

    ## ── Inline UP Mail / database quiz ───────────────────────────────────────
    python:
        sq_quiz_state.setup(
            "Digital Tools Check",
            "Kuya Neil tests what you just learned",
            "💻",
            [
                (
                    "Jaden finishes a draft in Google Docs at 11 PM and his laptop dies. Is his work lost?",
                    [
                        ("No — Google Docs auto-saves to Drive in real time", True, "Correct. Google Docs saves every keystroke to Drive automatically. As long as he was working in Docs, nothing is lost."),
                        ("Yes — he needs to manually export and save to a USB drive after every session", False, "Manual exports are optional. Google Docs auto-saves to Drive. His work is safe the moment he types it."),
                        ("Only if he remembered to hit the Save button before the laptop died", False, "Google Docs has no manual Save button — it saves automatically and continuously. This is one of its core features."),
                    ]
                ),
                (
                    "Which WiFi network should Jaden use for a 3-hour research session in the dorm?",
                    [
                        ("eduroam — stable, uses UP Mail credentials, doesn't reset", True, "Correct. eduroam is the reliable network for sustained work. UPV-Guest resets every 24 hours and is not built for extended sessions."),
                        ("UPV-Guest — open access, no login needed, faster connection", False, "UPV-Guest resets every 24 hours and is not designed for sustained work. eduroam is the right choice for long sessions."),
                        ("It doesn't matter — both networks deliver the same performance for research tasks", False, "eduroam is the campus-grade network. UPV-Guest has usage limits and resets. For serious work, always use eduroam."),
                    ]
                ),
                (
                    "Jaden finds an article on JSTOR dated 2001. What should he check before citing it?",
                    [
                        ("Author credentials, the journal's peer-review status, and whether newer research supersedes it", True, "Exactly. Older sources are not automatically bad, but you must verify they haven't been contradicted or updated by more recent peer-reviewed work."),
                        ("Nothing — JSTOR only hosts verified academic sources, so all results are equally citable", False, "JSTOR hosts a wide range of materials. The student still needs to check peer-review status, author credentials, and relevance. Not all JSTOR content is equal."),
                        ("Only the date — anything published more than five years ago should not be cited in a current paper", False, "Age is one factor but not a hard rule. A foundational 1968 history text may be more authoritative than a 2020 blog post. Check peer-review status and authority, not just the date."),
                    ]
                ),
            ]
        )
    window hide
    call screen sq_quiz_game()
    $ _lab_quiz = _return
    window show

    if _lab_quiz >= 2:
        kuya_neil "You've got it. The tools work — you just have to use them."
    else:
        kuya_neil "Review what you missed. The tools are only as good as how well you understand them."

    narrator_char "(Encyclopedia unlocked: Computer Lab & UP Mail.)"
    $ persistent.encyclopedia_unlocks.add("computer_lab")
    $ complete_task("talk_kuya_neil")
    window hide
    return


## ============================================================================
## SCENE 3 — Prof. Santos / Research Writing
## INTERACTIVE: Thesis-building menu + sq_up_mandates (mandatory)
## ============================================================================
label act7_npc_prof_santos:
    scene expression "images/ui/room204.png"
    window show
    narrator_char "(Room 204. Prof. Santos is marking papers. She looks up at the knock.)"
    prof_santos "Freshmen. Sit down."
    player_char "Kuya Neil sent us. Research paper, due Friday, just started."
    prof_santos "Friday. It's Wednesday. Show me what you have."
    narrator_char "(Jaden opens his notebook. One paragraph. Half a bibliography. Three sources he hasn't read.)"
    prof_santos "Alright. What's your argument?"
    jaden "My argument?"
    prof_santos "A research paper argues something. It doesn't just describe. What is your claim?"
    jaden "I thought I just... had to write about the topic."
    prof_santos "That's the most common freshman mistake. Your topic is the Propaganda Movement?"
    jaden "Yes, Ma'am."
    prof_santos "What do you want to say ABOUT it?"
    narrator_char "(Jaden thinks. You can help him.)"

    menu:
        "The movement failed politically, but it changed Filipino consciousness.":
            $ act7_jaden_thesis = "failure"
            jump act7_santos_thesis_good
        "It was a turning point that made independence inevitable.":
            $ act7_jaden_thesis = "turning"
            jump act7_santos_thesis_good
        "It was mostly the work of ilustrado elites, not ordinary Filipinos.":
            $ act7_jaden_thesis = "class"
            jump act7_santos_thesis_good
        "I don't know. I need to research more first.":
            jump act7_santos_thesis_weak

label act7_santos_thesis_weak:
    prof_santos "That's honest. But you don't research first, then form a claim. You form a working claim, research to test it, then refine it."
    prof_santos "Without a direction, you'll collect facts forever and never write a paper."
    prof_santos "Start with: the movement failed politically but succeeded in changing consciousness. Then test it."
    $ act7_jaden_thesis = "failure"
    jump act7_santos_thesis_good

label act7_santos_thesis_good:
    prof_santos "That is a thesis. Not a topic — a claim. Now everything you write must support or complicate it."
    prof_santos "Every source you cite: ask yourself — does this strengthen, weaken, or nuance my argument?"
    prof_santos "That is research at UP. Not collecting facts. Building a case."
    player_char "What makes a source good enough to cite?"
    prof_santos "Peer-reviewed journal articles and primary sources — first. Check author credentials and publication date."
    prof_santos "On citation: APA 7th edition. Plagiarism is not just copy-paste — closely paraphrasing without citation is also a violation."
    prof_santos "It goes on your academic record. It is not a small thing."
    jaden "APA format looks complicated."
    prof_santos "That's what the TLRC is for. CAS building. Writing workshop, paper review, APA guide. Go there today."
    narrator_char "(She slides a one-page argument outline across the desk.)"
    prof_santos "Scaffold your paper on this. You have time if you start tonight."
    jaden "Thank you, Prof."
    prof_santos "Don't thank me. Write the paper."
    narrator_char "(She reopens her markings. The meeting is over.)"
    narrator_char "(She pauses — looks up one more time.)"
    prof_santos "You know why UP has three mandates and not just one?"

    ## ── Mandatory subquest: UP Three Mandates quiz ───────────────────────────
    if "sq_up_mandates" not in subquests_completed:
        jump sq_up_mandates
    else:
        prof_santos "Instruction, research, extension. You are part of all three."

    narrator_char "(Encyclopedia unlocked: UP Research Culture.)"
    $ persistent.encyclopedia_unlocks.add("up_research")
    $ complete_task("talk_prof_santos")
    window hide
    return


## ============================================================================
## SCENE 4 — Bea + TLRC Visit
## INTERACTIVE: Menu-driven coordinator tour + sq_apa_challenge (mandatory)
## ============================================================================
label act7_npc_classmate_bea:
    scene expression "images/ui/cas_hallway.png"
    window show
    narrator_char "(CAS corridor. Bea nearly walks into you both.)"
    bea "Oh! You two — are you going to the TLRC?"
    player_char "Prof. Santos sent us."
    bea "I'm Bea — same Kas 1 section. Come on, I'll introduce you."
    jaden "I sit in the back. I zone out a lot."
    bea "I know. You're going in today."
    narrator_char "(The TLRC. A bright room at the end of the hall. Banner: 'Free Academic Support for All UPV Students.')"
    narrator_char "(Two tutors are already working with students. Whiteboards covered in essay outlines.)"
    tlrc_coord "Bea! And you brought friends."
    bea "They need a paper review before Friday."
    tlrc_coord "Friday — okay. Tell me what you need most."

    $ act7_tlrc_asked = []

label act7_tlrc_loop:
    menu:
        "What is peer tutoring, exactly?" if "tutoring" not in act7_tlrc_asked:
            $ act7_tlrc_asked.append("tutoring")
            jump act7_tlrc_tutoring
        "Can you review my draft before I submit?" if "review" not in act7_tlrc_asked:
            $ act7_tlrc_asked.append("review")
            jump act7_tlrc_review
        "What's the writing workshop like?" if "workshop" not in act7_tlrc_asked:
            $ act7_tlrc_asked.append("workshop")
            jump act7_tlrc_workshop
        "Can we watch a session right now?":
            jump act7_tlrc_observe

label act7_tlrc_tutoring:
    tlrc_coord "Juniors and seniors who excelled in the subject, matched to you one-on-one."
    tlrc_coord "They don't do your work. They ask questions until you can do it yourself."
    tlrc_coord "Subjects: College Algebra, Chemistry, Statistics, Economics, Research Methods, and academic writing."
    jump act7_tlrc_loop

label act7_tlrc_review:
    tlrc_coord "Bring a draft two days before your deadline. We read it for structure, clarity, and citation — not content."
    jaden "I don't have a draft yet."
    tlrc_coord "Then tonight you write. Tomorrow, 3 PM — bring what you have. Even rough. We work with rough."
    jump act7_tlrc_loop

label act7_tlrc_workshop:
    tlrc_coord "Paper structure, APA 7th edition, argumentation, anti-plagiarism — all in one session."
    tlrc_coord "Study Skills Seminars also: time management, active reading, test prep. Open to everyone, free."
    tlrc_coord "The students who benefit most show up early — before the grade drops."
    jump act7_tlrc_loop

label act7_tlrc_observe:
    scene expression "images/ui/tlrc.png"
    narrator_char "(She leads you to a carrel. A third-year is working with a freshman on an essay paragraph.)"
    peer_tutor "Before we fix this — tell me what this sentence is trying to argue."
    narrator_char "(The freshman thinks. Ventures an answer. The tutor asks another question, doesn't give the answer.)"
    narrator_char "(Five minutes later, the freshman rewrites the sentence herself — and it's better.)"
    jaden "(quietly) That's what Prof. Santos was doing. Questions instead of answers."
    player_char "Yeah."
    jaden "I've been waiting for someone to just tell me what to do."
    player_char "UP doesn't really work that way."
    jaden "I'm starting to understand that."
    jump act7_tlrc_finish

label act7_tlrc_finish:
    narrator_char "(The coordinator hands Jaden a Tutoring Request Form and a workshop schedule.)"
    tlrc_coord "Hours: Monday to Friday, 8 AM to 5 PM. See you tomorrow at 3, Jaden."
    bea "Before we leave — I'm actually going to test you on APA. Every paper you write at UP will need it."

    ## ── Mandatory subquest: APA Challenge quiz ───────────────────────────────
    if "sq_apa_challenge" not in subquests_completed:
        jump sq_apa_challenge
    else:
        bea "Good. You already know it. Don't let your guard down."

    narrator_char "(Encyclopedia unlocked: Teaching and Learning Resource Center (TLRC).)"
    $ persistent.encyclopedia_unlocks.add("tlrc")
    $ complete_task("visit_tlrc")
    $ complete_task("talk_classmate_bea")
    window hide
    return


## ============================================================================
## SCENE 5 — Study Session (Library Study Room)
## INTERACTIVE: Player chooses the study group's focus + short resolution
## ============================================================================
label act7_study_session:
    scene expression "images/ui/Library_Interior.png"
    window show
    narrator_char "(Library study room 2. Tuesday, 4 PM. Bea is already there with notes spread out.)"
    bea "You both made it."
    jaden "I turned in the draft. TLRC gave me feedback. I rewrote the introduction."
    player_char "How did it feel?"
    jaden "Terrible. Then better."
    bea "That's writing."
    narrator_char "(Three notebooks, three laptops, one shared carrel. Outside, the library is filling up with students.)"
    bea "What do we focus on first?"

    menu:
        "Jaden's Kas 1 argument — let's stress-test the thesis.":
            jump act7_study_thesis
        "APA citations — let's check everyone's reference lists.":
            jump act7_study_apa
        "Study strategies — this week wiped everyone out.":
            jump act7_study_skills

label act7_study_thesis:
    bea "Okay. Jaden, state your thesis out loud. We'll ask questions."
    jaden "The Propaganda Movement failed politically but succeeded in reshaping Filipino national consciousness."
    player_char "What's your strongest piece of evidence?"
    jaden "Rizal's Noli — it didn't end Spanish rule, but it changed how Filipinos saw themselves."
    bea "Good. That's your anchor paragraph. Build outward from that."
    narrator_char "(An hour passes. Arguments sharpened. Sources connected. Jaden's paper becomes a paper.)"
    jump act7_study_end

label act7_study_apa:
    bea "Reference lists out. I'll check in-text citations; you check the reference list format."
    narrator_char "(The next hour: hunting for missing DOIs, fixing italics, correcting sentence-case titles.)"
    jaden "This is tedious."
    bea "Every time. But professors notice. Points lost on format are the most avoidable losses in any paper."
    narrator_char "(By the time they finish, every citation is clean.)"
    jump act7_study_end

label act7_study_skills:
    player_char "What's everyone's biggest problem this week?"
    jaden "I procrastinated until it was a crisis."
    bea "I over-read and under-wrote. Too many sources, too little structure."
    player_char "Two different problems, same fix: start earlier, with less."
    bea "One draft, ugly, on time beats a perfect draft after the deadline."
    jaden "That is the most useful thing anyone has said to me all week."
    narrator_char "(They work through the rest of the afternoon. Not perfectly, but together.)"
    jump act7_study_end

label act7_study_end:
    narrator_char "(6:45 PM. Library lights flicker once — fifteen-minute warning before closing.)"
    jaden "Same time next week?"
    bea "Tuesdays and Thursdays, 4 PM. You're both in now."
    jaden "I walked past this library for two weeks before going in."
    player_char "You went in. That's the part that matters."
    narrator_char "(They pack up. The library empties around them.)"
    narrator_char "(Jaden still looks tired. But it's a different kind — not the paralyzed kind. The kind that comes after actually doing something.)"
    narrator_char "(Tomorrow: the TLRC at 3 PM, with a draft and questions and the willingness to show up with what he has.)"
    narrator_char "(That — the willingness to show up — is the whole skill.)"
    $ complete_task("attend_study_session")
    window hide
    return


## ============================================================================
## END OF ACT 7 DIALOGUES
## ============================================================================
play music "audio/Act8.mp3" fadein 1.0
