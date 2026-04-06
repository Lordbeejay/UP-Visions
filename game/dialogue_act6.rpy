## ============================================================================
## ACT 6 DIALOGUES — Student Support Services
## KEY THEME: GCSU (mental health & counseling), HSU (health), Allowance & Scholarships
## STORY: Dan is unwell. Player helps him through HSU → GCSU → Scholarship Service.
## ============================================================================

## --- ACT 6 INIT ---
label act6_start:
    # play music moved to end of previous act
    jump act6_map

## --- Compatibility stubs for removed NPCs (old saves may reference these) ---
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
## ACT 6 STORY — Find Dan
## ============================================================================
label act6_npc_dan:
    window show
    narrator_char "(You're cutting through the CAS corridor when you spot Dan sitting on a bench near the water fountain.)"
    narrator_char "(He's hunched forward, elbows on his knees, staring at the ground. He looks pale.)"
    player_char "Dan?"
    dan "Oh. Hey."
    player_char "You look terrible. Are you okay?"
    dan "I'm fine."
    player_char "You said that last time too."
    dan "..."
    dan "I feel a bit dizzy. I think it's the heat."
    player_char "Have you eaten today?"
    dan "..."
    player_char "Dan."
    dan "Yesterday. I had something yesterday."
    player_char "That's not fine. Come on."
    dan "Where are we going?"
    player_char "HSU. Now."
    dan "It's not that serious—"
    player_char "You haven't eaten in a day, you're dizzy, and you're gray. It's that serious."
    narrator_char "(Dan doesn't argue. That, more than anything, tells you how bad he's actually feeling.)"
    jump act6_at_hsu


## ============================================================================
## HSU SCENE — Physical checkup, services explained through treatment
## ============================================================================
label act6_at_hsu:
    narrator_char "(The Health Services Unit. Located near the Administration Building, a green cross sign above the door.)"
    narrator_char "(A handwritten notice: 'HSU — Open Mon–Fri, 8:00 AM to 5:00 PM. All UPV students served FREE.')"
    narrator_char "(The nurse at the triage desk takes one look at Dan and immediately points him to a chair.)"
    hsu_nurse "Sit. Student ID."
    narrator_char "(Dan hands it over. The nurse logs him in without ceremony.)"
    hsu_nurse "When did you last eat?"
    dan "Yesterday morning."
    hsu_nurse "And before that?"
    dan "I've been... not very hungry."
    narrator_char "(She takes his blood pressure, temperature, and pulse. Notes every reading on a form.)"
    hsu_nurse "Blood pressure is low — 90 over 60. Temperature normal. Pulse weak. You're dehydrated and hypoglycemic."
    hsu_nurse "How long has this been going on?"
    dan "A week, maybe."
    narrator_char "(The physician comes out from the inner office. She looks at the chart, then at Dan.)"
    physician "First year?"
    dan "Yes, Ma'am."
    physician "Tell me honestly — is this just physical? Or is something else going on?"
    dan "I don't know what you mean."
    physician "Are you sleeping? Going to class? Do you feel like yourself?"
    narrator_char "(A long pause.)"
    dan "Not really. To all of those."
    physician "How's your allowance situation?"
    narrator_char "(Dan looks at the floor.)"
    dan "My parents haven't been able to send anything this month. They're dealing with something back home."
    dan "I didn't want to make it a big deal. I thought I could get through it."
    physician "You haven't eaten properly in a week because you have no money for food."
    dan "When you say it like that it sounds worse than it is."
    physician "It sounds exactly as serious as it is."
    physician "You came in dizzy. The dizziness is from not eating. The not eating is from having no money. The stress of carrying that alone is affecting your sleep, your concentration, your mood."
    physician "This isn't just physical, Dan. And it isn't something you should be managing alone."
    player_char "What do we do?"
    physician "Two things. First — immediate medical care."
    physician "I'm giving you oral rehydration salts for the dehydration, a glucose drink for your blood sugar, and a vitamin B complex pack."
    physician "The HSU maintains a stock of essential medicines — analgesics, antihistamines, antacids, ORS, wound care supplies, and vitamins. All free for enrolled students."
    physician "You show your student ID, we log the consultation, and you receive what you need at no cost."
    player_char "What about things the HSU can't handle?"
    physician "If a case is beyond our capacity, we issue a referral letter and coordinate with Miagao District Hospital — a few minutes from campus."
    physician "For specialist care, we refer to Western Visayas Medical Center in Iloilo City. You are not left to navigate that alone."
    physician "We also handle the Annual Physical Examination required for your enrollment clearance — height, weight, vision, blood pressure, general health screening."
    physician "And if you miss class due to illness, come here first. We issue a Medical Certificate that documents your condition. Bring it to your professors as official documentation of your absence."
    dan "I didn't know any of that."
    physician "Most freshmen don't until they need it. Now you do."
    physician "Second thing — I'm writing you a referral to the GCSU. The Guidance and Counseling Services Unit."
    dan "I don't need a counselor. I'm not—"
    physician "I know what you're about to say. What you're carrying — the stress, the isolation, the shame of struggling — that is exactly what the GCSU exists for."
    physician "Going there is not a sign that something is wrong with you. It is a sign that you are taking care of yourself."
    physician "The HSU and the GCSU work together. When a student comes in physically run-down and the root is psychological or financial, we refer. That's the system."
    narrator_char "(She writes the referral, hands it to Dan with the medication pack and a glucose drink.)"
    physician "Eat something the moment you leave. Then go directly to the GCSU."
    dan "...Thank you, Ma'am."
    narrator_char "(Encyclopedia unlocked: HSU — Health Services Unit.)"
    $ persistent.encyclopedia_unlocks.add("hsu_ape")
    $ complete_task("visit_hsu_annual")
    jump act6_corridor_jenny


