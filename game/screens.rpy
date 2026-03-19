################################################################################
## Styles
################################################################################
screen notebook_intro_screen():
    modal True
    zorder 200

    add "#1a1a2e" alpha 0.97

    # Centered notebook card — visually inspired by dialogue UI, not a dialogue window
    frame:
        xalign 0.5
        yalign 0.5
        xsize 680
        ysize 560
        padding (0, 0, 0, 0)
        background Frame(Solid("#1a0a10f0"), 0, 0)

        vbox:
            spacing 0

            # Header (accented strip)
            frame:
                background Frame(Solid("#f6d79d11"), 0, 0)
                xfill True
                padding (24, 18, 24, 18)
                hbox:
                    spacing 12
                    text "🔍" size 24
                    vbox:
                        spacing 2
                        text "DETECTIVE NOTEBOOK" size 13 color gui.accent_color bold True
                        text "Freshie Field Notes — Day 1" size 11 color "#6b7280"

            # Content area (scrollable list)
            frame:
                xfill True
                ysize 420
                padding (18, 14, 18, 14)
                background Solid("#0f0f1a")

                viewport:
                    xfill True
                    ysize 420
                    scrollbars "vertical"
                    mousewheel True

                    vbox:
                        spacing 10
                        xfill True

                        text "Find answers to these questions by talking to the locals." size 12 color "#9ca3af" italic True
                        null height 8

                        for q in notebook_questions:
                            frame:
                                xfill True
                                padding (10, 8, 10, 8)
                                background Frame(Solid("#111128"), 0, 0)

                                hbox:
                                    spacing 12
                                    xfill True
                                    text "?" size 18 color "#a78bfa" yalign 0.5
                                    vbox:
                                        spacing 2
                                        xfill True
                                        text q.text size 13 color "#e2e8f0"
                                        text "[ not yet discovered ]" substitute False size 11 color "#4b5563" italic True

            # Footer button
            frame:
                background Frame(Solid("#1e1e3a"), 0, 0)
                xfill True
                padding (20, 12, 20, 12)
                hbox:
                    xfill True
                    textbutton "Start Exploring →" style "notebook_btn" xalign 0.5 action Return()

style notebook_btn:
    background gui.accent_color
    hover_background gui.hover_color
    padding (20, 10, 20, 10)

style notebook_btn_text:
    color "#ffffff"
    hover_color "#ffffff"
    size 13
    bold True



## Make the namebox available for styling through the Character object.
init python:
    speaker_portraits = {
        ## Act 1
        "Jaden": "images/npcs/jaden.png",
        "Manong Josh": "images/npcs/manongjosh.png",
        "Aleng Maria": "images/npcs/alengmaria.png",
        "Manong Chris": "images/npcs/manong_chris.png",
        "Joseph": "images/npcs/joseph_driver.png",
        ## Act 2
        "ate bea": "images/npcs/ate_bea.png",
        "kuya mark": "images/npcs/kuya_mark.png",
        "maam reyes": "images/npcs/maam_reyes.png",
        "sir allan": "images/npcs/sir_allan.png",
        ## Act 3/4 NPCs
        "Sarah": "images/npcs/sarah.png",
        "Caezar": "images/npcs/caezar.png",
        "Manong Guard": "images/npcs/manong_guard.png",
        "Sir Ruel": "images/npcs/sir_ruel.png",
        "Ms. Santos": "images/npcs/ms_santos.png",
        "Dorm Manager": "images/npcs/dorm_mgr.png",
        ## Act 5
        "Prof. Lena": "images/npcs/prof_lena.png",
        "Kuya Rico": "images/npcs/kuya_rico.png",
        "Ate Grace": "images/npcs/ate_grace.png",
        "Dan": "images/npcs/classmate_dan.png",
        ## Act 6
        "Mika": "images/npcs/mika.png",
        "Kuya Tomas": "images/npcs/kuya_tomas.png",
        "Ate Jenny": "images/npcs/ate_jenny.png",
        "Coach Ramon": "images/npcs/coach_ramon.png",
        ## Act 7
        "Ate Rosa": "images/npcs/ate_rosa.png",
        "Kuya Neil": "images/npcs/kuya_neil.png",
        "Prof. Santos": "images/npcs/prof_santos.png",
        "Bea": "images/npcs/classmate_bea.png",
        ## Act 8
        "Ate Linda": "images/npcs/ate_linda.png",
        "Nanay Elena": "images/npcs/nanay_elena.png",
        "Prof. Reyes": "images/npcs/prof_reyes.png",
    }

    speaker_titles = {
        ## Act 1
        "Jaden": "Fellow Freshie",
        "Manong Josh": "Town Guide",
        "Aleng Maria": "Carinderia Owner",
        "Manong Chris": "Local Resident",
        "Joseph": "Tricycle Driver",
        ## Act 2
        "ate bea": "Upperclassman Guide",
        "kuya mark": "Campus Security",
        "maam reyes": "Admin Staff",
        "sir allan": "Faculty Member",
        ## Act 3/4
        "Sarah": "Fellow Student",
        "Caezar": "Campus Regular",
        "Manong Guard": "Gate Guard",
        "Sir Ruel": "Strict Professor",
        "Ms. Santos": "OSA Staff",
        "Dorm Manager": "Dorm Manager",
        ## Act 5
        "Prof. Lena": "GE Professor",
        "Kuya Rico": "Senior Adviser",
        "Ate Grace": "Council Rep",
        "Dan": "Fellow Freshie",
        ## Act 6
        "Mika": "Org Recruiter",
        "Kuya Tomas": "Scholarship Staff",
        "Ate Jenny": "OSA Staff",
        "Coach Ramon": "Sports Coordinator",
        ## Act 7
        "Ate Rosa": "Campus Librarian",
        "Kuya Neil": "Lab Attendant",
        "Prof. Santos": "Research Mentor",
        "Bea": "Study Organizer",
        ## Act 8
        "Ate Linda": "Canteen Worker",
        "Nanay Elena": "Dorm Housemother",
        "Prof. Reyes": "Senior Faculty",
    }

    # Warm portrait assets so they appear instantly on first dialogue line.
    for _portrait_path in speaker_portraits.values():
        try:
            renpy.cache_pin(_portrait_path)
        except Exception:
            try:
                renpy.load_image(_portrait_path)
            except Exception:
                pass

    def get_speaker_portrait(who_text):
        if not who_text:
            return None
        return speaker_portraits.get(who_text)

    def get_speaker_title(who_text):
        if not who_text:
            return None
        return speaker_titles.get(who_text)

    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    left_margin 280
    right_margin 80
    bottom_margin 56
    background Solid("#00000000")
    padding (0, 0, 0, 0)

style say_content_vbox is vbox:
    xfill True
    yfill True
    spacing 8
    padding (36, 20, 36, 20)

style namebox:
    xalign 0.5
    xfill False
    yalign 0.0
    top_margin 0
    bottom_margin 4
    left_margin 0
    right_margin 0
    background Frame("gui/namebox_gold.png", 8, 8, 8, 8)
    padding (18, 5, 18, 5)

style say_label:
    properties gui.text_properties("name")
    size 22
    bold True
    xalign 0.5
    text_align 0.5
    yalign 0.5
    color "#1a0a10"
    outlines []
    antialias False

style say_dialogue:
    properties gui.text_properties("dialogue")
    xalign 0.5
    xfill True
    text_align 0.5
    top_margin 4
    bottom_margin 4
    left_margin 40
    right_margin 40
    color "#f1debf"
    outlines [(2, "#1a0a10", 0, 0), (1, "#f6d79d22", 1, 1)]
    line_spacing 8
    antialias False
    adjust_spacing False

