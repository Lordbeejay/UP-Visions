## ============================================================================
## ACT 7 DIALOGUES — Library & Academic Resources
## KEY THEME: UPV Library, TLRC peer tutoring, academic tools
## STORY: Jaden is panicking about a paper. Player helps him through the
##        Library → Computer Lab → Prof. Santos → TLRC → Study Session.
## ============================================================================

## --- ACT 7 INIT ---
label act7_start:
    # play music moved to end of previous act
    jump act7_map


## ============================================================================
## ACT 7 STORY — Find Jaden outside the library
## ============================================================================
label act7_npc_jaden:
    window show
    narrator_char "(You spot Jaden near the steps of the library building. The same Jaden from the Banwa entrance on your first day.)"
    narrator_char "(He's got a notebook open on his lap but he's not writing. He's just staring at it.)"
    player_char "Jaden? I haven't seen you since day one."
    jaden "Oh — hey. Yeah. I've been..."
    player_char "What's wrong?"
    jaden "I have a research paper due Friday. For Kas 1. Three sources minimum, APA format, five pages."
    jaden "I have never written an academic paper in my life."
    player_char "Okay. When did you find out?"
    jaden "The first day of class."
    player_char "Jaden, that was two weeks ago."
    jaden "I know. I kept telling myself I'd start tomorrow. And then it was this week."
    jaden "I don't even know what JSTOR is. I Googled it and I got more confused."
    player_char "Have you been inside the library yet?"
    jaden "I've walked past it."
    player_char "Come on."
    jaden "I don't know how to use a library."
    player_char "That's exactly why we're going in."
    narrator_char "(Jaden closes his notebook, grabs his bag, and follows. He looks like a man being walked to his own execution.)"
    jump act7_library_scene


## ============================================================================
## LIBRARY SCENE — Ate Rosa shows them the tools
## ============================================================================
label act7_library_scene:
    narrator_char "(Inside the UPV Library. Cool air, low shelves, the smell of old books and something close to quiet.)"
    narrator_char "(Jaden looks around. He seems surprised it doesn't feel more intimidating.)"
    ate_rosa "Good morning! First time here?"
    jaden "Is it that obvious?"
    ate_rosa "You're both standing at the entrance looking like you're about to ask for directions in a foreign country."
    ate_rosa "I'm Ate Rosa, one of the librarians. Tell me what you need."
    player_char "He has a Kas 1 research paper due Friday. Three academic sources, APA, five pages. He doesn't know where to start."
    ate_rosa "Friday. Okay. That's tight but manageable. Step one — come with me."
    narrator_char "(She moves with quiet efficiency toward the Reference Section.)"
    ate_rosa "For Philippine history topics — which Kas 1 usually covers — you start in two places."
    ate_rosa "First: the Filipiniana Section. Right here. These are books and materials specific to Philippine culture, history, and society."
    ate_rosa "Second: the Thesis and Dissertation Section — past UPV research papers. They cite sources you can then track down yourself."
    jaden "So I use other people's papers to find my sources?"
    ate_rosa "You use their reference lists as a map. That's standard academic practice."
    jaden "...I did not know that was allowed."
    ate_rosa "It's not just allowed — it's how research works. You build on what came before you."
    ate_rosa "Now — your third source should be a journal article. That's where online databases come in."
    jaden "JSTOR. I've heard of it but I can't access it from my phone."
    ate_rosa "You need your UP Mail credentials. Do you have your UP Mail set up?"
    jaden "I have an account but I've never used it for anything."
    ate_rosa "Then your next stop is the computer lab. Kuya Neil there will walk you through setting up remote database access."
    ate_rosa "Once you're connected, JSTOR, ScienceDirect, and Philippine E-Journals are all free through your UP account."
    player_char "How do I borrow physical books in the meantime?"
    ate_rosa "Your student ID is your library card. General circulation books — three days. Reserve books — room use or overnight after 4 PM."
    ate_rosa "Overdue fines add up fast: ₱5 per day for general books, ₱10 per hour for reserve. Return on time."
    ate_rosa "And if you can't find a book — ask us. We know every shelf."
    jaden "This is actually... really useful. Why did no one tell us about this during orientation?"
    ate_rosa "They did. You weren't ready to hear it yet."
    narrator_char "(She pulls a slim volume from the Filipiniana shelf and sets it in Jaden's hands.)"
    ate_rosa "Start here. Agoncillo's 'History of the Filipino People.' If Kas 1 is your course, this is your foundation."
    ate_rosa "Library hours: Monday to Friday, 8 AM to 7 PM. Saturdays, 8 AM to noon."
    ate_rosa "Come back whenever you need help. That's what we're here for."
    narrator_char "(Encyclopedia unlocked: UPV Library.)"
    $ persistent.encyclopedia_unlocks.add("upv_library")
    $ complete_task("talk_ate_rosa")
    jump act7_computer_lab_scene


