## ============================================================================
## ACT 1 DIALOGUES — Arrival in Miagao (Banwa Area)
## ============================================================================

## --- ACT 1 INIT ---
label act1_start:
    $ talked_jaden = False
    $ talked_josh = False
    $ talked_maria = False
    $ talked_chris = False
    $ talked_joseph = False
    jump act1_map

## ============================================================================
## NPC 1 — JADEN
## ============================================================================
label act1_npc_jaden:
    window show
    jaden "Oh! Hey. You're a freshie too, right? I can tell by the confused look."
    player_char "Is it that obvious?"
    jaden "Don't worry, I had the same face when I first got here."
    jaden "Name's Jaden. I'm from Iloilo City—but even I had to look up where Miagao was before enrolling."
    menu:
        "So... where exactly IS Miagao?":
            jump act1_jaden_location
        "Why is UPV even here and not in the city?":
            jump act1_jaden_upv_history

label act1_jaden_location:
    jaden "Miagao is a municipality in Iloilo Province—about 40 kilometers southwest of Iloilo City."
    jaden "You take the Guimbal or Miagao-bound jeepney from Tagbak Terminal and ride for roughly an hour."
    jaden "It sits right along the coast. That's why sometimes you can smell the ocean from campus."
    jaden "The town is actually a National Cultural Treasure—the Miagao Church, that big baroque one near the plaza? UNESCO recognizes it."
    player_char "Wow. I didn't know I'd be studying near a UNESCO site."
    jaden "Right? People sleep on Miagao. It's quiet, it's old, it's got history."
    menu:
        "Why is UPV even here though?":
            jump act1_jaden_upv_history
        "(That's enough for now)":
            jump act1_jaden_end

label act1_jaden_upv_history:
    jaden "Good question. UPV—University of the Philippines Visayas—was established in 1979."
    jaden "The main campus was intentionally placed in Miagao, away from the city."
    jaden "The idea was to build a university that served the Visayas region specifically, focused on marine science, fisheries, and coastal development."
    jaden "Makes sense, right? You need to be near the sea to study the sea."
    player_char "So that's why there are wet labs and fishponds on campus."
    jaden "Exactly. UPV is one of the few UP campuses built with a specific regional identity in mind."
    jaden "The Miagao campus is the main research hub. You chose well."
    jaden "Not many people get to study in a place this historically and ecologically rich."
    jump act1_jaden_end

label act1_jaden_end:
    jaden "Anyway, if you need someone to eat dinner with at the carinderia later, I'm usually around the plaza by 6."
    $ talked_jaden = True
    $ complete_task("talk_jaden")
    window hide
    return

## ============================================================================
## NPC 2 — MANONG JOSH
## ============================================================================
label act1_npc_manong_josh:
    window show
    manong_josh "Ay, estudyante ka? Bagong-abot?"
    player_char "Yes po, Manong. Just arrived today."
    manong_josh "Maayo. Sit, sit. You look lost. Let me tell you about the town."
    menu:
        "What are the important landmarks here?":
            jump act1_josh_landmarks
        "Is there anything I need to know about Miagao before going around?":
            jump act1_josh_general

label act1_josh_landmarks:
    manong_josh "Okay, listen well. First, the Miagao Church—Santo Tomas de Villanueva Parish. Built in 1797."
    manong_josh "That's the big yellow-orange church you can see from almost anywhere in the town center."
    manong_josh "Beside it is the Miagao Plaza—that's where the weekend market is, and sometimes fiestas."
    manong_josh "Then there's the Miagao Public Market. That's where you buy your cheap ulam, vegetables, fresh fish."
    manong_josh "Open early morning until noon mostly. If you go past 10 AM, the good stuff is already gone."
    player_char "What about near the university?"
    manong_josh "Near UPV gate, there are small stores—sari-sari, loading stations, a few carinderias."
    manong_josh "The main road going into campus is called the avenue. Tricycle stop is right outside the gate."
    manong_josh "If you need the municipal hall for any documents, it's also along the main road near the church."
    menu:
        "Anything else I should know?":
            jump act1_josh_general
        "(That's very helpful, Manong)":
            jump act1_josh_end

label act1_josh_general:
    manong_josh "General knowledge? Okay. Miagao is small. Once you know the church, the market, and the university, you know the town."
    manong_josh "The town is safest during daytime. Don't wander unfamiliar streets alone at night as a freshie."
    manong_josh "Also—Miagao people are friendly but private. Greet them properly. 'Manong,' 'Manang,' 'Ate,' 'Kuya.'"
    manong_josh "Don't shout across the street. Walk up and speak properly. They will remember you."
    player_char "Good to know, Manong."
    manong_josh "And the beach—Miagao has access to the Iloilo Strait. Sometimes students go on weekends."
    manong_josh "But be careful. Ask locals first before swimming. Not all spots are safe."
    jump act1_josh_end