style say_dialogue_center is say_dialogue:
    top_margin 0
    bottom_margin 0
    xfill False
    xmaximum 1600
    xalign 0.5
    yalign 0.5
    size 28
    color "#f1debf"
    outlines [(3, "#1e0c12", 0, 0), (1, "#f6d79d44", 2, 2)]

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"
    zorder 1
    default _hovered_choice = -1

    ## Outer glow border
    frame:
        style "choice_area"

        frame:
            style "choice_content"

            vbox:
                style "choice_vbox"

                ## Decorative top ornament
                hbox:
                    xalign 0.5
                    spacing 6

                    frame:
                        xsize 30
                        ysize 2
                        yalign 0.5
                        background Solid("#f6d79d44")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 6
                        ysize 6
                        yalign 0.5
                        background Solid("#f6d79d")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 60
                        ysize 2
                        yalign 0.5
                        background Solid("#f6d79d")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 6
                        ysize 6
                        yalign 0.5
                        background Solid("#f6d79d")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 30
                        ysize 2
                        yalign 0.5
                        background Solid("#f6d79d44")
                        padding (0, 0, 0, 0)

                null height 4

                for _idx, i in enumerate(items):
                    textbutton (("◇ " if _hovered_choice == _idx else "  ") + i.caption) action i.action hovered SetScreenVariable("_hovered_choice", _idx) unhovered SetScreenVariable("_hovered_choice", -1) at choice_hover_anim


transform choice_hover_anim:
    on idle:
        easein 0.1 xoffset 0 zoom 1.0
    on hover:
        easein 0.1 xoffset 12 zoom 1.03


## Act Transition screen #######################################################
##
## Shown between acts: completion banner and next-act title card.

transform tr_overlay_fade:
    alpha 0.0
    easein 0.3 alpha 1.0

transform tr_panel_rise:
    alpha 0.0 yoffset 20
    pause 0.05
    easein 0.25 alpha 1.0 yoffset 0

transform tr_title_reveal:
    alpha 0.0 zoom 0.95
    pause 0.1
    easein 0.2 alpha 1.0 zoom 1.0

transform tr_divider_grow:
    alpha 0.0 xzoom 0.0
    pause 0.15
    easein 0.2 alpha 1.0 xzoom 1.0

transform tr_subtitle_fade:
    alpha 0.0 yoffset 5
    pause 0.2
    easein 0.2 alpha 1.0 yoffset 0

transform tr_star_spin:
    alpha 0.0 rotate 0
    pause 0.08
    easein 0.25 alpha 1.0 rotate 360

screen act_transition(title, subtitle, mode="complete"):

    ## Full overlay — gradient-like with layered solids
    add Solid("#000000bb") at tr_overlay_fade

    ## Outer decorative frame (border glow effect)
    frame:
        xalign 0.5
        yalign 0.5
        xminimum 680
        xmaximum 780
        padding (4, 4, 4, 4)
        background Frame(Solid("#f6d79d44"), 0, 0)
        at tr_panel_rise

        ## Main panel
        frame:
            xfill True
            padding (48, 40, 48, 40)
            background Frame(Solid("#1e0c12f0"), 0, 0)

            vbox:
                xalign 0.5
                spacing 0

                ## Top ornament: triple line
                hbox:
                    xalign 0.5
                    spacing 8
                    at tr_divider_grow

                    frame:
                        xsize 60
                        ysize 2
                        yalign 0.5
                        background Solid("#f6d79d88")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 12
                        ysize 12
                        yalign 0.5
                        background Solid("#f6d79d")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 120
                        ysize 2
                        yalign 0.5
                        background Solid("#f6d79d")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 12
                        ysize 12
                        yalign 0.5
                        background Solid("#f6d79d")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 60
                        ysize 2
                        yalign 0.5
                        background Solid("#f6d79d88")
                        padding (0, 0, 0, 0)

                null height 24

                ## Completion star or intro label
                if mode == "complete":
                    text "★":
                        xalign 0.5
                        size 40
                        color "#f6d79d"
                        outlines [(2, "#1e0c12", 0, 0)]
                        at tr_star_spin
                elif mode == "welcome":
                    text "✦":
                        xalign 0.5
                        size 36
                        color "#ffd700"
                        outlines [(2, "#1e0c12", 0, 0)]
                        at tr_star_spin
                elif mode == "ending":
                    text "★":
                        xalign 0.5
                        size 36
                        color "#ffd700"
                        outlines [(2, "#1e0c12", 0, 0)]
                        at tr_star_spin
                elif mode == "credits":
                    text "◇":
                        xalign 0.5
                        size 20
                        color "#f6d79d66"
                        at tr_subtitle_fade
                else:
                    text "— NEW CHAPTER —":
                        xalign 0.5
                        size 14
                        color "#f6d79d99"
                        outlines [(1, "#1e0c12", 0, 0)]
                        at tr_subtitle_fade

                null height 12

                ## Main title
                if mode == "complete":
                    text title:
                        xalign 0.5
                        text_align 0.5
                        size 38
                        color "#b8e6b0"
                        outlines [(4, "#1e0c12", 0, 0), (2, "#3a7a3a55", 2, 2)]
                        at tr_title_reveal
                elif mode == "welcome":
                    text title:
                        xalign 0.5
                        text_align 0.5
                        size 42
                        color "#ffd700"
                        outlines [(4, "#1e0c12", 0, 0), (2, "#8b6914aa", 2, 2)]
                        at tr_title_reveal
                elif mode == "ending":
                    text title:
                        xalign 0.5
                        text_align 0.5
                        size 40
                        color "#ffd700"
                        outlines [(4, "#1e0c12", 0, 0), (2, "#8b6914aa", 2, 2)]
                        at tr_title_reveal
                elif mode == "credits":
                    text title:
                        xalign 0.5
                        text_align 0.5
                        size 18
                        color "#888888"
                        outlines [(2, "#1e0c12", 0, 0)]
                        at tr_title_reveal
                else:
                    text title:
                        xalign 0.5
                        text_align 0.5
                        size 46
                        color "#ffd700"
                        outlines [(4, "#1e0c12", 0, 0), (2, "#8b6914aa", 2, 2)]
                        at tr_title_reveal

                null height 8

                ## Center divider
                hbox:
                    xalign 0.5
                    spacing 6
                    at tr_divider_grow

                    frame:
                        xsize 80
                        ysize 1
                        yalign 0.5
                        background Solid("#f6d79d66")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 6
                        ysize 6
                        yalign 0.5
                        background Solid("#f6d79d")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 80
                        ysize 1
                        yalign 0.5
                        background Solid("#f6d79d66")
                        padding (0, 0, 0, 0)

                null height 14

                ## Subtitle
                if subtitle:
                    text subtitle:
                        xalign 0.5
                        text_align 0.5
                        size 22
                        color "#f1debf"
                        outlines [(2, "#1e0c12", 0, 0)]
                        line_spacing 6
                        at tr_subtitle_fade

                null height 24

                ## Bottom ornament: triple line (mirrors top)
                hbox:
                    xalign 0.5
                    spacing 8
                    at tr_divider_grow

                    frame:
                        xsize 60
                        ysize 2
                        yalign 0.5
                        background Solid("#f6d79d88")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 12
                        ysize 12
                        yalign 0.5
                        background Solid("#f6d79d")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 120
                        ysize 2
                        yalign 0.5
                        background Solid("#f6d79d")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 12
                        ysize 12
                        yalign 0.5
                        background Solid("#f6d79d")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 60
                        ysize 2
                        yalign 0.5
                        background Solid("#f6d79d88")
                        padding (0, 0, 0, 0)

    ## Click or key to dismiss
    key "dismiss" action Return()

    ## Auto-dismiss
    timer 2.0 action Return()


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xfill True
    xalign 0.5
    spacing 6

style choice_content is default:
    xfill True
    ymaximum 200
    yalign 0.5
    background Frame(Solid("#1e0c12ee"), 0, 0)
    padding (20, 14, 20, 14)

style choice_area is default:
    xalign 0.5
    yalign 1.0
    xfill True
    ysize gui.textbox_height
    left_margin 120
    right_margin 120
    bottom_margin 92
    background Frame(Solid("#f6d79d22"), 0, 0)
    padding (3, 3, 3, 3)

style choice_button is default:
    properties gui.button_properties("choice_button")
    background Solid("#00000000")
    hover_background Frame(Solid("#f6d79d11"), 0, 0)
    selected_background Solid("#00000000")
    insensitive_background Solid("#00000000")
    left_padding 8
    right_padding 8
    top_padding 4
    bottom_padding 4
    xfill True
    xalign 0.5

style choice_button_text is default:
    properties gui.text_properties("choice_button")
    color "#f1debf"
    hover_color "#ffd700"
    outlines [(2, "#1e0c12", 0, 0)]


################################################################################
## Student Portal
################################################################################





################################################################################
## Main Portal Screen
################################################################################




