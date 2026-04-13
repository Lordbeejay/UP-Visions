## ============================================================================
## ACT 8 DIALOGUES — THE FINALE: End of First Week
## KEY THEME: Reflection, belonging, identity, the Iskolar ng Bayan's purpose
## STORY: Friday evening. Every thread from the week comes full circle.
##        Jaden, Dan's recovery, Ate Linda, Nanay Elena, Prof. Reyes, the oval.
##        Each person the player met this week echoes in the last scene.
##
## LABEL MAP (matches script.rpy MapNode targets):
##   act8_npc_jaden        → Scene 1: Jaden recaps the full week (callbacks Acts 1–7)
##   act8_npc_ate_linda    → Scene 2: Canteen — Ate Linda, community, belonging
##   act8_npc_nanay_elena  → Scene 3: Dorm — Dan recovery + Nanay Elena
##   act8_npc_prof_reyes   → Scene 4: Admin steps — Prof. Reyes + mandatory sq_week_review
##   act8_end_of_week      → Scene 5: Campus oval — the finale ending
## ============================================================================

## --- ACT 8 INIT ---
label act8_start:
    # play music moved to end of previous act
    jump act8_map


## ============================================================================
## SCENE 1 — Jaden (CAS Building Steps)
## CALLBACKS: Every act, 1 through 7 — explicit and by name
## ============================================================================
label act8_npc_jaden:
    window show
    narrator_char "(Friday. Late afternoon. The CAS building steps.)"
    narrator_char "(Jaden drops down beside you with a half-eaten pandesal and that look.)"
    narrator_char "(The same one he had on Monday at the banwa gate — except now it sits differently on him. Less lost. More settled.)"
    jaden "Hey."
    player_char "Hey."
    jaden "Paper's in. Submitted to the TLRC for a final check this morning, handed to Prof. Lena an hour ago."
    player_char "How do you feel?"
    jaden "Like I ran a marathon through every building on this campus."
    jaden "But — good? Is that allowed?"
    narrator_char "(A pause. The campus has that Friday-afternoon feeling — people moving slower, the week's weight starting to lift.)"
    jaden "Has it really only been one week?"
    player_char "Feels longer."
    jaden "SO much happened."
    narrator_char "(He starts counting on his fingers.)"
    jaden "Monday — we got off at the wrong stop in Miagao town. I panicked. You didn't."
    player_char "I was panicking internally."
    jaden "Ha. You hid it well."
    jaden "Then Manong Josh with his landmarks rundown. Aleng Maria screaming at us to eat."
    jaden "Tol Joseph and the SB-19 tricycle. Manong Chris and the Kinaray-a phrases."
    player_char "The Miagao Church. I didn't know I was studying near a UNESCO World Heritage Site."
    jaden "Right? We just — walked past it. Like it was a regular church."
    narrator_char "(A beat.)"
    jaden "Then BOX 1. Ate Bea and her five freshie rules. Kuya Mark and the ID policy."
    jaden "I still keep my Notice of Admission in a clear sleeve. Rule number one."
    player_char "Ma'am Reyes and the flip card game."
    jaden "Registrar, Cashier, OSA. 8 AM to 5 PM, no exceptions."
    jaden "Enrollment Tetris on Tuesday. Sir Noel watching me rebuild my schedule for the third time like I was defusing something."
    player_char "You deleted your PE slot by accident."
    jaden "TWICE. I deleted it TWICE."
    narrator_char "(He laughs. It's an easy laugh — the kind that only works when you're safely on the other side of something.)"
    jaden "Then the dorm. Room 207. Your side of the corridor was just a mattress on day one."
    player_char "It looked like a storage closet."
    jaden "Now it has a lamp and books on the shelf. That happened fast."
    narrator_char "(He leans back on the step, looking out at the campus.)"
    jaden "Wednesday — Prof. Lena. Three chapters by Thursday. I thought she was joking."
    player_char "She doesn't joke."
    jaden "She NEVER jokes."
    jaden "Ate Grace and the student rights speech. Kuya Rico and the building numbers."
    jaden "I ended up in the fisheries lab looking for a history class."
    narrator_char "(You almost choke.)"
    player_char "Classic freshie move. Happens every year."
    jaden "You sound exactly like Kuya Rico."
    narrator_char "(A quiet moment.)"
    jaden "Then Dan."
    narrator_char "(His voice shifts. Quieter.)"
    jaden "I walked past him three times that day. I thought he just had a headache."
    player_char "He was carrying it alone."
    jaden "You saw it."
    jaden "You said 'HSU. Now.' Just like that."
    jaden "Three offices in one afternoon. The physician, the counselor, Kuya Tomas at the scholarship office."
    jaden "And Dan looked like a different person by the end of it."
    player_char "He looked like he'd been allowed to breathe."
    jaden "(quietly) Yeah. Exactly that."
    narrator_char "(Across the campus, a late class ends. Students spill out, talking loudly.)"
    jaden "And then yesterday — you dragging me into the library."
    player_char "You needed to be dragged."
    jaden "Ate Rosa with the Agoncillo. Kuya Neil and the UP Mail setup."
    jaden "Prof. Santos and her 'what is your ARGUMENT' face."
    jaden "The TLRC tutor asking questions instead of giving answers."
    jaden "I spent three hours writing a paragraph I was proud of. That's never happened to me before."
    player_char "And today the paper is in."
    jaden "And today the paper is in."
    narrator_char "(The campus light is going gold.)"
    narrator_char "(A long, comfortable silence.)"
    jaden "I was terrified on Monday. Like — what if I can't keep up? What if everyone here is smarter than me?"
    player_char "And now?"
    jaden "Now I know where the library is. The TLRC. The HSU. The GCSU. The scholarship office."
    jaden "I know Ate Rosa by name. I know which carinderia has the best sinangag."
    jaden "I know that a room number's first digit is the floor — and that it means NOTHING if you don't check the building prefix first."
    player_char "That's actually a lot."
    jaden "That's actually everything."
    narrator_char "(He stands and brushes crumbs off his jacket.)"
    jaden "Walk with me? Ate Linda saves the last adobo for regulars and the canteen closes soon."
    player_char "You're already a regular?"
    jaden "Third time this week. She knows my name."
    narrator_char "(You grab your bag. The two of you walk toward the canteen.)"
    narrator_char "(Past the CAS corridor, past the flagpole, into the last warm light of the week.)"
    $ complete_task("talk_jaden_act8")
    window hide
    return


