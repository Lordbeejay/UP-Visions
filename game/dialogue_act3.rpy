## ============================================================================
## ACT 3 DIALOGUES — Social / Exploration (After Enrollment)
## Converted from Ink dialogue files
## ============================================================================

## --- Mikhaela ---
label npc_mikhaela:
    window show

    mikhaela "Did you survive Sir Ruel?"
    mikhaela "Want some? It's isaw from the kiosk near the gate. Best reward after enrollment."

    menu:
        "Sure, thanks.":
            jump npc_mikhaela_eat
        "No thanks, I'm good.":
            jump npc_mikhaela_decline

label npc_mikhaela_eat:
    narrator_char "(You take a stick of isaw. It's perfectly grilled.)"
    $ complete_task("talk_mikhaela")
    window hide
    return

label npc_mikhaela_decline:
    mikhaela "Your loss!"
    $ complete_task("talk_mikhaela")
    window hide
    return

## --- Jaden ---
label act3_npc_jaden:
    window show

    jaden "Hey! You survived Sir Ruel!"

    menu:
        "Barely. He's intense.":
            jump npc_jaden_intense
        "It was easy.":
            jump npc_jaden_easy
        "I need food. Now.":
            jump npc_jaden_hungry

label npc_jaden_intense:
    jaden "Same. I just came from the CUB too, got my partial stipend tagged."
    jump npc_jaden_invite

label npc_jaden_easy:
    jaden "Same. I just came from the CUB too, got my partial stipend tagged."
    jump npc_jaden_invite

label npc_jaden_hungry:
    jaden "Same. I just came from the CUB too, got my partial stipend tagged."
    jump npc_jaden_invite

label npc_jaden_invite:
    jaden "Hey, I'm heading to Lover's Lane to meet some friends. It's on the way to the dorms. Want to walk with me?"

    menu:
        "Sure, let's go.":
            jump npc_jaden_go
        "Where is Lover's Lane?":
            jump npc_jaden_explain

label npc_jaden_explain:
    jaden "It's near HSU, after the dormitory area. Let's go there after you've finished talking with the dorm staff."
    jaden "It's nice and windy there. Come on, it's walking distance."
    jump npc_jaden_go

label npc_jaden_go:
    jaden "All settled?"
    jaden "Come on, let's walk it off. My friends are waiting at Lover's Lane."
    $ complete_task("talk_jaden")
    window hide
    return

label Act3_npc_jaden:
    jump act3_npc_jaden

## --- Caezar (at Lover's Lane) ---
label npc_caezar:
    window show

    caezar "Oy, JADEN! Finally."
    caezar "Welcome to UPV. First day survival rate is currently 100%%, I see."
    caezar "So, freshie. What's the plan? You here to get honors, or here to save the world?"

    menu:
        "I need to maintain my scholarship. Grades are priority.":
            jump npc_caezar_response
        "I want to meet people. Join orgs.":
            jump npc_caezar_response
        "I just want to graduate on time.":
            jump npc_caezar_response

label npc_caezar_response:
    caezar "Good answers."
    caezar "Just remember: UP isn't just about the classroom."
    narrator_char "(He gestures to the field and the trees.)"
    caezar "Look at this. Don't forget to look up once in a while."
    $ complete_task("talk_caezar")
    window hide
    return