################################################################################
## Student Portal Screen
## Replicates the BORRES, JOSAIAH LOBATON student dashboard UI
##CRS Screen
################################################################################
screen student_portal():

    ## Background
    add Solid(LIGHT_PINK_BG)

    ## Top Info Bar (student info area)
    frame:
        xalign 0.5
        ypos 190
        xsize 900
        ysize 600
        background Solid("#ffffff")
        padding (20, 20, 20, 20)

        hbox:
            spacing 30
            xalign 0.0
            yalign 0.5

            ## Student Photo Placeholder
            frame:
                xsize 120
                ysize 155
                background Solid("#8b1a1a")
                ## In a real project, replace with: add "images/student_photo.png"
                text "PHOTO" color "#ffffff" size 16 xalign 0.5 yalign 0.5

            ## Student Info Text
            vbox:
                spacing 4
                yalign 0.5

                hbox:
                    spacing 6
                    text "Student ID :" bold True color TEXT_DARK size 16
                    text "202150631" color TEXT_DARK size 16

                hbox:
                    spacing 6
                    text "Name :" bold True color TEXT_DARK size 16
                    text "BORRES, JOSAIAH LOBATON" color TEXT_DARK size 16

                hbox:
                    spacing 6
                    text "Degree Program :" bold True color TEXT_DARK size 16
                    text "B.S. in Computer Science" color TEXT_DARK size 16

                hbox:
                    spacing 6
                    text "Degree Level:" bold True color TEXT_DARK size 16
                    text "Undergraduate" color TEXT_DARK size 16

                hbox:
                    spacing 6
                    text "Year Level :" bold True color TEXT_DARK size 16
                    text "4" color TEXT_DARK size 16

                null height 10

                hbox:
                    spacing 6
                    text "Scholarship :" bold True color TEXT_DARK size 16
                    text "Free Tuition and Other Fees" color TEXT_DARK size 16

    ## Main Content Panel
    frame:
        xalign 0.5
        ypos 190
        xsize 900
        ysize 680
        background Solid(LIGHT_PINK_BG)
        padding (0, 0, 0, 0)

        vbox:
            spacing 0

            ## Header Banner
            frame:
                xsize 900
                ysize 48
                background Solid(DARK_MAROON)
                text "Second Semester ,  A.Y. 2025-2026" color "#ffffff" bold True size 18 xalign 0.5 yalign 0.5

            ## Content Area
            frame:
                xsize 900
                background Solid(LIGHT_PINK_BG)
                padding (60, 24, 60, 24)

                vbox:
                    spacing 24

                    ##──────────────────────────────────────
                    ## PERSONAL DATA Section
                    ##──────────────────────────────────────
                    vbox:
                        spacing 10

                        text "PERSONAL DATA" bold True color TEXT_DARK size 18

                        ## Buttons
                        use portal_button("My Login Account", "login_account")
                        use portal_button("My Personal Information", "personal_info")
                        use portal_button("My Existing Accountability", "accountability")
                        use portal_button("My Class Syllabus", "class_syllabus")
                        use portal_button("My Study Plan", "study_plan")
                        use portal_button("My Schedule, Grades & Checklist", "schedule_grades")

                    ##──────────────────────────────────────
                    ## APPS Section
                    ##──────────────────────────────────────
                    vbox:
                        spacing 10

                        text "APPS" bold True color TEXT_DARK size 18

                        ## Disabled label
                        hbox:
                            xalign 0.5
                            spacing 8
                            text "Evaluate Teacher" bold True color TEXT_DARK size 16 xalign 0.5
                            text "(Disabled)" color DISABLED_TEXT bold True size 16

                        use portal_button("Graduation Application", "graduation_app")
                        use portal_button("Remote Learning Survey", "remote_survey")

                    ##──────────────────────────────────────
                    ## REGISTRATION Section
                    ##──────────────────────────────────────
                    vbox:
                        spacing 10

                        text "REGISTRATION" bold True color TEXT_DARK size 18

                        use portal_button("View Subjects", "view_subjects")
                        use portal_button_badge("Enrollment", "enrollment_status", "1")

            ## Footer Banner
            frame:
                xsize 900
                ysize 28
                background Solid(DARK_MAROON)
                null


################################################################################
## Reusable Portal Button (plain)
################################################################################

screen portal_button(label, action_tag):
    button:
        xsize 780
        ysize 48
        background Frame(Solid(BUTTON_BG), 0, 0)
        hover_background Frame(Solid("#e8d4d4"), 0, 0)
        padding (16, 0, 16, 0)

        ## Border via solid frame trick
        frame:
            xsize 780
            ysize 48
            background Solid(BUTTON_BORDER)
            padding (1, 1, 1, 1)

            frame:
                xfill True
                yfill True
                background Solid(BUTTON_BG)
                hover_background Solid("#e8d4d4")
                padding (14, 0, 14, 0)

                text label color TEXT_DARK size 16 yalign 0.5

        action NullAction()


################################################################################
## Reusable Portal Button WITH red badge
################################################################################

screen portal_button_badge(label, action_tag, badge_count):
    hbox:
        spacing 8
        yalign 0.5

        button:
            xsize 740
            ysize 48
            padding (0, 0, 0, 0)

            frame:
                xsize 740
                ysize 48
                background Solid(BUTTON_BORDER)
                padding (1, 1, 1, 1)

                frame:
                    xfill True
                    yfill True
                    background Solid(BUTTON_BG)
                    hover_background Solid("#e8d4d4")
                    padding (14, 0, 14, 0)

                    text label color TEXT_DARK size 16 yalign 0.5

            action NullAction()

        ## Red circle badge
        frame:
            xsize 32
            ysize 32
            background Solid(RED_BADGE)
            xalign 0.5
            yalign 0.5

            text badge_count color "#ffffff" bold True size 16 xalign 0.5 yalign 0.5


################################################################################
## CRS Enrollment UI wrapper for Act 2 flow
################################################################################

screen crs_enrollment_ui():
    use student_portal

    frame:
        xalign 0.5
        yalign 0.97
        xsize 900
        ysize 70
        background Solid(DARK_MAROON)
        padding (20, 12, 20, 12)

        hbox:
            xfill True
            spacing 20

            text "CRS Simulation" color "#ffffff" bold True size 20 yalign 0.5

            null width 1

            textbutton "Done":
                action Return("completed")

            textbutton "Back":
                action Return("cancelled")


################################################################################
## Entry point label
################################################################################

label start_portal:
    call screen student_portal()
    return





screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')
            textbutton _("ENCYCLOPEDIA") action ShowMenu("encyclopedia") ## Encyclopedia Button



## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing 4

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Settings") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button:
    size_group "navigation"
    xsize 300
    ysize 50
    padding (20, 8, 20, 8)
    idle_background Frame(Solid("#00000000"), 4, 4, 4, 4)
    hover_background Frame(Solid("#00cc9922"), 4, 4, 4, 4)
    selected_idle_background Frame(Solid("#00cc9933"), 4, 4, 4, 4)
    selected_hover_background Frame(Solid("#00cc9944"), 4, 4, 4, 4)

style navigation_button_text:
    font "fonts/PressStart2P-Regular.ttf"
    size 15
    yalign 0.5
    idle_color "#ffffff88"
    hover_color "#00cc99"
    selected_idle_color "#00cc99"
    selected_hover_color "#ffffff"
    outlines [ (2, "#000000", 0, 0) ]


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu


# ── Transforms ──

transform parallax_loop(speed):
    subpixel True
    xpan 0
    linear speed xpan 360
    repeat

# Title gently breathes
transform title_breathe:
    yoffset 0
    ease 4.0 yoffset -6
    ease 4.0 yoffset 0
    repeat

# Title entrance — drops in and fades
transform title_enter:
    alpha 0.0 zoom 1.05 yoffset -40
    pause 0.2
    easein 1.2 alpha 1.0 zoom 1.0 yoffset 0

# Subtitle slides in after title
transform subtitle_enter:
    alpha 0.0 yoffset 10
    pause 1.0
    easein 0.6 alpha 1.0 yoffset 0

# Separator line grows from center
transform separator_enter:
    alpha 0.0 xzoom 0.0
    pause 0.8
    easein 0.5 alpha 1.0 xzoom 1.0

# Staggered button slide-up
transform btn_appear(delay):
    alpha 0.0 yoffset 30
    pause delay
    easein 0.35 alpha 1.0 yoffset 0

