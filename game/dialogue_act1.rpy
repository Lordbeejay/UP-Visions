transform fit_screen:
    xalign 0.5
    yalign 0.5
    fit "cover"


## ============================================================================
## ACT 1 — DIALOGUE LABELS ONLY
## All classes, data, screens, and helpers have been moved to:
##   - variables.rpy (classes, items, GC data, helpers, unlock flags)
##   - screens.rpy   (notebook, inventory, quiz, phone screens)
## ============================================================================

## ============================================================================
## ACT 1 GAME FLOW
## ============================================================================

## ----------------------------------------------------------------------------
## ACT 1 START — show notebook intro, then begin
## ----------------------------------------------------------------------------

label act1_start:
    play music "audio/Act1.mp3" fadein 1.0
    
    $ talked_jaden   = False
    $ talked_josh    = False
    $ talked_maria   = False
    $ talked_chris   = False
    $ talked_joseph  = False
    $ jaden_second_talk = False
    $ gc_unlocked    = False
    $ gc_revealed    = []
    $ gc_open_count  = 0
    $ collected_items = []
    $ quiz_score     = 0

    ## Unlock inventory from the start of Act 1 (items can be collected)
    $ inventory_unlocked = True

    ## Reset notebook questions
    $ [setattr(q, 'answered', False) for q in notebook_questions]
    $ [setattr(q, 'chosen_item_id', None) for q in notebook_questions]


    ## Brief intro narration
    narrator_char "You've just arrived in Miagao."
    narrator_char "It's nothing like where you came from."
    narrator_char "You don't know the streets. You don't know the faces. You don't know the rules."
    narrator_char "But you have a notebook — and questions that need answers."

    ## Show notebook intro screen
    call screen notebook_intro_screen()

    ## Hint about inventory
    narrator_char "(Tip: Press [[I]] anytime to review your collected items.)"

    jump act1_map


## ============================================================================
## NPC 1 — JADEN (FIRST TALK)
## ============================================================================

label act1_npc_jaden:
    

    scene expression "images/ui/UI_Miagao.png" at fit_screen
    window show

    jaden "Oh! Hey. You're a freshie too, right? I can tell by the confused look."
    player_char "Is it that obvious?"
    jaden "Don't worry, I had the same face when I first got here."
    jaden "Name's Jaden. I'm from Iloilo City — but even I had to look up where Miagao was before enrolling."

    menu:
        "So... where exactly IS Miagao?":
            jump act1_jaden_location
        "Why is UPV even here and not in the city?":
            jump act1_jaden_upv_history

label act1_jaden_location:
    jaden "Miagao is a municipality in Iloilo Province — about 40 kilometers southwest of Iloilo City."
    jaden "You take the Guimbal or Miagao-bound jeepney from Tagbak Terminal. About an hour."
    jaden "It sits right along the coast. That's why sometimes you can smell the ocean from campus."
    jaden "The town is actually a National Cultural Treasure — the Miagao Church, that baroque one near the plaza?"
    jaden "UNESCO recognizes it. Wild, right?"

    player_char "I didn't know I'd be studying near a UNESCO site."

    ## ITEM DROP
    $ collect_item(ITEM_MIAGAO_LOCATION)
    $ collect_item(ITEM_CHURCH_UNESCO)
    show screen item_pickup_screen(ITEM_MIAGAO_LOCATION)
    pause 2.5
    hide screen item_pickup_screen
    show screen item_pickup_screen(ITEM_CHURCH_UNESCO)
    pause 2.5
    hide screen item_pickup_screen

    jaden "Right? People sleep on Miagao. It's quiet, old, has history."

    menu:
        "Why is UPV even here though?":
            jump act1_jaden_upv_history
        "(That's enough for now)":
            jump act1_jaden_end