## ============================================================================
## CORRIDOR SCENE — Ate Jenny explains the three-office system
## ============================================================================
label act6_corridor_jenny:
    narrator_char "(You step out of the HSU with Dan. He's drinking the glucose mix, color slowly returning to his face.)"
    narrator_char "(In the OSA corridor, Ate Jenny is posting a new scholarship announcement on the bulletin board. She turns when she hears you.)"
    ate_jenny "Oh — Dan, right? From the freshman batch?"
    dan "Yeah."
    ate_jenny "You okay? You look like you just came from the HSU."
    dan "I did."
    ate_jenny "Referral to the GCSU?"
    narrator_char "(Dan holds up the envelope. Ate Jenny nods — the practiced recognition of someone who has seen this many times.)"
    ate_jenny "Good. That's the right path. Can I walk with you for a moment?"
    ate_jenny "I'm Ate Jenny from the Office of Student Affairs — the OSA."
    ate_jenny "The OSA is the coordinating hub for all student welfare services. If you don't know where to go for a problem, you come here first and we point you in the right direction."
    ate_jenny "There are three offices every student needs to know: the HSU, the GCSU, and the Scholarship Service."
    ate_jenny "Physical health. Mental health. Financial stability. These three are connected — you can't fully fix one without addressing the others."
    player_char "Is the GCSU really confidential? Dan is worried about that."
    ate_jenny "Protected by Republic Act 9258 — the Guidance and Counseling Act of 2004."
    ate_jenny "Nothing discussed in a GCSU session can be disclosed to your parents, your professors, the college dean, or anyone else without your written consent."
    ate_jenny "The only legal exceptions are serious intent to harm yourself or others, or a court order. Even then, the counselor involves you in the process."
    ate_jenny "You are protected by law in that room."
    dan "I didn't know there was a law for that."
    ate_jenny "Most students don't. That's part of why I'm here."
    ate_jenny "The counselor is Ma'am Garcia. She's been here twelve years. Just be honest with her. That's all she needs."
    narrator_char "(She stops at the GCSU door and holds it open.)"
    ate_jenny "I'll be at the OSA after. My door is always open."
    $ complete_task("talk_ate_jenny")
    jump act6_at_gcsu