# Button hover — lift + glow
transform btn_hover_lift:
    on hover:
        easein 0.12 yoffset -4 zoom 1.02
    on idle:
        easeout 0.2 yoffset 0 zoom 1.0

# Bottom panel slides up from offscreen
transform bottom_panel_enter:
    alpha 0.0 yoffset 60
    pause 0.5
    easein 0.6 alpha 1.0 yoffset 0

# Overlay fades in
transform overlay_fadein:
    alpha 0.0
    linear 1.5 alpha 1.0

screen main_menu():
    tag menu

    # ── Parallax Background ──
    add "gui/main_menu/layer7.png" at parallax_loop(360.0)
    add "gui/main_menu/layer6.png" at parallax_loop(300.0)
    add "gui/main_menu/layer5.png" at parallax_loop(240.0)
    add "gui/main_menu/layer4.png" at parallax_loop(180.0)
    add "gui/main_menu/layer3.png" at parallax_loop(120.0)
    add "gui/main_menu/layer2.png" at parallax_loop(90.0)
    add "gui/main_menu/layer1.png" at parallax_loop(60.0)

    # ── Overlays for depth ──
    # Top vignette — darkens the sky slightly
    add Solid("#00000055") at overlay_fadein

    # ── Title Block ──
    if gui.show_name:
        vbox at title_enter:
            align (0.5, 0.35)
            spacing 0

            text "[config.name!t]" at title_breathe:
                style "mm_title"
                xalign 0.5

            # Decorative separator line
            frame at separator_enter:
                xalign 0.5
                xsize 360
                ysize 3
                background Solid("#00cc99")
                top_margin 12
                bottom_margin 12

            text "v. [config.version]" at subtitle_enter:
                style "mm_version"
                xalign 0.5

    # ── Bottom Navigation Panel ──
    # Frosted dark panel that anchors the buttons
    frame at bottom_panel_enter:
        align (0.5, 0.88)
        xsize 1400
        ysize 100
        background Frame(Solid("#0a0a1acc"), 6, 6, 6, 6)
        padding (40, 0, 40, 0)

        # Accent border line at the top of the panel
        add Solid("#00cc9966", xsize=1400, ysize=2):
            yalign 0.0

        hbox:
            align (0.5, 0.5)
            spacing 0

            textbutton _("NEW GAME") action Start() style "mm_btn" at btn_appear(0.7), btn_hover_lift
            textbutton _("CONTINUE") action ShowMenu("load") style "mm_btn" at btn_appear(0.85), btn_hover_lift
            textbutton _("SETTINGS") action ShowMenu("preferences") style "mm_btn" at btn_appear(1.0), btn_hover_lift
            textbutton _("ABOUT") action ShowMenu("about") style "mm_btn" at btn_appear(1.15), btn_hover_lift
            textbutton _("QUIT") action Quit(confirm=not main_menu) style "mm_btn_quit" at btn_appear(1.3), btn_hover_lift

# ── Main Menu Styles ──

style mm_btn is button:
    xsize 260
    ysize 80
    padding (0, 0, 0, 0)
    idle_background Solid("#00000000")
    hover_background Frame(Solid("#00cc9922"), 4, 4, 4, 4)

style mm_btn_text is text:
    font "fonts/PressStart2P-Regular.ttf"
    size 18
    xalign 0.5
    yalign 0.5
    text_align 0.5
    idle_color "#ffffffaa"
    hover_color "#00cc99"
    selected_color "#ffffff"
    insensitive_color "#ffffff22"
    outlines [ (2, "#000000", 0, 0) ]
    kerning 1

# Quit button — distinct red tint
style mm_btn_quit is mm_btn:
    hover_background Frame(Solid("#cc333322"), 4, 4, 4, 4)

style mm_btn_quit_text is mm_btn_text:
    hover_color "#ff6666"

style mm_title is default:
    font "fonts/PressStart2P-Regular.ttf"
    size 64
    color "#ffffff"
    outlines [ (8, "#000000cc", 0, 0), (4, "#00cc9955", 0, 0) ]

style mm_version is default:
    font "fonts/PressStart2P-Regular.ttf"
    size 12
    color "#00cc9988"
    outlines [ (1, "#000000aa", 0, 0) ]

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    font "fonts/PressStart2P-Regular.ttf"
    size 48
    color "#00cc99"
    yalign 0.5
    outlines [ (3, "#000000", 0, 0) ]

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Settings"), scroll="viewport"):

        style_prefix "pref"

        vbox:
            spacing 36

            # ═══════════════════════════════════════
            # DISPLAY SECTION
            # ═══════════════════════════════════════
            frame:
                xfill True
                background Frame(Solid("#0e1b2a99"), 6, 6, 6, 6)
                padding (30, 20, 30, 20)

                vbox:
                    spacing 14

                    hbox:
                        spacing 12
                        text ">" style "pref_icon_text"
                        label _("Display") style "pref_section_label"

                    if renpy.variant("pc") or renpy.variant("web"):
                        hbox:
                            spacing 16
                            xoffset 28
                            textbutton _("Window") action Preference("display", "window") style "pref_pill_btn"
                            textbutton _("Fullscreen") action Preference("display", "fullscreen") style "pref_pill_btn"

            # ═══════════════════════════════════════
            # SKIP SECTION
            # ═══════════════════════════════════════
            frame:
                xfill True
                background Frame(Solid("#0e1b2a99"), 6, 6, 6, 6)
                padding (30, 20, 30, 20)

                vbox:
                    spacing 14

                    hbox:
                        spacing 12
                        text ">>" style "pref_icon_text"
                        label _("Skip") style "pref_section_label"

                    hbox:
                        spacing 12
                        xoffset 28
                        textbutton _("Unseen Text") action Preference("skip", "toggle") style "pref_chip_btn"
                        textbutton _("After Choices") action Preference("after choices", "toggle") style "pref_chip_btn"
                        textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle")) style "pref_chip_btn"

            # ═══════════════════════════════════════
            # TEXT SECTION
            # ═══════════════════════════════════════
            frame:
                xfill True
                background Frame(Solid("#0e1b2a99"), 6, 6, 6, 6)
                padding (30, 20, 30, 20)

                vbox:
                    spacing 18

                    hbox:
                        spacing 12
                        text "Aa" style "pref_icon_text"
                        label _("Text") style "pref_section_label"

                    # Text Speed
                    vbox:
                        xoffset 28
                        spacing 8
                        text _("Text Speed") style "pref_slider_label_text"
                        hbox:
                            spacing 16
                            bar value Preference("text speed") style "pref_styled_bar"
                            text _("FAST") style "pref_bar_hint_text"

                    # Auto-Forward
                    vbox:
                        xoffset 28
                        spacing 8
                        text _("Auto-Forward Time") style "pref_slider_label_text"
                        hbox:
                            spacing 16
                            bar value Preference("auto-forward time") style "pref_styled_bar"
                            text _("SLOW") style "pref_bar_hint_text"

            # ═══════════════════════════════════════
            # AUDIO SECTION
            # ═══════════════════════════════════════
            frame:
                xfill True
                background Frame(Solid("#0e1b2a99"), 6, 6, 6, 6)
                padding (30, 20, 30, 20)

                vbox:
                    spacing 18

                    hbox:
                        spacing 12
                        text "♪" style "pref_icon_text"
                        label _("Audio") style "pref_section_label"

                    if config.has_music:
                        vbox:
                            xoffset 28
                            spacing 8
                            text _("Music") style "pref_slider_label_text"
                            bar value Preference("music volume") style "pref_styled_bar_music"

                    if config.has_sound:
                        vbox:
                            xoffset 28
                            spacing 8
                            hbox:
                                spacing 16
                                text _("Sound") style "pref_slider_label_text"
                                if config.sample_sound:
                                    textbutton _("[ Test ]") action Play("sound", config.sample_sound) style "pref_test_btn"
                            bar value Preference("sound volume") style "pref_styled_bar_sfx"

                    if config.has_voice:
                        vbox:
                            xoffset 28
                            spacing 8
                            hbox:
                                spacing 16
                                text _("Voice") style "pref_slider_label_text"
                                if config.sample_voice:
                                    textbutton _("[ Test ]") action Play("voice", config.sample_voice) style "pref_test_btn"
                            bar value Preference("voice volume") style "pref_styled_bar_voice"

                    if config.has_music or config.has_sound or config.has_voice:
                        null height 6
                        hbox:
                            xoffset 28
                            textbutton _("Mute All") action Preference("all mute", "toggle") style "pref_mute_btn"