label act1_josh_end:
    manong_josh "You seem like a good kid. Study hard. Miagao will treat you well if you respect it."
    $ talked_josh = True
    $ complete_task("talk_manong_josh")
    window hide
    return

## ============================================================================
## NPC 3 — ALENG MARIA
## ============================================================================
label act1_npc_aleng_maria:
    window show
    aleng_maria "Uy, estudyante! Gutom ka na? Kain na dali!"
    player_char "Actually, Aleng, I wanted to ask about food around here."
    aleng_maria "Ay, tamang-tama! I know everything about food in Miagao. Sit, sit."
    menu:
        "How much does a meal usually cost here?":
            jump act1_maria_food_cost
        "Where are the best budget carinderias?":
            jump act1_maria_carinderias
        "How should I budget for daily living here?":
            jump act1_maria_budget

label act1_maria_food_cost:
    aleng_maria "For rice meals in carinderias—expect ₱45 to ₱70 per meal. Rice plus one viand."
    aleng_maria "You want extra rice? Add ₱5 to ₱10. Some carinderias give unlimited rice, look for those!"
    aleng_maria "Merienda—puto, suman, banana cue—₱5 to ₱15 lang. Buy near the market early."
    aleng_maria "Bottled water—₱10 to ₱15 sa sari-sari. Better to buy a big 5-gallon refill for ₱20 to ₱25."
    player_char "That's surprisingly affordable."
    aleng_maria "Miagao is tipid-friendly if you know where to go. Avoid the sit-down restaurants unless it's a special occasion."
    menu:
        "Where should I eat regularly?":
            jump act1_maria_carinderias
        "How much should I budget per day?":
            jump act1_maria_budget

label act1_maria_carinderias:
    aleng_maria "Okay, I will tell you the secret spots. But promise you'll still come back to me, ha?"
    player_char "Of course, Aleng!"
    aleng_maria "Near the UPV gate, there are a few carinderias—ask for the one with the tarpaulin of the lechon. Masustansya at mura."
    aleng_maria "Inside the campus area, there's the CASAS cafeteria and some student-run canteens. Good for budget meals."
    aleng_maria "Near the public market, the vendors sell cooked food in the morning—sinugno, tinola, sometimes kare-kare. Very cheap."
    aleng_maria "For meryenda, look for the old woman selling biko and puto near the church on weekends."
    aleng_maria "And my stall, of course! ₱60 for rice, pinakbet, and fish. With smile pa."
    player_char "What's pinakbet?"
    aleng_maria "Ay, you don't know pinakbet? That's your homework. Order it next time you're here."
    menu:
        "How much should I budget daily overall?":
            jump act1_maria_budget
        "(That's very helpful, Aleng)":
            jump act1_maria_end

label act1_maria_budget:
    aleng_maria "Okay, budget lesson. Listen carefully, ha?"
    aleng_maria "For food alone: ₱150 to ₱200 per day is comfortable. ₱120 if you're really tipid."
    aleng_maria "Breakfast can be ₱30 to ₱40—pandesal plus coffee or lugaw."
    aleng_maria "Lunch: ₱50 to ₱70. Dinner: ₱50 to ₱70."
    aleng_maria "Fare within town—tricycle is ₱10 to ₱15 per ride, depending on distance."
    aleng_maria "From town center to UPV gate, usual fare is ₱15."
    aleng_maria "Jeepney going to Iloilo City from Miagao—around ₱50 to ₱65 one way."
    aleng_maria "So for a week? Budget ₱1,500 minimum for food and local fare. More if you buy toiletries or extras."
    player_char "That helps a lot. I'll try to stick to ₱200 a day."
    aleng_maria "Smart! And cook sometimes if you can. Instant noodles plus egg plus vegetables—filling and cheap."
    aleng_maria "Buy your rice in bulk from the market. It's much cheaper per kilo than buying cooked every meal."
    jump act1_maria_end

label act1_maria_end:
    aleng_maria "Don't skip meals to save money—your brain needs food more than your wallet needs savings."
    aleng_maria "Now, do you want to order something?"
    player_char "Next time, Aleng. I still have people to talk to."
    aleng_maria "Sige! I'll save you the last portion of adobo!"
    $ talked_maria = True
    $ complete_task("talk_aleng_maria")
    window hide
    return