## ============================================================================
## GCSU SCENE — Full counseling session with service information woven in
## ============================================================================
label act6_at_gcsu:
    narrator_char "(The Guidance and Counseling Services Unit. A small sign on the door: 'All sessions are confidential. Walk-ins welcome. Mon–Fri, 8AM–5PM.')"
    narrator_char "(Inside: calm lighting, a few chairs, plants on the windowsill. Ma'am Garcia looks up and closes her notebook.)"
    guidance_counselor "Come in. Sit down. I'm Ma'am Garcia, licensed guidance counselor."
    guidance_counselor "There's no rush here. Take a moment."
    narrator_char "(Dan sits. He's still holding the referral envelope.)"
    dan "The physician at the HSU sent me. She said I should talk to someone."
    guidance_counselor "And what do you think about that?"
    dan "I think I'm probably wasting your time."
    guidance_counselor "You haven't eaten properly in a week, you came to the clinic alone, and you think you're wasting my time."
    guidance_counselor "That tells me a lot about what's been going on inside your head."
    narrator_char "(Dan doesn't answer.)"
    guidance_counselor "Let me tell you what we do here first — so you know what you walked into."
    guidance_counselor "The GCSU provides free, confidential counseling to all enrolled UPV students. No co-pay, no referral required."
    guidance_counselor "Our services: Individual Counseling — private one-on-one sessions for any personal, academic, or emotional concern."
    guidance_counselor "Group Counseling — facilitated sessions where students with similar concerns work through them together."
    guidance_counselor "Psychological Testing and Assessment — standardized tools to understand your personality, aptitude, and learning style."
    guidance_counselor "Academic Counseling — for students struggling academically, considering shifting programs, or at risk of academic dismissal."
    guidance_counselor "Career Guidance — aligning your course, your strengths, and your long-term goals."
    guidance_counselor "Crisis Intervention — immediate support for students in acute distress. We also coordinate referrals to licensed psychiatrists in Iloilo."
    guidance_counselor "And the Freshmen Adjustment Program — a series of group sessions at the start of semester on homesickness, stress management, and building support networks."
    guidance_counselor "Everything is protected under Republic Act 9258. Nothing leaves this room."
    player_char "What about his parents? Can you tell them anything?"
    guidance_counselor "Not without his written consent. The law is clear on that."
    guidance_counselor "He is the client. We are on his side."
    dan "Okay."
    guidance_counselor "Good. Now — what does a normal day look like for you right now?"
    dan "Wake up. Try to go to class. Sit in the back so no one notices if I zone out. Come back to the dorm. Lie there."
    guidance_counselor "Do you sleep?"
    dan "Not really. I keep thinking."
    guidance_counselor "What things?"
    dan "Whether I should just go home."
    narrator_char "(A long pause.)"
    guidance_counselor "Tell me about home."
    dan "My family is having a hard time. My parents couldn't send my allowance this month. Probably next month too."
    dan "I keep thinking — what am I doing here? I'm struggling academically, I have no money, I'm far from everyone I know."
    dan "Every day feels like I'm already behind and I can't catch up."
    guidance_counselor "That's a heavy load."
    dan "Everyone else seems fine."
    guidance_counselor "They don't. Most of them are just better at hiding it than you are."
    guidance_counselor "What you're describing is called adjustment difficulty — combined with financial stress as a compounding factor."
    guidance_counselor "This is the most common presentation I see in first-semester freshmen. You are not unusual. You are not weak."
    guidance_counselor "There's also something called impostor syndrome — the feeling that you don't truly belong here, that everyone else is more prepared."
    guidance_counselor "I want you to understand: the UP System Admissions Test does not make mistakes. You earned your place here. That score is real."
    dan "It doesn't feel real right now."
    guidance_counselor "It rarely does in the first month. That's what the adjustment period is."
    guidance_counselor "What helps: routine, community, and small wins. Regular sleep and meals — even just structure reduces anxiety. One or two people you can be honest with. And noticing the small things you manage each day."
    guidance_counselor "Let's try something right now. Slow breath with me."
    guidance_counselor "In... hold... and out."
    narrator_char "(A quiet moment. Dan breathes. Something in his posture shifts — just slightly.)"
    guidance_counselor "Good. Here's what I need you to understand."
    guidance_counselor "The stress you're carrying has a specific, concrete cause: you don't have enough money to eat. That is not a character flaw. That is a circumstance."
    guidance_counselor "And circumstances can be addressed. There is an office for exactly this."
    guidance_counselor "The Scholarship Service at the New Administration Building handles Student Emergency Assistance, STFAP re-bracketing, and scholarship applications."
    guidance_counselor "I'm writing you a referral letter right now. Cases referred by the GCSU are prioritized — your processing will be flagged as urgent."
    dan "I didn't know the counselor's office could do that."
    guidance_counselor "We don't just listen. We connect. That's the point of the system."
    guidance_counselor "But I also want you to come back here after. Not because something is wrong with you — because adjustment is a process, and you shouldn't navigate it alone."
    guidance_counselor "We can do regular sessions. Work through what you're feeling before it compounds. That's preventive counseling — you don't wait for a crisis."
    guidance_counselor "One follow-up session. Can you commit to that?"
    dan "...Yes."
    guidance_counselor "Good."
    narrator_char "(She seals the referral envelope. Hands Dan a small card: 'GCSU — Walk-in hours Mon–Fri, 8AM–5PM. You don't need a reason. You just need to come.')"
    narrator_char "(Dan holds it carefully.)"
    player_char "You ready?"
    dan "Yeah. Let's go."
    narrator_char "(Encyclopedia unlocked: GCSU — Guidance and Counseling Services Unit.)"
    $ persistent.encyclopedia_unlocks.add("gcsu")
    $ complete_task("talk_dan_gcsu")
    jump act6_at_scholarship


