## ============================================================================
## ACT 3 DIALOGUES — Social / Exploration (After Enrollment)
## Upgraded to match Act 1 dialogue style
## ============================================================================

## --- Mikhaela ---
label npc_mikhaela:
    show mikhaela at right
    window show

    mikhaela "Uy, you made it out alive from Sir Ruel's gauntlet?"
    player_char "Barely. My legs still hurt from all the uphill walking."
    mikhaela "Valid. Here, reward food. Isaw from the kiosk near the gate—freshly grilled."

    menu:
        "Sure, thanks.":
            jump npc_mikhaela_eat
        "No thanks, I'm good.":
            jump npc_mikhaela_decline

label npc_mikhaela_eat:
    narrator_char "(You take a stick of isaw. Smoky, savory, and exactly what you needed.)"
    mikhaela "See? Best post-enrollment therapy."
    mikhaela "Campus life tip: always keep emergency snack money."
    player_char "Noted. Food is now part of my survival strategy."
    $ complete_task("talk_mikhaela")
    hide mikhaela
    window hide
    return

label npc_mikhaela_decline:
    mikhaela "Your loss! But if you change your mind, this kiosk closes late."
    mikhaela "Good luck with the rest of your rounds, freshie."
    $ complete_task("talk_mikhaela")
    hide mikhaela
    window hide
    return

## --- Jaden ---
label Act3_npc_jaden:
    show jaden at left
    window show

    jaden "Hey! You survived Sir Ruel and enrollment day. That's already a major achievement."

    menu:
        "Barely. He's intense.":
            jump npc_jaden_intense
        "It was easy.":
            jump npc_jaden_easy
        "I need food. Now.":
            jump npc_jaden_hungry

label npc_jaden_intense:
    jaden "Right? One look from him and your soul submits requirements on its own."
    jaden "I just came from CUB too—got my partial stipend tagged."
    player_char "Nice. At least we both progressed today."
    jump npc_jaden_invite

label npc_jaden_easy:
    jaden "Confident. I respect it."
    jaden "I just came from CUB too—got my partial stipend tagged."
    player_char "Then today wasn't a waste after all."
    jump npc_jaden_invite

label npc_jaden_hungry:
    jaden "Same energy. Enrollment paperwork burns calories for some reason."
    jaden "I just came from CUB too—got my partial stipend tagged."
    player_char "Congrats. Food first, then planning."
    jump npc_jaden_invite

label npc_jaden_invite:
    jaden "I'm heading to Lover's Lane to meet a friend. It's on the way to the dorms."
    jaden "Want to walk with me?"

    menu:
        "Sure, let's go.":
            jump npc_jaden_go
        "Where is Lover's Lane?":
            jump npc_jaden_explain

label npc_jaden_explain:
    jaden "It's near HSU, just past the dormitory area."
    jaden "Shady trees, good breeze, and people hang out there between classes."
    jaden "Come on—it's walking distance."
    jump npc_jaden_go

label npc_jaden_go:
    jaden "All set? Let's walk it off."
    jaden "My friend is waiting at Lover's Lane. You'll like the vibe there."
    $ complete_task("talk_jaden")
    hide jaden
    window hide
    return

## --- Caezar (at Lover's Lane) ---
label npc_caezar:
    show caezar at center
    window show

    caezar "Oy, Jaden. Finally."
    caezar "And this must be the new batch. Welcome to UPV."
    caezar "First day survival rate looks like 100%% so far."
    caezar "So, freshie—what's your game plan?"

    menu:
        "I need to maintain my scholarship. Grades are priority.":
            jump npc_caezar_scholar
        "I want to meet people. Join orgs.":
            jump npc_caezar_orgs
        "I just want to graduate on time.":
            jump npc_caezar_grad

label npc_caezar_scholar:
    caezar "Solid. Discipline early, freedom later."
    caezar "Just don't isolate yourself. Even scholars need a support circle."
    jump npc_caezar_response

label npc_caezar_orgs:
    caezar "Good call. Orgs can shape your whole UP life."
    caezar "Pick one that builds your skills, and one that's just fun."
    jump npc_caezar_response

label npc_caezar_grad:
    caezar "Most practical answer of the day."
    caezar "Keep that pace, but don't speedrun college so hard you forget to live it."
    jump npc_caezar_response

label npc_caezar_response:
    caezar "Whatever path you take, remember this: UP isn't just classrooms and deadlines."
    narrator_char "(He gestures toward the field and the line of trees along the path.)"
    caezar "Look around once in a while. These moments matter too."
    player_char "I'll remember that."
    $ complete_task("talk_caezar")
    hide caezar
    window hide
    return
