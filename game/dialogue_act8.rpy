## ============================================================================
## ACT 8 DIALOGUES — End of First Week: Finding Your Place
## KEY THEME: Reflection, identity, belonging, looking ahead
## ============================================================================

## --- ACT 8 INIT ---
label act8_start:
    $ talked_jaden_act8 = False
    $ talked_ate_linda = False
    $ talked_nanay_elena = False
    $ talked_prof_reyes = False
    jump act8_map

## ============================================================================
## NPC 1 — JADEN (Returning friend — deeper conversation)
## KEY INFO: Reflecting on the freshman week, campus identity, homesickness
## ============================================================================
label act8_npc_jaden:
    show jaden_sprite at left
    window show
    jaden "Hey! Can you believe it's almost the end of our first week?"
    player_char "It went by so fast. I feel like I just got off the bus yesterday."
    jaden "Right? So much happened. Let's grab a snack at the canteen and talk."
    menu:
        "How are you feeling about everything?":
            jump act8_jaden_feelings
        "Do you miss home?":
            jump act8_jaden_homesick
        "What are you most excited about?":
            jump act8_jaden_excited

label act8_jaden_feelings:
    jaden "Honestly? A mix of everything."
    jaden "Excited — because this is UP. The dream. We made it."
    jaden "Overwhelmed — because there's so much to learn, and not just academic stuff."
    jaden "How to navigate the campus. How to budget money. How to cook without burning the kitchen."
    jaden "Anxious — because the expectations are real. Everyone back home thinks I'll be valedictorian just because it's UP."
    player_char "I feel the same way."
    jaden "I think that's normal. The seniors I've talked to say the first month is the hardest."
    jaden "After that, you find your rhythm. Your people. Your places."
    jaden "We just need to get through this adjustment period together."
    menu:
        "Do you miss home?":
            jump act8_jaden_homesick
        "What are you excited about?":
            jump act8_jaden_excited
        "(I'm glad we're in this together.)":
            jump act8_jaden_end

label act8_jaden_homesick:
    jaden "Every single day."
    jaden "I miss my mom's cooking. I miss my little sister's annoying voice. I miss my dog."
    jaden "The first night in the dorm, I couldn't sleep. I just stared at the ceiling."
    jaden "But you know what helped? Talking to people who feel the same way."
    jaden "We're all homesick. We're all far from where we're comfortable."
    jaden "And that shared struggle — it bonds people."
    player_char "It does."
    jaden "I've been calling home every other day. Just hearing their voices helps."
    jaden "But I also know I need to be here. For my future, and for theirs."
    menu:
        "What are you excited about?":
            jump act8_jaden_excited
        "(Thanks for being honest.)":
            jump act8_jaden_end

label act8_jaden_excited:
    jaden "The freedom! For the first time, I get to decide things for myself."
    jaden "What to eat, where to go, how to spend my time."
    jaden "I joined two orgs — the Environmental Society and the Photography Club."
    jaden "I'm excited about the org activities. And meeting people from different provinces."
    jaden "UPV brings students from Iloilo, Antique, Capiz, Aklan, Negros — and some from Luzon and Mindanao."
    jaden "Everyone has a different story. Different perspective. That's beautiful."
    player_char "I hadn't thought of it that way."
    jaden "That's the real education, I think. Not just the classroom stuff."
    jaden "It's learning to live with people who are different from you."
    jump act8_jaden_end

label act8_jaden_end:
    jaden "Hey — whatever happens this semester, we've got each other's backs, okay?"
    jaden "That's what batchmates are for."
    jaden "See you in class Monday!"
    $ talked_jaden_act8 = True
    $ complete_task("talk_jaden_act8")
    hide jaden_sprite
    window hide
    return