## ============================================================================
## NPC 4 — MANONG CHRIS
## ============================================================================
label act1_npc_manong_chris:
    window show
    manong_chris "Ay, bag-o ka diri? Taga-diin ka?"
    player_char "Po? Sorry, I didn't catch that."
    manong_chris "Haha! That's okay. I asked where you're from. I'm Chris. I've lived in Miagao all my life."
    menu:
        "What language do people speak here?":
            jump act1_chris_language
        "What are the local customs I should know?":
            jump act1_chris_customs
        "What's the Mass schedule at the church?":
            jump act1_chris_mass

label act1_chris_language:
    manong_chris "In Miagao, the local language is Kinaray-a—or Karay-a. It's different from Hiligaynon, which is spoken in Iloilo City."
    manong_chris "Don't worry, most people here also understand and speak Hiligaynon and Filipino."
    manong_chris "But if you learn even a few Kinaray-a words, locals will love you for it."
    manong_chris "\"Kumusta ka?\" — How are you? In Kinaray-a: \"Kamusta ka na?\""
    manong_chris "\"Salamat\" — Thank you. Same in Kinaray-a!"
    manong_chris "\"Wara\" — None or Nothing. You'll hear this a lot."
    manong_chris "\"Diin ka pa?\" — Where are you going? Useful when locals ask you."
    manong_chris "\"Estudyante ako sa UPV\" — I'm a student at UPV. Say this and people immediately become friendlier."
    player_char "Estudyante ako sa UPV!"
    manong_chris "Maayo! Perfect accent. You're already half-local."
    menu:
        "What customs should I know?":
            jump act1_chris_customs
        "What about Mass schedule?":
            jump act1_chris_mass

label act1_chris_customs:
    manong_chris "Miagao people are respectful and expect the same in return. Here are the important ones:"
    manong_chris "First—greet elders. 'Manong,' 'Manang,' 'Lolo,' 'Lola.' A nod isn't enough. Say the words."
    manong_chris "Second—during the Angelus at 6 PM, if you're near the church and the bells ring, pause. Don't talk loudly. Some still pray."
    manong_chris "Third—Fiesta season is a big deal here. The town fiesta honors Santo Tomas de Villanueva, usually in September."
    manong_chris "During fiestas, locals open their homes. If invited in, it's rude to refuse food. Take at least a little."
    manong_chris "Fourth—don't litter near the church or plaza. Miagaoanons take pride in these places."
    manong_chris "Fifth—if you see someone farming or fishing, don't just stare. Ask politely if you're curious. They're happy to share."
    player_char "Got it. Respect the people, the place, and the customs."
    manong_chris "Exactly. You'll fit in fine."
    menu:
        "What's the Mass schedule?":
            jump act1_chris_mass
        "(That's enough for now)":
            jump act1_chris_end

label act1_chris_mass:
    manong_chris "The Miagao Church—Santo Tomas de Villanueva Parish—has Mass almost every day."
    manong_chris "Typical Sunday schedule: 5:30 AM, 7:00 AM, and 9:00 AM. Sometimes an evening Mass around 5:30 PM."
    manong_chris "Weekday Masses are usually early morning—6:00 AM."
    manong_chris "If there's a special occasion like First Friday, expect extra morning and evening services."
    manong_chris "Even if you're not Catholic, the church is open for visitors. It's a historical site—just be respectful inside."
    manong_chris "No shorts inside the church. Cover your shoulders if you can."
    player_char "I'll keep that in mind if I ever visit."
    manong_chris "You should. The facade with the coconut trees carved in stone—it's unlike anything else."
    jump act1_chris_end

label act1_chris_end:
    manong_chris "Miagao is small, but it has a big soul. Treat it well and you'll have a good four years here."
    manong_chris "And if you're ever lost—just look for the church tower. You can see it from almost anywhere."
    $ talked_chris = True
    $ complete_task("talk_manong_chris")
    window hide
    return

## ============================================================================
## NPC 5 — JOSEPH THE TRICYCLE DRIVER
## ============================================================================
label act1_npc_joseph_driver:
    window show
    joseph "Sakay! Saan? Saan?"
    player_char "Actually, Joseph—wait, how did I know your name?"
    joseph "Ha? My name's stitched on my jacket, 'nak. Joseph. Most people just call me Tol Joseph."
    player_char "Ah! Right. Can I ask you about the tricycle routes here?"
    joseph "Of course! That's my specialty. Ask away."
    menu:
        "What are the main routes in Miagao?":
            jump act1_joseph_routes
        "How much is the fare to UPV campus?":
            jump act1_joseph_fare
        "Where are the main drop-off and pick-up points?":
            jump act1_joseph_dropoffs