## ============================================================================
## SCENE 2 — Canteen (Ate Linda)
## CALLBACKS: Aleng Maria (Act 1), community belonging, Iskolar ng Bayan
## ============================================================================
label act8_npc_ate_linda:
    window show
    narrator_char "(The canteen. Nearly closing time. A few students still eating, trays stacked on one side.)"
    narrator_char "(Ate Linda is wiping down the counter. She looks up at Jaden first, then you — recognition breaking into a warm expression.)"
    ate_linda "Ay! Two of you today. Sit, sit — there's still adobo. I was about to pack it up."
    jaden "I told you."
    narrator_char "(She sets down two plates without being asked. The rice is still warm. The adobo smells like the end of a long week.)"
    ate_linda "First week done?"
    player_char "Just about."
    ate_linda "How are you feeling, anak?"
    player_char "Tired. But okay."
    ate_linda "That's the right answer. If you said 'great,' I'd be worried."
    ate_linda "The first week is supposed to be hard. It means you're taking it seriously."
    narrator_char "(She refills your water without asking.)"
    narrator_char "(The gesture reminds you of Aleng Maria in Miagao town — a different woman, the same language.)"
    narrator_char "(The whole week has been people handing you things: food, information, direction, time.)"
    narrator_char "(The campus feeds you in every way there is.)"
    jaden "Did you always work here, Ate?"
    ate_linda "Fifteen years. Since before your professors were as old as they are now."
    ate_linda "I've seen every kind of freshman. Scared ones, overconfident ones, ones who cried in the hallway on day three."
    ate_linda "And I've seen every single one of them — in time — become someone who belongs here."
    player_char "Does it always happen?"
    ate_linda "Always. Some faster, some slower. But it happens."
    ate_linda "You know what makes UP students different? They don't just survive the place. They grow into it."
    ate_linda "The campus changes them. And they change the campus back."
    ate_linda "You're part of that now — whether you feel it yet or not."
    narrator_char "(She refills Jaden's water too, without being asked.)"
    ate_linda "One piece of advice, since you're in my canteen and I'm feeling generous."
    ate_linda "Take care of the people around you. Your batchmates. Your dormmates."
    ate_linda "This journey — don't do it alone. And don't let them do it alone either."
    ate_linda "When you see someone struggling, you do what you did for Dan this week. You show up."
    ate_linda "That's what Iskolar ng Bayan actually looks like. Not the degree. On day eight."
    narrator_char "(You eat. The adobo is good.)"
    narrator_char "(Outside the canteen window, the sun is dropping lower. The campus oval glows.)"
    $ complete_task("talk_ate_linda")
    window hide
    return