## ============================================================================
## SCHOLARSHIP SERVICE SCENE — Full orientation on STFAP, Emergency Fund, stipends
## ============================================================================
label act6_at_scholarship:
    narrator_char "(The Scholarship Service, New Administration Building. Bulletin boards are dense with announcements — scholarship deadlines, bracket tables, STFAP notices.)"
    narrator_char "(A laminated sign on the desk: 'Scholarship Service — STFAP, University Scholarships, External Grants. All processing done here.')"
    narrator_char "(Kuya Tomas reads the referral letter, sets it down, and opens a folder.)"
    kuya_tomas "Referral from Ma'am Garcia. Flagged urgent. Sit down."
    kuya_tomas "I'm going to explain three things in order of how fast they can help you."
    kuya_tomas "First — the Student Emergency Assistance Fund."
    kuya_tomas "This is a university fund for students in sudden financial crisis. It covers immediate needs: meals, photocopying, basic transport."
    kuya_tomas "Maximum assistance is ₱1,500 per application. Processing takes 24 to 48 hours after submission."
    kuya_tomas "For cases flagged by the GCSU — like yours — we prioritize. You should have something by end of week."
    dan "That would get me through this."
    kuya_tomas "Fill out this form. Student number, college, contact details, and a brief description of your situation. Keep it honest and specific."
    kuya_tomas "Second — STFAP re-bracketing."
    kuya_tomas "STFAP stands for Socialized Tuition and Financial Assistance Program. It's UP's core equity mechanism."
    kuya_tomas "Every enrolled student is assigned a bracket — A down to E9 — based on their household income and assets at enrollment."
    kuya_tomas "Bracket A is the standard full assessment. Bracket E9 means zero tuition."
    kuya_tomas "Brackets E5 through E9 also include a monthly living allowance — between ₱1,000 and ₱4,000 depending on your sub-bracket."
    player_char "So lower-bracket students receive money every month?"
    kuya_tomas "Yes. That's the financial assistance component of STFAP — it's not just a tuition reduction."
    kuya_tomas "If your family's financial situation changed significantly since you enrolled, you can request a re-bracketing assessment."
    kuya_tomas "The documents needed: a Sworn Affidavit of Income from your parents — notarized — a brief letter explaining the change, and your current enrollment form."
    kuya_tomas "If your parents can't produce the affidavit quickly, come back and explain the circumstances. We handle cases individually."
    kuya_tomas "For single-parent households, OFW families, or informal sector workers — the document requirements are different. Always come in and ask first."
    dan "What if I lied on the original application without meaning to?"
    kuya_tomas "If the error was honest and unintentional, come in and explain. We can correct it."
    kuya_tomas "Deliberate misrepresentation is a disciplinary offense — scholarship cancelled, repayment required, academic sanctions."
    kuya_tomas "But honest mistakes, and genuinely changed circumstances — we handle those with understanding."
    kuya_tomas "Third — scholarships with monthly stipends."
    narrator_char "(He slides a printed sheet across the desk. Dan scans it. His eyes stop partway down.)"
    dan "Some of these give ₱3,000 a month."
    kuya_tomas "Some give more. Let me explain the main types."
    kuya_tomas "University and College Scholarships — automatic, based on your GWA. University Scholar requires 1.20 or better. College Scholar requires 1.45. No application — your grades do the work."
    kuya_tomas "University Scholars are exempted from all tuition and miscellaneous fees. College Scholars receive partial to full exemption."
    kuya_tomas "DOST-SEI Scholarship — Department of Science and Technology. For STEM students. Covers full tuition plus a monthly stipend of around ₱7,000."
    kuya_tomas "CHED Merit Scholarship — Commission on Higher Education. Based on entrance scores. Full tuition and monthly allowance."
    kuya_tomas "UPV Foundation Scholarships — donor-funded, specific criteria. Some are need-based, others merit-based. Applications open each semester."
    kuya_tomas "LGU Scholarships — some local government units offer educational assistance. Check with your home barangay or municipality."
    player_char "What does he need to apply for any of these?"
    kuya_tomas "A document folder you keep ready at all times. Contents: latest grades transcript, certificate of family income or ITR, a short personal essay, and at least one recommendation letter."
    kuya_tomas "When a scholarship opens — and they open quickly — you grab the folder and submit. No scrambling."
    kuya_tomas "Deadlines are absolute. One day late means disqualification, no exceptions."
    kuya_tomas "Check this bulletin board every Monday. Announcements go up here before social media, before email."
    kuya_tomas "And maintain your GWA. Most scholarships require at least 2.00 every semester to renew. Fall below, you get one semester of probation."
    narrator_char "(Dan picks up the pen. Fills out the emergency fund form. His handwriting is small and careful.)"
    dan "I kept thinking there was nothing I could do."
    kuya_tomas "That's the most common thing I hear in this office."
    kuya_tomas "UP has been doing this for over a hundred years. The principle hasn't changed — no Filipino should be denied education because of poverty."
    kuya_tomas "STFAP, the emergency fund, the scholarships — these are the mechanism that keeps that promise."
    kuya_tomas "You just have to find the door."
    narrator_char "(Dan sets the pen down. The form is complete.)"
    narrator_char "(Emergency fund application: submitted. STFAP re-bracketing: documents listed. Scholarship applications: three open this month.)"
    narrator_char "(An hour ago he was on a bench, gray-faced and alone.)"
    player_char "(This is what a support system looks like when it actually works.)"
    narrator_char "(Encyclopedia unlocked: Scholarship Service — STFAP & Financial Assistance.)"
    $ persistent.encyclopedia_unlocks.add("scholarship_service")
    $ complete_task("talk_kuya_tomas")
    jump act6_dan_resolution


