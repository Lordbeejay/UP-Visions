## ============================================================================
## ACT 8 DIALOGUES — End of First Week: Finding Your Place
## KEY THEME: Reflection, belonging, identity, looking ahead
## STORY: Friday evening. Jaden finds the player. They walk the campus together
##        one last time — canteen, dorm, Prof. Reyes, the oval at sunset.
##        Every person and place from the week comes full circle.
## ============================================================================

## --- ACT 8 INIT ---
label act8_start:
    # play music moved to end of previous act
    jump act8_map


## ============================================================================
## ACT 8 STORY — Jaden finds the player at the end of the week
## ============================================================================
label act8_npc_jaden:
    window show
    narrator_char "(Friday. Late afternoon.)"
    narrator_char "(You're sitting on the steps outside the CAS building when Jaden drops down beside you.)"
    narrator_char "(He has his bag on one shoulder and a half-eaten pandesal in his hand.)"
    jaden "Hey."
    player_char "Hey."
    jaden "Paper got submitted. TLRC reviewed it this morning. I think it's okay."
    player_char "You finished it."
    jaden "We finished it. You dragged me into that library."
    narrator_char "(A pause. The campus has that Friday-afternoon feeling — people moving slower, the week's weight starting to lift.)"
    jaden "Has it really only been one week?"
    player_char "Feels longer."
    jaden "So much happened. Dan's whole thing with the GCSU. Your dorm check-in. Prof. Lena's reading list."
    jaden "I feel like I've been here a month."
    player_char "Are you okay? Really?"
    jaden "Yeah. Actually yeah. Better than I thought I'd be."
    jaden "I was terrified on day one. Like — what if I can't keep up? What if everyone here is smarter than me?"
    player_char "And now?"
    jaden "Now I know where the library is. And the TLRC. And the HSU. And the GCSU."
    jaden "I know Ate Rosa by name. I know which carinderia has the best sinangag."
    jaden "That's something."
    player_char "That's actually a lot."
    jaden "Hey — walk with me? I want to get food at the canteen before it closes. Ate Linda always saves the last serving of adobo for regulars."
    player_char "You're already a regular?"
    jaden "Third time this week. She knows my name."
    narrator_char "(You grab your bag. The two of you walk toward the canteen.)"
    $ complete_task("talk_jaden_act8")
    jump act8_canteen_scene


## ============================================================================
## CANTEEN SCENE — Ate Linda, community, belonging
## ============================================================================
label act8_canteen_scene:
    narrator_char "(The canteen. Nearly closing time. A few students still eating, trays stacked on one side.)"
    narrator_char "(Ate Linda is wiping down a counter. She looks up at Jaden with recognition.)"
    ate_linda "Ay, two of you today! Sit, sit. There's still adobo."
    jaden "Told you."
    narrator_char "(She sets down two plates without being asked. The rice is still warm.)"
    ate_linda "First week done?"
    player_char "Just about."
    ate_linda "How are you feeling, anak?"
    player_char "Tired. But okay."
    ate_linda "That's the right answer. If you said 'great,' I'd be worried you weren't paying attention."
    ate_linda "The first week is supposed to be hard. It means you're taking it seriously."
    jaden "Did you always work here, Ate?"
    ate_linda "Fifteen years. Since before your professors were as old as they are now."
    ate_linda "I've seen every kind of freshman. Scared ones, overconfident ones, ones who cried in the hallway."
    ate_linda "And I've seen every one of them, in time, become someone who belongs here."
    player_char "Does it always happen?"
    ate_linda "Always. Some faster, some slower. But it happens."
    ate_linda "You know what makes UP students different? They don't just survive the place. They grow into it."
    ate_linda "The campus changes them. And they change the campus back."
    ate_linda "You're part of that now, whether you feel it yet or not."
    narrator_char "(She refills your water without asking.)"
    ate_linda "One piece of advice, since you're in my canteen and I'm feeling generous."
    ate_linda "Take care of the people around you. Your batchmates. Your dormmates."
    ate_linda "This journey — you shouldn't do it alone. And neither should they."
    ate_linda "When you see someone struggling, you do what you did for Dan. You show up."
    ate_linda "That's what being an Iskolar ng Bayan actually looks like. Before the degree. On day eight."
    narrator_char "(You eat. The adobo is good. Outside the canteen window, the sun is starting to drop.)"
    $ complete_task("talk_ate_linda")
    jump act8_dorm_scene