## ============================================================================
## SCENE 3 — Dormitory (Dan Recovery + Nanay Elena)
## CALLBACKS: Dorm check-in (Act 4), Room 207, Dan's crisis (Acts 5–6)
## ============================================================================
label act8_npc_nanay_elena:
    window show
    narrator_char "(The dorm corridor. End-of-week hum — students washing clothes, calling home, music behind closed doors.)"
    narrator_char "(You pass Room 207. The door is open a crack. Your desk lamp is on.)"
    narrator_char "(Someone is inside.)"
    narrator_char "(It's Dan.)"
    narrator_char "(He's at your desk — folder open, pen in hand. He glances up when he hears the door.)"
    dan "Oh! Hey. Sorry — the common room was loud. Nanay Elena said your door was open, so I figured..."
    player_char "It's okay. What are you working on?"
    dan "STFAP re-bracketing forms. Kuya Tomas helped me start. I need to finish before Monday."
    narrator_char "(He holds up the folder — a neat stack of documents, sticky notes, highlighted sections.)"
    dan "Income certificate, proof of residence, the sworn affidavit. Everything Kuya Tomas said to prepare."
    dan "He flagged my case as GCSU-referred. Priority processing."
    player_char "You look different."
    dan "I ate."
    narrator_char "(He almost smiles. Then — actually smiles. It reaches his eyes this time.)"
    dan "Two full meals today. The physician would be proud."
    narrator_char "(A quiet beat.)"
    dan "Hey. I wanted to say something."
    dan "Wednesday — I was on that bench near the water fountain. I kept thinking: just get through today. Don't make it a big deal."
    dan "And then you just — came up and said 'HSU. Now.'"
    dan "Those three words were the most important thing anyone said to me this week."
    player_char "You would have gone eventually."
    dan "Maybe. Or I would have spent three more days on that bench convincing myself I was fine."
    dan "So — thank you. Really."
    narrator_char "(He goes back to his forms. Quietly. Carefully. Like someone who's been given a second chance and intends to use it.)"
    narrator_char "(You step back into the corridor.)"
    narrator_char "(Nanay Elena is by the common room bulletin board, the same way she always seems to be — calm, present, watching.)"
    nanay_elena "Ah. There you are."
    narrator_char "(She turns to face you with that particular look — the practiced eye of someone who has watched a thousand freshmen find their footing.)"
    nanay_elena "I always feel better at the end of the first week. When I can see that everyone made it."
    player_char "Dan's doing better."
    nanay_elena "I know. He ate breakfast in the common room this morning."
    nanay_elena "That's how I know a student is turning around — they start eating at the table again."
    narrator_char "(She studies your face.)"
    nanay_elena "How are YOU really, anak? Not the answer you give to professors."
    player_char "Tired. A little overwhelmed. But — grounded. More than I was on Monday."
    nanay_elena "Grounded. That's a good word."
    nanay_elena "Monday, you didn't know where your room was. Room 207 was bare walls and a mattress."
    nanay_elena "You signed the dorm agreement without knowing any of the rules yet."
    nanay_elena "By Wednesday it had a lamp on the desk and papers on the shelf."
    nanay_elena "A room starts to look like someone lives there when they're ready to stay."
    player_char "It still feels small."
    nanay_elena "It is small. But UP was not built in the dormitory."
    nanay_elena "It was built in the classrooms, the library, the corridors, the quadrangles, the oval at sunset."
    nanay_elena "The dormitory is just where you rest."
    player_char "Nanay — I helped someone this week. A classmate. He was struggling alone and didn't know where to go."
    nanay_elena "Dan."
    player_char "How did you—"
    nanay_elena "Word gets around in a dorm. I heard he's doing better."
    nanay_elena "What you did — that's the thing nobody puts on a brochure."
    nanay_elena "Nobody tells you that sometimes being a UP student means being the person who notices."
    nanay_elena "The support services exist. The HSU, the GCSU, the scholarship office — they're all here."
    nanay_elena "But someone has to be the one to say: 'come on. Let's go.'"
    nanay_elena "You were that person this week."
    narrator_char "(Down the hall, someone laughs. The dorm is alive.)"
    nanay_elena "One more thing before you go."
    nanay_elena "There's a professor — Prof. Reyes. Every Friday evening, at the campus steps, just before sunset."
    nanay_elena "He's been doing it for twenty years. Only a few students ever find him."
    nanay_elena "Go. Take Jaden with you."
    jaden "(appearing in the doorway) Where are we going now?"
    nanay_elena "To hear something worth hearing."
    jaden "What does he talk about?"
    nanay_elena "Why you're here."
    $ complete_task("talk_nanay_elena")
    window hide
    return