## ============================================================================
## COMPUTER LAB SCENE — Kuya Neil sets up UP Mail + database access
## ============================================================================
label act7_computer_lab_scene:
    narrator_char "(The computer lab. Rows of desktops, a handwritten sign-in sheet at the door, and Kuya Neil eating a sandwich at his desk.)"
    kuya_neil "Oh! Freshies. Sign the logbook. What do you need?"
    player_char "He needs to set up his UP Mail and access JSTOR for a research paper."
    kuya_neil "Perfect. Come here."
    narrator_char "(Kuya Neil pulls up a chair without ceremony and opens a browser.)"
    kuya_neil "UP Mail first. Your account is firstname.lastname@up.edu.ph — you set the password during enrollment."
    kuya_neil "It's a Google Workspace account. Drive, Docs, Sheets, Meet — all of it. Free, unlimited storage."
    jaden "I thought it was just for email."
    kuya_neil "Most freshmen think that. It's not. It's your entire academic digital infrastructure."
    kuya_neil "Back up everything to Google Drive. Assignments, notes, everything. Don't lose a paper because your laptop died."
    kuya_neil "Now — databases. Go to the UP Remote Access Portal."
    narrator_char "(He types the URL. Jaden watches carefully.)"
    kuya_neil "Log in with your UP Mail. This portal gives you database access as if you're on campus, even from home."
    kuya_neil "JSTOR — academic journals across all fields. Best for humanities and social sciences. Your paper goes here."
    kuya_neil "ScienceDirect — science and medical journals. More useful for CFOS students but good to know."
    kuya_neil "Philippine E-Journals — local academic publications. For Philippine-specific topics, these are gold."
    jaden "Can I search by topic?"
    kuya_neil "Yes. And on JSTOR, filter by date, discipline, and article type. Look for peer-reviewed articles only — professors notice the difference."
    player_char "What about campus WiFi? His phone connection keeps dropping."
    kuya_neil "eduroam is the reliable network. Use your UP Mail credentials to connect. UPV-Guest resets every 24 hours — not great for sustained work."
    kuya_neil "For heavy research sessions — downloads, multiple tabs — come here to the lab. Wired connection is faster and stable."
    kuya_neil "Lab hours: Monday to Friday, 8 AM to 6 PM. Printing is ₱3 per page black-and-white."
    narrator_char "(Jaden opens JSTOR for the first time. Types in his topic. Forty-seven results appear.)"
    jaden "Oh. There's actually a lot here."
    kuya_neil "There's always a lot. The skill is narrowing it down. But that part — you'll need a different expert for."
    narrator_char "(He nods toward the hallway.)"
    kuya_neil "Prof. Santos has office hours right now. Room 204. She'll help you figure out which sources are actually worth using."
    narrator_char "(Encyclopedia unlocked: Computer Lab & UP Mail.)"
    $ persistent.encyclopedia_unlocks.add("computer_lab")
    $ complete_task("talk_kuya_neil")
    jump act7_prof_santos_scene