## ============================================================================
## NPC 2 — ATE LINDA (Canteen Worker / Community Member)
## KEY INFO: Local community perspective, campus-town relationship, Miagao beyond campus
## ============================================================================
label act8_npc_ate_linda:
    show ate_linda_sprite at center
    window show
    ate_linda "Anak, what will you have today? Adobo or sinigang?"
    player_char "Adobo please, Ate. By the way, you've been working here long?"
    ate_linda "Fifteen years! I was here before most of your professors."
    ate_linda "I've seen hundreds of freshmen come through those gates. Some things never change."
    menu:
        "What's life like outside campus?":
            jump act8_linda_miagao
        "What changes have you seen over the years?":
            jump act8_linda_changes
        "Any advice for a freshie?":
            jump act8_linda_advice

label act8_linda_miagao:
    ate_linda "Miagao is more than just 'the town where UPV is.' It has its own soul."
    ate_linda "The Miagao Church — you saw it already? It's a UNESCO World Heritage Site."
    ate_linda "Built in the 1700s, it survived invasions, earthquakes, and typhoons. It's a symbol of resilience."
    ate_linda "The beach — Guimbal and Miagao have beautiful coastlines. On weekends, students go there to unwind."
    ate_linda "The market — every Saturday morning. Fresh fish, vegetables, local delicacies. Much cheaper than the canteen."
    ate_linda "Get to know the townspeople. They'll look out for you. Miagao residents are protective of UP students."
    ate_linda "When typhoons come, the community and the campus help each other."
    player_char "It sounds like a real community."
    ate_linda "It is. You're not just a student here. You're a temporary resident of Miagao. Respect the place, and it will take care of you."
    menu:
        "What changes have you seen?":
            jump act8_linda_changes
        "Any advice?":
            jump act8_linda_advice
        "(Thank you, Ate.)":
            jump act8_linda_end

label act8_linda_changes:
    ate_linda "Oh, so many changes."
    ate_linda "When I started, there weren't many buildings. Now there's the New Administration Building, new classrooms."
    ate_linda "Students used to write letters. Now everyone is on their phones."
    ate_linda "The courses changed too. More marine science, more technology. UPV keeps evolving."
    ate_linda "But some things stay the same — finals week panic, homesick freshmen, the pride of being an Iskolar ng Bayan."
    ate_linda "Every September, I see the same faces — scared, excited, trying to figure things out."
    ate_linda "And every March, I see those same faces transformed. Confident, capable, ready."
    player_char "That gives me hope."
    ate_linda "It should, anak. You'll look back at this moment and smile."
    menu:
        "Any advice?":
            jump act8_linda_advice
        "(Thank you, Ate.)":
            jump act8_linda_end

label act8_linda_advice:
    ate_linda "Eat well. You can't study on an empty stomach."
    ate_linda "Budget your money. The allowance seems like a lot until it runs out mid-month."
    ate_linda "Be kind to the maintenance staff, the guards, the canteen workers. We all make this campus run."
    ate_linda "Don't drink too much on weekends. I've seen careers derailed by bad decisions."
    ate_linda "Call your parents. They miss you more than they'll say."
    ate_linda "And when things get really hard — and they will — remember why you came here."
    ate_linda "You have the privilege that thousands would envy. Don't waste it."
    player_char "I won't, Ate. I promise."
    ate_linda "Good. Now eat your adobo before it gets cold."
    jump act8_linda_end

label act8_linda_end:
    ate_linda "Come back tomorrow. I'm making kare-kare!"
    $ talked_ate_linda = True
    $ complete_task("talk_ate_linda")
    hide ate_linda_sprite
    window hide
    return

## ============================================================================
## NPC 3 — NANAY ELENA (Dorm Housemother)
## KEY INFO: Self-care, well-being, practical life skills
## ============================================================================
label act8_npc_nanay_elena:
    show nanay_elena_sprite at right
    window show
    nanay_elena "Good evening, anak. You look tired. Did you eat dinner?"
    player_char "Not yet, Nanay Elena. It's been a long day."
    nanay_elena "Come, sit down for a moment. Let me tell you what I always tell the new students."
    menu:
        "What's that, Nanay?":
            jump act8_elena_care
        "How do you handle homesick students?":
            jump act8_elena_homesick
        "Any rules for the dorm I should know?":
            jump act8_elena_rules