# ═══════════════════════════════════════════════════
# SETTINGS STYLES
# ═══════════════════════════════════════════════════

# Section header icon (>, >>, Aa, ♪)
style pref_icon_text:
    font "fonts/PressStart2P-Regular.ttf"
    size 18
    color "#00cc99"
    yalign 0.5
    outlines [ (2, "#000000", 0, 0) ]

# Section label
style pref_section_label:
    bottom_margin 0

style pref_section_label_text:
    font "fonts/PressStart2P-Regular.ttf"
    size 20
    color "#ffffff"
    yalign 0.5
    outlines [ (2, "#00000088", 0, 0) ]

# Slider labels
style pref_slider_label_text:
    font "fonts/PressStart2P-Regular.ttf"
    size 13
    color "#ffffffbb"
    outlines [ (1, "#000000", 0, 0) ]

# Bar end-hint (FAST, SLOW)
style pref_bar_hint_text:
    font "fonts/PressStart2P-Regular.ttf"
    size 10
    color "#ffffff44"
    yalign 0.5
    outlines [ (1, "#000000", 0, 0) ]

# ── Pill Button (Display: Window/Fullscreen) ──
style pref_pill_btn is gui_button:
    xsize 200
    ysize 44
    idle_background Frame(Solid("#ffffff0e"), 6, 6, 6, 6)
    hover_background Frame(Solid("#00cc9933"), 6, 6, 6, 6)
    selected_idle_background Frame(Solid("#00cc9955"), 6, 6, 6, 6)
    selected_hover_background Frame(Solid("#00cc9977"), 6, 6, 6, 6)

style pref_pill_btn_text:
    font "fonts/PressStart2P-Regular.ttf"
    size 14
    xalign 0.5
    yalign 0.5
    text_align 0.5
    idle_color "#ffffff77"
    hover_color "#00cc99"
    selected_idle_color "#00cc99"
    selected_hover_color "#ffffff"
    outlines [ (1, "#000000", 0, 0) ]

# ── Chip Button (Skip toggles) ──
style pref_chip_btn is gui_button:
    padding (18, 10, 18, 10)
    idle_background Frame(Solid("#ffffff0e"), 6, 6, 6, 6)
    hover_background Frame(Solid("#3399ff33"), 6, 6, 6, 6)
    selected_idle_background Frame(Solid("#3399ff55"), 6, 6, 6, 6)
    selected_hover_background Frame(Solid("#3399ff77"), 6, 6, 6, 6)

style pref_chip_btn_text:
    font "fonts/PressStart2P-Regular.ttf"
    size 12
    idle_color "#ffffff77"
    hover_color "#66bbff"
    selected_idle_color "#66bbff"
    selected_hover_color "#ffffff"
    outlines [ (1, "#000000", 0, 0) ]

# ── Slider Bars ──
# Text Speed / Auto-Forward (teal)
style pref_styled_bar is gui_slider:
    xsize 600
    ysize 24
    base_bar Frame(Solid("#ffffff14"), 6, 6, 6, 6)
    hover_base_bar Frame(Solid("#ffffff22"), 6, 6, 6, 6)
    thumb Frame(Solid("#00cc99"), 6, 6, 6, 6)
    hover_thumb Frame(Solid("#66e0c1"), 6, 6, 6, 6)
    thumb_offset 12

# Music (warm amber)
style pref_styled_bar_music is pref_styled_bar:
    thumb Frame(Solid("#ffaa33"), 6, 6, 6, 6)
    hover_thumb Frame(Solid("#ffcc66"), 6, 6, 6, 6)

# Sound FX (blue)
style pref_styled_bar_sfx is pref_styled_bar:
    thumb Frame(Solid("#3399ff"), 6, 6, 6, 6)
    hover_thumb Frame(Solid("#66bbff"), 6, 6, 6, 6)

# Voice (pink)
style pref_styled_bar_voice is pref_styled_bar:
    thumb Frame(Solid("#ff6699"), 6, 6, 6, 6)
    hover_thumb Frame(Solid("#ff99bb"), 6, 6, 6, 6)

# ── Test Button ──
style pref_test_btn is gui_button:
    padding (8, 4, 8, 4)
    idle_background Solid("#00000000")
    hover_background Solid("#00000000")
    yalign 0.5

style pref_test_btn_text:
    font "fonts/PressStart2P-Regular.ttf"
    size 10
    idle_color "#ffffff44"
    hover_color "#ffcc00"
    outlines [ (1, "#000000", 0, 0) ]

# ── Mute All Button ──
style pref_mute_btn is gui_button:
    padding (22, 10, 22, 10)
    idle_background Frame(Solid("#ff334422"), 6, 6, 6, 6)
    hover_background Frame(Solid("#ff334444"), 6, 6, 6, 6)
    selected_idle_background Frame(Solid("#ff334466"), 6, 6, 6, 6)
    selected_hover_background Frame(Solid("#ff334488"), 6, 6, 6, 6)

style pref_mute_btn_text:
    font "fonts/PressStart2P-Regular.ttf"
    size 13
    idle_color "#ff666688"
    hover_color "#ff6666"
    selected_idle_color "#ff6666"
    selected_hover_color "#ffffff"
    outlines [ (1, "#000000", 0, 0) ]


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100

    frame at notify_appear:
        xalign 0.5
        ypos 80
        xminimum 320
        padding (3, 3, 3, 3)
        background Frame(Solid("#f6d79d44"), 0, 0)

        frame:
            xfill True
            padding (28, 16, 28, 16)
            background Frame(Solid("#1e0c12ee"), 0, 0)

            hbox:
                xalign 0.5
                spacing 10

                text "★":
                    size 20
                    color "#ffd700"
                    outlines [(2, "#1e0c12", 0, 0)]
                    yalign 0.5

                text "[message!tq]":
                    size 20
                    color "#b8e6b0"
                    outlines [(2, "#1e0c12", 0, 0)]
                    yalign 0.5

                text "★":
                    size 20
                    color "#ffd700"
                    outlines [(2, "#1e0c12", 0, 0)]
                    yalign 0.5

    timer 3.0 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0 yoffset -20
        easein 0.35 alpha 1.0 yoffset 0
    on hide:
        easeout 0.4 alpha 0.0 yoffset -20


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}

screen debug_overlay():
    zorder 999
    frame:
        xalign 1.0
        yalign 0.0
        xsize 400
        background Solid("#000000cc")
        padding (10, 10, 10, 10)
        vbox:
            spacing 4
            text "=== DEBUG ===" color "#ffff00" size 14
            text "act: [current_act]" color "#ffffff" size 12
            text "tasks: [tasks_completed]" color "#aaffaa" size 11

################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    background Solid("#00000000")

style game_menu_navigation_frame:
    background Solid("#00000000")

style game_menu_content_frame:
    background Solid("#00000000")

# Styling the sliders to be thin and elegant instead of blocky

style slider:   
    ysize 12
    base_bar Solid("#ffffff44")
    thumb Solid("#ffcc00") 
    hover_base_bar Solid("#ffffff88")

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)


# style vslider:
#     variant "small"
#     xsize gui.slider_size
#     base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
#     thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900


## ============================================================================
## GAME SCREENS — Notebook, Items, Quiz, Phone (moved from dialogue_act1.rpy)
## These are universal screens available across all acts.
## ============================================================================

## ----------------------------------------------------------------------------
## SCREEN: NOTEBOOK INTRO ANIMATION
## Shows the notebook with blank questions before Act 1 starts
## ----------------------------------------------------------------------------