## ============================================================================
## PROF. SANTOS SCENE — Research process, APA, critical thinking
## ============================================================================
label act7_prof_santos_scene:
    narrator_char "(Room 204. Prof. Santos is at her desk marking papers. She looks up at a knock on the door.)"
    prof_santos "Come in. Freshmen — I can always tell. Sit down."
    player_char "Kuya Neil sent us. Jaden has a Kas 1 research paper due Friday and he's just started."
    prof_santos "Friday. And it's Wednesday."
    jaden "I know."
    prof_santos "I'm not going to lecture you on time management. You're already aware of the problem. Let's solve it."
    prof_santos "Show me what you have so far."
    narrator_char "(Jaden opens his notebook. One paragraph. Half a bibliography. Three sources he's clearly not read.)"
    prof_santos "Alright. First things first: what's your argument?"
    jaden "My argument?"
    prof_santos "A research paper is not a summary. It is an argument supported by evidence. What is your claim?"
    jaden "I... thought I just had to write about the topic."
    prof_santos "That's the most common freshman mistake. You describe when you should be arguing."
    prof_santos "Tell me your topic."
    jaden "The Propaganda Movement."
    prof_santos "Good. Now — what do you want to say ABOUT the Propaganda Movement that isn't just retelling it?"
    jaden "That it... failed? But it still mattered?"
    prof_santos "That is a thesis. The movement failed politically but succeeded in reshaping Filipino national consciousness."
    prof_santos "Now everything you write — every source you cite — must support or complicate that argument."
    prof_santos "This is what research means at UP. Not collecting facts. Building a case."
    player_char "What about his sources? He found some on JSTOR but doesn't know how to evaluate them."
    prof_santos "For journal articles: check the author's credentials, the publication, and the date. Peer-reviewed journals only."
    prof_santos "For books: the Filipiniana section has primary sources. Eyewitness accounts, original documents. Those carry weight."
    prof_santos "And for citation — APA 7th edition. Learn it now. Plagiarism at UP is not just a failed grade — it's an academic offense that goes on your record."
    prof_santos "Paraphrase, don't copy. Cite everything you borrowed, even ideas. If you're unsure, cite it anyway."
    jaden "APA format looks complicated. The in-text citations, the reference list format—"
    prof_santos "That's what the TLRC is for."
    player_char "The TLRC?"
    prof_santos "Teaching and Learning Resource Center. In the CAS building. They have an academic writing workshop specifically for freshmen."
    prof_santos "They'll walk you through APA format, paper structure, and they'll review your draft before you submit it."
    prof_santos "I've referred students there before. Several of them went from near-failing to Dean's List by second semester."
    prof_santos "The tool exists. Use it."
    narrator_char "(She writes a note on a slip of paper and hands it to Jaden.)"
    prof_santos "This is the argument structure outline I give my own students. Use it as a scaffold for your paper."
    prof_santos "You have enough time if you start tonight. The library closes at 7. Be there until it does."
    jaden "Thank you, Prof."
    prof_santos "Don't thank me. Write the paper."
    narrator_char "(Encyclopedia unlocked: UP Research Culture.)"
    $ persistent.encyclopedia_unlocks.add("up_research")
    $ complete_task("talk_prof_santos")
    if "sq_up_mandates" not in subquests_completed:
        menu:
            "★ Before we go — quiz me on UP's three mandates.":
                jump sq_up_mandates
            "(Got it. We'll head to the TLRC.)":
                pass
    window hide
    jump act7_tlrc_entrance


## ============================================================================
## TLRC ENTRANCE — Bea finds them in the hallway
## ============================================================================
label act7_tlrc_entrance:
    window show
    narrator_char "(In the CAS corridor, heading toward the TLRC, you nearly walk into Bea.)"
    bea "Oh! You two. Are you going where I think you're going?"
    player_char "TLRC. Prof. Santos sent us."
    bea "I was just there! I signed up for the writing workshop."
    bea "I'm Bea, by the way — we're in the same Kas 1 section."
    jaden "Jaden."
    bea "I know. You sit in the back and look like you're either asleep or having a very intense internal conversation."
    jaden "Both, usually."
    bea "Come on — I'll introduce you to the coordinator. She's really good."
    jump act7_visit_tlrc