## ============================================================================
## DORM SCENE — Nanay Elena, the week in full
## ============================================================================
label act8_dorm_scene:
    narrator_char "(The dorm corridor. The building has that end-of-week hum — students washing clothes, calling home, music from behind closed doors.)"
    narrator_char "(Nanay Elena is by the common room, organizing something on the bulletin board.)"
    narrator_char "(She turns when she hears you.)"
    nanay_elena "Ah. The two of you, together. Good."
    nanay_elena "I always feel better when I see freshmen traveling in pairs. Means you found each other."
    jaden "She dragged me through the library."
    nanay_elena "Then she did her job."
    narrator_char "(She studies the player's face with the practiced eye of someone who has watched a thousand students pass through these halls.)"
    nanay_elena "How are you really, anak? I don't mean the answer you give to professors."
    player_char "Tired. A little overwhelmed. But — grounded. More than I was on Monday."
    nanay_elena "Grounded. That's a good word."
    nanay_elena "Monday you didn't know where anything was. Now you know the library, the HSU, the GCSU, the scholarship office, the canteen."
    nanay_elena "You know people. You have a batchmate beside you."
    nanay_elena "That's not small. That's everything."
    player_char "Nanay, I helped someone this week. A classmate. He was struggling alone and didn't know where to go."
    nanay_elena "Dan?"
    player_char "How did you—"
    nanay_elena "Word gets around in a dorm. I heard he's doing better."
    nanay_elena "What you did — that's the thing nobody puts on a brochure. No one tells you that sometimes being a UP student means being the person who notices."
    nanay_elena "The support services exist. But someone has to be the one to say 'come on, let's go.'"
    nanay_elena "You were that person."
    narrator_char "(A long moment.)"
    nanay_elena "One more thing before you go."
    nanay_elena "There's a professor who gives a talk every Friday evening at the campus steps, just before sunset. Prof. Reyes."
    nanay_elena "He's been doing it for twenty years. Only a few students ever find him."
    nanay_elena "Go. Take Jaden."
    jaden "What does he talk about?"
    nanay_elena "Why you're here."
    $ complete_task("talk_nanay_elena")
    jump act8_prof_reyes_scene


## ============================================================================
## PROF. REYES SCENE — Iskolar ng Bayan, the meaning of UP
## ============================================================================
label act8_prof_reyes_scene:
    narrator_char "(The steps of the Administration Building. The last of the daylight is gold on the campus oval.)"
    narrator_char "(Prof. Reyes is there — older, with the quiet gravity of someone who has thought about the same things for a very long time.)"
    narrator_char "(There are three other students already sitting on the steps, listening.)"
    narrator_char "(He pauses when he sees you. Nods. Continues.)"
    prof_reyes "You missed the beginning. That's fine. The most important part is still coming."
    prof_reyes "I was saying: the University of the Philippines was not built to produce employees."
    prof_reyes "It was built to produce citizens. Leaders. People who think clearly and act with conscience."
    prof_reyes "The Filipino taxpayer funds this university. The jeepney driver, the farmer, the market vendor."
    prof_reyes "They don't have a UP degree. Many of them never will. But they pay for yours."
    prof_reyes "Iskolar ng Bayan — Scholar of the Nation. That is not a title. It is a debt."
    prof_reyes "Not a debt that crushes you. A debt that directs you."
    player_char "What does paying it back look like?"
    prof_reyes "Good question. It looks like this: you use your education in service."
    prof_reyes "Not necessarily in government — though that matters. In any field, in any work."
    prof_reyes "The engineer who designs flood-resistant housing for typhoon-prone provinces. That is service."
    prof_reyes "The scientist who studies coral reef recovery in Philippine waters. That is service."
    prof_reyes "The teacher who goes back to their hometown and makes sure the next generation has a chance. That is service."
    prof_reyes "You don't need a grand stage. You need a conscience and a skill."
    jaden "What if we don't know yet what we want to do?"
    prof_reyes "Then your job right now is to pay attention."
    prof_reyes "Pay attention in class — not to memorize, but to understand. The world is a set of problems waiting for people who can think."
    prof_reyes "Pay attention to each other. Learn from people who come from different places, different struggles."
    prof_reyes "Pay attention to this campus. It has a history. It has a soul. Know it."
    prof_reyes "And pay attention to yourself. What moves you. What you cannot ignore."
    prof_reyes "That thing you cannot ignore — follow it. It will lead you somewhere that matters."
    narrator_char "(The sun touches the horizon. The oval turns amber.)"
    prof_reyes "Honor and Excellence. That is the UP motto."
    prof_reyes "Honor — be honest, even when it costs you. Be ethical, even when no one is watching."
    prof_reyes "Excellence — not in grades alone. In character. In how you treat the people around you."
    prof_reyes "In the work you do, whether anyone claps for it or not."
    prof_reyes "You will face difficulty here. Subjects that defeat you. Moments where you question your place."
    prof_reyes "When that happens — and it will — remember: you are not here by accident. The entrance exam does not make mistakes."
    prof_reyes "You earned your seat. Now grow into it."
    prof_reyes "Welcome to UP Visayas. Go make something of this."
    narrator_char "(He doesn't wait for applause. He simply gathers his things and walks back toward the building.)"
    narrator_char "(The three other students sit quietly for a moment. Then one of them starts clapping — and you join.)"
    jaden "(quietly) I needed to hear that."
    player_char "(quietly) Yeah. Me too."
    $ complete_task("talk_prof_reyes")
    if "sq_honor_excellence" not in subquests_completed:
        menu:
            "★ Before we go — test me on Honor and Excellence.":
                jump sq_honor_excellence
            "(Let's just sit here a minute longer.)":
                pass
    window hide
    jump act8_oval_ending