label act1_jaden_upv_history:
    jaden "UPV — University of the Philippines Visayas — was established in 1979."
    jaden "The main campus was intentionally placed in Miagao, away from the city."
    jaden "Built to serve the Visayas region. Marine science, fisheries, coastal development."
    jaden "You need to be near the sea to study the sea."

    player_char "So that's why there are wet labs and fishponds on campus."

    jaden "Exactly. UPV is one of the few UP campuses with a specific regional identity."
    jaden "You chose well."

    ## ITEM DROP
    $ collect_item(ITEM_UPV_HISTORY)
    show screen item_pickup_screen(ITEM_UPV_HISTORY)
    pause 2.5
    hide screen item_pickup_screen

    jump act1_jaden_end

label act1_jaden_end:
    jaden "Anyway — I'm going to keep walking around. Still figuring out where everything is."
    jaden "If you want to compare notes later, find me."
    if "sq_oblation" not in subquests_completed:
        $ _flip = renpy.random.randint(0, 1)
        if _flip == 0:
            menu:
                "★ Actually — tell me about the Oblation statue. What does it really mean?":
                    jump sq_oblation
                "(Alright, see you around.)":
                    jump act1_jaden_complete
        else:
            menu:
                "(Alright, see you around.)":
                    jump act1_jaden_complete
                "★ Actually — tell me about the Oblation statue. What does it really mean?":
                    jump sq_oblation
    else:
        jump act1_jaden_complete

label act1_jaden_complete:
    $ talked_jaden = True
    $ complete_task("talk_jaden")
    hide jaden with dissolve
    window hide
    return


## ============================================================================
## NPC 1 — JADEN (SECOND TALK — unlocks Group Chat)
## Must be triggered before quiz by talking to Jaden again
## ============================================================================

label act1_npc_jaden_second:
    window show

    if not talked_jaden:
        jump act1_npc_jaden

    
    jaden "Oh, you again! Did you find everyone?"

    if len(collected_items) < 5:
        jaden "You look like you're still missing some info. Talk to more people first."
        jaden "Manong Josh, Aleng Maria, Manong Chris, Tol Joseph — they all know things."
        window hide
        return

    jaden "Okay wait — I just made a group chat for us freshies."
    jaden "Here. I'm adding you."

    ## Phone buzz effect
    narrator_char "✉  Your phone buzzes."
    narrator_char "'Jaden added you to UPV Freshies 2024 🌊'"

    $ gc_unlocked = True
    $ phone_unlocked = True
    $ reveal_gc_batch()

    jaden "Press [[P]] anytime to check the chat. People are already posting chaos in there."
    jaden "Also — before you head to BOX 1, I think there's a checkpoint or something?"
    jaden "Like they test if you actually learned anything today. Good luck."

    $ jaden_second_talk = True
    hide jaden with dissolve
    window hide
    return


## ============================================================================
## NPC 2 — MANONG JOSH
## ============================================================================

label act1_npc_manong_josh:
    

    scene expression "images/ui/marillac.png" at fit_screen
    window show

    manong_josh "Ay, estudyante ka? Bagong-abot?"
    player_char "Yes po, Manong. Just arrived today."
    manong_josh "Maayo. Sit, sit. You look lost."

    menu:
        "What are the important landmarks here?":
            jump act1_josh_landmarks
        "Is there anything I need to know about Miagao?":
            jump act1_josh_general

label act1_josh_landmarks:
    manong_josh "Listen well. The Miagao Church — Santo Tomas de Villanueva Parish. Built in 1797."
    manong_josh "Big yellow-orange church. You can see it from almost anywhere."
    manong_josh "Beside it — the Plaza. Weekend market, fiestas."
    manong_josh "Then the Public Market. Cheap ulam, vegetables, fresh fish."
    manong_josh "Open early. If you go past 10 AM, the good stuff is already gone."

    player_char "What about near the university?"

    manong_josh "Near the UPV gate — sari-sari stores, carinderias, loading stations."
    manong_josh "Municipal hall is along the main road near the church. Documents, LGU stuff."

    ## ITEM DROP
    $ collect_item(ITEM_LANDMARKS)
    $ collect_item(ITEM_MARKET_HOURS)
    show screen item_pickup_screen(ITEM_LANDMARKS)
    pause 2.5
    hide screen item_pickup_screen
    show screen item_pickup_screen(ITEM_MARKET_HOURS)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "Anything else I should know?":
            jump act1_josh_general
        "(That's very helpful, Manong)":
            jump act1_josh_end