screen notebook_intro_screen():
    modal True
    zorder 200

    add "#1a1a2e" alpha 0.97

    window:
        id "window"

        ## Outer glow border
        frame:
            xfill True
            yfill True
            padding (3, 3, 3, 3)
            background Frame(Solid("#f6d79d33"), 0, 0)

            ## Inner border accent
            frame:
                xfill True
                yfill True
                padding (2, 2, 2, 2)
                background Frame(Solid("#f6d79d11"), 0, 0)

                ## Main dark panel
                frame:
                    xfill True
                    yfill True
                    padding (0, 0, 0, 0)
                    background Frame(Solid("#1a0a10f0"), 0, 0)

                    fixed:
                        ## Centered notebook card
                        frame:
                            xalign 0.5
                            yalign 0.5
                            xsize 680
                            ysize 560
                            padding (0, 0, 0, 0)
                            background Frame(Solid("#1a0a10f0"), 0, 0)

                            vbox:
                                spacing 0

                                ## Header (uses same visual language as dialogue namebox)
                                frame:
                                    background Frame(Solid("#f6d79d11"), 0, 0)
                                    xfill True
                                    padding (28, 20, 28, 20)
                                    hbox:
                                        spacing 12
                                        text "🔍" size 28
                                        vbox:
                                            spacing 2
                                            text "DETECTIVE NOTEBOOK" size 13 color gui.accent_color bold True
                                            text "Freshie Field Notes — Day 1" size 11 color "#6b7280"

                                ## Content area (scrollable)
                                frame:
                                    xfill True
                                    ysize 420
                                    padding (20, 16, 20, 16)

                                    viewport:
                                        xfill True
                                        ysize 420
                                        scrollbars "vertical"
                                        mousewheel True

                                        vbox:
                                            spacing 10
                                            xfill True

                                            text "Find answers to these questions by talking to the locals." size 12 color "#9ca3af" italic True
                                            null height 8

                                            for q in notebook_questions:
                                                frame:
                                                    xfill True
                                                    padding (12, 10, 12, 10)
                                                    background Frame(Solid("#111128"), 0, 0)

                                                    hbox:
                                                        spacing 12
                                                        xfill True
                                                        text "?" size 18 color "#a78bfa" yalign 0.5
                                                        vbox:
                                                            spacing 2
                                                            xfill True
                                                            text q.text size 13 color "#e2e8f0"
                                                            text "[ not yet discovered ]" substitute False size 11 color "#4b5563" italic True

                                ## Button
                                frame:
                                    background Frame(Solid("#1e1e3a"), 0, 0)
                                    xfill True
                                    padding (24, 12, 24, 12)
                                    hbox:
                                        xfill True
                                        spacing 0
                                        textbutton "Start Exploring →" style "notebook_btn" xalign 0.5 action Return()

style notebook_btn:
    background gui.accent_color
    hover_background gui.hover_color
    padding (24, 10, 24, 10)

style notebook_btn_text:
    color "#ffffff"
    hover_color "#ffffff"
    size 13
    bold True

## ----------------------------------------------------------------------------
## SCREEN: ITEM PICKUP NOTIFICATION
## Brief flash when player receives an info item
## ----------------------------------------------------------------------------

screen item_pickup_screen(item):
    zorder 300
    modal False

    frame:
        xalign 0.5
        yalign 0.0
        yoffset 80
        background "#1e1e3a"
        padding (20, 14, 24, 14)
        at item_pickup_anim

        hbox:
            spacing 12
            yalign 0.5
            text item.icon size 22 yalign 0.5
            vbox:
                spacing 2
                text "INFO ITEM COLLECTED" size 10 color "#a78bfa" bold True
                text item.label size 13 color "#f1f5f9" bold True
                text item.short size 11 color "#94a3b8"

transform item_pickup_anim:
    alpha 0.0 yoffset -20
    ease 0.3 alpha 1.0 yoffset 0
    pause 2.0
    ease 0.4 alpha 0.0 yoffset -10

## ----------------------------------------------------------------------------
## SCREEN: INVENTORY (can be toggled, I key)
## ----------------------------------------------------------------------------

screen inventory_screen():
    modal True
    zorder 150

    key "K_p" action Hide("phone_screen")
    key "K_i" action Hide("inventory_screen")
    key "K_ESCAPE" action Hide("inventory_screen")
    key "K_e" action [Hide("inventory_screen"), Show("encyclopedia_screen")]

    add "#000000" alpha 0.6

    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 540
        background "#F9F6F0" # Book paper color
        padding (0, 0, 0, 0)

        # Spine shadow in the middle
        add Solid("#E8E0D5"):
            xalign 0.5
            xsize 2
            ysize 540

        vbox:
            spacing 0

            # Header
            frame:
                background "#2C3E50"
                xfill True
                padding (30, 20, 30, 20)
                hbox:
                    xfill True
                    text "FRESHMAN DICTIONARY" size 16 color "#F9F6F0" bold True xalign 0.0 yalign 0.5
                    text "Entries: [len(collected_items)]/14" size 14 color "#BDC3C7" xalign 1.0 yalign 0.5

            # Content
            frame:
                background Solid("#00000000")
                xfill True
                ysize 420
                padding (40, 30, 40, 30)

                vpgrid:
                    cols 2
                    spacing 40
                    xfill True
                    yinitial 0.0

                    if len(collected_items) == 0:
                        text "No entries yet.\nTalk to locals to gather information." size 14 color "#7F8C8D" italic True xalign 0.5

                    for item in collected_items:
                        vbox:
                            xfill True
                            spacing 6

                            # Term and Source
                            hbox:
                                spacing 8
                                text item.icon size 18 yalign 0.5
                                text item.label size 16 color "#2C3E50" bold True yalign 0.5
                                text "— " + item.source size 11 color "#95A5A6" italic True yalign 0.7
                            
                            # Definition
                            text item.short size 13 color "#34495E"
                            
                            # Separator
                            null height 8
                            # ✅ FIX
                            frame:
                                background Solid("#E0DCD3")
                                xfill True
                                ysize 1
                                padding (0, 0, 0, 0)

            # Footer
            frame:
                background Solid("#00000000")
                xfill True
                padding (20, 10, 20, 10)
                hbox:
                    xalign 0.5
                    spacing 24
                    text "[[I]] / [[ESC]] — Close" substitute False size 11 color "#95A5A6" italic True yalign 0.5
                    textbutton "📖 Encyclopedia [[E]]" substitute False action [Hide("inventory_screen"), Show("encyclopedia_screen")] style "inv_enc_btn"

style inv_enc_btn:
    background "#2C3E50"
    hover_background "#1e2d3d"
    padding (10, 5, 10, 5)
    color "#BDC3C7"
    hover_color "#ffffff"
    size 11

## ----------------------------------------------------------------------------
## SCREEN: ENCYCLOPEDIA — Detailed knowledge book, organised by NPC source
## Key: E (on map or from inventory)
## ----------------------------------------------------------------------------

