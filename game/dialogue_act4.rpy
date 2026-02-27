## ============================================================================
## ACT 4 DIALOGUES — Dorm Accommodation
## Converted from Ink dialogue files
## ============================================================================

## --- Dorm Manager ---
label npc_dorm_manager:
    window show

    dorm_mgr "Male or Female wing?"
    dorm_mgr "We are at 90%% capacity. We prioritize students based on the Point System. Where is your permanent residence?"

    menu:
        "Luzon / Mindanao / Outside Panay.":
            jump npc_dorm_far
        "Aklan / Capiz / Antique (3-4 hours away).":
            jump npc_dorm_mid
        "Iloilo City / Oton (1-2 hours away).":
            jump npc_dorm_near

label npc_dorm_far:
    dorm_mgr "Okay, that gives you maximum points for Distance. Income bracket?"
    jump npc_dorm_rules

label npc_dorm_mid:
    dorm_mgr "Okay, that gives you good points for Distance. Income bracket?"
    jump npc_dorm_rules

label npc_dorm_rules:
    dorm_mgr "Alright. You qualify for a slot. Here are the rules:"
    dorm_mgr "1. Curfew is 10:00 PM. The gates are locked."
    dorm_mgr "2. No electric coils, heaters, or rice cookers inside the room."
    dorm_mgr "3. Visitors are allowed in the lobby only."

    menu:
        "Understood.":
            jump npc_dorm_sign
        "What happens if I miss curfew?":
            jump npc_dorm_curfew

label npc_dorm_curfew:
    dorm_mgr "First offense, warning. Second offense, community service. Third offense, eviction. Don't test me."
    jump npc_dorm_sign

label npc_dorm_sign:
    dorm_mgr "Sign here. Your room key is #207."
    $ complete_task("talk_dorm_manager")
    window hide
    return

label npc_dorm_near:
    dorm_mgr "You live in the city? You are currently Waitlist #5."
    dorm_mgr "You might need to look for a boarding house in town if a slot doesn't open up by Friday."
    $ complete_task("talk_dorm_manager")
    window hide
    return