label act1_josh_general:
    manong_josh "Miagao is small. Church, market, university — you know all three, you know the town."
    manong_josh "Safe during daytime. Don't wander unfamiliar streets alone at night."
    manong_josh "Greet people properly. 'Manong,' 'Manang,' 'Ate,' 'Kuya.' They will remember you."

    player_char "Good to know, Manong."

    manong_josh "And the beach — Iloilo Strait. Students go on weekends. But ask locals before swimming."
    manong_josh "Not all spots are safe."

    ## ITEM DROP
    $ collect_item(ITEM_SAFETY_TIPS)
    show screen item_pickup_screen(ITEM_SAFETY_TIPS)
    pause 2.5
    hide screen item_pickup_screen

    jump act1_josh_end

label act1_josh_end:
    manong_josh "You seem like a good kid. Study hard."
    if "sq_miagao_heritage" not in subquests_completed:
        $ _flip = renpy.random.randint(0, 1)
        if _flip == 0:
            menu:
                "★ Manong, can you tell me more about the Miagao Church and the town's history?":
                    jump sq_miagao_heritage
                "(Thank you, Manong.)":
                    jump act1_josh_complete
        else:
            menu:
                "(Thank you, Manong.)":
                    jump act1_josh_complete
                "★ Manong, can you tell me more about the Miagao Church and the town's history?":
                    jump sq_miagao_heritage
    else:
        jump act1_josh_complete

label act1_josh_complete:
    $ talked_josh = True
    $ complete_task("talk_manong_josh")
    hide manong_josh with dissolve
    window hide
    return


## ============================================================================
## NPC 3 — ALENG MARIA
## ============================================================================

label act1_npc_aleng_maria:

    scene expression "images/ui/tinda.png" at fit_screen
    window show

    aleng_maria "Uy, estudyante! Gutom ka na? Kain na dali!"
    player_char "Actually, Aleng — I wanted to ask about food and budget around here."
    aleng_maria "Ay, tamang-tama! Sit, sit."

    menu:
        "How much does a meal cost here?":
            jump act1_maria_food_cost
        "How should I budget for the week?":
            jump act1_maria_budget
        "Where are the best spots to eat?":
            jump act1_maria_carinderias

label act1_maria_food_cost:
    aleng_maria "Rice meals — ₱45 to ₱70. Rice plus one viand."
    aleng_maria "Extra rice — ₱5 to ₱10. Some places give unlimited rice. Look for those!"
    aleng_maria "Merienda — puto, suman, banana cue — ₱5 to ₱15."
    aleng_maria "Water — ₱10 to ₱15 per bottle. Better to get a 5-gallon refill for ₱20 to ₱25."

    player_char "That's surprisingly affordable."

    aleng_maria "Miagao is tipid-friendly. Avoid sit-down restaurants. Carinderia life!"

    ## ITEM DROP
    $ collect_item(ITEM_MEAL_COST)
    show screen item_pickup_screen(ITEM_MEAL_COST)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "Where should I eat regularly?":
            jump act1_maria_carinderias
        "How much for the whole week?":
            jump act1_maria_budget

label act1_maria_carinderias:
    aleng_maria "Near the UPV gate — look for the tarpaulin with the lechon. Masustansya at mura."
    aleng_maria "Inside campus — CASAS cafeteria and student canteens."
    aleng_maria "Public market mornings — sinugno, tinola, kare-kare. Very cheap."
    aleng_maria "And my stall, of course! ₱60 — rice, pinakbet, fish. With smile pa."

    player_char "What's pinakbet?"
    aleng_maria "Ay, you don't know pinakbet?! That's your homework."

    menu:
        "Weekly budget?":
            jump act1_maria_budget
        "(Got it, Aleng!)":
            jump act1_maria_end