## ============================================================================
## ENDING — The oval at sunset. Everything comes together.
## ============================================================================
label act8_oval_ending:
    window show
    narrator_char "(The campus oval. The light is almost gone.)"
    narrator_char "(Jaden is beside you. You're both quiet.)"
    narrator_char "(You think about Monday.)"
    narrator_char "(The bus into Miagao, the gate, Manong Guard checking your ID.)"
    narrator_char "(Jaden panicking about directions. The carinderia by the entrance.)"
    narrator_char "(Everything that happened since then.)"
    narrator_char "(The dorm room, bare and unfamiliar.)"
    narrator_char "(Prof. Lena's reading list. Kuya Rico pointing at building numbers. Ate Grace on student rights.)"
    narrator_char "(Dan on a bench with fifty pesos, gray-faced, carrying it alone.)"
    narrator_char "(The physician who asked the right question. The counselor who listened. The scholarship officer who had a folder ready.)"
    narrator_char "(Ate Rosa handing Jaden a book and saying: 'start here.')"
    narrator_char "(Prof. Santos saying: 'you describe when you should be arguing.')"
    narrator_char "(The TLRC tutor asking questions until the freshman found her own answer.)"
    narrator_char "(Nanay Elena's hot coffee. Ate Linda's adobo.)"
    narrator_char "(All of it — in one week.)"
    jaden "What are you thinking about?"
    player_char "How much I didn't know seven days ago."
    jaden "And now?"
    player_char "I still don't know a lot. But I know where to go."
    jaden "That's actually huge."
    narrator_char "(The campus lights come on. One by one, along the path to the dorms.)"
    narrator_char "(Somewhere behind you, the library is still lit. The TLRC closes in an hour. The HSU sign glows green.)"
    narrator_char "(Dan is in a better place. Jaden finished his paper. You checked into a dorm room that is starting to feel like yours.)"
    narrator_char "(You are tired. You are homesick, a little. You are not sure about everything that comes next.)"
    narrator_char "(But you are here.)"
    narrator_char "(And you know how to be here now.)"
    narrator_char "(That was what the first week was for.)"
    jaden "Same time Monday?"
    player_char "Same time Monday."
    narrator_char "(You walk back to the dorms together as the last light disappears behind the Miagao hills.)"
    narrator_char "(End of Week One.)"
    narrator_char "(Welcome to UP Visayas.)"
    narrator_char "(This is just the beginning.)"
    $ complete_task("end_of_first_week")
    window hide
    return


## ============================================================================
## END OF ACT 8 DIALOGUES
## ============================================================================
    # No next act music — game ends here