## ============================================================================
## TLRC SCENE — Full support service visit
## ============================================================================
label act7_visit_tlrc:
    window show
    narrator_char "(The TLRC. A bright room at the end of the CAS hall. A banner above the door: 'Free Academic Support for All UPV Students.')"
    narrator_char "(Inside: whiteboards with formulas and paper outlines, study carrels, a shelf of supplementary materials. Two tutors are already working with students.)"
    tlrc_coord "Bea! And you brought friends."
    bea "They need the writing workshop and a paper review before Friday."
    tlrc_coord "Friday. Okay — sit down, let me explain what we can do."
    tlrc_coord "I'm the TLRC Coordinator. We exist for one reason: no UP student should fail because they didn't have help."
    tlrc_coord "Four services. Let me walk you through them quickly."
    tlrc_coord "One — Peer Tutoring. Juniors and seniors who excelled in specific subjects, matched to you one-on-one."
    tlrc_coord "They don't do your work. They guide you until you can do it yourself. There's a difference."
    jaden "What subjects?"
    tlrc_coord "College Algebra, General Chemistry, Statistics, Basic Economics, Research Methods, and academic writing."
    tlrc_coord "Two — Supplemental Instruction. For gateway courses with high failure rates — think math, chemistry, stats."
    tlrc_coord "An SI Leader runs weekly review sessions. Not a re-lecture — a guided discussion. Students who attend consistently score higher."
    tlrc_coord "Three — Academic Writing Support. Workshops on paper structure, APA 7th edition, argumentation, anti-plagiarism."
    tlrc_coord "And paper review: bring a draft two days before your deadline. We read it for structure, clarity, and citation — not content."
    jaden "Can you review mine? It's due Friday."
    tlrc_coord "Bring a draft by tomorrow, 3 PM. That gives us time to give you feedback before you finalize."
    jaden "I don't have a draft yet."
    tlrc_coord "Then tonight you write. Tomorrow at 3, you bring what you have — even rough. We work with rough."
    bea "That's exactly what I needed to hear."
    tlrc_coord "Four — Study Skills Seminars. Time management, active reading, test preparation. Open to all, free."
    player_char "What's the biggest thing freshmen get wrong academically?"
    tlrc_coord "Waiting. They wait until the problem is a crisis before they come here."
    tlrc_coord "The students who benefit most are the ones who show up early — before the grade drops, before the deadline panic."
    tlrc_coord "The library has the resources. We teach you how to use them. Those two combined — that's how students go from surviving to thriving."
    player_char "Can he also observe a tutoring session? So he knows what to expect?"
    tlrc_coord "Right this way."
    narrator_char "(She leads you to a carrel where a third-year is working with a freshman on an essay outline.)"
    peer_tutor "Okay — before we fix this paragraph, tell me: what is this sentence trying to argue?"
    narrator_char "(The freshman thinks. Ventures an answer. The tutor listens, asks another question, doesn't give the answer.)"
    narrator_char "(Five minutes later, the freshman rewrites the sentence herself — and it's better.)"
    jaden "(quietly) That's what Prof. Santos was doing. Asking questions instead of just telling me."
    player_char "Yeah."
    jaden "I think I've been waiting for someone to just tell me what to do."
    player_char "UP doesn't really work that way."
    jaden "I'm starting to understand that."
    narrator_char "(The coordinator hands Jaden a Tutoring Request Form and a workshop schedule.)"
    tlrc_coord "Office hours: Monday to Friday, 8 AM to 5 PM. See you tomorrow at 3."
    narrator_char "(Encyclopedia unlocked: Teaching and Learning Resource Center (TLRC).)"
    $ persistent.encyclopedia_unlocks.add("tlrc")
    $ complete_task("visit_tlrc")
    $ complete_task("talk_classmate_bea")
    if "sq_apa_challenge" not in subquests_completed:
        menu:
            "★ Before we leave — test me on APA citation format.":
                jump sq_apa_challenge
            "(Got it. See you tomorrow.)":
                pass
    window hide
    jump act7_resolution


## ============================================================================
## RESOLUTION — Outside TLRC, evening
## ============================================================================
label act7_resolution:
    window show
    narrator_char "(Outside. The afternoon has cooled into early evening. The library lights are still on.)"
    jaden "I feel like I just attended three weeks of orientation in one afternoon."
    player_char "You kind of did."
    jaden "Library. Computer lab. Prof. Santos. TLRC."
    jaden "These were all here the whole time."
    player_char "Yeah."
    jaden "I just... never went in."
    player_char "You went in today."
    bea "And you're going back tomorrow. With a draft."
    jaden "With a draft. Right."
    narrator_char "(A pause. Somewhere in the library building, a door closes. The last of the afternoon students heading home.)"
    jaden "Hey — do you want to form a study group? The three of us?"
    bea "I already have one. Tuesdays and Thursdays, 4 PM, library study room 2."
    bea "You're both in now."
    jaden "What if I show up and I don't know anything?"
    bea "That's the point of the group, Jaden."
    narrator_char "(You walk back toward the dorms together. Jaden still looks tired. But it's a different kind of tired.)"
    narrator_char "(Not the paralyzed kind. The kind that comes after you've actually done something.)"
    narrator_char "(Tomorrow he'll sit in the TLRC with a rough draft and a counselor who asks questions instead of giving answers.)"
    narrator_char "(And that — the willingness to show up with what he has — is the whole skill.)"
    narrator_char "\[ACT 7 COMPLETE] — Library & Academic Resources."
    $ complete_task("attend_study_session")
    window hide
    return


## ============================================================================
## END OF ACT 7 DIALOGUES
## ============================================================================
play music "audio/Act8.mp3" fadein 1.0