label act8_elena_care:
    nanay_elena "You are not just a student. You are a whole person."
    nanay_elena "Your mind needs study, yes. But your body needs rest and food."
    nanay_elena "Your heart needs friends and laughter."
    nanay_elena "And your spirit needs purpose."
    nanay_elena "I've seen students collapse from overwork, get sick from irregular meals, burn out from isolation."
    nanay_elena "Don't let that be you."
    nanay_elena "Set a sleep schedule. Eat three meals a day. Talk to someone when you feel low."
    nanay_elena "The degree means nothing if you sacrifice your health to get it."
    player_char "You sound like my mom."
    nanay_elena "That's because all mothers worry the same way. I just happen to have 50 children every semester."
    menu:
        "How do you handle homesick students?":
            jump act8_elena_homesick
        "Dorm rules?":
            jump act8_elena_rules
        "(Thank you, Nanay.)":
            jump act8_elena_end

label act8_elena_homesick:
    nanay_elena "Every single batch has them. It's natural."
    nanay_elena "I make sure there's always hot water for coffee. Sometimes that's all it takes."
    nanay_elena "I check on the quiet ones — the students who stay in their rooms too much."
    nanay_elena "I organize movie nights in the common room on Saturdays. Everyone's invited."
    nanay_elena "And I listen. That's the most important thing — just listening."
    nanay_elena "If you're feeling homesick, anak, know that it's not weakness. It means you love your family."
    nanay_elena "But also know — you are building a second family here. Give it time."
    player_char "That means a lot, Nanay."
    menu:
        "Dorm rules?":
            jump act8_elena_rules
        "(Thank you, Nanay.)":
            jump act8_elena_end

label act8_elena_rules:
    nanay_elena "Rules keep everyone safe and comfortable. Here are the important ones:"
    nanay_elena "Curfew — main gate closes at 10 PM. If you'll be late, inform me in advance."
    nanay_elena "Visitors — allowed in the common area only. No visitors in rooms after 8 PM."
    nanay_elena "Noise — quiet hours start at 10 PM. Study time is sacred."
    nanay_elena "Cleanliness — keep your room tidy. Inspection every two weeks."
    nanay_elena "No cooking in rooms — use the communal kitchen. Fire safety."
    nanay_elena "Laundry — schedule your slot. There's a schedule posted in the laundry area."
    nanay_elena "Respect — everyone here comes from different backgrounds. Treat each other with kindness."
    nanay_elena "If you have problems with a roommate, come to me. I'll mediate."
    player_char "Got it. I'll follow the rules."
    nanay_elena "Good. And remember — this is your home now. Treat it like one."
    jump act8_elena_end

label act8_elena_end:
    nanay_elena "Now go eat dinner. The canteen is still open."
    nanay_elena "And get to bed early tonight. Your brain needs rest."
    $ talked_nanay_elena = True
    $ complete_task("talk_nanay_elena")
    hide nanay_elena_sprite
    window hide
    return

## ============================================================================
## NPC 4 — PROF. REYES (Chancellor's Welcome Speaker / Senior Faculty)
## KEY INFO: UP identity, Iskolar ng Bayan, responsibility to nation
## ============================================================================
label act8_npc_prof_reyes:
    show prof_reyes_sprite at center
    window show
    prof_reyes "Come in, come in. You caught me just in time."
    prof_reyes "I'm Prof. Reyes, one of the senior faculty here. You must be part of the new batch."
    player_char "Yes, Prof. I was told you give the best advice to freshmen."
    prof_reyes "Flattery works on me. Sit down."
    menu:
        "What does it mean to be an Iskolar ng Bayan?":
            jump act8_reyes_iskolar
        "What should I expect from my UP years?":
            jump act8_reyes_expect
        "Any final words for a freshman?":
            jump act8_reyes_final