## ============================================================================
## SCENE 4 — Prof. Reyes (Administration Building Steps)
## CALLBACKS: All acts, Iskolar ng Bayan, the full week
## INTERACTIVE: sq_week_review (mandatory finale quiz), sq_honor_excellence (optional)
## ============================================================================
label act8_npc_prof_reyes:
    window show
    narrator_char "(The steps of the Administration Building. The last of the daylight is gold on the campus oval.)"
    narrator_char "(Prof. Reyes is there — older, with the quiet gravity of someone who has thought about the same things for a very long time.)"
    narrator_char "(Three other students are already sitting on the steps. One of them — you notice — is Caezar.)"
    narrator_char "(He gives you a small nod. Stays quiet. Some things don't change.)"
    narrator_char "(Prof. Reyes pauses when he sees you. Nods. Continues.)"
    prof_reyes "You missed the beginning. That's fine. The most important part is still coming."
    prof_reyes "I was saying: the University of the Philippines was not built to produce employees."
    prof_reyes "It was built to produce citizens. Leaders. People who think clearly and act with conscience."
    prof_reyes "The Filipino taxpayer funds this university."
    prof_reyes "The jeepney driver in Miagao — the one who took you from the plaza to the gate on your first day."
    prof_reyes "The market vendor who sold you your first meal here. The tricycle driver with the SB-19 sticker."
    narrator_char "(You recognize those people. You know their names now.)"
    prof_reyes "They don't have a UP degree. Many of them never will. But they pay for yours."
    prof_reyes "Iskolar ng Bayan — Scholar of the Nation. That is not a title. It is a debt."
    prof_reyes "Not a debt that crushes you. A debt that directs you."
    player_char "What does paying it back look like?"
    prof_reyes "It looks like this: you use your education in service."
    prof_reyes "Not necessarily in government — though that matters. In any field, in any work."
    prof_reyes "The engineer who designs flood-resistant housing for typhoon-prone communities. That is service."
    prof_reyes "The scientist who studies coral reef recovery in Philippine waters. That is service."
    prof_reyes "The teacher who goes back to their hometown so the next generation has a chance. That is service."
    prof_reyes "The student who notices a classmate on a bench, gray-faced and carrying it alone — and says 'come on. Let's go.' That is also service."
    narrator_char "(Jaden goes still beside you.)"
    jaden "(quietly) That last one."
    player_char "(quietly) Yeah."
    prof_reyes "You don't need a grand stage. You need a conscience and a skill."
    jaden "What if we don't know yet what we want to do?"
    prof_reyes "Then your job right now is to pay attention."
    prof_reyes "Pay attention in class — not to memorize, but to understand."
    prof_reyes "Pay attention to each other. Learn from people who come from different places, different struggles."
    prof_reyes "Pay attention to this campus. It has a history. It has a soul. Know it."
    prof_reyes "This week you saw the support services — the HSU, the GCSU, the scholarship office."
    prof_reyes "You saw the enrollment system. The dorm. The library. The professors and the staff and the canteen workers."
    prof_reyes "That network — every one of those people — that is the university working as it was designed to."
    prof_reyes "Pay attention to yourself. What moves you. What you cannot ignore."
    prof_reyes "That thing you cannot ignore — follow it. It will lead you somewhere that matters."
    narrator_char "(The sun touches the horizon. The oval turns amber.)"
    prof_reyes "Honor and Excellence. The UP motto."
    prof_reyes "Honor — be honest, even when it costs you. Be ethical, even when no one is watching."
    prof_reyes "Excellence — not in grades alone. In character. In how you treat the people around you."
    prof_reyes "In the work you do, whether anyone claps for it or not."
    prof_reyes "You will face difficulty here. Subjects that defeat you. Moments where you question your place."
    prof_reyes "When that happens — and it will — remember: you are not here by accident."
    prof_reyes "You survived a week that was designed to be overwhelming."
    prof_reyes "You learned where every important door is. You helped someone who needed it."
    prof_reyes "You showed up for a friend's paper. You showed up for yourself."
    prof_reyes "The entrance exam does not make mistakes."
    prof_reyes "You earned your seat. Now grow into it."
    prof_reyes "Welcome to UP Visayas. Go make something of this."
    narrator_char "(He gathers his things quietly and walks back toward the building.)"
    narrator_char "(Caezar starts clapping first — slow, deliberate. The other students join. Then you and Jaden.)"
    jaden "(quietly) I needed to hear that."
    player_char "(quietly) Yeah. Me too."
    narrator_char "(Caezar catches your eye on the way out.)"
    caezar "Good week?"
    player_char "Intense week."
    caezar "That's the same thing here."
    narrator_char "(He heads back toward Lover's Lane. The campus lights begin to flicker on.)"
    $ complete_task("talk_prof_reyes")

    ## ── Mandatory finale: Week in Review ─────────────────────────────────────
    if "sq_week_review" not in subquests_completed:
        prof_reyes "(He pauses at the top of the steps and turns back — just once.)"
        prof_reyes "One final thing. Everything you learned this week — seven days of it."
        prof_reyes "Let's see if it stayed with you."
        jump sq_week_review

    ## ── Optional: Honor and Excellence ──────────────────────────────────────
    if "sq_honor_excellence" not in subquests_completed:
        menu:
            "★ Prof. Reyes — one final challenge on Honor and Excellence.":
                jump sq_honor_excellence
            "(Let's sit here a moment longer.)":
                pass
    window hide
    return