screen encyclopedia_screen():
    modal True
    zorder 155

    key "K_e" action Hide("encyclopedia_screen")
    key "K_i" action [Hide("encyclopedia_screen"), Show("inventory_screen")]
    key "K_ESCAPE" action Hide("encyclopedia_screen")

    default enc_selected = ""

    add "#000000" alpha 0.78

    python:
        _enc_order = ["Jaden", "Manong Josh", "Aleng Maria", "Manong Chris", "Tol Joseph"]
        _enc_has   = [s for s in _enc_order if any(i.source == s for i in collected_items)]
        _enc_extra = [s for s in dict.fromkeys(i.source for i in collected_items) if s not in _enc_order]
        _enc_srcs  = _enc_has + _enc_extra

        _enc_meta = {
            "Jaden":        ("🎒", "Fellow freshie from Iloilo City with UPV tips."),
            "Manong Josh":  ("🏘️", "Long-time Miagao local who knows every corner."),
            "Aleng Maria":  ("🍚", "Carinderia owner near the UPV gate — feeds half the campus."),
            "Manong Chris": ("🙏", "Born-and-raised Miagaoanon fluent in Kinaray-a."),
            "Tol Joseph":   ("🛺", "The tricycle driver who knows every route and fare."),
        }

    frame:
        xalign 0.5
        yalign 0.5
        xsize 880
        ysize 560
        background "#F5EFE0"
        padding (0, 0, 0, 0)

        vbox:
            spacing 0

            ## Header
            frame:
                background "#1e130a"
                xfill True
                padding (28, 14, 28, 14)
                hbox:
                    xfill True
                    yalign 0.5
                    vbox:
                        spacing 2
                        text "📖  MIAGAO FRESHMAN ENCYCLOPEDIA" size 15 color "#d4a843" bold True
                        text "Complete knowledge gathered from locals" size 10 color "#8b7355" italic True
                    text "[len(collected_items)] entries" size 12 color "#8b6914" xalign 1.0 yalign 0.5

            ## Body
            hbox:
                spacing 0

                ## TOC panel
                frame:
                    xsize 210
                    ysize 492
                    background "#E8DFC8"
                    padding (0, 0, 0, 0)

                    vbox:
                        spacing 0
                        frame:
                            background "#2c1810"
                            xfill True
                            padding (14, 10, 14, 10)
                            text "CHAPTERS" size 10 color "#d4a843" bold True

                        if len(_enc_srcs) == 0:
                            frame:
                                background Solid("#00000000")
                                xfill True
                                padding (14, 20, 14, 20)
                                text "Talk to locals to\nunlock chapters." size 11 color "#8b7355" italic True

                        for _esrc in _enc_srcs:
                            python:
                                _emeta  = _enc_meta.get(_esrc, ("📄", "A local source."))
                                _ecount = len([i for i in collected_items if i.source == _esrc])
                                _eword  = "entry" if _ecount == 1 else "entries"
                                _eact   = (enc_selected == _esrc)

                            button:
                                xfill True
                                background ("#3d2214" if _eact else None)
                                hover_background "#2c1810"
                                padding (14, 12, 14, 12)
                                action SetScreenVariable("enc_selected", _esrc)
                                hbox:
                                    spacing 8
                                    text _emeta[0] size 14 yalign 0.5
                                    vbox:
                                        spacing 1
                                        text _esrc size 12 color ("#d4a843" if _eact else "#4a3020") bold True
                                        text "[_ecount] [_eword]" size 9 color "#8b7355"

                            frame:
                                background Solid("#D4C4A066")
                                xfill True
                                ysize 1
                                padding (0, 0, 0, 0)

                ## Spine
                frame:
                    xsize 3
                    ysize 492
                    background "#d4a843"
                    padding (0, 0, 0, 0)

                ## Content panel
                frame:
                    xsize 667
                    ysize 492
                    background "#FDFAF4"
                    padding (0, 0, 0, 0)

                    if enc_selected == "":
                        frame:
                            xfill True
                            ysize 492
                            background Solid("#00000000")
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 14
                                text "📖" size 52 xalign 0.5
                                text "Select a Chapter" size 18 color "#4a3020" bold True xalign 0.5
                                text "Choose a source from the left\nto read the knowledge you collected." size 12 color "#8b7355" italic True xalign 0.5 text_align 0.5

                    else:
                        python:
                            _eitems  = [i for i in collected_items if i.source == enc_selected]
                            _echmeta = _enc_meta.get(enc_selected, ("📄", "Information gathered from a local."))

                        vbox:
                            spacing 0

                            ## Chapter header
                            frame:
                                background "#E8DFC8"
                                xfill True
                                padding (20, 12, 20, 12)
                                hbox:
                                    spacing 12
                                    text _echmeta[0] size 26 yalign 0.5
                                    vbox:
                                        spacing 2
                                        text enc_selected size 17 color "#1e130a" bold True
                                        text _echmeta[1] size 11 color "#6b5a3a" italic True

                            ## Scrollable entries
                            viewport:
                                xfill True
                                ysize 398
                                scrollbars "vertical"
                                mousewheel True
                                yinitial 0.0

                                frame:
                                    xfill True
                                    background Solid("#00000000")
                                    padding (20, 12, 20, 12)

                                    vbox:
                                        xfill True
                                        spacing 0

                                        for _eitem in _eitems:
                                            frame:
                                                xfill True
                                                background Solid("#00000000")
                                                padding (0, 10, 0, 10)
                                                vbox:
                                                    xfill True
                                                    spacing 5

                                                    hbox:
                                                        spacing 10
                                                        text _eitem.icon size 20 yalign 0.5
                                                        text _eitem.label size 14 color "#1e130a" bold True yalign 0.5

                                                    text _eitem.short size 12 color "#3a2a1a"

                                                    if _eitem.full and _eitem.full != _eitem.short:
                                                        null height 4
                                                        frame:
                                                            background "#EDE4CC"
                                                            xfill True
                                                            padding (12, 8, 12, 8)
                                                            text _eitem.full size 11 color "#4a3a1a"

                                                    null height 6
                                                    frame:
                                                        background Solid("#D8CCAA")
                                                        xfill True
                                                        ysize 1
                                                        padding (0, 0, 0, 0)

            ## Footer
            frame:
                background "#E8DFC8"
                xfill True
                padding (20, 8, 20, 8)
                hbox:
                    xalign 0.5
                    spacing 24
                    text "[[E]] / [[ESC]] — Close" substitute False size 10 color "#8b7355" italic True yalign 0.5
                    text "[[I]] — Dictionary" substitute False size 10 color "#8b7355" italic True yalign 0.5
                    text "Scroll with mouse wheel" size 10 color "#8b7355" italic True yalign 0.5

## ----------------------------------------------------------------------------
## SCREEN: QUIZ MINIGAME
## Player drags/selects items to answer notebook questions
## ----------------------------------------------------------------------------

screen quiz_screen():
    modal True
    zorder 200

    add "#0a0a1a" alpha 0.98

    default quiz_state = {
        "current_q": 0,
        "score": 0,
        "done": False,
        "feedback": None,
        "chosen": None,
    }

    use quiz_inner(quiz_state)

screen quiz_inner(state):

    python:
        q       = notebook_questions[state["current_q"]]
        total_q = len(notebook_questions)
        items   = collected_items[:]

    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        background "#0f0f1a"
        padding (0, 0, 0, 0)

        vbox:
            spacing 0

            ## Top bar
            frame:
                background "#1e1e3a"
                xfill True
                padding (24, 16, 24, 16)
                hbox:
                    xfill True
                    vbox:
                        text "🔍  NOTEBOOK QUIZ" size 13 color "#a78bfa" bold True
                        text "Question [state['current_q']+1] of [total_q]" size 11 color "#6b7280"
                    text "Score: [state['score']]/[total_q]" size 13 color "#10b981" bold True xalign 1.0 yalign 0.5

            ## Progress bar
            frame:
                background "#111128"
                xfill True
                ysize 6
                padding (0, 0, 0, 0)
                frame:
                    background "#7C3AED"
                    xsize int(700 * (state["current_q"] / total_q))
                    ysize 6

            ## Question
            frame:
                background "#111128"
                xfill True
                padding (32, 24, 32, 16)
                vbox:
                    spacing 8
                    text "QUESTION" size 10 color "#a78bfa" bold True
                    text q.text size 16 color "#f1f5f9" bold True
                    text "Select the info item that answers this question:" size 12 color "#9ca3af" italic True

                    if state["feedback"] == "correct":
                        frame:
                            background "#064e3b"
                            xfill True
                            padding (12, 8, 12, 8)
                            text "✓  Correct! That information answers this question." size 12 color "#10b981"

                    elif state["feedback"] == "wrong":
                        frame:
                            background "#450a0a"
                            xfill True
                            padding (12, 8, 12, 8)
                            text "✗  Not quite. Hint: [q.hint]" size 12 color "#f87171"

            ## Items grid
            frame:
                background "#0d0d20"
                xfill True
                padding (16, 12, 16, 12)

                vpgrid:
                    cols 2
                    xfill True
                    spacing 8

                    for item in items:
                        python:
                            is_chosen  = (state["chosen"] == item.item_id)
                            bg_color   = "#2e1065" if is_chosen else "#1a1a2e"
                            border_col = "#7C3AED" if is_chosen else "#1e1e3a"

                        button:
                            background bg_color
                            xfill True
                            padding (12, 10, 12, 10)
                            if state["feedback"] is None:
                                action [
                                    SetDict(state, "chosen", item.item_id),
                                ]
                            else:
                                action NullAction()
                            hbox:
                                spacing 10
                                yalign 0.5
                                text item.icon size 18 yalign 0.5
                                vbox:
                                    spacing 2
                                    text item.label size 12 color "#e2e8f0" bold True
                                    text item.short size 10 color "#94a3b8"

            ## Confirm button
            frame:
                background "#1e1e3a"
                xfill True
                padding (24, 14, 24, 14)

                if state["feedback"] is None:
                    textbutton "Confirm Answer →":
                        xalign 0.5
                        style "quiz_btn"
                        sensitive (state["chosen"] is not None)
                        action [
                            Function(save_quiz_answer, state["current_q"], state["chosen"]),
                            If(
                                state["chosen"] == q.correct_item_id,
                                [
                                    SetDict(state, "feedback", "correct"),
                                    SetDict(state, "score", state["score"] + 1),
                                ],
                                SetDict(state, "feedback", "wrong")
                            )
                        ]

                else:
                    python:
                        next_label = "Next Question →" if state["current_q"] < total_q - 1 else "Finish Quiz ✓"

                    textbutton next_label:
                        xalign 0.5
                        style "quiz_btn"
                        action [
                            If(
                                state["current_q"] < total_q - 1,
                                [
                                    SetDict(state, "current_q", state["current_q"] + 1),
                                    SetDict(state, "feedback",  None),
                                    SetDict(state, "chosen",    None),
                                ],
                                [
                                    SetVariable("quiz_score", state["score"]),
                                    Return(state["score"])
                                ]
                            )
                        ]

