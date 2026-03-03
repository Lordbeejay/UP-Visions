## ============================================================================
## ACT 3 DIALOGUES — Social / Exploration (After Enrollment)
## Converted from Ink dialogue files
## ============================================================================

## --- Mikhaela ---
label npc_mikhaela:
    window show

    mikhaela "Did you survive Sir Ruel?"
    mikhaela "Want some? It's isaw from the kiosk near the gate. Best post-enrollment reward."

    menu:
        "Sure, thanks.":
            jump npc_mikhaela_eat
        "No thanks, I'm good.":
            jump npc_mikhaela_decline

label npc_mikhaela_eat:
    narrator_char "(You take a stick of isaw. It's perfectly grilled.)"
    mikhaela "See? Instant morale boost."
    $ complete_task("talk_mikhaela")
    window hide
    return

label npc_mikhaela_decline:
    mikhaela "Your loss! I'll save you one if you change your mind."
    $ complete_task("talk_mikhaela")
    window hide
    return

## --- Jaden ---
label act3_npc_jaden:
    jump Act3_npc_jaden

label Act3_npc_jaden:
    window show

    jaden "Hey! You survived Sir Ruel."

    menu:
        "Barely. He's intense.":
            jump npc_jaden_intense
        "It was easy.":
            jump npc_jaden_easy
        "I need food. Now.":
            jump npc_jaden_hungry

label npc_jaden_intense:
    jaden "Same. I came from CUB and got my stipend papers tagged."
    jaden "That line took forever."
    jump npc_jaden_invite

label npc_jaden_easy:
    jaden "Wow, confident freshie."
    jaden "I came from CUB too and got my stipend papers tagged."
    jump npc_jaden_invite

label npc_jaden_hungry:
    jaden "Real. Enrollment burns more energy than PE."
    jaden "I just finished at CUB too."
    jump npc_jaden_invite

label npc_jaden_invite:
    jaden "I'm heading to Lover's Lane to meet some friends. Want to walk with me?"

    menu:
        "Sure, let's go.":
            jump npc_jaden_go
        "Where is Lover's Lane?":
            jump npc_jaden_explain

label npc_jaden_explain:
    jaden "It's near HSU, just past the dormitory road."
    jaden "It's breezy there, and the sunset is good. It's walking distance."
    jump npc_jaden_go

label npc_jaden_go:
    jaden "All settled?"
    jaden "Come on, let's walk it off. My friends are waiting at Lover's Lane."
    $ complete_task("talk_jaden")
    window hide
    return

## --- Caezar (at Lover's Lane) ---
label npc_caezar:
    window show

    caezar "Oy, Jaden! Finally."
    caezar "Welcome to UPV. First-day survival rate is still 100%%, I see."
    caezar "So, freshie, what's the plan? Honors, org life, or just survive semester one?"

    menu:
        "I need to maintain my scholarship. Grades are priority.":
            jump npc_caezar_response
        "I want to meet people. Join orgs.":
            jump npc_caezar_response
        "I just want to graduate on time.":
            jump npc_caezar_response

label npc_caezar_response:
    caezar "Good answer."
    caezar "Just remember: UP isn't just about the classroom."
    narrator_char "(He gestures to the field and the trees.)"
    caezar "Look around once in a while. That's part of learning too."
    $ complete_task("talk_caezar")
    window hide
    return
