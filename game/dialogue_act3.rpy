## ============================================================================
## ACT 3 DIALOGUES — Social / Exploration (After Enrollment)
## Converted from Ink dialogue files
## ============================================================================

## --- Mikhaela ---
label npc_mikhaela:
    scene bg act3_dialogue
    window show

    mikhaela "You survived Sir Ruel? Respect."
    mikhaela "Want some? Got this isaw from the kiosk near the gate. Best post-enrollment reward."

    menu:
        "Sure, thanks.":
            jump npc_mikhaela_eat
        "No thanks, I'm good.":
            jump npc_mikhaela_decline

label npc_mikhaela_eat:
    narrator_char "(You take a stick of isaw. Smoky, savory, and exactly what you needed.)"
    $ complete_task("talk_mikhaela")
    window hide
    return

label npc_mikhaela_decline:
    mikhaela "Your loss, freshie."
    $ complete_task("talk_mikhaela")
    window hide
    return

## --- Jaden ---
label act3_npc_jaden:
    scene bg act3_dialogue
    window show

    jaden "Hey! You made it out of Sir Ruel's class alive."

    menu:
        "Barely. He's intense.":
            jump npc_jaden_intense
        "It was easy.":
            jump npc_jaden_easy
        "I need food. Now.":
            jump npc_jaden_hungry

label npc_jaden_intense:
    jaden "Same. I just came from the CUB too—got my partial stipend tagged."
    jump npc_jaden_invite

label npc_jaden_easy:
    jaden "Confident ka ah. I just came from the CUB too—got my partial stipend tagged."
    jump npc_jaden_invite

label npc_jaden_hungry:
    jaden "Real. I just came from the CUB too—got my partial stipend tagged."
    jump npc_jaden_invite

label npc_jaden_invite:
    jaden "I'm heading to Ceazar to meet some friends. It's on the way to the dorms—walk with me?"

    menu:
        "Sure, let's go.":
            jump npc_jaden_go
        "Where is Ceazar?":
            jump npc_jaden_explain

label npc_jaden_explain:
    jaden "It's near HSU, just past the dorm area."
    jaden "Finish up with the dorm staff first, then let's head there. Nice breeze, short walk."
    jump npc_jaden_go

label npc_jaden_go:
    jaden "All settled?"
    jaden "Come on, let's walk it off. My friends are waiting at Ceazar."
    $ complete_task("talk_jaden")
    window hide
    return

label Act3_npc_jaden:
    jump act3_npc_jaden

## --- Caezar (at Ceazar) ---
label npc_caezar:
    scene bg act3_dialogue
    window show

    caezar "Oy, JADEN! Finally."
    caezar "Welcome to UPV. First-day survival rate is currently 100%%, I see."
    caezar "So, freshie—what's the game plan? Honors? Or saving the world?"

    menu:
        "I need to maintain my scholarship. Grades are priority.":
            jump npc_caezar_response
        "I want to meet people. Join orgs.":
            jump npc_caezar_response
        "I just want to graduate on time.":
            jump npc_caezar_response

label npc_caezar_response:
    caezar "Solid answer."
    caezar "Just remember: UP isn't only about classrooms and deadlines."
    narrator_char "(He gestures toward the field and the trees.)"
    caezar "Look around. Don't forget to look up once in a while."
    $ complete_task("talk_caezar")
    window hide
    return