## ============================================================================
## RESOLUTION — Dan and player outside New Admin
## ============================================================================
label act6_dan_resolution:
    narrator_char "(Outside the New Admin Building. Late afternoon. The campus is quieter at this hour.)"
    dan "That was... a lot."
    player_char "How do you feel?"
    dan "Tired. But lighter."
    dan "It doesn't fix everything."
    player_char "No. But you know where to go now."
    dan "The HSU for physical health. The GCSU for everything else. The Scholarship Service for money."
    dan "Three offices. I didn't know any of them existed two hours ago."
    player_char "Most freshmen don't until they need them."
    dan "Why doesn't anyone tell you during orientation?"
    player_char "They do. We just don't listen because we think we won't need it."
    dan "..."
    dan "Hey. Thank you. For not leaving me on that bench."
    player_char "You walked me to the HSU last week. I owed you one."
    dan "That's twice you've said that."
    player_char "I'll keep saying it until you stop needing me to."
    narrator_char "(Dan almost smiles. It's not much — but it's something.)"
    narrator_char "(You walk back toward the dorms together as the sun drops behind the CAS building.)"
    narrator_char "(You think about the physician who asked the right question. The counselor who listened. The scholarship officer who had a folder ready.)"
    narrator_char "(Nobody fixed anything for Dan today. They handed him the tools and showed him the door.)"
    narrator_char "(The rest — the forms, the follow-ups, the slow climb back — that's still his work.)"
    narrator_char "(But he's not doing it alone anymore.)"
    window hide
    return

## ============================================================================
## END OF ACT 6 DIALOGUES
## ============================================================================
play music "audio/Act7.mp3" fadein 1.0