style quiz_btn:
    background "#7C3AED"
    hover_background "#6d28d9"
    insensitive_background "#2d2d4a"
    padding (28, 10, 28, 10)
    color "#ffffff"
    insensitive_color "#4b5563"
    hover_color "#ffffff"
    size 13
    bold True

## ----------------------------------------------------------------------------
## SCREEN: QUIZ RESULTS
## ----------------------------------------------------------------------------

screen quiz_results_screen(score):
    modal True
    zorder 200

    add "#000000" alpha 0.95

    frame:
        xalign 0.5
        yalign 0.5
        xsize 520
        background "#0f0f1a"
        padding (0, 0, 0, 0)

        vbox:
            spacing 0

            frame:
                background "#1e1e3a"
                xfill True
                padding (32, 24, 32, 20)
                vbox:
                    spacing 8
                    xalign 0.5
                    text "🔍  CASE CLOSED" size 22 color "#a78bfa" bold True xalign 0.5

                    python:
                        total = len(notebook_questions)
                        total_q = len(notebook_questions)
                        pct   = int((score / total) * 100)
                        if pct == 100:
                            grade   = "PERFECT DETECTIVE"
                            g_color = "#10b981"
                            g_msg   = "You absorbed everything. Miagao has no secrets from you."
                        elif pct >= 66:
                            grade   = "GOOD INSTINCTS"
                            g_color = "#f59e0b"
                            g_msg   = "Solid work. A few gaps — but you'll fill them in time."
                        else:
                            grade   = "STILL LEARNING"
                            g_color = "#f87171"
                            g_msg   = "You missed some locals. Their knowledge would have helped."

                    text "[score]/[total_q]  ([pct]%%)" size 36 color g_color bold True xalign 0.5
                    text grade size 13 color g_color bold True xalign 0.5
                    null height 4
                    text g_msg size 12 color "#9ca3af" italic True xalign 0.5

            frame:
                background "#111128"
                xfill True
                padding (24, 16, 24, 16)
                vbox:
                    spacing 6
                    for i in range(len(notebook_questions)):
                        python:
                            q2   = notebook_questions[i]
                            ok   = q2.answered and (q2.chosen_item_id == q2.correct_item_id)
                            ic   = "✓" if ok else "✗"
                            tcol = "#10b981" if ok else "#f87171"
                        hbox:
                            spacing 10
                            text ic size 13 color tcol yalign 0.5
                            text q2.text size 12 color "#cbd5e1" yalign 0.5

            frame:
                background "#1e1e3a"
                xfill True
                padding (24, 14, 24, 14)

                if score >= 4:
                    textbutton "Continue to BOX 1 →":
                        xalign 0.5
                        style "notebook_btn"
                        action Return()
                else:
                    vbox:
                        spacing 8
                        text "You need at least 4/6 correct to enter BOX 1." size 12 color "#f87171" italic True xalign 0.5
                        textbutton "Try Again":
                            xalign 0.5
                            style "quiz_btn"
                            action Return(-1)

## ----------------------------------------------------------------------------
## SCREEN: PHONE / GROUP CHAT UI
## Toggle with [P] key — available universally after GC unlock in Act 1
## ----------------------------------------------------------------------------

screen phone_screen():
    modal True
    zorder 250

    key "p" action Hide("phone_screen")
    key "K_ESCAPE" action Hide("phone_screen")

    add "#000000" alpha 0.6

    ## Phone frame
    frame:
        xalign 0.98
        yalign 0.5
        xsize 320
        ysize 580
        background "#111111"
        padding (0, 0, 0, 0)

        vbox:
            spacing 0

            ## Status bar
            frame:
                background "#1a1a1a"
                xfill True
                ysize 28
                padding (12, 0, 12, 0)
                hbox:
                    xfill True
                    yalign 0.5
                    text "9:41 AM" size 10 color "#ffffff" bold True yalign 0.5
                    text "●●●  WiFi  🔋" size 9 color "#9ca3af" xalign 1.0 yalign 0.5

            ## App bar
            frame:
                background "#1e1e1e"
                xfill True
                padding (12, 10, 12, 10)
                hbox:
                    spacing 10
                    xfill True
                    yalign 0.5
                    text "←" size 14 color "#7C3AED" yalign 0.5
                    vbox:
                        spacing 1
                        text "UPV Freshies 2024 🌊" size 12 color "#f1f5f9" bold True
                        text "Batch [gc_open_count]/[len(gc_all_messages)]  •  4 members" size 10 color "#6b7280"
                    text "⋮" size 16 color "#6b7280" xalign 1.0 yalign 0.5

            ## Messages area
            frame:
                background "#0d0d0d"
                xfill True
                ysize 430
                padding (8, 8, 8, 8)

                vpgrid:
                    cols 1
                    xfill True
                    yinitial 1.0
                    spacing 10

                    if len(gc_revealed) == 0:
                        frame:
                            background "#1a1a1a"
                            xfill True
                            padding (12, 16, 12, 16)
                            text "Talk to Jaden again to unlock the group chat..." size 11 color "#4b5563" italic True xalign 0.5

                    for idx in gc_revealed:
                        python:
                            msg   = gc_all_messages[idx // 3][idx % 3]
                            align = 1.0 if msg.is_player else 0.0

                        if msg.is_player:
                            hbox:
                                xfill True
                                xalign 1.0
                                null width 40
                                frame:
                                    background "#7C3AED"
                                    padding (10, 7, 10, 7)
                                    text msg.text size 11 color "#ffffff"

                        else:
                            hbox:
                                spacing 6
                                xfill True

                                ## Avatar circle (simulated)
                                frame:
                                    background msg.avatar_color
                                    xsize 28
                                    ysize 28
                                    padding (0, 0, 0, 0)
                                    text msg.sender[0] size 12 color "#ffffff" bold True xalign 0.5 yalign 0.5

                                vbox:
                                    spacing 2
                                    text msg.sender size 10 color "#9ca3af" bold True
                                    frame:
                                        background "#1e1e1e"
                                        padding (10, 7, 10, 7)
                                        text msg.text size 11 color "#e2e8f0"

                                null width 40

            ## Input bar + load more
            frame:
                background "#1a1a1a"
                xfill True
                padding (8, 8, 8, 8)
                vbox:
                    spacing 6

                    if gc_open_count < len(gc_all_messages):
                        textbutton "Next Batch →  ([gc_open_count + 1]/[len(gc_all_messages)])":
                            xalign 0.5
                            style "gc_load_btn"
                            action [
                                Function(reveal_gc_batch),
                                Function(renpy.restart_interaction),
                            ]

                    hbox:
                        spacing 6
                        xfill True
                        frame:
                            background "#2a2a2a"
                            xfill True
                            padding (10, 8, 10, 8)
                            text "Type a message..." size 11 color "#4b5563" italic True
                        frame:
                            background "#7C3AED"
                            padding (10, 8, 10, 8)
                            text "➤" size 12 color "#ffffff"

            ## Close hint
            frame:
                background "#111111"
                xfill True
                padding (8, 6, 8, 6)
                text "Press [[P]] to put phone away" substitute False size 9 color "#374151" italic True xalign 0.5

style gc_load_btn:
    background "#1e1e2e"
    hover_background "#2d2d4a"
    padding (16, 6, 16, 6)
    color "#a78bfa"
    hover_color "#c4b5fd"
    size 11