label act8_reyes_iskolar:
    prof_reyes "Iskolar ng Bayan. Scholar of the Nation. That's not just a title."
    prof_reyes "The Filipino taxpayer funds the University of the Philippines."
    prof_reyes "The jeepney driver, the market vendor, the farmer — they subsidize your education."
    prof_reyes "That means you OWE them. Not just a degree. But service."
    prof_reyes "UP was created to produce leaders who would serve the Filipino people."
    prof_reyes "Not to produce employees for multinational corporations — though many end up there."
    prof_reyes "The true Iskolar ng Bayan asks: 'How can I give back?'"
    prof_reyes "Whether in public service, community development, research, or advocacy — give back."
    player_char "That's a heavy responsibility."
    prof_reyes "It is. And that weight is what makes UP different from any other university."
    prof_reyes "We don't just teach. We challenge. We provoke. We demand excellence with purpose."
    menu:
        "What should I expect?":
            jump act8_reyes_expect
        "Final words?":
            jump act8_reyes_final
        "(That inspires me.)":
            jump act8_reyes_end

label act8_reyes_expect:
    prof_reyes "Expect difficulty. UP is not meant to be easy."
    prof_reyes "You will face subjects that confuse you. Professors who challenge your assumptions."
    prof_reyes "You will question your beliefs, your politics, your identity. That's by design."
    prof_reyes "Expect moments of brilliance — when a concept clicks, when your research reveals something new."
    prof_reyes "Expect friendship — the deepest kind, forged in shared hardship and late-night study sessions."
    prof_reyes "Expect failure — and learning to get back up. Nobody goes through UP unscathed."
    prof_reyes "And expect transformation. You will not leave UP the same person who entered."
    prof_reyes "Four years from now, you'll barely recognize the freshie who walked through those gates."
    player_char "I hope that's a good thing."
    prof_reyes "It will be. Trust the process."
    menu:
        "Final words?":
            jump act8_reyes_final
        "(Thank you, Prof.)":
            jump act8_reyes_end

label act8_reyes_final:
    prof_reyes "Here are my final words for you, freshie."
    prof_reyes "Honor and excellence. That's UP's motto. Live it."
    prof_reyes "Honor — be honest, be ethical, be brave. Stand up for what's right, even when it costs you."
    prof_reyes "Excellence — not just in grades, but in character. In how you treat people. In the work you produce."
    prof_reyes "Find your passion. Not the major your parents chose — YOUR passion."
    prof_reyes "Take care of each other. The student beside you might be struggling silently."
    prof_reyes "And when you finally hold that diploma — remember Miagao. Remember the dorm. Remember the canteen adobo."
    prof_reyes "Remember that this is where it all started."
    player_char "I will, Prof. I promise."
    prof_reyes "Good. Now go make us proud."
    jump act8_reyes_end

label act8_reyes_end:
    prof_reyes "My door is always open, Room 301, CAS Building. Consultation hours posted outside."
    prof_reyes "Welcome to UP Visayas. You belong here."
    $ talked_prof_reyes = True
    $ complete_task("talk_prof_reyes")
    hide prof_reyes_sprite
    window hide
    return

## ============================================================================
## ACT 8 COMPLETION — End of First Week
## ============================================================================
label act8_end_of_week:
    window show
    narrator_char "(You stand at the campus oval as the sun sets over Miagao.)"
    narrator_char "(The week that felt like a month is finally ending.)"
    narrator_char "(You've learned the campus. Met people who will shape your college years.)"
    narrator_char "(Discovered resources you didn't know existed.)"
    narrator_char "(And found, maybe for the first time, a sense of belonging in this unfamiliar place.)"
    narrator_char "(The road ahead is long. But you're no longer walking it alone.)"
    narrator_char "(Welcome to UP Visayas. This is just the beginning.)"
    narrator_char "\[ACT 8 COMPLETE] — End of First Week: Finding Your Place."
    $ complete_task("end_of_first_week")
    window hide
    return

## ============================================================================
## END OF ACT 8 DIALOGUES
## ============================================================================
