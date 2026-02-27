## ============================================================================
## ACT 2 DIALOGUES — Exploring BOX 1 (CUB / OSA / Enrollment)
## Converted from Ink dialogue files
## ============================================================================

## --- Ms. Santos (OSA at CUB) ---
label npc_ms_santos:
    window show

    ms_santos "Good morning. Catch your breath first. That uphill walk is a rite of passage."
    ms_santos "Alright. Under RA 10931, your tuition is free. But we need to tag external grants. Are you a recipient?"

    menu:
        "Yes, I passed the DOST-SEI exam.":
            jump npc_santos_dost
        "I have a CHED Merit Scholarship.":
            jump npc_santos_ched
        "None, ma'am. Just the Free Tuition Law.":
            jump npc_santos_none

label npc_santos_dost:
    ms_santos "Congrats. I need your Notice of Award. Tagged as DOST-RA 7687. Book allowance and stipend will be processed later. No grades below 5.0, okay?"
    jump npc_santos_clearance

label npc_santos_ched:
    ms_santos "Okay. Tagged as CHED Merit. We'll bill them for the extras."
    jump npc_santos_clearance

label npc_santos_none:
    ms_santos "Noted. You are under the standard Free Tuition. If you need extra help for living expenses later, watch out for the SLAS (Student Learning Assistance System) announcements."
    jump npc_santos_clearance

label npc_santos_clearance:
    ms_santos "Here is your clearance. Go back down to Sir Ruel at the New Admin."
    ms_santos "Oh, and one more thing..."
    ms_santos "That's the GCSU (Guidance and Counseling) next door. If the pressure gets too much—homesickness, academic stress, anything—just knock."
    ms_santos "It's free, confidential, and they have aircon. Don't be afraid to use it."
    $ complete_task("talk_ms_santos")
    window hide
    return

## --- Sarah (Enrollment Line) ---
label npc_sarah:
    window show
    sarah "Please have your Form 5 and Medical Clearance ready!"
    sarah "Attention! If you are a scholar (DOST/CHED) or need to apply for financial assistance, you must go to the OSA at the CUB first!"
    sarah "Do not line up here yet!"
    $ complete_task("talk_sarah")
    window hide
    return