label act1_maria_budget:
    aleng_maria "Listen carefully. Food alone: ₱150 to ₱200 per day."
    aleng_maria "Breakfast — ₱30 to ₱40. Lunch — ₱50 to ₱70. Dinner — ₱50 to ₱70."
    aleng_maria "Tricycle fare within town — ₱10 to ₱15. Plaza to UPV: ₱15."
    aleng_maria "Jeepney to Iloilo City — ₱50 to ₱65 one way."
    aleng_maria "Week total? Minimum ₱1,500 for food and fare."

    player_char "I'll try to stick to ₱200 a day."
    aleng_maria "Smart! And cook sometimes. Instant noodles, egg, vegetables — filling and cheap."

    ## ITEM DROPS
    $ collect_item(ITEM_TRICYCLE_FARE)
    $ collect_item(ITEM_WEEKLY_BUDGET)
    show screen item_pickup_screen(ITEM_TRICYCLE_FARE)
    pause 2.5
    hide screen item_pickup_screen
    show screen item_pickup_screen(ITEM_WEEKLY_BUDGET)
    pause 2.5
    hide screen item_pickup_screen

    jump act1_maria_end

label act1_maria_end:
    aleng_maria "Don't skip meals to save money. Your brain needs food more than your wallet needs savings."
    aleng_maria "Sige! I'll save you the last portion of adobo!"
    $ talked_maria = True
    $ complete_task("talk_aleng_maria")
    hide aleng_maria_sprite with dissolve
    window hide
    return


## ============================================================================
## NPC 4 — MANONG CHRIS
## ============================================================================

label act1_npc_manong_chris:

    scene expression "images/ui/marillac.png" at fit_screen
    window show

    manong_chris "Ay, bag-o ka diri? Taga-diin ka?"
    player_char "Po? Sorry, I didn't catch that."
    manong_chris "Haha! I asked where you're from. I'm Chris. Lived in Miagao all my life."

    menu:
        "What language do people speak here?":
            jump act1_chris_language
        "What customs should I know?":
            jump act1_chris_customs
        "What's the Mass schedule at the church?":
            jump act1_chris_mass

label act1_chris_language:
    manong_chris "Local language is Kinaray-a — different from Hiligaynon in Iloilo City."
    manong_chris "Most people here also speak Hiligaynon and Filipino. But Kinaray-a? They'll love you for it."
    manong_chris "Repeat after me. Kamusta ka na?"
    player_char "Kamusta ka na!"
    manong_chris "Salamat — same as Filipino. Wara — means none or nothing."
    manong_chris "And the best one: 'Estudyante ako sa UPV.' Say that and doors open."
    player_char "Estudyante ako sa UPV!"
    manong_chris "Maayo! You're already half-local."

    ## ITEM DROP
    $ collect_item(ITEM_KINARAYA)
    show screen item_pickup_screen(ITEM_KINARAYA)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "What customs should I know?":
            jump act1_chris_customs
        "Mass schedule?":
            jump act1_chris_mass

label act1_chris_customs:
    manong_chris "Greet elders — Manong, Manang, Lolo, Lola. A nod is not enough."
    manong_chris "At 6 PM when the Angelus bells ring — pause. Don't talk loudly."
    manong_chris "Fiesta honors Santo Tomas de Villanueva — usually September. If invited inside someone's home, accept the food."
    manong_chris "Don't litter near the church or plaza. Miagaoanons take pride in these places."

    ## ITEM DROP
    $ collect_item(ITEM_LOCAL_CUSTOMS)
    show screen item_pickup_screen(ITEM_LOCAL_CUSTOMS)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "Mass schedule?":
            jump act1_chris_mass
        "(That's enough for now)":
            jump act1_chris_end

label act1_chris_mass:
    manong_chris "Sunday — 5:30 AM, 7:00 AM, 9:00 AM. Sometimes 5:30 PM."
    manong_chris "Weekdays — 6:00 AM."
    manong_chris "Even if you're not Catholic — it's open. Historical site. Just be respectful."
    manong_chris "No shorts. Cover your shoulders."

    ## ITEM DROP
    $ collect_item(ITEM_MASS_SCHEDULE)
    show screen item_pickup_screen(ITEM_MASS_SCHEDULE)
    pause 2.5
    hide screen item_pickup_screen

    jump act1_chris_end