## ============================================================================
## SCENE 5 — Campus Oval: THE FINALE
## The ending that ties every act together.
## ============================================================================
label act8_end_of_week:
    window show
    narrator_char "(The campus oval. The light is almost gone. The grass is dark gold.)"
    narrator_char "(Jaden is beside you. Neither of you say anything for a while.)"
    narrator_char "(The kind of quiet that doesn't need filling.)"
    narrator_char "(You think about Monday.)"

    ## — Act 1: Arrival in Miagao —
    narrator_char "~"
    narrator_char "(The jeepney pulling into Miagao for the first time. The smell of the sea.)"
    narrator_char "(The Miagao Church tower visible above the trees — a UNESCO World Heritage Site you nearly walked past without knowing.)"
    narrator_char "(Manong Josh pointing out landmarks. Aleng Maria telling you not to skip meals.)"
    narrator_char "(Manong Chris and Kinaray-a. Tol Joseph and the tricycle with the SB-19 sticker.)"
    narrator_char "(Not knowing what any of it was called yet. Not knowing what any of it meant.)"

    ## — Act 2: BOX 1 / New Admin —
    narrator_char "~"
    narrator_char "(The BOX 1 gate. Showing your Notice of Admission instead of a real ID — because you didn't have one yet.)"
    narrator_char "(Ate Bea and her five freshie rules. Kuya Mark and the security protocols.)"
    narrator_char "(Ma'am Reyes and the flip card game: Registrar, Cashier, OSA. 8 AM to 5 PM, no exceptions.)"
    narrator_char "(The moment you realized there was a whole system here — and that you were beginning to understand it.)"

    ## — Act 3: Enrollment —
    narrator_char "~"
    narrator_char "(The CRS portal. Enrollment Tetris.)"
    narrator_char "(Eighteen units fitting into a weekly grid like puzzle pieces — three attempts, no overlaps, one lunch break preserved.)"
    narrator_char "(Sir Noel saying: 'Without pre-enlistment, you won't have any subjects to confirm.')"
    narrator_char "(Caezar at Lover's Lane: 'Look around once in a while. That's part of learning too.')"

    ## — Act 4: Dorm Life —
    narrator_char "~"
    narrator_char "(Room 207. Empty. Just a mattress and a bare wooden frame.)"
    narrator_char "(The dorm manager handing you a key. 'Welcome to the dorm.')"
    narrator_char "(The point system. The curfew. The rules you signed before you understood them.)"
    narrator_char "(Setting up the lamp, the fan, the books on the shelf — turning four walls into somewhere you could stay.)"

    ## — Act 5: First Day of Classes —
    narrator_char "~"
    narrator_char "(Prof. Lena's voice, first day: 'If you're in the wrong room, now is the time to leave.')"
    narrator_char "(No one left.)"
    narrator_char "(Kuya Rico and building numbers. Ate Grace and the UP Student Code.)"
    narrator_char "(The reading list: three chapters by Thursday. You read them.)"
    narrator_char "(The first time you sat in a UP classroom and thought: I belong here.)"

    ## — Act 6: Student Support Services —
    narrator_char "~"
    narrator_char "(Dan on a bench near the water fountain. Pale. Carrying something too heavy to carry alone.)"
    narrator_char "(The physician who asked the right question. The counselor who listened.)"
    narrator_char "(The scholarship officer who already had a folder ready.)"
    narrator_char "(HSU for the body. GCSU for the mind. Scholarship Service for the money.)"
    narrator_char "(Three offices. Three kinds of help. One person who said 'come on. Let's go.')"
    narrator_char "(Dan tonight, at your desk, filling out STFAP forms — a plan in his hands.)"

    ## — Act 7: Library & Academic Resources —
    narrator_char "~"
    narrator_char "(Jaden on the library steps. Notebook open. Writing nothing.)"
    narrator_char "(Ate Rosa handing him Agoncillo: 'For Kas 1, this is your foundation.')"
    narrator_char "(Kuya Neil and UP Mail and forty-seven JSTOR results.)"
    narrator_char "(Prof. Santos: 'A research paper argues something. It doesn't just describe. What is your claim?')"
    narrator_char "(The TLRC tutor asking questions until the freshman found her own answer.)"
    narrator_char "(Jaden's paper: in. Submitted. Real.)"

    ## — Act 8: The Week in Full —
    narrator_char "~"
    narrator_char "(Ate Linda's adobo. Nanay Elena's steady voice.)"
    narrator_char "(Prof. Reyes and the oval at golden hour.)"
    narrator_char "(All of it — in one week.)"
    narrator_char "~"

    narrator_char "(Seven days ago you didn't know which jeepney to take from Miagao town.)"
    narrator_char "(You didn't know building numbers, or what CRS meant, or what a STFAP bracket was.)"
    narrator_char "(You didn't know anyone's name.)"
    narrator_char "(Now you know Jaden. You know Dan. You know Ate Linda and Nanay Elena.)"
    narrator_char "(You know Ate Rosa and Kuya Neil and Prof. Santos and the TLRC tutor who asks questions instead of giving answers.)"
    narrator_char "(You know where to go when something goes wrong.)"
    narrator_char "(And you know how to show up for someone who doesn't know yet.)"

    jaden "What are you thinking about?"
    player_char "How much I didn't know seven days ago."
    jaden "And now?"
    player_char "I still don't know a lot. But I know where to go."
    jaden "That's actually huge."
    jaden "That's the whole first week, actually. That's what it was for."

    narrator_char "(The campus lights come on. One by one, along the path to the dorms.)"
    narrator_char "(Behind you, the library is still lit. The TLRC closes in an hour. The HSU sign glows green.)"
    narrator_char "(Dan has a plan. Jaden's paper is in.)"
    narrator_char "(Room 207 has a lamp and books on a shelf and a key that belongs to you.)"
    narrator_char "(You are tired. You are a little homesick. You are not certain about everything that comes next.)"
    narrator_char "(But you are here.)"
    narrator_char "(And you know how to be here now.)"
    narrator_char "(That was what the first week was for.)"

    jaden "Same time Monday?"
    player_char "Same time Monday."

    narrator_char "(You walk back to the dorms together as the last light disappears behind the Miagao hills.)"
    narrator_char "(Behind you, the oval is still and the Administration Building is lit from within.)"
    narrator_char "(Somewhere across campus, a group of freshmen are still figuring out the building numbers.)"
    narrator_char "(You were them, a week ago.)"
    narrator_char "(You are not, anymore.)"

    $ complete_task("end_of_first_week")
    window hide

    ## ── Finale screens ───────────────────────────────────────────────────────
    call screen act_transition("WEEK ONE — COMPLETE",
        "You learned where every door is.\nNow walk through them.", "complete")

    call screen act_transition("Welcome to UP Visayas",
        "Iskolar ng Bayan.\nHonor and Excellence.\nThis is just the beginning.", "ending")

    return


## ============================================================================
## END OF ACT 8 DIALOGUES
## ============================================================================