label act1_joseph_routes:
    joseph "Okay, Miagao tricycle routes. There are a few main loops:"
    joseph "Route 1: Town Center (Plaza / Church) to UPV Gate. This is the most common student route."
    joseph "Route 2: Town Center to Public Market. Short route, mostly locals and vendors."
    joseph "Route 3: UPV Gate to Poblacion interior. For students going deeper into the barangays."
    joseph "Route 4: Town Center to nearby barangays like Kirayan, Sapa, Guibongan. Longer routes, higher fare."
    joseph "Most routes you'll use as a student are Route 1 and 2."
    player_char "Good to know. I was worried I'd get lost trying to navigate."
    joseph "Just tell me where you're going. I know every road in this town."
    menu:
        "What's the fare to UPV?":
            jump act1_joseph_fare
        "Where are the drop-off points?":
            jump act1_joseph_dropoffs

label act1_joseph_fare:
    joseph "Fare guide! Listen well, ha, because drivers don't always post it."
    joseph "Town Center to UPV Gate: ₱15 regular. Sometimes ₱10 if you're a student and the driver is feeling generous."
    joseph "Within town center (short hops): ₱10 flat. Market to plaza, plaza to church area."
    joseph "To farther barangays: ₱20 to ₱30, depending on distance."
    joseph "Special trip—meaning you hire the whole tricycle for yourself: negotiate. Usually ₱50 to ₱80 for nearby areas."
    joseph "If a driver quotes you too high, ask politely: 'Pila man gid ang tama nga bayad?' — What's the right fare?"
    joseph "Most drivers are honest. But knowing the base fares protects you."
    player_char "What about going to Iloilo City?"
    joseph "For that, you take a jeepney, not a tricycle. Jeepney terminal is a short walk from the plaza."
    joseph "Fare to Iloilo City (Tagbak Terminal) is around ₱50 to ₱65. Takes 45 minutes to 1 hour."
    joseph "Last trip back to Miagao from Tagbak is usually around 6:30 to 7:00 PM. Don't miss it or you'll be stranded."
    menu:
        "Where are the main drop-off points?":
            jump act1_joseph_dropoffs
        "(That's all I need for now)":
            jump act1_joseph_end

label act1_joseph_dropoffs:
    joseph "Main drop-off and pick-up points—very important for a freshie!"
    joseph "1. UPV Main Gate — Standard drop-off for students. Tricycles queue here especially during 7 AM and 1 PM class hours."
    joseph "2. Miagao Plaza — Central hub. From here you can reach the church, the market, most eateries."
    joseph "3. Miagao Public Market — Drop-off if you're doing grocery or buying supplies."
    joseph "4. Municipal Hall area — If you need government documents or LGU services."
    joseph "5. Highway junction — Where jeepneys to Iloilo or Antique pass. If you're going out of town."
    joseph "As a rule: if you're not sure where to get off, just say 'Plaza' and walk from there. The plaza is the center of everything."
    player_char "That's really useful. I'll remember—when in doubt, plaza."
    joseph "Exactly! And if you ever need a ride at odd hours, I'm usually parked near the church from 5 AM to 9 PM."
    joseph "Just look for the tricycle with the SB-19 sticker on the windshield. That's mine."
    jump act1_joseph_end

label act1_joseph_end:
    joseph "Welcome to Miagao, 'nak. It's a humble town, but students who respect it always look back on it fondly."
    joseph "Now—need a ride somewhere? Free orientation tour for first-day freshies!"
    player_char "Maybe later, Tol Joseph. I still have things to sort out here."
    joseph "Anytime! I'll be here."
    $ talked_joseph = True
    $ complete_task("talk_joseph_driver")
    window hide
    return

## ============================================================================
## TASK 2 — BOX 1
## ============================================================================
label act1_box1_arrive:
    window show
    narrator_char "(You arrive at BOX 1. The area is quieter here—a small covered waiting area near the barangay boundary.)"
    narrator_char "(There's a posted map of Miagao on the wall, a bench, and a small bulletin board with student notices.)"
    narrator_char "(You've completed your first orientation in the Banwa Area.)"
    play sound "task_complete.ogg"
    narrator_char "\[TASK 1 COMPLETE] — Gained Local's Favorability from all 5 residents."
    narrator_char "\[TASK 2 COMPLETE] — Reached BOX 1."
    narrator_char "\[ACT 1 COMPLETE] — Arrival in Miagao."
    $ complete_task("reach_box1")
    $ complete_task("act1_complete")
    window hide
    return

## ============================================================================
## END OF ACT 1
## ============================================================================