label act1_chris_end:
    manong_chris "Miagao is small, but it has a big soul."
    manong_chris "If you're ever lost — look for the church tower. You can see it from almost anywhere."
    $ talked_chris = True
    $ complete_task("talk_manong_chris")
    hide manong_chris with dissolve
    window hide
    return


## ============================================================================
## NPC 5 — JOSEPH THE TRICYCLE DRIVER
## ============================================================================

label act1_npc_joseph_driver:
    

    scene expression "images/ui/tinda.png" at fit_screen
    window show

    joseph "Sakay! Saan? Saan?"
    player_char "Wait — Tol Joseph? Your name is on your jacket."
    joseph "Ha! Yes. Most people just call me Tol Joseph. You need a ride?"
    player_char "Actually — can I ask about the routes and fares first?"
    joseph "Of course. That's my specialty."

    menu:
        "What are the main tricycle routes?":
            jump act1_joseph_routes
        "How much is the fare to UPV?":
            jump act1_joseph_fare
        "Where are the main drop-off points?":
            jump act1_joseph_dropoffs

label act1_joseph_routes:
    joseph "Route 1 — Town Center to UPV Gate. Most common for students."
    joseph "Route 2 — Town Center to Public Market. Short hop."
    joseph "Route 3 — UPV Gate to Poblacion interior."
    joseph "Route 4 — Town Center to barangays: Kirayan, Sapa, Guibongan. Longer, higher fare."
    joseph "As a student — you'll mostly use Route 1 and 2."

    ## ITEM DROP
    $ collect_item(ITEM_ROUTES)
    show screen item_pickup_screen(ITEM_ROUTES)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "What's the fare to UPV?":
            jump act1_joseph_fare
        "Drop-off points?":
            jump act1_joseph_dropoffs

label act1_joseph_fare:
    joseph "Listen — drivers don't always post fares, so memorize this."
    joseph "Plaza to UPV Gate: ₱15. Short hops within town: ₱10."
    joseph "Farther barangays: ₱20 to ₱30."
    joseph "Special trip — whole tricycle to yourself: ₱50 to ₱80."
    joseph "If quoted too high: 'Pila man gid ang tama nga bayad?' — What's the right fare?"

    player_char "What about going to Iloilo City?"

    joseph "Jeepney from the highway junction. ₱50 to ₱65. Takes 45 minutes to an hour."
    joseph "Last trip back to Miagao from Tagbak — 6:30 to 7:00 PM."
    joseph "Miss it and you're sleeping in the city."

    ## ITEM DROP
    $ collect_item(ITEM_JEEPNEY_CITY)
    show screen item_pickup_screen(ITEM_JEEPNEY_CITY)
    pause 2.5
    hide screen item_pickup_screen

    menu:
        "Drop-off points?":
            jump act1_joseph_dropoffs
        "(That's what I needed)":
            jump act1_joseph_end

label act1_joseph_dropoffs:
    joseph "Drop-off points — very important!"
    joseph "UPV Main Gate. Miagao Plaza — the center of everything."
    joseph "Public Market. Municipal Hall. Highway junction for out-of-town."
    joseph "Rule: if you're not sure where to go — say 'Plaza.' Walk from there."

    ## ITEM DROP
    $ collect_item(ITEM_DROPOFFS)
    show screen item_pickup_screen(ITEM_DROPOFFS)
    pause 2.5
    hide screen item_pickup_screen

    jump act1_joseph_end

label act1_joseph_end:
    joseph "Welcome to Miagao, 'nak. Students who respect this town always look back on it fondly."
    joseph "Find me anytime — tricycle with the SB-19 sticker. That's me."
    $ talked_joseph = True
    $ complete_task("talk_joseph_driver")
    hide joseph_driver with dissolve
    window hide
    return


## ============================================================================
## NAVIGATION LABELS — Move between Act 1 maps
## ============================================================================

label act1_go_tindahan:
    narrator_char "(You head left toward the Tindahan area.)"
    $ act1_nav_target = "tindahan"
    ## Player enters tindahan from the right side (waypoint 7)
    $ player_map_x = 4900
    $ player_map_y = 2400
    window hide
    return

label act1_go_marillac:
    narrator_char "(You head right toward the Marillac area.)"
    $ act1_nav_target = "marillac"
    ## Player enters marillac from the top-left (waypoint 0)
    $ player_map_x = 325
    $ player_map_y = 650
    window hide
    return

label act1_go_banwa:
    narrator_char "(You head back to the Banwa entrance.)"
    $ act1_nav_target = "banwa"
    ## Set entry position based on which map we're leaving
    if current_map_bg == "ui/overhead_tindahan.png":
        ## Coming from tindahan — appear at left exit (waypoint 5)
        $ player_map_x = 100
        $ player_map_y = 2500
    else:
        ## Coming from marillac — appear at right exit (waypoint 7)
        $ player_map_x = 4900
        $ player_map_y = 2500
    window hide
    return


## ============================================================================
## PRE-BOX1 GATE — Must talk to Jaden again + complete quiz
## ============================================================================

label act1_prebox1_gate:
    window show

    narrator_char "(You approach BOX 1. A sign on the gate reads:)"
    narrator_char "\"Before you enter — let's see what you've learned today.\""

    ## Check if Jaden second talk happened
    if not jaden_second_talk:
        narrator_char "(Someone's waving at you from behind. It's Jaden.)"
        jump act1_npc_jaden_second

    ## Check if enough items collected
    if len(collected_items) < 8:
        narrator_char "(You feel like you haven't talked to enough people yet.)"
        narrator_char "(Talk to more locals before proceeding to BOX 1.)"
        window hide
        return

    ## Launch quiz
    narrator_char "The gate officer hands you a small card:"
    narrator_char "\"Answer these questions using what you've learned today.\""
    narrator_char "\"Your notebook doesn't help here. Only your memory does.\""

label act1_quiz_attempt:
    $ quiz_result = renpy.call_screen("quiz_screen")
    $ quiz_score  = quiz_result if quiz_result and quiz_result > 0 else 0

    $ results_return = renpy.call_screen("quiz_results_screen", quiz_score)

    if results_return == -1 or quiz_score < 4:
        ## Reset notebook question answers for retry
        $ [setattr(q, 'answered', False) for q in notebook_questions]
        $ [setattr(q, 'chosen_item_id', None) for q in notebook_questions]
        narrator_char "(You need at least 4/6 correct to enter BOX 1. Review what you've learned and try again.)"
        window hide
        return

    jump act1_box1_arrive


## ============================================================================
## ACT 1 COMPLETION
## ============================================================================

label act1_box1_arrive:
    window show

    narrator_char "(You step through the gate into BOX 1.)"
    narrator_char "(The bulletin board is covered in student notices. There's a posted map on the wall.)"
    narrator_char "(For the first time today, you feel like you might actually know where you are.)"

    play sound "task_complete.ogg"

    if quiz_score == len(notebook_questions):
        narrator_char "✓ PERFECT DETECTIVE — You absorbed everything Miagao had to offer today."
    elif quiz_score >= 4:
        narrator_char "✓ GOOD INSTINCTS — Most of Miagao's secrets are yours now."
    else:
        narrator_char "✓ STILL LEARNING — Some gaps remain. They'll catch up with you later."

    narrator_char "[[TASK 1 COMPLETE]] — Collected [len(collected_items)]/14 Info Items."
    narrator_char "[[TASK 2 COMPLETE]] — Completed Notebook Quiz: [quiz_score]/[len(notebook_questions)]."
    narrator_char "[[TASK 3 COMPLETE]] — Reached BOX 1."
    narrator_char "[[ACT 1 COMPLETE]] — Arrival in Miagao."

    $ complete_task("reach_box1")
    $ complete_task("act1_complete")

    stop music fadeout 1.0
    play music "audio/Act2.mp3" fadein 1.0
    window hide
    return

## ============================================================================
## END OF ACT 1
## ============================================================================
