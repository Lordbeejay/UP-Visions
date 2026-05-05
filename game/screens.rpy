################################################################################
# Top Navigation Bar: Encyclopedia, Dictionary, Phone
################################################################################
screen top_navbar(selected=None):
    frame:
        xalign 0.5
        yalign 0.0
        xsize 420
        ysize 56
        background Solid(DARK_MAROON)
        padding (8, 8, 8, 8)
        frame:
            xfill True
            yfill True
            background Solid("#fff4")
            hbox:
                xalign 0.5
                spacing 24
                
                textbutton "Encyclopedia" action ToggleScreen("encyclopedia_screen") style "nav_btn"
                textbutton "Dictionary [D]" action ToggleScreen("dictionary_screen") style "nav_btn"
                textbutton "Phone" action ToggleScreen("phone_screen") style "nav_btn"

    ## Keyboard shortcut
    key "d" action ToggleScreen("dictionary_screen")
################################################################################
init offset = -1

## Student Portal Colors
define DARK_MAROON = "#5c1a1a"
define LIGHT_PINK_BG = "#f0e6e6"
define WHITE = "#ffffff"
define TEXT_DARK = "#3a1a1a"
define RED_BADGE = "#cc0000"
define BUTTON_BG = "#f5eded"
define BUTTON_BORDER = "#c8b0b0"
define DISABLED_TEXT = "#cc4444"


style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    $ _who_text = renpy.filter_text_tags(who, deny=["color"]) if who is not None else None
    $ _speaker_portrait = get_speaker_portrait(_who_text)

    ## Narration/act transition lines render as clean center text (no large box overlay).
    if who is None:
        text what id "what":
            style "say_dialogue_center"
            xalign 0.5
            yalign 0.5

    else:
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

                            ## Corner accents (top-left)
                            frame:
                                xpos 8
                                ypos 8
                                xsize 20
                                ysize 2
                                background Solid("#f6d79d66")
                                padding (0, 0, 0, 0)
                            frame:
                                xpos 8
                                ypos 8
                                xsize 2
                                ysize 20
                                background Solid("#f6d79d66")
                                padding (0, 0, 0, 0)

                            ## Corner accents (top-right)
                            frame:
                                xalign 1.0
                                xoffset -8
                                ypos 8
                                xsize 20
                                ysize 2
                                background Solid("#f6d79d66")
                                padding (0, 0, 0, 0)
                            frame:
                                xalign 1.0
                                xoffset -8
                                ypos 8
                                xsize 2
                                ysize 20
                                background Solid("#f6d79d66")
                                padding (0, 0, 0, 0)

                            ## Corner accents (bottom-left)
                            frame:
                                xpos 8
                                yalign 1.0
                                yoffset -8
                                xsize 20
                                ysize 2
                                background Solid("#f6d79d66")
                                padding (0, 0, 0, 0)
                            frame:
                                xpos 8
                                yalign 1.0
                                yoffset -28
                                xsize 2
                                ysize 20
                                background Solid("#f6d79d66")
                                padding (0, 0, 0, 0)

                            ## Corner accents (bottom-right)
                            frame:
                                xalign 1.0
                                xoffset -8
                                yalign 1.0
                                yoffset -8
                                xsize 20
                                ysize 2
                                background Solid("#f6d79d66")
                                padding (0, 0, 0, 0)
                            frame:
                                xalign 1.0
                                xoffset -8
                                yalign 1.0
                                yoffset -28
                                xsize 2
                                ysize 20
                                background Solid("#f6d79d66")
                                padding (0, 0, 0, 0)

                            ## Top inner highlight edge
                            frame:
                                xalign 0.5
                                ypos 4
                                xsize 600
                                ysize 1
                                background Solid("#f6d79d18")
                                padding (0, 0, 0, 0)

                            ## Bottom inner highlight edge
                            frame:
                                xalign 0.5
                                yalign 1.0
                                yoffset -4
                                xsize 600
                                ysize 1
                                background Solid("#f6d79d18")
                                padding (0, 0, 0, 0)

                            ## Content area
                            vbox:
                                style "say_content_vbox"

                                if who is not None:
                                    ## Namebox with flanking ornaments
                                    hbox:
                                        xalign 0.5
                                        spacing 10

                                        ## Left ornament
                                        hbox:
                                            yalign 0.5
                                            spacing 4
                                            frame:
                                                xsize 24
                                                ysize 1
                                                yalign 0.5
                                                background Solid("#f6d79d44")
                                                padding (0, 0, 0, 0)
                                            frame:
                                                xsize 5
                                                ysize 5
                                                yalign 0.5
                                                background Solid("#f6d79d")
                                                padding (0, 0, 0, 0)

                                        window:
                                            id "namebox"
                                            style "namebox"
                                            text _who_text id "who"

                                        ## Right ornament
                                        hbox:
                                            yalign 0.5
                                            spacing 4
                                            frame:
                                                xsize 5
                                                ysize 5
                                                yalign 0.5
                                                background Solid("#f6d79d")
                                                padding (0, 0, 0, 0)
                                            frame:
                                                xsize 24
                                                ysize 1
                                                yalign 0.5
                                                background Solid("#f6d79d44")
                                                padding (0, 0, 0, 0)

                                text what id "what"

        ## ── Portrait box (left side, separate from dialogue window) ──
        frame:
            xalign 0.0
            yalign 1.0
            xoffset 40
            yoffset -56
            xsize 220
            ysize 310
            padding (3, 3, 3, 3)
            background Frame(Solid("#f6d79d33"), 0, 0)

            frame:
                xfill True
                yfill True
                padding (2, 2, 2, 2)
                background Frame(Solid("#f6d79d11"), 0, 0)

                frame:
                    xfill True
                    yfill True
                    padding (0, 0, 0, 0)
                    background Frame(Solid("#1a0a10f0"), 0, 0)

                    fixed:
                        ## Corner accents (top-left)
                        frame:
                            xpos 6
                            ypos 6
                            xsize 14
                            ysize 2
                            background Solid("#f6d79d66")
                            padding (0, 0, 0, 0)
                        frame:
                            xpos 6
                            ypos 6
                            xsize 2
                            ysize 14
                            background Solid("#f6d79d66")
                            padding (0, 0, 0, 0)

                        ## Corner accents (top-right)
                        frame:
                            xalign 1.0
                            xoffset -6
                            ypos 6
                            xsize 14
                            ysize 2
                            background Solid("#f6d79d66")
                            padding (0, 0, 0, 0)
                        frame:
                            xalign 1.0
                            xoffset -6
                            ypos 6
                            xsize 2
                            ysize 14
                            background Solid("#f6d79d66")
                            padding (0, 0, 0, 0)

                        ## Corner accents (bottom-left)
                        frame:
                            xpos 6
                            yalign 1.0
                            yoffset -6
                            xsize 14
                            ysize 2
                            background Solid("#f6d79d66")
                            padding (0, 0, 0, 0)
                        frame:
                            xpos 6
                            yalign 1.0
                            yoffset -22
                            xsize 2
                            ysize 14
                            background Solid("#f6d79d66")
                            padding (0, 0, 0, 0)

                        ## Corner accents (bottom-right)
                        frame:
                            xalign 1.0
                            xoffset -6
                            yalign 1.0
                            yoffset -6
                            xsize 14
                            ysize 2
                            background Solid("#f6d79d66")
                            padding (0, 0, 0, 0)
                        frame:
                            xalign 1.0
                            xoffset -6
                            yalign 1.0
                            yoffset -22
                            xsize 2
                            ysize 14
                            background Solid("#f6d79d66")
                            padding (0, 0, 0, 0)

                        ## Portrait image and title
                        vbox:
                            xfill True
                            yfill True
                            spacing 0

                            frame:
                                xfill True
                                ysize 240
                                padding (0, 0, 0, 0)
                                background Solid("#00000000")
                                if _speaker_portrait is not None:
                                    add _speaker_portrait:
                                        xalign 0.5
                                        yalign 0.5
                                        fit "contain"
                                        xsize 200
                                        ysize 240
                                else:
                                    text "?" xalign 0.5 yalign 0.5 size 72 color "#f6d79d44"

                            ## Title ribbon banner below portrait
                            $ _speaker_title = get_speaker_title(_who_text)
                            if _speaker_title is not None:
                                frame:
                                    xalign 0.5
                                    ysize 40
                                    xsize 200
                                    padding (0, 0, 0, 0)
                                    yoffset -8
                                    add Solid("#5c1a1a"):
                                        xysize (200, 40)
                                    add Solid("#f6d79d"):
                                        xysize (160, 32)
                                        xpos 20
                                        ypos 4
                                    add Solid("#5c1a1a"):
                                        xysize (20, 20)
                                        xpos 0
                                        ypos 20
                                    add Solid("#5c1a1a"):
                                        xysize (20, 20)
                                        xpos 180
                                        ypos 20
                                    text _speaker_title:
                                        xalign 0.5
                                        text_align 0.5
                                        size 15
                                        color "#1a0a10"
                                        bold True
                                        yalign 0.5
                                        outlines [(2, "#f6d79d33", 0, 0)]


## Make the namebox available for styling through the Character object.
init python:
    speaker_portraits = {
        ## Act 1
        "Jaden": "images/npcs/jaden.png",
        "Manong Josh": "images/npcs/manongjosh.png",
        "Aleng Maria": "images/npcs/alengmaria.png",
        "Manong Chris": "images/npcs/manongchris.png",
        "Joseph": "images/npcs/manong_driver.png",
        ## Act 2
        "ate bea": "images/npcs/ate_bea.png",
        "kuya mark": "images/npcs/kuya_mark.png",
        "maam reyes": "images/npcs/maam_reyes.png",
        "sir allan": "images/npcs/sir_allan.png",
        "Sir Noel": "images/npcs/sir_allan.png",
        ## Act 3/4 NPCs
        "Sarah": "images/npcs/sarah.png",
        "Caezar": "images/npcs/caezar.png",
        "Manong Guard": "images/npcs/manong_guard.png",
        "Sir Ruel": "images/npcs/sir_ruel.png",
        "Ms. Santos": "images/npcs/ms_santos.png",
        "Dorm Manager": "images/npcs/dorm_mgr.png",
        ## Act 5
        "Prof. Lena": "images/npcs/prof_lena.png",
        "Kuya Rico": "images/npcs/manong_guard.png",
        "Ate Grace": "images/npcs/ate_grace.png",
        "Dan": "images/npcs/Caezar.png",
        "School Physician": "images/npcs/physician.png",
        ## Act 6
        "Mika": "images/npcs/mika.png",
        "Kuya Tomas": "images/npcs/kuya_tomas.png",
        "Ate Jenny": "images/npcs/OSa.png",
        "Coach Ramon": "images/npcs/coach_ramon.png",
        "Ma'am Garcia": "images/npcs/maam_garcia.png",
        ## Act 7
        "Ate Rosa": "images/npcs/ow_cub.png",
        "Kuya Neil": "images/npcs/ow_lovers.png",
        "Prof. Santos": "images/npcs/ow_hsu.png",
        "Bea": "images/npcs/ate_bea.png",
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
        "Manong Driver": "Campus Shuttle Driver",
        "School Physician": "Campus Physician",
        "School Dentist": "Campus Dentist",
        ## Act 2
        "ate bea": "Upperclassman Guide",
        "kuya mark": "Campus Security",
        "maam reyes": "Admin Staff",
        "sir allan": "Faculty Member",
        "Sir Noel": "Faculty Member",
        ## Act 3/4
        "Sarah": "Fellow Student",
        "Mikhaela": "Fellow Student",
        "Caezar": "Campus Regular",
        "Manong Guard": "Gate Guard",
        "Sir Ruel": "Strict Professor",
        "Ms. Santos": "OSA Staff",
        "Dorm Manager": "Dorm Manager",
        ## Act 5
        "Prof. Lena": "Passionate Mentor",
        "Kuya Rico": "Reliable Upperclassman",
        "Ate Grace": "Supportive Ate",
        "Dan": "Chill Classmate",
        "Ria": "Study Buddy",
        "Nurse Santos": "Caring Nurse",
        ## Act 6
        "Mika": "Freshman Dreamer",
        "Kuya Tomas": "Dorm Leader",
        "Ate Jenny": "Friendly Ate",
        "Coach Ramon": "Motivator",
        ## Act 7
        "Ate Rosa": "Library Guardian",
        "Kuya Neil": "Tech Wiz",
        "Prof. Santos": "Stern Professor",
        "Bea": "Quiet Achiever",
        ## Act 8
        "Ate Linda": "Gentle Guide",
        "Nanay Elena": "Wise Elder",
        "Prof. Reyes": "Inspiring Scholar",
        ## Support/Other
        "Ma'am Garcia": "Guidance Counselor",
        "TLRC Coordinator": "Learning Resource Head",
        "Peer Tutor": "Peer Tutor",
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

    ## ── WELCOME MODE: "You just arrived in Miagao" ─────────────────────────
    ## Postcard/arrival-stamp layout — wider panel, layered border glow,
    ## stamp ribbon across the top, hand-lettered feel.
    if mode == "welcome":

        ## Deep vignette overlay
        add Solid("#000000e8") at tr_overlay_fade

        ## Outermost glow ring — amber
        frame:
            xalign 0.5
            yalign 0.5
            xminimum 860
            xmaximum 900
            padding (5, 5, 5, 5)
            background Frame(Solid("#f6d79d55"), 0, 0)
            at tr_panel_rise

            ## Mid glow ring — deeper gold
            frame:
                xfill True
                padding (3, 3, 3, 3)
                background Frame(Solid("#c8921888"), 0, 0)

                ## Main panel — warm dark parchment
                frame:
                    xfill True
                    padding (0, 0, 0, 0)
                    background Frame(Solid("#1a0a0ef8"), 0, 0)

                    vbox:
                        spacing 0

                        ## ── Stamp ribbon top ────────────────────────────────
                        frame:
                            xfill True
                            padding (0, 0, 0, 0)
                            background Solid("#2a0e0e")

                            hbox:
                                xfill True
                                xalign 0.5
                                yalign 0.5
                                spacing 0

                                ## Left decorative border stripe
                                frame:
                                    xsize 6
                                    ysize 44
                                    background Solid("#f6d79d")
                                    padding (0, 0, 0, 0)
                                frame:
                                    xsize 3
                                    ysize 44
                                    background Solid("#2a0e0e")
                                    padding (0, 0, 0, 0)
                                frame:
                                    xsize 3
                                    ysize 44
                                    background Solid("#f6d79d88")
                                    padding (0, 0, 0, 0)

                                ## Stamp label
                                text "✈  YOU HAVE ARRIVED":
                                    xalign 0.5
                                    xfill True
                                    text_align 0.5
                                    size 13
                                    color "#f6d79d"
                                    bold True
                                    outlines [(1, "#1a0a0e", 0, 0)]
                                    yalign 0.5
                                    at tr_subtitle_fade

                                ## Right decorative border stripe (mirror)
                                frame:
                                    xsize 3
                                    ysize 44
                                    background Solid("#f6d79d88")
                                    padding (0, 0, 0, 0)
                                frame:
                                    xsize 3
                                    ysize 44
                                    background Solid("#2a0e0e")
                                    padding (0, 0, 0, 0)
                                frame:
                                    xsize 6
                                    ysize 44
                                    background Solid("#f6d79d")
                                    padding (0, 0, 0, 0)

                        ## ── Perforated edge ─────────────────────────────────
                        ## Simulated stamp serration — row of small gold squares
                        hbox:
                            xfill True
                            xalign 0.5
                            spacing 4
                            at tr_divider_grow
                            ## 55 dots across ~860px panel
                            for _dot_i in range(55):
                                frame:
                                    xsize 8
                                    ysize 8
                                    background Solid("#f6d79d33")
                                    padding (0,0,0,0)

                        null height 32

                        ## ── Location stamp ──────────────────────────────────
                        text "◈  MIAGAO, ILOILO  ◈":
                            xalign 0.5
                            size 12
                            color "#c89218bb"
                            bold True
                            outlines [(1, "#1a0a0e", 0, 0)]
                            at tr_subtitle_fade

                        null height 10

                        ## ── Grand title ─────────────────────────────────────
                        text title:
                            xalign 0.5
                            text_align 0.5
                            size 56
                            color "#ffd700"
                            outlines [(5, "#1a0a0e", 0, 0), (3, "#8b691488", 3, 3), (1, "#f6d79d44", -1, -1)]
                            at tr_title_reveal

                        null height 4

                        ## ── Double rule under title ──────────────────────────
                        hbox:
                            xalign 0.5
                            spacing 0
                            at tr_divider_grow
                            frame:
                                xsize 340
                                ysize 2
                                background Solid("#f6d79d")
                                padding (0,0,0,0)
                        null height 2
                        hbox:
                            xalign 0.5
                            spacing 0
                            frame:
                                xsize 220
                                ysize 1
                                background Solid("#f6d79d55")
                                padding (0,0,0,0)

                        null height 20

                        ## ── Subtitle ─────────────────────────────────────────
                        if subtitle:
                            text subtitle:
                                xalign 0.5
                                text_align 0.5
                                size 20
                                color "#f1debf"
                                outlines [(2, "#1a0a0e", 0, 0)]
                                line_spacing 8
                                at tr_subtitle_fade

                        null height 32

                        ## ── Bottom perforated edge ───────────────────────────
                        hbox:
                            xfill True
                            xalign 0.5
                            spacing 4
                            at tr_divider_grow
                            for _dot_i in range(55):
                                frame:
                                    xsize 8
                                    ysize 8
                                    background Solid("#f6d79d33")
                                    padding (0,0,0,0)

                        ## ── Footer ribbon ────────────────────────────────────
                        frame:
                            xfill True
                            padding (0, 0, 0, 0)
                            background Solid("#2a0e0e")

                            text "UP VISAYAS — ISKOLAR NG BAYAN":
                                xalign 0.5
                                size 10
                                color "#f6d79d66"
                                bold True
                                yalign 0.5
                                at tr_subtitle_fade

        ## Click or key to dismiss
        key "dismiss" action Return()
        ## Slightly longer so the player can read the arrival moment
        timer 3.2 action Return()

    ## ── ALL OTHER MODES ───────────────────────────────────────────────────────
    else:

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

                    ## Icon / label
                    if mode == "complete":
                        text "★":
                            xalign 0.5
                            size 40
                            color "#f6d79d"
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
    ymaximum 700
    yalign 0.5
    background Frame(Solid("#1e0c12ee"), 0, 0)
    padding (20, 14, 20, 14)

style choice_area is default:
    xalign 0.5
    yalign 1.0
    xfill True
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


    # Quick menu removed as requested



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
        style_prefix "up_nav"

        ## This centers the entire menu perfectly inside your left sidebar
        xalign 0.5
        yalign 0.5
        spacing 24  

        ## Retro Menu Header
        text "SYSTEM" style "up_nav_header"
        
        ## Small decorative divider under the header
        frame:
            background Solid("#f6d79d")
            xsize 100
            ysize 4
            xalign 0.5
            padding (0,0,0,0)
        
        null height 20

        textbutton _("Return") action Return()
        textbutton _("Settings") action ShowMenu("preferences")
        textbutton _("About") action ShowMenu("about")
        textbutton _("Help") action ShowMenu("help")

        if not main_menu:
            null height 10

            ## Thin gold divider before the destructive action
            frame:
                background Solid("#f6d79d44")
                xsize 100
                ysize 1
                xalign 0.5
                padding (0,0,0,0)

            null height 10

            textbutton _("Main Menu") action MainMenu()


## ============================================================================
## 8-BIT UP AESTHETIC STYLES
## ============================================================================

style up_nav_header is text:
    xalign 0.5
    color "#f6d79d"
    size 32
    outlines [(3, "#1a0a10", 0, 0)]
    ## 👇 UNCOMMENT THE LINE BELOW AND PUT YOUR FONT FILE PATH HERE 👇
    # font "gui/fonts/8bit_font.ttf" 

style up_nav_button is button:
    xalign 0.5
    xsize 260
    padding (10, 16, 10, 16)
    ## Sharp, flat boxes for that retro pixel feel
    background Solid("#1a0a1099")      # Dark translucent box
    hover_background Solid("#f6d79d")  # Solid Sablay Gold on hover
    selected_background Solid("#f6d79d")

style up_nav_button_text is button_text:
    xalign 0.5
    text_align 0.5
    color "#f1debf"             # Off-white/gold text
    hover_color "#5c1a1a"       # UP Maroon text when hovered!
    selected_color "#5c1a1a"    # UP Maroon text when selected!
    size 20
    outlines [(2, "#1a0a10", 0, 0)]
    hover_outlines []           # Removes outline on hover for a clean retro look
    selected_outlines []
    
    ## 👇 UNCOMMENT THE LINE BELOW AND PUT YOUR FONT FILE PATH HERE 👇
    # font "gui/fonts/8bit_font.ttf"
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

            textbutton _("NEW GAME") action [Stop('music', fadeout=1.0), Start()] style "mm_btn" at btn_appear(0.7), btn_hover_lift
            textbutton _("CONTINUE") action [Stop('music', fadeout=1.0), ShowMenu("load")] style "mm_btn" at btn_appear(0.85), btn_hover_lift
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

    ## Deep dark background for the whole screen
    add Solid("#0e1b2a") # Faint dark blue/grey
    add Solid("#1a0a10ed") # Dark overlay for better readability

    ## Left Sidebar (UPV Maroon)
    frame:
        background Solid("#5c1a1a")
        xsize 360
        xalign 0.0
        yfill True

    ## Gold accent line separating the navigation from the settings content
    frame:
        background Solid("#f6d79d")
        xsize 2
        xpos 360
        yfill True

    frame:
        style "game_menu_outer_frame"

        hbox:
            ## Window for the navigation menu (Left Side)
            frame:
                style "game_menu_navigation_frame"
                xsize 360
                use navigation

            ## Window for the inner content (Settings, Save slots, etc. on the Right Side)
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

    ## Custom Title Design (e.g. says "System Preferences" or "Save Game" at the top)
    text title:
        xpos 420
        ypos 40
        size 46
        color "#f6d79d"
        bold True
        outlines [(2, "#1a0a10", 0, 0)]

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
    else:
        key "game_menu" action Return()

    if renpy.variant("mobile"):
        $ return_action = ShowMenu("main_menu") if main_menu else Hide()
        key "rollback" action return_action


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

    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:
            spacing 36
            xalign 0.5
            xmaximum 850

            frame:
                xfill True
                background Frame(Solid("#1a0a10f0"), 0, 0)
                padding (40, 30, 40, 30)

                vbox:
                    spacing 20

                    ## Section Header
                    hbox:
                        spacing 12
                        yalign 0.5
                        text "✦" size 26 color "#f6d79d" yalign 0.5 at tr_star_spin
                        text _("Project Information") size 24 color "#f6d79d" bold True yalign 0.5
                        
                    ## UPV Maroon Divider
                    frame:
                        xsize 770 ysize 2 background Solid("#5c1a1a") padding (0,0,0,0)

                    ## Core Game Info & Synopsis
                    vbox:
                        xoffset 36
                        spacing 10
                        text "[config.name!t]" size 32 color "#f6d79d" bold True outlines [(2, "#1a0a10", 0, 0)]
                        text _("Version [config.version!t]") size 16 color "#f1debf" 
                        
                        null height 15
                        
                        ## Synopsis / Description
                        text _("A point-and-click adventure set in UP Visayas - Miagao campus. Navigate your first day as an Iskolar ng Bayan, exploring the campus map, handling enrollment, and surviving the start of your university life."):
                            size 18 
                            color "#e2e8f0" 
                            line_spacing 6
                            xmaximum 700

                    null height 15

                    ## Secondary Thin Divider
                    frame:
                        xsize 770 ysize 1 background Solid("#5c1a1a") padding (0,0,0,0)

                    null height 5

                    ## Credits Section (Two Columns)
                    vbox:
                        xoffset 36
                        spacing 20

                        text "DEVELOPMENT TEAM" size 20 color "#f6d79d" bold True

                        hbox:
                            spacing 120  ## Space between the two columns
                            
                            ## Left Column
                            vbox:
                                spacing 16
                                use credit_line("Project Lead / Programmer", "Josaiah Borres")
                                use credit_line("Lead Writer", "Adrian Joel Jaspa")
                                use credit_line("UI / UX Design", "Brethren Ace de la Gente")
                                
                            ## Right Column
                            vbox:
                                spacing 16
                                use credit_line("Background & Sprite Art", "Ace, Adrian, Josaiah")
                                use credit_line("Music & Sound Effects", "Ace, Adrian, Josaiah, No Copyright Music")
                                use credit_line("Special Thanks", "The UPV Community")

                    null height 15
                    frame:
                        xsize 770 ysize 1 background Solid("#5c1a1a") padding (0,0,0,0)
                    null height 5

                    ## Engine Text / Legal (Pulls from options.rpy)
                    vbox:
                        xoffset 36
                        if gui.about:
                            text "[gui.about!t]" size 14 color "#9ca3af" line_spacing 4


## ============================================================================
## HELPER SCREEN FOR CREDITS
## ============================================================================
## This makes it super easy to add perfectly aligned credits!
screen credit_line(role, name):
    vbox:
        text role size 14 color "#f6d79d" bold True
        text name size 18 color "#f1debf"

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

## ============================================================================
## SAVE SCREEN — uses game_menu sidebar (Return / Settings / About / Help)
## ============================================================================

screen save():
    tag menu
    use game_menu(_("Save Game")):

        vbox:
            xalign 0.5
            yalign 0.38
            spacing 24

            ## Section ornament
            hbox:
                xalign 0.5
                spacing 10
                frame:
                    xsize 80 ysize 1 yalign 0.5
                    background Solid("#f6d79d44") padding (0,0,0,0)
                frame:
                    xsize 6 ysize 6 yalign 0.5
                    background Solid("#f6d79d88") padding (0,0,0,0)
                text "✦  SAVE YOUR PROGRESS  ✦":
                    size 13 color "#f6d79d88" bold True yalign 0.5
                frame:
                    xsize 6 ysize 6 yalign 0.5
                    background Solid("#f6d79d88") padding (0,0,0,0)
                frame:
                    xsize 80 ysize 1 yalign 0.5
                    background Solid("#f6d79d44") padding (0,0,0,0)

            ## Cards
            hbox:
                xalign 0.5
                spacing 20

                for slot in range(1, 4):
                    $ slot_label = "0" + str(slot)

                    button:
                        action FileSave(slot)
                        xsize 310
                        ysize 420
                        padding (0, 0, 0, 0)
                        background Solid("#1a0a10")
                        hover_background Solid("#2a0d18")

                        vbox:
                            xfill True
                            spacing 0

                            ## Top glow bar
                            frame:
                                xfill True ysize 3 padding (0,0,0,0)
                                background If(FileLoadable(slot), Solid("#f6d79d"), Solid("#2a1020"))

                            ## Thumbnail
                            frame:
                                xfill True ysize 190 padding (0,0,0,0)
                                background Solid("#0a0408")
                                if FileLoadable(slot):
                                    add FileScreenshot(slot) size (310, 190)
                                else:
                                    vbox:
                                        xalign 0.5 yalign 0.5 spacing 10
                                        hbox:
                                            xalign 0.5 spacing 6
                                            frame:
                                                xsize 30 ysize 1 yalign 0.5
                                                background Solid("#2a1020") padding (0,0,0,0)
                                            frame:
                                                xsize 5 ysize 5 yalign 0.5
                                                background Solid("#2a1020") padding (0,0,0,0)
                                            frame:
                                                xsize 30 ysize 1 yalign 0.5
                                                background Solid("#2a1020") padding (0,0,0,0)
                                        text "✦":
                                            xalign 0.5 size 28 color "#2a1020"
                                        text "NO SAVE DATA":
                                            xalign 0.5 size 9 color "#2a1020" bold True
                                        hbox:
                                            xalign 0.5 spacing 6
                                            frame:
                                                xsize 30 ysize 1 yalign 0.5
                                                background Solid("#2a1020") padding (0,0,0,0)
                                            frame:
                                                xsize 5 ysize 5 yalign 0.5
                                                background Solid("#2a1020") padding (0,0,0,0)
                                            frame:
                                                xsize 30 ysize 1 yalign 0.5
                                                background Solid("#2a1020") padding (0,0,0,0)

                            ## Shadow strip
                            frame:
                                xfill True ysize 4 padding (0,0,0,0)
                                background Solid("#00000088")

                            ## Slot identity band
                            frame:
                                xfill True ysize 52 background Solid("#110609")
                                padding (18, 0, 18, 0)
                                hbox:
                                    xfill True yalign 0.5
                                    frame:
                                        xsize 3 ysize 26 yalign 0.5
                                        background If(FileLoadable(slot), Solid("#f6d79d"), Solid("#3a1020"))
                                        padding (0,0,0,0)
                                    null width 12
                                    text "SLOT  [slot_label]":
                                        size 18 color "#f6d79d" bold True yalign 0.5
                                    frame:
                                        xalign 1.0 xsize 8 ysize 8 yalign 0.5
                                        background If(FileLoadable(slot), Solid("#f6d79d"), Solid("#2a1020"))
                                        padding (0,0,0,0)

                            ## Thin maroon rule
                            frame:
                                xfill True ysize 1 padding (0,0,0,0)
                                background Solid("#3a0a14")

                            ## Info panel
                            frame:
                                xfill True ysize 138 background Solid("#120709")
                                padding (18, 14, 18, 14)
                                vbox:
                                    xfill True spacing 8
                                    if FileLoadable(slot):
                                        hbox:
                                            spacing 6 yalign 0.5
                                            frame:
                                                xsize 3 ysize 14 yalign 0.5
                                                background Solid("#c8a87a") padding (0,0,0,0)
                                            text "ACT  [current_act]":
                                                size 10 color "#c8a87a" bold True yalign 0.5
                                        text FileSaveName(slot):
                                            size 16 color "#f6d79d" bold True
                                            outlines [(1, "#000000", 0, 0)]
                                        text FileTime(slot,
                                            format=_("{#file_time}%b %d, %Y  —  %H:%M"),
                                            empty=_("")):
                                            size 11 color "#5a3040" line_spacing 4
                                    else:
                                        null height 12
                                        text "— Empty Slot —":
                                            size 14 color "#2a1020" italic True
                                        text "Click to save here":
                                            size 11 color "#2a1020"

                            ## DEL strip
                            frame:
                                xfill True ysize 32 padding (0,0,0,0)
                                if FileLoadable(slot):
                                    background Solid("#1e060e")
                                    hbox:
                                        xalign 0.5 yalign 0.5 spacing 8
                                        frame:
                                            xsize 1 ysize 10 yalign 0.5
                                            background Solid("#3a1828") padding (0,0,0,0)
                                        text "DEL  to delete":
                                            size 9 color "#3a1828" bold True yalign 0.5
                                        frame:
                                            xsize 1 ysize 10 yalign 0.5
                                            background Solid("#3a1828") padding (0,0,0,0)
                                else:
                                    background Solid("#0e0508")

                        key "save_delete" action FileDelete(slot)

            ## Footer
            hbox:
                xalign 0.5 spacing 8
                frame:
                    xsize 50 ysize 1 yalign 0.5
                    background Solid("#3a1828") padding (0,0,0,0)
                text "Press DEL on a filled slot to delete it":
                    size 11 color "#3a1828" yalign 0.5
                frame:
                    xsize 50 ysize 1 yalign 0.5
                    background Solid("#3a1828") padding (0,0,0,0)


## ============================================================================
## LOAD SCREEN — fullscreen, no sidebar, only a Return button
## ============================================================================

screen load():
    tag menu

    ## Background
    add Solid("#0e1b2a")
    add Solid("#1a0a10ed")

    ## Left maroon accent strip
    frame:
        background Solid("#5c1a1a")
        xsize 6 xalign 0.0 yfill True
    frame:
        background Solid("#f6d79d")
        xsize 2 xpos 6 yfill True

    ## Return button — top left
    textbutton "◀  Return":
        action Return()
        xpos 28 ypos 28
        text_size 13
        text_color "#f6d79d66"
        text_hover_color "#f6d79d"
        text_bold True
        background Solid("#00000000")
        hover_background Solid("#00000000")
        padding (10, 8, 10, 8)

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
    else:
        key "game_menu" action Return()

    ## Title
    text "CONTINUE":
        xalign 0.5 ypos 44
        size 44 color "#f6d79d" bold True
        outlines [(2, "#1a0a10", 0, 0)]

    ## Spinning star ornament
    text "✦":
        xalign 0.5 ypos 100
        size 16 color "#f6d79d66"
        at tr_star_spin

    vbox:
        xalign 0.5
        yalign 0.54
        spacing 26

        ## Section ornament
        hbox:
            xalign 0.5 spacing 10
            frame:
                xsize 100 ysize 1 yalign 0.5
                background Solid("#f6d79d44") padding (0,0,0,0)
            frame:
                xsize 6 ysize 6 yalign 0.5
                background Solid("#f6d79d88") padding (0,0,0,0)
            text "✦  CHOOSE YOUR SAVE FILE  ✦":
                size 13 color "#f6d79d88" bold True yalign 0.5
            frame:
                xsize 6 ysize 6 yalign 0.5
                background Solid("#f6d79d88") padding (0,0,0,0)
            frame:
                xsize 100 ysize 1 yalign 0.5
                background Solid("#f6d79d44") padding (0,0,0,0)

        ## Cards — wider since no sidebar
        hbox:
            xalign 0.5
            spacing 28

            for slot in range(1, 4):
                $ slot_label = "0" + str(slot)

                button:
                    action FileLoad(slot)
                    sensitive FileLoadable(slot)
                    xsize 400
                    ysize 430
                    padding (0, 0, 0, 0)
                    background Solid("#1a0a10")
                    hover_background Solid("#2a0d18")
                    insensitive_background Solid("#0e0508")

                    vbox:
                        xfill True
                        spacing 0

                        ## Top glow bar
                        frame:
                            xfill True ysize 3 padding (0,0,0,0)
                            background If(FileLoadable(slot), Solid("#f6d79d"), Solid("#1a0a10"))

                        ## Thumbnail
                        frame:
                            xfill True ysize 222 padding (0,0,0,0)
                            background Solid("#0a0408")
                            if FileLoadable(slot):
                                add FileScreenshot(slot) size (400, 222)
                            else:
                                vbox:
                                    xalign 0.5 yalign 0.5 spacing 10
                                    hbox:
                                        xalign 0.5 spacing 6
                                        frame:
                                            xsize 40 ysize 1 yalign 0.5
                                            background Solid("#1e0a10") padding (0,0,0,0)
                                        frame:
                                            xsize 5 ysize 5 yalign 0.5
                                            background Solid("#1e0a10") padding (0,0,0,0)
                                        frame:
                                            xsize 40 ysize 1 yalign 0.5
                                            background Solid("#1e0a10") padding (0,0,0,0)
                                    text "✦":
                                        xalign 0.5 size 32 color "#1e0a10"
                                    text "NO SAVE DATA":
                                        xalign 0.5 size 9 color "#1e0a10" bold True
                                    hbox:
                                        xalign 0.5 spacing 6
                                        frame:
                                            xsize 40 ysize 1 yalign 0.5
                                            background Solid("#1e0a10") padding (0,0,0,0)
                                        frame:
                                            xsize 5 ysize 5 yalign 0.5
                                            background Solid("#1e0a10") padding (0,0,0,0)
                                        frame:
                                            xsize 40 ysize 1 yalign 0.5
                                            background Solid("#1e0a10") padding (0,0,0,0)

                        ## Shadow strip
                        frame:
                            xfill True ysize 4 padding (0,0,0,0)
                            background Solid("#00000088")

                        ## Slot identity band
                        frame:
                            xfill True ysize 52 background Solid("#110609")
                            padding (20, 0, 20, 0)
                            hbox:
                                xfill True yalign 0.5
                                frame:
                                    xsize 3 ysize 26 yalign 0.5
                                    background If(FileLoadable(slot), Solid("#f6d79d"), Solid("#2a1020"))
                                    padding (0,0,0,0)
                                null width 14
                                text "SLOT  [slot_label]":
                                    size 20 color "#f6d79d" bold True yalign 0.5
                                frame:
                                    xalign 1.0 xsize 8 ysize 8 yalign 0.5
                                    background If(FileLoadable(slot), Solid("#f6d79d"), Solid("#2a1020"))
                                    padding (0,0,0,0)

                        ## Maroon rule
                        frame:
                            xfill True ysize 1 padding (0,0,0,0)
                            background Solid("#3a0a14")

                        ## Info panel
                        frame:
                            xfill True ysize 134 background Solid("#120709")
                            padding (20, 14, 20, 14)
                            vbox:
                                xfill True spacing 8
                                if FileLoadable(slot):
                                    hbox:
                                        spacing 6 yalign 0.5
                                        frame:
                                            xsize 3 ysize 14 yalign 0.5
                                            background Solid("#c8a87a") padding (0,0,0,0)
                                        text "ACT  [current_act]":
                                            size 10 color "#c8a87a" bold True yalign 0.5
                                    text FileSaveName(slot):
                                        size 18 color "#f6d79d" bold True
                                        outlines [(1, "#000000", 0, 0)]
                                    text FileTime(slot,
                                        format=_("{#file_time}%b %d, %Y  —  %H:%M"),
                                        empty=_("")):
                                        size 12 color "#5a3040" line_spacing 4
                                else:
                                    null height 14
                                    text "— Empty —":
                                        size 15 color "#2a1020" italic True

                        ## Bottom strip
                        frame:
                            xfill True ysize 14 padding (0,0,0,0)
                            if FileLoadable(slot):
                                background Solid("#1e0a10")
                                text "▶  Load":
                                    xalign 0.5 yalign 0.5
                                    size 8 color "#f6d79d44" bold True
                            else:
                                background Solid("#0e0508")

        ## Footer
        hbox:
            xalign 0.5 spacing 8
            frame:
                xsize 70 ysize 1 yalign 0.5
                background Solid("#3a1828") padding (0,0,0,0)
            text "Greyed-out slots have no save data":
                size 11 color "#3a1828" yalign 0.5
            frame:
                xsize 70 ysize 1 yalign 0.5
                background Solid("#3a1828") padding (0,0,0,0)


## ============================================================================
## FILE SLOT STYLES
## ============================================================================

style up_slot_num_text is text:
    xalign 0.5
    size 26
    color "#f6d79d"
    bold True

style up_slot_numlabel_text is text:
    xalign 0.5
    size 9
    color "#5c3040"

style up_slot_badge_text is text:
    size 10
    color "#c8a87a"

style up_slot_name_text is text:
    xalign 0.0
    size 15
    color "#f6d79d"
    bold True
    outlines [(1, "#000000", 0, 0)]

style up_slot_time_text is text:
    xalign 0.0
    size 11
    color "#7a5060"
    line_spacing 4

style up_slot_delkey_text is text:
    size 9
    color "#3a1828"

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("System Preferences"), scroll="viewport"):

        vbox:
            spacing 36
            xalign 0.5
            xmaximum 850  # Keeps the settings centered and readable

            # ═══════════════════════════════════════
            # DISPLAY SETTINGS
            # ═══════════════════════════════════════
            frame:
                xfill True
                background Frame(Solid("#1a0a10f0"), 0, 0) # Deep dark background matching dialogue boxes
                padding (40, 30, 40, 30)

                vbox:
                    spacing 20

                    ## Section Header
                    hbox:
                        spacing 12
                        yalign 0.5
                        text "✦" size 26 color "#f6d79d" yalign 0.5 at tr_star_spin
                        text _("Display") size 24 color "#f6d79d" bold True yalign 0.5
                        
                    ## UPV Maroon Divider
                    frame:
                        xsize 770 ysize 2 background Solid("#5c1a1a") padding (0,0,0,0)

                    if renpy.variant("pc") or renpy.variant("web"):
                        hbox:
                            spacing 20
                            xoffset 36
                            textbutton _("Windowed") action Preference("display", "window") style "up_pref_btn"
                            textbutton _("Fullscreen") action Preference("display", "fullscreen") style "up_pref_btn"

            # ═══════════════════════════════════════
            # DIALOGUE & SKIPPING
            # ═══════════════════════════════════════
            frame:
                xfill True
                background Frame(Solid("#1a0a10f0"), 0, 0)
                padding (40, 30, 40, 30)

                vbox:
                    spacing 20

                    hbox:
                        spacing 12
                        yalign 0.5
                        text "✦" size 26 color "#f6d79d" yalign 0.5 at tr_star_spin
                        text _("Reading & Pacing") size 24 color "#f6d79d" bold True yalign 0.5
                        
                    frame:
                        xsize 770 ysize 2 background Solid("#5c1a1a") padding (0,0,0,0)

                    hbox:
                        spacing 20
                        xoffset 36
                        textbutton _("Skip Unseen") action Preference("skip", "toggle") style "up_pref_btn"
                        textbutton _("Skip After Choices") action Preference("after choices", "toggle") style "up_pref_btn"
                        textbutton _("Skip Transitions") action InvertSelected(Preference("transitions", "toggle")) style "up_pref_btn"

                    null height 10

                    vbox:
                        xoffset 36
                        spacing 10
                        text _("Text Speed") size 16 color "#e2e8f0" bold True
                        hbox:
                            spacing 16
                            bar value Preference("text speed") style "slider" xsize 400
                            text _("Fast") size 14 color "#6b7280" yalign 0.5

                    vbox:
                        xoffset 36
                        spacing 10
                        text _("Auto-Forward Time") size 16 color "#e2e8f0" bold True
                        hbox:
                            spacing 16
                            bar value Preference("auto-forward time") style "slider" xsize 400
                            text _("Slow") size 14 color "#6b7280" yalign 0.5

            # ═══════════════════════════════════════
            # AUDIO LEVELS
            # ═══════════════════════════════════════
            frame:
                xfill True
                background Frame(Solid("#1a0a10f0"), 0, 0)
                padding (40, 30, 40, 30)

                vbox:
                    spacing 20

                    hbox:
                        spacing 12
                        yalign 0.5
                        text "✦" size 26 color "#f6d79d" yalign 0.5 at tr_star_spin
                        text _("Audio Levels") size 24 color "#f6d79d" bold True yalign 0.5
                        
                    frame:
                        xsize 770 ysize 2 background Solid("#5c1a1a") padding (0,0,0,0)

                    if config.has_music:
                        vbox:
                            xoffset 36
                            spacing 10
                            text _("Music Volume") size 16 color "#e2e8f0" bold True
                            bar value Preference("music volume") style "slider" xsize 400

                    if config.has_sound:
                        vbox:
                            xoffset 36
                            spacing 10
                            hbox:
                                xminimum 400
                                text _("Sound Effects Volume") size 16 color "#e2e8f0" bold True yalign 0.5
                                if config.sample_sound:
                                    textbutton _("Test") action Play("sound", config.sample_sound) style "up_pref_test_btn" xalign 1.0
                            bar value Preference("sound volume") style "slider" xsize 400

                    if config.has_voice:
                        vbox:
                            xoffset 36
                            spacing 10
                            hbox:
                                xminimum 400
                                text _("Voice Volume") size 16 color "#e2e8f0" bold True yalign 0.5
                                if config.sample_voice:
                                    textbutton _("Test") action Play("voice", config.sample_voice) style "up_pref_test_btn" xalign 1.0
                            bar value Preference("voice volume") style "slider" xsize 400

                    if config.has_music or config.has_sound or config.has_voice:
                        null height 10
                        hbox:
                            xoffset 36
                            textbutton _("Mute All Audio") action Preference("all mute", "toggle") style "up_pref_btn"

## ============================================================================
## CUSTOM STYLES FOR THE PREFERENCES SCREEN
## ============================================================================
style up_pref_btn is button:
    background Frame(Solid("#5c1a1a99"), 4, 4, 4, 4)       # Deep Maroon Background
    hover_background Frame(Solid("#f6d79d"), 4, 4, 4, 4)   # Gold on hover
    selected_background Frame(Solid("#f6d79d"), 4, 4, 4, 4)# Gold when selected
    padding (20, 10, 20, 10)

style up_pref_btn_text is button_text:
    color "#f1debf"             # Light gold text
    hover_color "#1a0a10"       # Dark text on hover
    selected_color "#1a0a10"    # Dark text when selected
    size 16
    bold True

style up_pref_test_btn is button:
    background Frame(Solid("#f6d79d22"), 4, 4, 4, 4)
    hover_background Frame(Solid("#f6d79d"), 4, 4, 4, 4)
    padding (12, 4, 12, 4)
    yalign 0.5

style up_pref_test_btn_text is button_text:
    color "#f6d79d"
    hover_color "#1a0a10"
    size 14
    bold True

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
            spacing 24
            xalign 0.5
            xmaximum 850

            ## Retro Tabs for switching devices
            hbox:
                xalign 0.5
                spacing 20
                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard") style "up_tab_btn"
                textbutton _("Mouse") action SetScreenVariable("device", "mouse") style "up_tab_btn"
                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad") style "up_tab_btn"

            ## Content Box
            frame:
                xfill True
                background Frame(Solid("#1a0a10f0"), 0, 0)
                padding (40, 30, 40, 30)

                vbox:
                    spacing 20
                    
                    ## UPV Maroon Divider
                    frame:
                        xsize 770 ysize 2 background Solid("#5c1a1a") padding (0,0,0,0)

                    if device == "keyboard":
                        use keyboard_help
                    elif device == "mouse":
                        use mouse_help
                    elif device == "gamepad":
                        use gamepad_help


screen keyboard_help():
    vbox:
        spacing 16
        xoffset 36
        use help_section(_("Enter"), _("Advances dialogue and activates the interface."))
        use help_section(_("Space"), _("Advances dialogue without selecting choices."))
        use help_section(_("Arrow Keys"), _("Navigate the interface."))
        use help_section(_("Escape"), _("Accesses the game menu."))
        use help_section(_("Ctrl"), _("Skips dialogue while held down."))
        use help_section(_("Tab"), _("Toggles dialogue skipping."))
        use help_section(_("Page Up"), _("Rolls back to earlier dialogue."))
        use help_section(_("Page Down"), _("Rolls forward to later dialogue."))
        use help_section("H", _("Hides the user interface."))
        use help_section("S", _("Takes a screenshot."))
        use help_section("V", _("Toggles assistive self-voicing."))

screen mouse_help():
    vbox:
        spacing 16
        xoffset 36
        use help_section(_("Left Click"), _("Advances dialogue and activates the interface."))
        use help_section(_("Middle Click"), _("Hides the user interface."))
        use help_section(_("Right Click"), _("Accesses the game menu."))
        use help_section(_("Mouse Wheel Up\nClick Rollback Side"), _("Rolls back to earlier dialogue."))
        use help_section(_("Mouse Wheel Down"), _("Rolls forward to later dialogue."))

screen gamepad_help():
    vbox:
        spacing 16
        xoffset 36
        use help_section(_("Right Trigger\nA/Bottom Button"), _("Advances dialogue and activates the interface."))
        use help_section(_("Left Trigger\nLeft Shoulder"), _("Rolls back to earlier dialogue."))
        use help_section(_("Right Shoulder"), _("Rolls forward to later dialogue."))
        use help_section(_("D-Pad, Sticks"), _("Navigate the interface."))
        use help_section(_("Start, Guide"), _("Accesses the game menu."))
        use help_section(_("Y/Top Button"), _("Hides the user interface."))
        textbutton _("Calibrate") action GamepadCalibrate() style "up_pref_test_btn" xalign 0.0

## Helper screen to format the two-column retro text
screen help_section(key_name, description):
    hbox:
        xfill True
        text key_name:
            xsize 220
            color "#f6d79d"
            bold True
            size 16
        text description:
            color "#f1debf"
            size 16
            xmaximum 500


## ============================================================================
## CUSTOM STYLES FOR HELP TABS
## ============================================================================

style up_tab_btn is button:
    xalign 0.5
    padding (20, 10, 20, 10)
    ## Sharp flat boxes for retro tabs
    background Solid("#1a0a1099")      
    hover_background Solid("#5c1a1a")  # UP Maroon on hover
    selected_background Solid("#f6d79d") # Sablay Gold when active

style up_tab_btn_text is button_text:
    xalign 0.5
    text_align 0.5
    color "#f1debf"             
    hover_color "#f6d79d"       # Gold text on maroon background when hovered
    selected_color "#1a0a10"    # Dark text on gold background when selected
    size 18
    bold True

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

    add Solid("#0d0406") alpha 0.82 at confirm_overlay_in

    frame:
        xalign 0.5
        yalign 0.5
        padding (0, 0, 0, 0)
        background Solid("#00000000")
        at confirm_panel_in

        frame:
            padding (3, 3, 3, 3)
            background Frame(Solid("#f6d79d44"), 0, 0)

            frame:
                padding (2, 2, 2, 2)
                background Frame(Solid("#c8921833"), 0, 0)

                frame:
                    xminimum 420
                    xmaximum 520
                    padding (0, 0, 0, 0)
                    background Solid("#1a0a0ef8")

                    vbox:
                        spacing 0

                        ## Header bar
                        frame:
                            background Solid("#2a0e0e")
                            xfill True
                            padding (24, 14, 24, 14)
                            hbox:
                                spacing 10
                                yalign 0.5
                                text "\u26a0" size 14 color "#ffd700" yalign 0.5
                                text "CONFIRM ACTION" size 13 color "#ffd700" bold True yalign 0.5

                        ## Gold rule
                        frame:
                            background Solid("#f6d79d33")
                            xfill True
                            ysize 1
                            padding (0, 0, 0, 0)

                        ## Message body
                        frame:
                            background Solid("#0d0406")
                            xfill True
                            padding (32, 28, 32, 24)
                            vbox:
                                spacing 0
                                xalign 0.5
                                text _(message):
                                    xalign 0.5
                                    text_align 0.5
                                    size 15
                                    color "#f1debf"
                                    bold True
                                    line_spacing 4

                        ## Gold rule
                        frame:
                            background Solid("#f6d79d22")
                            xfill True
                            ysize 1
                            padding (0, 0, 0, 0)

                        ## Action buttons
                        frame:
                            background Solid("#130609")
                            xfill True
                            padding (24, 16, 24, 16)
                            hbox:
                                xalign 0.5
                                spacing 20

                                ## Yes - crimson confirm
                                button:
                                    xsize 160
                                    padding (0, 12, 0, 12)
                                    background Solid("#5c1a1a")
                                    hover_background Solid("#7c2222")
                                    action yes_action
                                    hbox:
                                        xalign 0.5
                                        spacing 8
                                        yalign 0.5
                                        text "\u2713" size 14 color "#ffd700" yalign 0.5
                                        text _("Yes") size 14 color "#ffd700" bold True yalign 0.5

                                ## No - dark dismiss
                                button:
                                    xsize 160
                                    padding (0, 12, 0, 12)
                                    background Solid("#2a1018")
                                    hover_background Solid("#3c1828")
                                    action no_action
                                    hbox:
                                        xalign 0.5
                                        spacing 8
                                        yalign 0.5
                                        text "\u2717" size 14 color "#c8921888" yalign 0.5
                                        text _("No") size 14 color "#f6d79d88" bold True yalign 0.5

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


transform confirm_overlay_in:
    alpha 0.0
    easein 0.18 alpha 1.0

transform confirm_panel_in:
    alpha 0.0 zoom 0.95 yoffset 12
    easein 0.22 alpha 1.0 zoom 1.0 yoffset 0


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Solid("#00000000")
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"
    color "#f1debf"
    size 15

style confirm_button:
    background "#5c1a1a"
    hover_background "#7c2222"
    padding (20, 10, 20, 10)

style confirm_button_text:
    color "#ffd700"
    hover_color "#ffffff"
    size 14
    bold True


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
        ypos 110
        xminimum 320
        padding (3, 3, 3, 3)
        background Frame(Solid("#f6d79d55"), 0, 0)

        frame:
            xfill True
            padding (2, 2, 2, 2)
            background Frame(Solid("#c8921833"), 0, 0)

            frame:
                xfill True
                padding (20, 12, 20, 12)
                background Solid("#1a0a0ef5")

                hbox:
                    xalign 0.5
                    spacing 10
                    yalign 0.5

                    text "★":
                        size 13
                        color "#ffd700"
                        outlines [(1, "#1a0a0e", 0, 0)]
                        yalign 0.5

                    text "[message!tq]":
                        size 14
                        color "#f1debf"
                        outlines [(1, "#1a0a0e", 0, 0)]
                        yalign 0.5

                    text "★":
                        size 13
                        color "#ffd700"
                        outlines [(1, "#1a0a0e", 0, 0)]
                        yalign 0.5

    timer 3.0 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0 yoffset -16
        easein 0.28 alpha 1.0 yoffset 0
    on hide:
        easeout 0.32 alpha 0.0 yoffset -16


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

    ## Emoji assigned per question index — swap these to match your actual q.text order
    ## Q0 → transport/arrival, Q1 → food/community, Q2 → language/locals,
    ## Q3 → campus/landmark, Q4 → fees/admin, Q5 → general/town
    python:
        _nb_icons = ["🛺", "🍚", "🗣️", "🏛️", "📋", "🏘️"]

    add Solid("#0d0406") alpha 0.96

    ## Outermost glow ring
    frame:
        xalign 0.5
        yalign 0.5
        xsize 720
        padding (4, 4, 4, 4)
        background Frame(Solid("#f6d79d55"), 0, 0)

        frame:
            xfill True
            padding (2, 2, 2, 2)
            background Frame(Solid("#c8921833"), 0, 0)

            frame:
                xfill True
                padding (0, 0, 0, 0)
                background Solid("#1a0a0ef8")

                vbox:
                    spacing 0

                    ## ── Header bar ─────────────────────────────────────────────
                    frame:
                        background Solid("#2a0e0e")
                        xfill True
                        padding (28, 16, 28, 16)

                        hbox:
                            xfill True
                            yalign 0.5
                            spacing 0

                            ## Left L-bracket accent
                            vbox:
                                yalign 0.5
                                spacing 0
                                frame:
                                    xsize 20
                                    ysize 2
                                    background Solid("#f6d79d")
                                    padding (0,0,0,0)
                                null height 2
                                frame:
                                    xsize 2
                                    ysize 16
                                    background Solid("#f6d79d")
                                    padding (0,0,0,0)

                            null width 10

                            ## Center: icon + title
                            hbox:
                                xfill True
                                xalign 0.5
                                yalign 0.5
                                spacing 12
                                text "🔍":
                                    size 24
                                    yalign 0.5
                                vbox:
                                    yalign 0.5
                                    spacing 2
                                    text "DETECTIVE NOTEBOOK":
                                        size 16
                                        color "#f6d79d"
                                        bold True
                                        outlines [(1, "#1a0a0e", 0, 0)]
                                    text "Field Notes — Day 1  ·  Miagao, Iloilo":
                                        size 11
                                        color "#c89218cc"
                                        italic True

                            null width 10

                            ## Right L-bracket accent (mirrored)
                            vbox:
                                yalign 0.5
                                xalign 1.0
                                spacing 0
                                frame:
                                    xsize 20
                                    ysize 2
                                    xalign 1.0
                                    background Solid("#f6d79d")
                                    padding (0,0,0,0)
                                null height 2
                                frame:
                                    xsize 2
                                    ysize 16
                                    xalign 1.0
                                    background Solid("#f6d79d")
                                    padding (0,0,0,0)

                    ## Gold separator
                    frame:
                        xfill True
                        ysize 1
                        background Solid("#f6d79d44")
                        padding (0,0,0,0)

                    ## ── Instruction strip ──────────────────────────────────────
                    frame:
                        background Solid("#1e0c10")
                        xfill True
                        padding (28, 10, 28, 10)
                        hbox:
                            spacing 8
                            yalign 0.5
                            text "◈":
                                size 10
                                color "#c89218"
                                yalign 0.5
                            text "Talk to every local — each one holds a clue.":
                                size 12
                                color "#c89218cc"
                                italic True
                                yalign 0.5
                            text "◈":
                                size 10
                                color "#c89218"
                                yalign 0.5

                    ## Gold separator
                    frame:
                        xfill True
                        ysize 1
                        background Solid("#f6d79d22")
                        padding (0,0,0,0)

                    ## ── Questions list ─────────────────────────────────────────
                    frame:
                        background Solid("#130609")
                        xfill True
                        padding (24, 18, 24, 18)

                        vbox:
                            spacing 8

                            python:
                                _nb_total = len(notebook_questions)

                            for _nb_i in range(_nb_total):
                                python:
                                    _nb_q    = notebook_questions[_nb_i]
                                    _nb_icon = _nb_icons[_nb_i] if _nb_i < len(_nb_icons) else "📌"
                                    _nb_num  = str(_nb_i + 1)

                                ## Question card
                                frame:
                                    background Solid("#1e0a10")
                                    xfill True
                                    padding (0, 0, 0, 0)

                                    hbox:
                                        spacing 0
                                        xfill True

                                        ## Left accent stripe
                                        frame:
                                            xsize 4
                                            ysize 52
                                            background Solid("#f6d79d66")
                                            padding (0,0,0,0)

                                        ## Number badge
                                        frame:
                                            xsize 36
                                            ysize 52
                                            background Solid("#2a0e0e")
                                            padding (0,0,0,0)
                                            text _nb_num:
                                                xalign 0.5
                                                yalign 0.5
                                                size 13
                                                color "#f6d79d66"
                                                bold True

                                        ## Emoji
                                        frame:
                                            xsize 44
                                            ysize 52
                                            background Solid("#00000000")
                                            padding (0,0,0,0)
                                            text _nb_icon:
                                                xalign 0.5
                                                yalign 0.5
                                                size 20

                                        ## Question text + status
                                        frame:
                                            xfill True
                                            ysize 52
                                            background Solid("#00000000")
                                            padding (0, 0, 16, 0)
                                            vbox:
                                                yalign 0.5
                                                spacing 3
                                                text _nb_q.text:
                                                    size 13
                                                    color "#f1debf"
                                                    outlines [(1, "#1a0a0e", 0, 0)]
                                                text "● not yet discovered":
                                                    substitute False
                                                    size 10
                                                    color "#f6d79d33"
                                                    italic True

                    ## Gold separator
                    frame:
                        xfill True
                        ysize 1
                        background Solid("#f6d79d44")
                        padding (0,0,0,0)

                    ## ── Footer ─────────────────────────────────────────────────
                    frame:
                        background Solid("#2a0e0e")
                        xfill True
                        padding (28, 14, 28, 14)

                        hbox:
                            xfill True
                            yalign 0.5

                            text "[_nb_total] questions to solve":
                                size 11
                                color "#f6d79d55"
                                yalign 0.5

                            textbutton "Begin Exploring  →":
                                xalign 1.0
                                style "notebook_btn"
                                action Return()

style notebook_btn:
    background "#5c1a1a"
    hover_background "#7a2020"
    padding (28, 11, 28, 11)

style notebook_btn_text:
    color "#f6d79d"
    hover_color "#ffd700"
    size 13
    bold True
    outlines [(1, "#1a0a0e", 0, 0)]

## ----------------------------------------------------------------------------
## SCREEN: ITEM PICKUP NOTIFICATION
## Brief flash when player receives an info item
## ----------------------------------------------------------------------------

screen item_pickup_screen(item):
    zorder 300
    modal False

    ## Outer glow border - same triple-frame as other UI panels
    frame:
        xalign 0.5
        yalign 0.0
        yoffset 24
        padding (3, 3, 3, 3)
        background Frame(Solid("#f6d79d55"), 0, 0)
        at item_pickup_anim

        frame:
            padding (2, 2, 2, 2)
            background Frame(Solid("#c8921833"), 0, 0)

            frame:
                padding (0, 0, 0, 0)
                background Solid("#1a0a0ef2")

                hbox:
                    spacing 0

                    ## Gold left accent bar
                    frame:
                        xsize 4
                        ysize 62
                        background Solid("#ffd700")
                        padding (0, 0, 0, 0)

                    ## Content
                    frame:
                        padding (16, 14, 20, 14)
                        background Solid("#00000000")
                        hbox:
                            spacing 14
                            yalign 0.5

                            ## Icon badge
                            frame:
                                xysize (38, 38)
                                yalign 0.5
                                background Solid("#3c1a28")
                                text item.icon size 20 xalign 0.5 yalign 0.5

                            ## Text block
                            vbox:
                                spacing 4
                                yalign 0.5

                                ## Label row
                                hbox:
                                    spacing 6
                                    yalign 0.5
                                    frame:
                                        xsize 3
                                        ysize 10
                                        yalign 0.5
                                        background Solid("#ffd700")
                                        padding (0, 0, 0, 0)
                                    text "\u2605  INFO ITEM COLLECTED" size 9 color "#c89218" bold True yalign 0.5

                                text item.name size 13 color "#ffd700" bold True
                                text item.desc size 11 color "#f1debf88"

transform item_pickup_anim:
    alpha 0.0 yoffset -16
    ease 0.25 alpha 1.0 yoffset 0
    pause 2.2
    ease 0.35 alpha 0.0 yoffset -10

## ----------------------------------------------------------------------------
## SCREEN: INVENTORY (can be toggled, I key)
## ----------------------------------------------------------------------------

screen dictionary_screen():
    modal True
    zorder 150

    # Direct keybindings for closing the dictionary
    key "d" action Hide("dictionary_screen")
    key "game_menu" action Hide("dictionary_screen") # Esc key

    # (Optional: keep these if you want to close other overlays from here)
    key "K_p" action Hide("phone_screen")
    key "K_i" action Hide("inventory_screen")

    add Solid("#0d0406") alpha 0.92

    ## Outer glow border
    frame:
        xalign 0.5
        yalign 0.5
        xsize 836
        padding (4, 4, 4, 4)
        background Frame(Solid("#f6d79d33"), 0, 0)

        frame:
            xfill True
            padding (2, 2, 2, 2)
            background Frame(Solid("#c8921822"), 0, 0)

            frame:
                xfill True
                padding (0, 0, 0, 0)
                background Solid("#1a0a0ef8")

                vbox:
                    spacing 0

                    ## Header
                    frame:
                        background Solid("#2a0e0e")
                        xfill True
                        padding (24, 14, 24, 14)
                        hbox:
                            xfill True
                            yalign 0.5
                            vbox:
                                spacing 3
                                hbox:
                                    spacing 8
                                    text "📖" size 15 yalign 0.5
                                    text "FRESHMAN DICTIONARY" size 15 color "#ffd700" bold True yalign 0.5
                                text "Words and terms collected from the locals of Miagao" size 10 color "#c8921888" italic True
                            frame:
                                xalign 1.0
                                yalign 0.5
                                background Solid("#1a0a0e")
                                padding (12, 6, 12, 6)
                                text "[len(collected_items)] entries" size 12 color "#ffd700" bold True

                    ## Progress bar
                    frame:
                        background Solid("#130609")
                        xfill True
                        ysize 3
                        padding (0, 0, 0, 0)

                    ## Content area — 2-column scrollable grid
                    frame:
                        background Solid("#0d0406")
                        xfill True
                        padding (0, 0, 0, 0)

                        if len(collected_items) == 0:
                            frame:
                                background Solid("#00000000")
                                xfill True
                                ysize 440
                                padding (0, 0, 0, 0)
                                vbox:
                                    xalign 0.5
                                    yalign 0.5
                                    spacing 12
                                    text "📜" size 44 xalign 0.5
                                    text "No entries yet." size 16 color "#f6d79d" bold True xalign 0.5
                                    text "Talk to locals around Miagao to\ncollect words and knowledge." size 12 color "#c8921888" italic True xalign 0.5 text_align 0.5
                        else:
                            viewport:
                                xfill True
                                ysize 440
                                mousewheel True
                                draggable True
                                scrollbars "vertical"

                                vbox:
                                    xfill True
                                    spacing 0
                                    xmaximum 800

                                    python:
                                        _inv_pairs = []
                                        for _ii in range(0, len(collected_items), 2):
                                            _inv_pairs.append(collected_items[_ii:_ii+2])

                                    for _row in _inv_pairs:
                                        hbox:
                                            xfill True
                                            spacing 0

                                            for _itm in _row:
                                                frame:
                                                    xsize 400
                                                    padding (22, 16, 22, 16)
                                                    background Solid("#00000000")

                                                    vbox:
                                                        xfill True
                                                        spacing 6

                                                        ## Term header
                                                        hbox:
                                                            spacing 10
                                                            yalign 0.5
                                                            frame:
                                                                xysize (32, 32) yalign 0.5
                                                                background Solid("#3c1a28")
                                                                text _itm.icon size 16 xalign 0.5 yalign 0.5
                                                            vbox:
                                                                spacing 2
                                                                text _itm.name size 14 color "#ffd700" bold True
                                                                text "— " + _itm.act size 10 color "#c8921888" italic True

                                                        ## Definition
                                                        text _itm.desc size 12 color "#f1debf" line_spacing 3

                                                        ## Bottom rule
                                                        null height 4
                                                        frame:
                                                            background Solid("#f6d79d22")
                                                            xfill True
                                                            ysize 1
                                                            padding (0, 0, 0, 0)

                                            ## Pad right cell if odd number
                                            if len(_row) == 1:
                                                frame:
                                                    xsize 400
                                                    padding (0, 0, 0, 0)
                                                    background Solid("#00000000")

                                    ## Vertical divider between columns
                                    ## (done via inner frame xsize 400 above)

                    ## Divider
                    frame:
                        background Solid("#f6d79d22")
                        xfill True
                        ysize 1
                        padding (0, 0, 0, 0)

                    ## Footer
                    frame:
                        background Solid("#2a0e0e")
                        xfill True
                        padding (20, 10, 20, 10)
                        hbox:
                            xfill True
                            yalign 0.5
                            hbox:
                                spacing 20
                                yalign 0.5
                                text "[[I]] / [[D]] / [[ESC]] — Close" substitute False size 10 color "#f6d79d55" italic True yalign 0.5
                                text "Scroll with mouse wheel" size 10 color "#f6d79d33" italic True yalign 0.5

style inv_enc_btn:
    background "#5c1a1a"
    hover_background "#7c2222"
    padding (14, 7, 14, 7)

style inv_enc_btn_text:
    color "#f6d79d"
    hover_color "#ffd700"
    size 11
    bold True

## ----------------------------------------------------------------------------
## SCREEN: ENCYCLOPEDIA — Detailed knowledge book, organised by NPC source
## Key: E (on map or from inventory)
## ----------------------------------------------------------------------------

screen encyclopedia_screen():
    modal True
    zorder 155

    key "K_e" action Hide("encyclopedia_screen")
    key "K_ESCAPE" action Hide("encyclopedia_screen")

    default enc_selected = ""

    add Solid("#0d0406") alpha 0.92

    python:
        _enc_order = [
            ## Act 1 — Arrival in Miagao
            "Jaden", "Manong Josh", "Aleng Maria", "Manong Chris", "Tol Joseph",
            ## Act 2 — Entering the University
            "Ate Bea", "Kuya Mark", "Ma'am Reyes",
            ## Act 3 — Enrollment
            "Sir Noel",
            ## Act 4 — Dorm Life
            "Dorm Manager",
            ## Act 5 — First Day of Classes
            "Prof. Lena", "Kuya Rico", "Ate Grace", "Dan",
            ## Act 6 — Org Fair & Campus Life
            "Mika", "Kuya Tomas", "Ate Jenny", "Coach Ramon",
            ## Act 7 — Library & Academic Resources
            "Ate Rosa", "Kuya Neil", "Prof. Santos", "Bea",
            ## Act 8 — Finding Your Place
            "Nanay Elena", "Prof. Reyes",
        ]
        _enc_has   = [s for s in _enc_order if any(i.act == s for i in collected_items)]
        _enc_extra = [s for s in dict.fromkeys(i.act for i in collected_items) if s not in _enc_order]
        _enc_srcs  = _enc_has + _enc_extra

        _enc_meta = {
            ## Act 1
            "Jaden":        ("🎒", "Fellow freshie from Iloilo City with UPV tips."),
            "Manong Josh":  ("🏘️", "Long-time Miagao local who knows every corner."),
            "Aleng Maria":  ("🍚", "Carinderia owner near the UPV gate — feeds half the campus."),
            "Manong Chris": ("🙏", "Born-and-raised Miagaoanon fluent in Kinaray-a."),
            "Tol Joseph":   ("🛺", "The tricycle driver who knows every route and fare."),
            ## Act 2
            "Ate Bea":      ("🎓", "Senior student volunteer at the BOX 1 entrance — freshie lifesaver."),
            "Kuya Mark":    ("🛡️", "Campus security officer who knows every rule on campus."),
            "Ma'am Reyes":  ("📋", "Administrative staff at New Admin who handles office directory queries."),
            ## Act 3
            "Sir Noel":     ("💻", "Faculty enrollment adviser who walks freshmen through CRS and scheduling."),
            ## Act 4
            "Dorm Manager": ("🏠", "The dormitory manager who handles check-in, rules, and room assignments."),
            ## Act 5
            "Prof. Lena":   ("📊", "Professor who explains the UP grading system on the first day of class."),
            "Kuya Rico":    ("📅", "Upperclassman who knows the MAO policy and campus building layout."),
            "Ate Grace":    ("⚖️", "OSA student assistant knowledgeable about student rights."),
            "Dan":          ("📚", "Classmate and study-tips enthusiast with a surprisingly organized planner."),
            ## Act 6
            "Mika":         ("🌿", "Org leader at the fair who explains org culture and anti-hazing laws."),
            "Kuya Tomas":   ("💰", "Scholarship upperclassman with practical advice on grants and STFAP."),
            "Ate Jenny":    ("🗓️", "OSA student rep who knows every UPV campus event by heart."),
            "Coach Ramon":  ("🏅", "Sports coordinator and long-time UPV athletics coach."),
            ## Act 7
            "Ate Rosa":     ("📖", "Friendly librarian at the Diwata Library — knows every resource on campus."),
            "Kuya Neil":    ("🖥️", "Computer lab technician who manages student access and printing."),
            "Prof. Santos": ("🔬", "Research professor who explains UP's three mandates and research culture."),
            "Bea":          ("📝", "Classmate and APA citation guru — already on her second coffee of the day."),
            ## Act 8
            "Nanay Elena":  ("🎒", "Veteran dormer who gives freshmen the real survival kit list."),
            "Prof. Reyes":  ("🏅", "Professor who embodies the meaning of UP's Honor and Excellence motto."),
        }

    ## Outer glow border
    frame:
        xalign 0.5
        yalign 0.5
        xsize 916
        padding (4, 4, 4, 4)
        background Frame(Solid("#f6d79d33"), 0, 0)

        frame:
            xfill True
            padding (2, 2, 2, 2)
            background Frame(Solid("#c8921822"), 0, 0)

            frame:
                xfill True
                padding (0, 0, 0, 0)
                background Solid("#1a0a0ef8")

                vbox:
                    spacing 0

                    ## Header
                    frame:
                        background Solid("#2a0e0e")
                        xfill True
                        padding (24, 14, 24, 14)
                        hbox:
                            xfill True
                            yalign 0.5
                            vbox:
                                spacing 3
                                hbox:
                                    spacing 8
                                    text "📚" size 15 yalign 0.5
                                    text "MIAGAO FRESHMAN ENCYCLOPEDIA" size 15 color "#ffd700" bold True yalign 0.5
                                text "Complete knowledge gathered from the locals" size 10 color "#c8921888" italic True
                            frame:
                                xalign 1.0
                                yalign 0.5
                                background Solid("#1a0a0e")
                                padding (12, 6, 12, 6)
                                text "[len(collected_items)] entries" size 12 color "#ffd700" bold True

                    ## Body: sidebar + content
                    hbox:
                        spacing 0

                        ## ── Sidebar / TOC ──────────────────────────────────────
                        frame:
                            xsize 218
                            ysize 502
                            background Solid("#130609")
                            padding (0, 0, 0, 0)

                            vbox:
                                spacing 0

                                ## Sidebar heading
                                frame:
                                    background Solid("#2a0e0e")
                                    xfill True
                                    padding (16, 10, 16, 10)
                                    hbox:
                                        spacing 6
                                        yalign 0.5
                                        frame:
                                            xsize 3
                                            ysize 12
                                            yalign 0.5
                                            background Solid("#ffd700")
                                            padding (0, 0, 0, 0)
                                        text "SOURCES" size 10 color "#ffd700" bold True yalign 0.5

                                if len(_enc_srcs) == 0:
                                    frame:
                                        background Solid("#00000000")
                                        xfill True
                                        padding (16, 24, 16, 24)
                                        vbox:
                                            spacing 8
                                            xalign 0.5
                                            text "📜" size 28 xalign 0.5
                                            text "Talk to locals to\nunlock chapters." size 11 color "#c8921866" italic True xalign 0.5 text_align 0.5

                                viewport:
                                    xfill True
                                    ysize 462
                                    mousewheel True
                                    draggable True

                                    vbox:
                                        spacing 0
                                        xfill True

                                        for _esrc in _enc_srcs:
                                            python:
                                                _emeta  = _enc_meta.get(_esrc, ("📄", "A local source."))
                                                _ecount = len([i for i in collected_items if i.act == _esrc])
                                                _eword  = "entry" if _ecount == 1 else "entries"
                                                _eact   = (enc_selected == _esrc)

                                            button:
                                                xfill True
                                                background Solid("#3c1a28" if _eact else "#00000000")
                                                hover_background Solid("#2a0e1a")
                                                padding (14, 12, 14, 12)
                                                action SetScreenVariable("enc_selected", _esrc)
                                                hbox:
                                                    spacing 10
                                                    yalign 0.5
                                                    ## Active indicator bar
                                                    frame:
                                                        xsize 3
                                                        ysize 30
                                                        yalign 0.5
                                                        background Solid("#ffd700" if _eact else "#00000000")
                                                        padding (0, 0, 0, 0)
                                                    frame:
                                                        xysize (28, 28) yalign 0.5
                                                        background Solid("#2a0e0e" if _eact else "#1e0a10")
                                                        text _emeta[0] size 14 xalign 0.5 yalign 0.5
                                                    vbox:
                                                        spacing 2
                                                        text _esrc size 12 color ("#ffd700" if _eact else "#f1debf") bold True
                                                        text "[_ecount] [_eword]" size 9 color "#c8921866"

                                            frame:
                                                background Solid("#f6d79d11")
                                                xfill True
                                                ysize 1
                                                padding (0, 0, 0, 0)

                        ## Gold spine
                        frame:
                            xsize 2
                            ysize 502
                            background Solid("#ffd70044")
                            padding (0, 0, 0, 0)

                        ## ── Content panel ──────────────────────────────────────
                        frame:
                            xfill True
                            ysize 502
                            background Solid("#0d0406")
                            padding (0, 0, 0, 0)

                            if enc_selected == "":
                                ## Empty state
                                frame:
                                    xfill True
                                    ysize 502
                                    background Solid("#00000000")
                                    vbox:
                                        xalign 0.5
                                        yalign 0.5
                                        spacing 14
                                        text "📚" size 52 xalign 0.5
                                        text "Select a Source" size 18 color "#ffd700" bold True xalign 0.5
                                        text "Choose someone from the left panel\nto read the knowledge you've gathered." size 12 color "#c8921888" italic True xalign 0.5 text_align 0.5

                            else:
                                python:
                                    _eitems  = [i for i in collected_items if i.act == enc_selected]
                                    _echmeta = _enc_meta.get(enc_selected, ("📄", "Information gathered from a local."))

                                vbox:
                                    spacing 0

                                    ## Chapter header
                                    frame:
                                        background Solid("#2a0e0e")
                                        xfill True
                                        padding (20, 14, 20, 14)
                                        hbox:
                                            spacing 14
                                            yalign 0.5
                                            frame:
                                                xysize (40, 40) yalign 0.5
                                                background Solid("#3c1a28")
                                                text _echmeta[0] size 22 xalign 0.5 yalign 0.5
                                            vbox:
                                                spacing 3
                                                yalign 0.5
                                                text enc_selected size 16 color "#ffd700" bold True
                                                text _echmeta[1] size 11 color "#c8921888" italic True

                                    ## Scrollable entries
                                    viewport:
                                        xfill True
                                        ysize 448
                                        scrollbars "vertical"
                                        mousewheel True
                                        yinitial 0.0

                                        vbox:
                                            xfill True
                                            spacing 0
                                            xmaximum 800

                                            for _eitem in _eitems:
                                                frame:
                                                    xfill True
                                                    background Solid("#00000000")
                                                    padding (22, 14, 22, 14)

                                                    vbox:
                                                        xfill True
                                                        spacing 8

                                                        ## Entry title row
                                                        hbox:
                                                            spacing 10
                                                            yalign 0.5
                                                            frame:
                                                                xysize (30, 30) yalign 0.5
                                                                background Solid("#3c1a28")
                                                                text _eitem.icon size 15 xalign 0.5 yalign 0.5
                                                            text _eitem.name size 15 color "#ffd700" bold True yalign 0.5

                                                        ## Short desc
                                                        text _eitem.desc size 13 color "#f1debf" line_spacing 3

                                                        ## Long desc (if different)
                                                        if _eitem.full and _eitem.full != _eitem.desc:
                                                            frame:
                                                                background Solid("#2a0e0e")
                                                                xfill True
                                                                padding (14, 10, 14, 10)
                                                                hbox:
                                                                    spacing 10
                                                                    yalign 0.5
                                                                    frame:
                                                                        xsize 2
                                                                        ysize 40
                                                                        yalign 0.5
                                                                        background Solid("#c89218")
                                                                        padding (0, 0, 0, 0)
                                                                    text _eitem.full size 12 color "#f6d79d" line_spacing 3

                                                        ## Divider
                                                        frame:
                                                            background Solid("#f6d79d1a")
                                                            xfill True
                                                            ysize 1
                                                            padding (0, 0, 0, 0)

                    ## Footer
                    frame:
                        background Solid("#2a0e0e")
                        xfill True
                        padding (20, 10, 20, 10)
                        hbox:
                            xfill True
                            yalign 0.5
                            hbox:
                                spacing 20
                                yalign 0.5
                                text "[[E]] / [[ESC]] — Close" substitute False size 10 color "#f6d79d55" italic True yalign 0.5
                                text "Scroll with mouse wheel" size 10 color "#f6d79d33" italic True yalign 0.5

## ----------------------------------------------------------------------------
## SCREEN: QUIZ MINIGAME
## Player drags/selects items to answer notebook questions
## ----------------------------------------------------------------------------

screen quiz_screen():
    modal True
    zorder 200

    add Solid("#0d0406") alpha 0.98

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
        q         = notebook_questions[state["current_q"]]
        total_q   = len(notebook_questions)
        items     = collected_items[:]
        _q_icons  = ["🛺", "🍚", "🗣️", "🏛️", "📋", "🏘️"]
        _q_icon   = _q_icons[state["current_q"]] if state["current_q"] < len(_q_icons) else "📌"
        _progress = state["current_q"] + 1
        _pct_done = int((_progress / total_q) * 100)

    ## ── Full-screen vignette ───────────────────────────────────────────────────
    ## Outer border glow — double ring
    frame:
        xalign 0.5
        yalign 0.5
        xsize 960
        padding (4, 4, 4, 4)
        background Frame(Solid("#f6d79d44"), 0, 0)

        frame:
            xfill True
            padding (2, 2, 2, 2)
            background Frame(Solid("#c8921822"), 0, 0)

            frame:
                xfill True
                padding (0, 0, 0, 0)
                background Solid("#1a0a0ef8")

                vbox:
                    spacing 0

                    ## ── TOP HEADER BAR ────────────────────────────────────────
                    frame:
                        background Solid("#2a0e0e")
                        xfill True
                        padding (20, 12, 20, 12)

                        hbox:
                            xfill True
                            yalign 0.5
                            spacing 0

                            ## Left: title block
                            vbox:
                                yalign 0.5
                                spacing 2
                                hbox:
                                    spacing 8
                                    text "🔍":
                                        size 14
                                        yalign 0.5
                                    text "DETECTIVE NOTEBOOK  —  FINAL QUIZ":
                                        size 13
                                        color "#f6d79d"
                                        bold True
                                        outlines [(1, "#1a0a0e", 0, 0)]
                                        yalign 0.5
                                text "Review what you've learned from the locals of Miagao":
                                    size 10
                                    color "#c89218aa"
                                    italic True

                            ## Right: score badge
                            frame:
                                xalign 1.0
                                yalign 0.5
                                background Solid("#1a0a0e")
                                padding (14, 6, 14, 6)
                                hbox:
                                    spacing 6
                                    yalign 0.5
                                    text "SCORE":
                                        size 9
                                        color "#f6d79d88"
                                        bold True
                                        yalign 0.5
                                    text "[state['score']]/[total_q]":
                                        size 16
                                        color "#ffd700"
                                        bold True
                                        outlines [(1, "#1a0a0e", 0, 0)]
                                        yalign 0.5

                    ## ── PROGRESS TRACK ────────────────────────────────────────
                    frame:
                        background Solid("#130609")
                        xfill True
                        padding (20, 10, 20, 10)

                        hbox:
                            xfill True
                            yalign 0.5
                            spacing 12

                            ## Step pips
                            hbox:
                                spacing 6
                                yalign 0.5
                                for _pi in range(total_q):
                                    python:
                                        if _pi < state["current_q"]:
                                            _pip_bg = "#f6d79d"
                                            _pip_sz = 10
                                        elif _pi == state["current_q"]:
                                            _pip_bg = "#ffd700"
                                            _pip_sz = 14
                                        else:
                                            _pip_bg = "#f6d79d22"
                                            _pip_sz = 10
                                    frame:
                                        xsize _pip_sz
                                        ysize _pip_sz
                                        yalign 0.5
                                        background Solid(_pip_bg)
                                        padding (0,0,0,0)
                                    if _pi < total_q - 1:
                                        frame:
                                            xsize 20
                                            ysize 1
                                            yalign 0.5
                                            background Solid("#f6d79d22")
                                            padding (0,0,0,0)

                            text "Question [_progress] of [total_q]":
                                xalign 1.0
                                size 11
                                color "#f6d79d88"
                                yalign 0.5

                    ## Gold rule
                    frame:
                        xfill True
                        ysize 1
                        background Solid("#f6d79d33")
                        padding (0,0,0,0)

                    ## ── MAIN BODY: two-panel layout ───────────────────────────
                    hbox:
                        xfill True
                        spacing 0

                        ## LEFT PANEL — Case file / question ─────────────────────
                        frame:
                            xsize 340
                            ysize 340
                            background Solid("#130609")
                            padding (0, 0, 0, 0)

                            vbox:
                                spacing 0
                                xfill True

                                ## Case number stamp
                                frame:
                                    background Solid("#1e0a10")
                                    xfill True
                                    padding (20, 10, 20, 10)
                                    hbox:
                                        spacing 10
                                        yalign 0.5
                                        frame:
                                            xsize 2
                                            ysize 28
                                            background Solid("#f6d79d")
                                            padding (0,0,0,0)
                                        vbox:
                                            yalign 0.5
                                            spacing 1
                                            text "CASE  #0[_progress]":
                                                size 9
                                                color "#f6d79d88"
                                                bold True
                                                outlines [(1, "#1a0a0e", 0, 0)]
                                            text "OPEN FOR REVIEW":
                                                size 9
                                                color "#c89218aa"
                                                italic True

                                ## Big emoji
                                frame:
                                    background Solid("#130609")
                                    xfill True
                                    padding (20, 20, 20, 8)
                                    text _q_icon:
                                        xalign 0.5
                                        size 56

                                ## Question text
                                frame:
                                    background Solid("#130609")
                                    xfill True
                                    padding (24, 8, 24, 16)
                                    vbox:
                                        spacing 6
                                        text "THE QUESTION":
                                            size 9
                                            color "#c89218"
                                            bold True
                                            outlines [(1, "#1a0a0e", 0, 0)]
                                        text q.text:
                                            size 15
                                            color "#f1debf"
                                            bold True
                                            outlines [(2, "#1a0a0e", 0, 0)]
                                            line_spacing 4

                                ## Feedback banner
                                if state["feedback"] == "correct":
                                    frame:
                                        background Solid("#0d2e1a")
                                        xfill True
                                        padding (20, 10, 20, 10)
                                        hbox:
                                            spacing 8
                                            yalign 0.5
                                            text "✓":
                                                size 18
                                                color "#b8e6b0"
                                                bold True
                                                yalign 0.5
                                            vbox:
                                                yalign 0.5
                                                spacing 1
                                                text "Correct!":
                                                    size 12
                                                    color "#b8e6b0"
                                                    bold True
                                                text "Good detective work.":
                                                    size 10
                                                    color "#b8e6b0aa"
                                                    italic True

                                elif state["feedback"] == "wrong":
                                    frame:
                                        background Solid("#2e0a0a")
                                        xfill True
                                        padding (20, 10, 20, 10)
                                        hbox:
                                            spacing 8
                                            yalign 0.5
                                            text "✗":
                                                size 18
                                                color "#f87171"
                                                bold True
                                                yalign 0.5
                                            vbox:
                                                yalign 0.5
                                                spacing 1
                                                text "Not quite.":
                                                    size 12
                                                    color "#f87171"
                                                    bold True
                                                text "Hint: [q.hint]":
                                                    size 10
                                                    color "#f8717188"
                                                    italic True

                                elif state["feedback"] is None:
                                    frame:
                                        background Solid("#1e0a10")
                                        xfill True
                                        padding (20, 10, 20, 10)
                                        text "Pick the clue that answers this.":
                                            size 10
                                            color "#f6d79d55"
                                            italic True
                                            xalign 0.5

                        ## Vertical divider
                        frame:
                            xsize 1
                            ysize 340
                            background Solid("#f6d79d22")
                            padding (0,0,0,0)

                        ## RIGHT PANEL — Evidence items ──────────────────────────
                        frame:
                            xfill True
                            ysize 340
                            background Solid("#1a0a0e")
                            padding (14, 14, 14, 14)

                            vbox:
                                spacing 8
                                xfill True

                                ## Section label
                                hbox:
                                    spacing 8
                                    yalign 0.5
                                    frame:
                                        xsize 3
                                        ysize 14
                                        yalign 0.5
                                        background Solid("#f6d79d")
                                        padding (0,0,0,0)
                                    text "EVIDENCE COLLECTED":
                                        size 10
                                        color "#f6d79d88"
                                        bold True
                                        yalign 0.5
                                        outlines [(1, "#1a0a0e", 0, 0)]

                                ## Evidence grid
                                viewport:
                                    id "evidence_vp"
                                    xfill True
                                    ysize 268
                                    mousewheel True
                                    draggable True
                                    scrollbars "vertical"

                                    frame:
                                        background None
                                        padding (0, 0, 16, 0)

                                        vpgrid:
                                            cols 2
                                            xfill True
                                            spacing 6

                                            for item in items:
                                                python:
                                                    is_chosen  = (state["chosen"] == item.item_id)
                                                    card_bg    = "#2e1810" if is_chosen else "#130609"
                                                    tab_col    = "#ffd700" if is_chosen else "#f6d79d33"
                                                    lbl_col    = "#ffd700" if is_chosen else "#f1debf"
                                                    src_col    = "#f6d79daa" if is_chosen else "#f6d79d44"

                                                button:
                                                    background card_bg
                                                    hover_background "#1e0c10"
                                                    xfill True
                                                    padding (0, 0, 0, 0)
                                                    if state["feedback"] is None:
                                                        action SetDict(state, "chosen", item.item_id)
                                                    else:
                                                        action NullAction()

                                                    hbox:
                                                        spacing 0
                                                        xfill True

                                                        ## Selection tab
                                                        frame:
                                                            xsize 3
                                                            ysize 56
                                                            background Solid(tab_col)
                                                            padding (0,0,0,0)

                                                        frame:
                                                            xfill True
                                                            padding (10, 8, 10, 8)
                                                            background Solid("#00000000")

                                                            vbox:
                                                                spacing 2
                                                                xfill True

                                                                hbox:
                                                                    spacing 6
                                                                    yalign 0.5
                                                                    text item.icon:
                                                                        size 16
                                                                        yalign 0.5
                                                                    text item.name:
                                                                        size 12
                                                                        color lbl_col
                                                                        bold True
                                                                        outlines [(1, "#1a0a0e", 0, 0)]
                                                                        yalign 0.5

                                                                text item.desc:
                                                                    size 9
                                                                    color src_col
                                                                    line_spacing 2

                    ## Gold rule
                    frame:
                        xfill True
                        ysize 1
                        background Solid("#f6d79d33")
                        padding (0,0,0,0)

                    ## ── ACTION BAR ────────────────────────────────────────────
                    frame:
                        background Solid("#2a0e0e")
                        xfill True
                        padding (24, 14, 24, 14)

                        hbox:
                            xfill True
                            yalign 0.5
                            spacing 0

                            ## Left: hint text
                            if state["feedback"] is None:
                                if state["chosen"] is None:
                                    text "← Select a piece of evidence from the right panel":
                                        size 11
                                        color "#f6d79d44"
                                        italic True
                                        yalign 0.5
                                else:
                                    text "Evidence selected — confirm when ready":
                                        size 11
                                        color "#c89218cc"
                                        italic True
                                        yalign 0.5
                            else:
                                text "":
                                    size 11

                            ## Right: action button
                            if state["feedback"] is None:
                                textbutton "Confirm Answer  →":
                                    xalign 1.0
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
                                    _btn_lbl = "Next Question  →" if state["current_q"] < total_q - 1 else "Close the Case  ✓"

                                textbutton _btn_lbl:
                                    xalign 1.0
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
    background "#5c1a1a"
    hover_background "#7a2020"
    insensitive_background "#2a1010"
    padding (32, 11, 32, 11)

style quiz_btn_text:
    color "#f6d79d"
    hover_color "#ffd700"
    insensitive_color "#f6d79d44"
    size 13
    bold True
    outlines [(1, "#1a0a0e", 0, 0)]

## ----------------------------------------------------------------------------
## SCREEN: QUIZ RESULTS
## ----------------------------------------------------------------------------

screen quiz_results_screen(score):
    modal True
    zorder 200

    add Solid("#0d0406") alpha 0.96

    python:
        _r_icons = ["🛺", "🍚", "🗣️", "🏛️", "📋", "🏘️"]

    frame:
        xalign 0.5
        yalign 0.5
        xsize 680
        padding (4, 4, 4, 4)
        background Frame(Solid("#f6d79d44"), 0, 0)

        frame:
            xfill True
            padding (2, 2, 2, 2)
            background Frame(Solid("#c8921822"), 0, 0)

            frame:
                xfill True
                padding (0, 0, 0, 0)
                background Solid("#1a0a0ef8")

                vbox:
                    spacing 0

                    ## ── VERDICT HEADER ───────────────────────────────────────
                    frame:
                        background Solid("#2a0e0e")
                        xfill True
                        padding (28, 20, 28, 20)

                        vbox:
                            spacing 0
                            xalign 0.5

                            ## Top ornament
                            hbox:
                                xalign 0.5
                                spacing 6
                                frame:
                                    xsize 60
                                    ysize 1
                                    yalign 0.5
                                    background Solid("#f6d79d55")
                                    padding (0,0,0,0)
                                frame:
                                    xsize 6
                                    ysize 6
                                    yalign 0.5
                                    background Solid("#f6d79d")
                                    padding (0,0,0,0)
                                frame:
                                    xsize 60
                                    ysize 1
                                    yalign 0.5
                                    background Solid("#f6d79d55")
                                    padding (0,0,0,0)

                            null height 14

                            text "🔍  CASE CLOSED":
                                size 22
                                color "#f6d79d"
                                bold True
                                xalign 0.5
                                outlines [(2, "#1a0a0e", 0, 0)]

                            null height 14

                            python:
                                total   = len(notebook_questions)
                                total_q = total
                                pct     = int((score / total) * 100)
                                stars   = "★★★" if pct == 100 else "★★☆" if pct >= 66 else "★☆☆"
                                if pct == 100:
                                    grade   = "PERFECT DETECTIVE"
                                    g_color = "#b8e6b0"
                                    g_msg   = "Miagao holds no secrets from you."
                                elif pct >= 66:
                                    grade   = "GOOD INSTINCTS"
                                    g_color = "#ffd700"
                                    g_msg   = "Solid work. A few gaps — you'll fill them in time."
                                else:
                                    grade   = "STILL LEARNING"
                                    g_color = "#f87171"
                                    g_msg   = "You missed some locals. Their knowledge would have helped."

                            ## Score block
                            frame:
                                xalign 0.5
                                background Solid("#1a0a0e")
                                padding (28, 14, 28, 14)

                                vbox:
                                    spacing 6
                                    xalign 0.5

                                    text stars:
                                        xalign 0.5
                                        size 24
                                        color g_color
                                        outlines [(1, "#1a0a0e", 0, 0)]

                                    text "[score]/[total_q]":
                                        size 48
                                        color g_color
                                        bold True
                                        xalign 0.5
                                        outlines [(3, "#1a0a0e", 0, 0)]

                                    text grade:
                                        size 12
                                        color g_color
                                        bold True
                                        xalign 0.5
                                        outlines [(1, "#1a0a0e", 0, 0)]

                            null height 10

                            text g_msg:
                                size 12
                                color "#f6d79daa"
                                italic True
                                xalign 0.5
                                text_align 0.5

                            null height 14

                            ## Bottom ornament
                            hbox:
                                xalign 0.5
                                spacing 6
                                frame:
                                    xsize 60
                                    ysize 1
                                    yalign 0.5
                                    background Solid("#f6d79d55")
                                    padding (0,0,0,0)
                                frame:
                                    xsize 6
                                    ysize 6
                                    yalign 0.5
                                    background Solid("#f6d79d")
                                    padding (0,0,0,0)
                                frame:
                                    xsize 60
                                    ysize 1
                                    yalign 0.5
                                    background Solid("#f6d79d55")
                                    padding (0,0,0,0)

                    ## Thin rule
                    frame:
                        xfill True
                        ysize 1
                        background Solid("#f6d79d33")
                        padding (0,0,0,0)

                    ## ── QUESTION BREAKDOWN ────────────────────────────────────
                    frame:
                        background Solid("#130609")
                        xfill True
                        padding (20, 16, 20, 16)

                        vbox:
                            spacing 6

                            hbox:
                                spacing 6
                                yalign 0.5
                                frame:
                                    xsize 3
                                    ysize 12
                                    yalign 0.5
                                    background Solid("#f6d79d")
                                    padding (0,0,0,0)
                                text "CASE REVIEW":
                                    size 10
                                    color "#f6d79d88"
                                    bold True
                                    yalign 0.5

                            null height 4

                            for i in range(len(notebook_questions)):
                                python:
                                    q2      = notebook_questions[i]
                                    ok      = q2.answered and (q2.chosen_item_id == q2.correct_item_id)
                                    verdict = "✓" if ok else "✗"
                                    tcol    = "#b8e6b0" if ok else "#f87171"
                                    card_bg = "#0d2e1a" if ok else "#2e0a0a"
                                    r_icon  = _r_icons[i] if i < len(_r_icons) else "📌"

                                frame:
                                    background Solid(card_bg)
                                    xfill True
                                    padding (0, 0, 0, 0)

                                    hbox:
                                        spacing 0
                                        xfill True

                                        ## Verdict stripe
                                        frame:
                                            xsize 3
                                            ysize 40
                                            background Solid(tcol)
                                            padding (0,0,0,0)

                                        ## Emoji
                                        frame:
                                            xsize 40
                                            ysize 40
                                            background Solid("#00000000")
                                            padding (0,0,0,0)
                                            text r_icon:
                                                xalign 0.5
                                                yalign 0.5
                                                size 16

                                        ## Question text
                                        frame:
                                            xfill True
                                            padding (0, 0, 12, 0)
                                            background Solid("#00000000")
                                            hbox:
                                                xfill True
                                                yalign 0.5
                                                spacing 8
                                                text q2.text:
                                                    xfill True
                                                    size 11
                                                    color "#f1debf"
                                                    yalign 0.5
                                                text verdict:
                                                    size 14
                                                    color tcol
                                                    bold True
                                                    yalign 0.5

                    ## Thin rule
                    frame:
                        xfill True
                        ysize 1
                        background Solid("#f6d79d33")
                        padding (0,0,0,0)

                    ## ── FOOTER ────────────────────────────────────────────────
                    frame:
                        background Solid("#2a0e0e")
                        xfill True
                        padding (24, 16, 24, 16)

                        if score >= 4:
                            hbox:
                                xfill True
                                yalign 0.5
                                text "The path ahead is clear.":
                                    size 11
                                    color "#f6d79d55"
                                    italic True
                                    yalign 0.5
                                textbutton "Continue to BOX 1  →":
                                    xalign 1.0
                                    style "notebook_btn"
                                    action Return()
                        else:
                            hbox:
                                xfill True
                                yalign 0.5
                                text "Need 4/6 to proceed. Review the locals' clues.":
                                    size 11
                                    color "#f87171aa"
                                    italic True
                                    yalign 0.5
                                textbutton "Try Again  ↺":
                                    xalign 1.0
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

    add Solid("#0d0406") alpha 0.7

    ## Phone shell — slides in from right side
    frame:
        xalign 0.97
        yalign 0.5
        xsize 310
        ysize 600
        background Solid("#0f0f0f")
        padding (0, 0, 0, 0)

        vbox:
            spacing 0

            ## ── Notch / top bar ─────────────────────────────────────────────
            frame:
                background Solid("#1a0a0e")
                xfill True
                ysize 30
                padding (14, 0, 14, 0)
                hbox:
                    xfill True
                    yalign 0.5
                    text "9:41" size 10 color "#ffd700" bold True yalign 0.5
                    hbox:
                        xalign 1.0
                        yalign 0.5
                        spacing 6
                        text "●●●" size 8 color "#c8921888" yalign 0.5
                        text "WiFi" size 8 color "#c8921888" yalign 0.5
                        text "🔋" size 9 yalign 0.5

            ## ── App title bar ───────────────────────────────────────────────
            frame:
                background Solid("#2a0e0e")
                xfill True
                padding (12, 10, 12, 10)
                hbox:
                    spacing 10
                    xfill True
                    yalign 0.5
                    frame:
                        xysize (32, 32) yalign 0.5
                        background Solid("#5c1a1a")
                        text "🌊" size 16 xalign 0.5 yalign 0.5
                    vbox:
                        spacing 2
                        yalign 0.5
                        text "UPV Freshies 2024" size 12 color "#ffd700" bold True
                        text "Batch [gc_open_count]/[len(gc_messages)]  •  4 members" size 9 color "#c8921888"
                    text "⋮" size 16 color "#c8921866" xalign 1.0 yalign 0.5

            ## Thin gold rule
            frame:
                background Solid("#ffd70033")
                xfill True
                ysize 1
                padding (0, 0, 0, 0)

            ## ── Messages area ───────────────────────────────────────────────
            frame:
                background Solid("#0d0406")
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
                            background Solid("#1a0a0e")
                            xfill True
                            padding (12, 18, 12, 18)
                            vbox:
                                spacing 6
                                xalign 0.5
                                text "💬" size 22 xalign 0.5
                                text "Talk to Jaden to unlock\nthe group chat..." size 11 color "#c8921866" italic True xalign 0.5 text_align 0.5

                    for idx in gc_revealed:
                        python:
                            msg   = gc_messages[idx // 4][idx % 4]
                            align = 1.0 if msg.is_player else 0.0

                        if msg.is_player:
                            ## Player message — right aligned, gold/crimson bubble
                            hbox:
                                xfill True
                                xalign 1.0
                                null width 50
                                frame:
                                    background Solid("#5c1a1a")
                                    padding (10, 8, 10, 8)
                                    text msg.text size 11 color "#f6d79d"

                        else:
                            ## Other member — left aligned with avatar
                            hbox:
                                spacing 6
                                xfill True

                                ## Avatar circle
                                frame:
                                    background Solid(msg.avatar_color)
                                    xsize 28
                                    ysize 28
                                    padding (0, 0, 0, 0)
                                    text msg.sender[0] size 12 color "#ffffff" bold True xalign 0.5 yalign 0.5

                                vbox:
                                    spacing 3
                                    text msg.sender size 9 color "#c89218" bold True
                                    frame:
                                        background Solid("#2a0e0e")
                                        padding (10, 8, 10, 8)
                                        text msg.text size 11 color "#f1debf"

                                null width 40

            ## Thin gold rule
            frame:
                background Solid("#ffd70033")
                xfill True
                ysize 1
                padding (0, 0, 0, 0)

            ## ── Input / Load more bar ───────────────────────────────────────
            frame:
                background Solid("#1a0a0e")
                xfill True
                padding (8, 8, 8, 8)
                vbox:
                    spacing 6

                    if gc_open_count < len(gc_messages):
                        textbutton "Next Batch →  ([gc_open_count + 1]/[len(gc_messages)])":
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
                            background Solid("#2a0e0e")
                            xfill True
                            padding (10, 8, 10, 8)
                            text "Type a message..." size 11 color "#c8921855" italic True
                        frame:
                            background Solid("#5c1a1a")
                            padding (10, 8, 10, 8)
                            text "➤" size 12 color "#ffd700"

            ## ── Close hint ──────────────────────────────────────────────────
            frame:
                background Solid("#0d0406")
                xfill True
                padding (8, 6, 8, 6)
                text "Press [[P]] to put phone away" substitute False size 9 color "#c8921855" italic True xalign 0.5

style gc_load_btn:
    background "#2a0e0e"
    hover_background "#3c1a28"
    padding (16, 6, 16, 6)

style gc_load_btn_text:
    color "#c89218"
    hover_color "#ffd700"
    size 11


## ============================================================================
## FLIP CARD MINI-GAME — Match offices with what they do
## ============================================================================
## Uses a grid of face-down cards. Player flips two at a time.
## If they match (office name ↔ office function), they stay revealed.
## All 6 pairs matched = game complete.
## ============================================================================

init python:

    ## Card pairs: (office_name, office_function)
    FLIP_CARD_PAIRS = [
        ("Registrar", "Enrollment, Transcripts\n& Form 5"),
        ("Cashier's Office", "Payment of Fees\n& Refunds"),
        ("OSA", "Scholarships, Orgs\n& Discipline"),
        ("Chancellor's Office", "Administrative\nLeadership"),
        ("Security Office", "Campus Safety\n& ID Policies"),
        ("Health Services", "Medical Checkups\n& Certificates"),
    ]

    ## Card colors for matched pairs (so each pair gets a distinct color)
    FLIP_CARD_COLORS = [
        "#4a90d9",  ## blue
        "#d94a4a",  ## red
        "#4ad97a",  ## green
        "#d9a04a",  ## orange
        "#9a4ad9",  ## purple
        "#4ad9d9",  ## teal
    ]

    import random as _random

    class FlipCardState:
        def __init__(self):
            self.reset()

        def reset(self):
            ## Build the card deck: 12 cards (6 pairs)
            self.cards = []
            for i, (name, func) in enumerate(FLIP_CARD_PAIRS):
                self.cards.append({
                    "id": i * 2,
                    "pair_id": i,
                    "text": name,
                    "is_name": True,
                    "flipped": False,
                    "matched": False,
                })
                self.cards.append({
                    "id": i * 2 + 1,
                    "pair_id": i,
                    "text": func,
                    "is_name": False,
                    "flipped": False,
                    "matched": False,
                })
            _random.shuffle(self.cards)
            self.first_pick = None
            self.second_pick = None
            self.matches_found = 0
            self.total_pairs = len(FLIP_CARD_PAIRS)
            self.attempts = 0
            self.show_mismatch = False
            self.game_complete = False

        def flip_card(self, card_idx):
            """Handle flipping a card."""
            card = self.cards[card_idx]

            ## Ignore if already matched or flipped
            if card["matched"] or card["flipped"]:
                return

            ## Ignore if two cards already shown (waiting for reset)
            if self.first_pick is not None and self.second_pick is not None:
                return

            card["flipped"] = True

            if self.first_pick is None:
                self.first_pick = card_idx
            else:
                self.second_pick = card_idx
                self.attempts += 1
                self._check_match()

        def _check_match(self):
            """Check if the two flipped cards match."""
            c1 = self.cards[self.first_pick]
            c2 = self.cards[self.second_pick]

            if c1["pair_id"] == c2["pair_id"]:
                ## Match found!
                c1["matched"] = True
                c2["matched"] = True
                self.matches_found += 1
                self.first_pick = None
                self.second_pick = None
                if self.matches_found >= self.total_pairs:
                    self.game_complete = True
            else:
                ## Mismatch — will need to flip back
                self.show_mismatch = True

        def clear_mismatch(self):
            """Flip mismatched cards back face-down."""
            if self.show_mismatch and self.first_pick is not None and self.second_pick is not None:
                self.cards[self.first_pick]["flipped"] = False
                self.cards[self.second_pick]["flipped"] = False
                self.first_pick = None
                self.second_pick = None
                self.show_mismatch = False

    ## Global instance
    flip_state = FlipCardState()


screen flip_card_game():

    ## Reset state when screen shows
    on "show" action Function(flip_state.reset)

    modal True
    zorder 200

    ## Dark overlay
    add Solid("#0d0d20ee"):
        xysize (1920, 1080)

    ## Main container
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        ## Title
        text "OFFICE MATCH GAME":
            xalign 0.5
            size 36
            color "#ffd700"
            outlines [(3, "#1e0c12", 0, 0)]

        text "Match each office with what it does!":
            xalign 0.5
            size 18
            color "#f1debf"
            outlines [(2, "#1e0c12", 0, 0)]

        ## Score display
        hbox:
            xalign 0.5
            spacing 30

            text "Matches: [flip_state.matches_found]/[flip_state.total_pairs]":
                size 16
                color "#b8e6b0"
                outlines [(2, "#1e0c12", 0, 0)]

            text "Attempts: [flip_state.attempts]":
                size 16
                color "#f6d79d"
                outlines [(2, "#1e0c12", 0, 0)]

        null height 10

        ## Card grid — 4 columns x 3 rows
        grid 4 3:
            xalign 0.5
            spacing 12

            for _ci in range(len(flip_state.cards)):
                $ _card = flip_state.cards[_ci]

                if _card["matched"]:
                    ## Matched card — stays face up with pair color
                    frame:
                        xysize (220, 130)
                        padding (10, 10, 10, 10)
                        background Solid(FLIP_CARD_COLORS[_card["pair_id"]])

                        vbox:
                            xfill True
                            yfill True
                            xalign 0.5
                            yalign 0.5

                            if _card["is_name"]:
                                text "📋":
                                    size 22
                                    xalign 0.5
                                null height 4
                            else:
                                text "📝":
                                    size 22
                                    xalign 0.5
                                null height 4

                            text _card["text"]:
                                size 13
                                color "#ffffff"
                                text_align 0.5
                                xalign 0.5
                                outlines [(1, "#00000088", 0, 0)]

                elif _card["flipped"]:
                    ## Flipped but not yet matched — show content
                    frame:
                        xysize (220, 130)
                        padding (10, 10, 10, 10)
                        background Solid("#2a1a3a")

                        vbox:
                            xfill True
                            yfill True
                            xalign 0.5
                            yalign 0.5

                            if _card["is_name"]:
                                text "📋":
                                    size 22
                                    xalign 0.5
                                null height 4
                            else:
                                text "📝":
                                    size 22
                                    xalign 0.5
                                null height 4

                            text _card["text"]:
                                size 13
                                color "#f1debf"
                                text_align 0.5
                                xalign 0.5

                else:
                    ## Face-down card — clickable
                    button:
                        xysize (220, 130)
                        padding (10, 10, 10, 10)
                        background Solid("#1e0c12")
                        hover_background Solid("#3a1a2a")

                        if flip_state.show_mismatch:
                            action Function(flip_state.clear_mismatch)
                        else:
                            action Function(flip_state.flip_card, _ci)

                        vbox:
                            xfill True
                            yfill True
                            xalign 0.5
                            yalign 0.5

                            text "?":
                                size 40
                                color "#f6d79d"
                                xalign 0.5
                                yalign 0.5
                                outlines [(2, "#1e0c12", 0, 0)]

        null height 6

        ## Mismatch hint
        if flip_state.show_mismatch:
            text "Not a match! Click any card to continue.":
                xalign 0.5
                size 16
                color "#f87171"
                outlines [(2, "#1e0c12", 0, 0)]

        ## Game complete message
        if flip_state.game_complete:
            null height 10
            text "All offices matched!":
                xalign 0.5
                size 24
                color "#10b981"
                outlines [(3, "#1e0c12", 0, 0)]

            null height 10

            textbutton "Continue":
                xalign 0.5
                text_size 20
                text_color "#ffd700"
                text_hover_color "#ffffff"
                text_outlines [(2, "#1e0c12", 0, 0)]
                action Return("completed")


## ============================================================================
## ENROLLMENT TETRIS — Drag subject blocks onto a weekly schedule grid
## ============================================================================
## Grid: 5 days (M-F) x 11 time slots (7AM-6PM, 1-hour rows)
## 6 academic subjects (3 units each = 18 units total)
## 2 non-unit subjects: PE, NSTP
## Each subject block spans 1-2 hours (60-120 min)
## Player clicks a subject from the palette, then clicks a grid cell to place it.
## No overlaps allowed. All 8 subjects placed = game complete.
## ============================================================================

init python:

    ## Subject definitions: (name, code, units, duration_hours, color)
    TETRIS_SUBJECTS = [
        ("Math 21",     "MATH 21",   3, 2, "#4a90d9"),   ## 120 min
        ("Eng 1",       "ENG 1",     3, 2, "#d94a4a"),   ## 120 min
        ("Fil 40",      "FIL 40",    3, 1, "#4ad97a"),   ## 60 min
        ("STS",         "STS",       3, 2, "#d9a04a"),   ## 120 min
        ("Kas 1",       "KAS 1",     3, 1, "#9a4ad9"),   ## 60 min
        ("CS 11",       "CS 11",     3, 2, "#4ad9d9"),   ## 120 min
        ("PE",          "PE",        0, 1, "#d97aaa"),   ## 60 min, non-unit
        ("NSTP",        "NSTP",      0, 2, "#7a9ad9"),   ## 120 min, non-unit
    ]

    TETRIS_DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    TETRIS_TIMES = [
        "7:00", "8:00", "9:00", "10:00", "11:00",
        "12:00", "1:00", "2:00", "3:00", "4:00", "5:00"
    ]

    class EnrollmentTetrisState:
        def __init__(self):
            self.reset()

        def reset(self):
            ## Grid: grid[day_idx][time_idx] = subject_index or -1
            self.grid = [[-1 for _ in range(len(TETRIS_TIMES))] for _ in range(len(TETRIS_DAYS))]
            ## Which subject is currently selected for placement
            self.selected_subject = -1
            ## Track which subjects have been placed (subject_idx -> list of (day, time) tuples)
            self.placements = {}
            ## Each subject needs to be placed on 2 different days (meeting pattern)
            ## For simplicity: each subject is placed once (one block on one day)
            self.placed_count = 0
            self.total_subjects = len(TETRIS_SUBJECTS)
            self.game_complete = False
            self.error_msg = ""
            self.total_units = 0

        def select_subject(self, subj_idx):
            """Select a subject from the palette to place."""
            if subj_idx in self.placements:
                self.error_msg = "Already placed!"
                return
            self.selected_subject = subj_idx
            self.error_msg = ""

        def place_at(self, day_idx, time_idx):
            """Try to place the selected subject at the given grid cell."""
            if self.selected_subject < 0:
                self.error_msg = "Select a subject first!"
                return

            subj_idx = self.selected_subject
            subj = TETRIS_SUBJECTS[subj_idx]
            duration = subj[3]  ## hours

            ## Check bounds
            if time_idx + duration > len(TETRIS_TIMES):
                self.error_msg = "Doesn't fit! Goes past 6:00 PM."
                return

            ## Check for overlaps
            for t in range(time_idx, time_idx + duration):
                if self.grid[day_idx][t] != -1:
                    existing = TETRIS_SUBJECTS[self.grid[day_idx][t]]
                    self.error_msg = "Conflict with " + existing[1] + "!"
                    return

            ## Place the subject
            for t in range(time_idx, time_idx + duration):
                self.grid[day_idx][t] = subj_idx

            self.placements[subj_idx] = (day_idx, time_idx)
            self.placed_count += 1
            self.total_units += subj[2]
            self.selected_subject = -1
            self.error_msg = ""

            if self.placed_count >= self.total_subjects:
                self.game_complete = True

        def remove_subject(self, subj_idx):
            """Remove a placed subject from the grid."""
            if subj_idx not in self.placements:
                return
            day_idx, time_idx = self.placements[subj_idx]
            duration = TETRIS_SUBJECTS[subj_idx][3]
            for t in range(time_idx, time_idx + duration):
                if self.grid[day_idx][t] == subj_idx:
                    self.grid[day_idx][t] = -1
            self.total_units -= TETRIS_SUBJECTS[subj_idx][2]
            del self.placements[subj_idx]
            self.placed_count -= 1
            self.game_complete = False
            self.error_msg = ""

    tetris_state = EnrollmentTetrisState()


screen enrollment_tetris_game():

    on "show" action Function(tetris_state.reset)

    modal True
    zorder 200

    ## Dark overlay
    add Solid("#0d0d20ee"):
        xysize (1920, 1080)

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 24

        ## === LEFT: Subject Palette ===
        vbox:
            spacing 8
            xsize 280

            text "ENROLLMENT TETRIS":
                size 22
                color "#ffd700"
                xalign 0.5
                outlines [(2, "#1e0c12", 0, 0)]

            text "Build your class schedule!":
                size 13
                color "#f1debf"
                xalign 0.5
                outlines [(1, "#1e0c12", 0, 0)]

            null height 6

            text "SUBJECTS":
                size 14
                color "#f6d79d"
                outlines [(1, "#1e0c12", 0, 0)]

            ## Subject list
            for _si in range(len(TETRIS_SUBJECTS)):
                $ _subj = TETRIS_SUBJECTS[_si]
                $ _placed = _si in tetris_state.placements
                $ _selected = tetris_state.selected_subject == _si

                if _placed:
                    ## Already placed — show with checkmark, click to remove
                    button:
                        xsize 270
                        ysize 42
                        background Solid(_subj[4] + "44")
                        hover_background Solid(_subj[4] + "66")
                        action Function(tetris_state.remove_subject, _si)
                        padding (8, 4, 8, 4)

                        hbox:
                            spacing 6
                            yalign 0.5
                            text "✓":
                                size 14
                                color "#10b981"
                            text _subj[1]:
                                size 13
                                color "#9f9f9f"
                                strikethrough True
                            if _subj[2] > 0:
                                text "(" + str(_subj[2]) + "u)":
                                    size 11
                                    color "#9f9f9f88"
                            else:
                                text "(non-unit)":
                                    size 11
                                    color "#9f9f9f88"

                elif _selected:
                    ## Currently selected
                    frame:
                        xsize 270
                        ysize 42
                        background Solid(_subj[4])
                        padding (8, 4, 8, 4)

                        hbox:
                            spacing 6
                            yalign 0.5
                            text "►":
                                size 14
                                color "#ffffff"
                            text _subj[1]:
                                size 13
                                color "#ffffff"
                                bold True
                            if _subj[2] > 0:
                                text "(" + str(_subj[2]) + "u, " + str(_subj[3]) + "hr)":
                                    size 11
                                    color "#ffffffcc"
                            else:
                                text "(non-unit, " + str(_subj[3]) + "hr)":
                                    size 11
                                    color "#ffffffcc"

                else:
                    ## Available to select
                    button:
                        xsize 270
                        ysize 42
                        background Solid("#1e0c12")
                        hover_background Solid(_subj[4] + "44")
                        action Function(tetris_state.select_subject, _si)
                        padding (8, 4, 8, 4)

                        hbox:
                            spacing 6
                            yalign 0.5

                            frame:
                                xsize 12
                                ysize 12
                                yalign 0.5
                                background Solid(_subj[4])
                                padding (0, 0, 0, 0)

                            text _subj[1]:
                                size 13
                                color "#f1debf"
                            if _subj[2] > 0:
                                text "(" + str(_subj[2]) + "u, " + str(_subj[3]) + "hr)":
                                    size 11
                                    color "#f6d79d88"
                            else:
                                text "(non-unit, " + str(_subj[3]) + "hr)":
                                    size 11
                                    color "#f6d79d88"

            null height 8

            ## Units counter
            hbox:
                xalign 0.5
                spacing 8
                text "Units:":
                    size 14
                    color "#f6d79d"
                    outlines [(1, "#1e0c12", 0, 0)]
                text "[tetris_state.total_units]/18":
                    size 14
                    color "#b8e6b0"
                    outlines [(1, "#1e0c12", 0, 0)]

            text "[tetris_state.placed_count]/[tetris_state.total_subjects] placed":
                size 12
                color "#f6d79d88"
                xalign 0.5

            ## Error message
            if tetris_state.error_msg:
                null height 4
                text "[tetris_state.error_msg]":
                    size 13
                    color "#f87171"
                    xalign 0.5
                    outlines [(1, "#1e0c12", 0, 0)]

        ## === RIGHT: Schedule Grid ===
        vbox:
            spacing 0

            ## Day headers
            hbox:
                spacing 0

                ## Empty corner cell (time label column)
                frame:
                    xsize 60
                    ysize 32
                    background Solid("#1e0c12")
                    padding (0, 0, 0, 0)
                    text "Time":
                        size 11
                        color "#f6d79d"
                        xalign 0.5
                        yalign 0.5

                for _day in TETRIS_DAYS:
                    frame:
                        xsize 120
                        ysize 32
                        background Solid(DARK_MAROON)
                        padding (0, 0, 0, 0)
                        text _day:
                            size 13
                            color "#ffffff"
                            bold True
                            xalign 0.5
                            yalign 0.5

            ## Time rows
            for _ti in range(len(TETRIS_TIMES)):
                hbox:
                    spacing 0

                    ## Time label
                    frame:
                        xsize 60
                        ysize 48
                        background Solid("#1a0a10")
                        padding (4, 0, 4, 0)
                        text TETRIS_TIMES[_ti]:
                            size 11
                            color "#f6d79d"
                            xalign 0.5
                            yalign 0.5

                    ## Day cells
                    for _di in range(len(TETRIS_DAYS)):
                        $ _cell_val = tetris_state.grid[_di][_ti]

                        if _cell_val >= 0:
                            ## Occupied cell — show subject color and name
                            $ _cs = TETRIS_SUBJECTS[_cell_val]
                            ## Only show label on the first cell of the block
                            $ _show_label = (_ti == 0 or tetris_state.grid[_di][_ti - 1] != _cell_val)

                            frame:
                                xsize 120
                                ysize 48
                                background Solid(_cs[4] + "cc")
                                padding (4, 2, 4, 2)

                                if _show_label:
                                    vbox:
                                        xalign 0.5
                                        yalign 0.5
                                        text _cs[1]:
                                            size 12
                                            color "#ffffff"
                                            bold True
                                            xalign 0.5
                                            outlines [(1, "#00000088", 0, 0)]
                                        if _cs[2] > 0:
                                            text str(_cs[2]) + " units":
                                                size 9
                                                color "#ffffffaa"
                                                xalign 0.5
                                        else:
                                            text "non-unit":
                                                size 9
                                                color "#ffffffaa"
                                                xalign 0.5

                        else:
                            ## Empty cell — clickable if subject is selected
                            if tetris_state.selected_subject >= 0:
                                button:
                                    xsize 120
                                    ysize 48
                                    background Solid("#1e0c1288")
                                    hover_background Solid(TETRIS_SUBJECTS[tetris_state.selected_subject][4] + "44")
                                    action Function(tetris_state.place_at, _di, _ti)
                                    padding (0, 0, 0, 0)

                                    ## Grid lines
                                    frame:
                                        xfill True
                                        yfill True
                                        background Solid("#2a1a2a22")
                                        padding (0, 0, 0, 0)
                            else:
                                frame:
                                    xsize 120
                                    ysize 48
                                    background Solid("#1e0c1288")
                                    padding (0, 0, 0, 0)

                                    frame:
                                        xfill True
                                        yfill True
                                        background Solid("#2a1a2a22")
                                        padding (0, 0, 0, 0)

            ## Bottom instruction
            null height 12

            if tetris_state.selected_subject >= 0:
                $ _sel_s = TETRIS_SUBJECTS[tetris_state.selected_subject]
                text "Click a time slot to place " + _sel_s[1] + " (" + str(_sel_s[3]) + " hr block)":
                    size 14
                    color "#f6d79d"
                    xalign 0.5
                    outlines [(1, "#1e0c12", 0, 0)]
            elif not tetris_state.game_complete:
                text "Select a subject, then click the grid to place it. Click placed subjects to remove.":
                    size 12
                    color "#f6d79d88"
                    xalign 0.5

            ## Game complete
            if tetris_state.game_complete:
                null height 12
                text "Schedule Complete! All subjects placed.":
                    size 20
                    color "#10b981"
                    xalign 0.5
                    outlines [(2, "#1e0c12", 0, 0)]

                null height 8

                textbutton "Continue":
                    xalign 0.5
                    text_size 20
                    text_color "#ffd700"
                    text_hover_color "#ffffff"
                    text_outlines [(2, "#1e0c12", 0, 0)]
                    action Return("completed")


## ============================================================================
## DORM ROOM SETUP — Budget-based item selection mini-game
## ============================================================================
## Player has ₱2,500 budget and must buy all REQUIRED essentials.
## Optional items can be bought if budget allows.
## Game completes when all required items are purchased.
## ============================================================================

init python:

    ## (name, price, icon, required, category, description)
    DORM_SHOP_ITEMS = [
        ## Required essentials
        ("Bed Sheet & Pillow",    250, "🛏️", True,  "Bedding",    "Cotton bed sheet and a pillow"),
        ("Blanket",               200, "🧶", True,  "Bedding",    "Light blanket for cool Miagao nights"),
        ("Electric Fan",          450, "🌀", True,  "Appliance",  "Stand fan — no aircon in standard rooms"),
        ("Study Lamp",            180, "💡", True,  "Study",      "Desk lamp for late-night studying"),
        ("Padlock",                80, "🔒", True,  "Security",   "For your personal cabinet"),
        ("Toiletries Kit",       150, "🧴", True,  "Personal",   "Soap, shampoo, toothbrush, toothpaste"),
        ("Towel",                 100, "🛁", True,  "Personal",   "Bath towel — you'll need this day one"),
        ("Extension Cord",       200, "🔌", True,  "Appliance",  "3-outlet extension — limited sockets"),
        ## Optional nice-to-haves
        ("Hangers (10 pcs)",      60, "👕", False, "Storage",    "For your clothes — closet space is tight"),
        ("Storage Box",          120, "📦", False, "Storage",    "Stackable box for extra supplies"),
        ("First Aid Kit",        180, "🩹", False, "Health",     "Basic medicine for headaches and colds"),
        ("Tumbler",               90, "🥤", False, "Personal",   "Reusable water bottle — stay hydrated"),
        ("Desk Organizer",       100, "📂", False, "Study",      "Keep your desk tidy"),
        ("Slippers",              80, "🩴", False, "Personal",   "Indoor slippers for the room"),
        ("Snack Stash",          150, "🍪", False, "Food",       "Biscuits and instant noodles for emergencies"),
        ("Mosquito Net",         200, "🦟", False, "Health",     "Miagao mosquitos are no joke"),
    ]

    DORM_BUDGET = 2500

    class DormSetupState:
        def __init__(self):
            self.reset()

        def reset(self):
            self.budget = DORM_BUDGET
            self.purchased = set()  ## indices of purchased items
            self.game_complete = False
            self.error_msg = ""

        def buy_item(self, idx):
            """Buy an item from the shop."""
            if idx in self.purchased:
                self.error_msg = "Already purchased!"
                return

            item = DORM_SHOP_ITEMS[idx]
            price = item[1]

            if price > self.budget:
                self.error_msg = "Not enough budget! (₱" + str(self.budget) + " left)"
                return

            self.budget -= price
            self.purchased.add(idx)
            self.error_msg = ""

            ## Check if all required items are purchased
            all_required = True
            for i, itm in enumerate(DORM_SHOP_ITEMS):
                if itm[3] and i not in self.purchased:  ## required but not bought
                    all_required = False
                    break

            if all_required:
                self.game_complete = True

        def refund_item(self, idx):
            """Refund a purchased item."""
            if idx not in self.purchased:
                return
            item = DORM_SHOP_ITEMS[idx]
            self.budget += item[1]
            self.purchased.discard(idx)
            self.game_complete = False
            self.error_msg = ""

        def required_remaining(self):
            """Count how many required items are still needed."""
            count = 0
            for i, itm in enumerate(DORM_SHOP_ITEMS):
                if itm[3] and i not in self.purchased:
                    count += 1
            return count

        def total_spent(self):
            return DORM_BUDGET - self.budget

    dorm_setup_state = DormSetupState()


screen dorm_room_setup_game():

    on "show" action Function(dorm_setup_state.reset)

    modal True
    zorder 200

    ## Background — dorm room
    add "images/ui/dormRoom.png":
        xysize (1920, 1080)
        alpha 0.3

    add Solid("#0d0d20cc"):
        xysize (1920, 1080)

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 12

        ## Title
        text "DORM ROOM SETUP":
            xalign 0.5
            size 28
            color "#ffd700"
            outlines [(3, "#1e0c12", 0, 0)]

        text "Buy essentials for your room within budget!":
            xalign 0.5
            size 14
            color "#f1debf"
            outlines [(1, "#1e0c12", 0, 0)]

        ## Budget bar
        hbox:
            xalign 0.5
            spacing 30

            hbox:
                spacing 6
                text "Budget:" size 16 color "#f6d79d" outlines [(1, "#1e0c12", 0, 0)]
                if dorm_setup_state.budget >= 500:
                    text "₱[dorm_setup_state.budget]" size 16 color "#10b981" bold True outlines [(1, "#1e0c12", 0, 0)]
                elif dorm_setup_state.budget >= 200:
                    text "₱[dorm_setup_state.budget]" size 16 color "#f6d79d" bold True outlines [(1, "#1e0c12", 0, 0)]
                else:
                    text "₱[dorm_setup_state.budget]" size 16 color "#f87171" bold True outlines [(1, "#1e0c12", 0, 0)]

            hbox:
                spacing 6
                text "Spent:" size 14 color "#f6d79d88" outlines [(1, "#1e0c12", 0, 0)]
                $ _spent = dorm_setup_state.total_spent()
                text "₱[_spent]" size 14 color "#f6d79d88" outlines [(1, "#1e0c12", 0, 0)]

            hbox:
                spacing 6
                $ _req_left = dorm_setup_state.required_remaining()
                text "Required left:" size 14 color "#f6d79d88" outlines [(1, "#1e0c12", 0, 0)]
                if _req_left > 0:
                    text "[_req_left]" size 14 color "#f87171" bold True outlines [(1, "#1e0c12", 0, 0)]
                else:
                    text "0 ✓" size 14 color "#10b981" bold True outlines [(1, "#1e0c12", 0, 0)]

        null height 4

        ## Error message
        if dorm_setup_state.error_msg:
            text "[dorm_setup_state.error_msg]":
                xalign 0.5
                size 14
                color "#f87171"
                outlines [(1, "#1e0c12", 0, 0)]

        ## Shop grid — 2 columns
        hbox:
            xalign 0.5
            spacing 16

            ## Required items column
            vbox:
                spacing 6
                xsize 500

                text "ESSENTIALS (Required)" size 14 color "#ff9966" outlines [(1, "#1e0c12", 0, 0)]

                for _si in range(len(DORM_SHOP_ITEMS)):
                    $ _item = DORM_SHOP_ITEMS[_si]
                    if _item[3]:  ## required items only
                        $ _bought = _si in dorm_setup_state.purchased

                        if _bought:
                            ## Purchased — show with checkmark, click to refund
                            button:
                                xsize 490
                                ysize 50
                                background Solid("#10b98133")
                                hover_background Solid("#10b98155")
                                action Function(dorm_setup_state.refund_item, _si)
                                padding (10, 4, 10, 4)

                                hbox:
                                    spacing 8
                                    yalign 0.5
                                    text "✓" size 16 color "#10b981"
                                    text _item[2] size 16  ## icon
                                    vbox:
                                        spacing 1
                                        text _item[0] size 13 color "#10b981" bold True
                                        text _item[5] size 10 color "#10b98188"
                                    null width 1
                                    text "₱" + str(_item[1]) size 12 color "#10b98188" yalign 0.5

                        else:
                            ## Available to buy
                            button:
                                xsize 490
                                ysize 50
                                background Solid("#1e0c12")
                                hover_background Solid("#3a1a2a")
                                action Function(dorm_setup_state.buy_item, _si)
                                padding (10, 4, 10, 4)

                                hbox:
                                    spacing 8
                                    yalign 0.5
                                    text _item[2] size 16  ## icon
                                    vbox:
                                        spacing 1
                                        text _item[0] size 13 color "#f1debf"
                                        text _item[5] size 10 color "#f6d79d88"
                                    null width 1
                                    if _item[1] <= dorm_setup_state.budget:
                                        text "₱" + str(_item[1]) size 13 color "#ffd700" bold True yalign 0.5
                                    else:
                                        text "₱" + str(_item[1]) size 13 color "#f8717188" yalign 0.5

            ## Optional items column
            vbox:
                spacing 6
                xsize 500

                text "OPTIONAL (Nice-to-haves)" size 14 color "#99ccff" outlines [(1, "#1e0c12", 0, 0)]

                for _si in range(len(DORM_SHOP_ITEMS)):
                    $ _item = DORM_SHOP_ITEMS[_si]
                    if not _item[3]:  ## optional items only
                        $ _bought = _si in dorm_setup_state.purchased

                        if _bought:
                            button:
                                xsize 490
                                ysize 50
                                background Solid("#4a90d933")
                                hover_background Solid("#4a90d955")
                                action Function(dorm_setup_state.refund_item, _si)
                                padding (10, 4, 10, 4)

                                hbox:
                                    spacing 8
                                    yalign 0.5
                                    text "✓" size 16 color "#4a90d9"
                                    text _item[2] size 16
                                    vbox:
                                        spacing 1
                                        text _item[0] size 13 color "#4a90d9" bold True
                                        text _item[5] size 10 color "#4a90d988"
                                    null width 1
                                    text "₱" + str(_item[1]) size 12 color "#4a90d988" yalign 0.5

                        else:
                            button:
                                xsize 490
                                ysize 50
                                background Solid("#1e0c12")
                                hover_background Solid("#2a1a3a")
                                action Function(dorm_setup_state.buy_item, _si)
                                padding (10, 4, 10, 4)

                                hbox:
                                    spacing 8
                                    yalign 0.5
                                    text _item[2] size 16
                                    vbox:
                                        spacing 1
                                        text _item[0] size 13 color "#f1debf"
                                        text _item[5] size 10 color "#f6d79d88"
                                    null width 1
                                    if _item[1] <= dorm_setup_state.budget:
                                        text "₱" + str(_item[1]) size 13 color "#99ccff" bold True yalign 0.5
                                    else:
                                        text "₱" + str(_item[1]) size 13 color "#f8717188" yalign 0.5

        null height 6

        ## Hint text
        if not dorm_setup_state.game_complete:
            text "Buy all 8 essentials to set up your room. Click purchased items to refund.":
                xalign 0.5
                size 12
                color "#f6d79d88"

        ## Game complete
        if dorm_setup_state.game_complete:
            null height 4
            text "Room Setup Complete! All essentials purchased.":
                size 20
                color "#10b981"
                xalign 0.5
                outlines [(2, "#1e0c12", 0, 0)]

            null height 6

            textbutton "Move In":
                xalign 0.5
                text_size 20
                text_color "#ffd700"
                text_hover_color "#ffffff"
                text_outlines [(2, "#1e0c12", 0, 0)]
                action Return("completed")


################################################################################
## Travel Cutscene Screen
## Self-contained: video + RPG-style border + vignette + HUD all in one screen.
##
## Usage in a label:
##   window hide
##   show screen travel_cutscene("images/maps/MyVideo.webm", "Location Name")
##   $ renpy.pause()
##   hide screen travel_cutscene
################################################################################

## Pulsing glow for the dot indicator
transform _travel_dot_pulse:
    alpha 1.0
    linear 0.55 alpha 0.15
    linear 0.55 alpha 1.0
    repeat

## Destination card slides up on appear
transform _travel_card_slidein:
    alpha 0.0
    yoffset 28
    linear 0.5 alpha 1.0 yoffset 0

## Staggered travel dots (sequential blink)
transform _travel_tdot1:
    block:
        alpha 0.2
        linear 0.28 alpha 1.0
        linear 0.28 alpha 0.2
        repeat

transform _travel_tdot2:
    pause 0.22
    block:
        alpha 0.2
        linear 0.28 alpha 1.0
        linear 0.28 alpha 0.2
        repeat

transform _travel_tdot3:
    pause 0.44
    block:
        alpha 0.2
        linear 0.28 alpha 1.0
        linear 0.28 alpha 0.2
        repeat

## Subtle scan line sweeping top to bottom
transform _travel_scan:
    ypos -3
    linear 2.8 ypos 1083
    repeat

screen travel_cutscene(video_path, destination, subtitle=""):
    zorder 500
    modal False

    ## ── Black base ──
    add Solid("#000000") xsize 1920 ysize 1080

    ## ── Video (fullscreen) ──
    add Movie(play=video_path) xsize 1920 ysize 1080 xpos 0 ypos 0

    ## ── Scan line (very subtle, sweeps over video) ──
    add Solid("#ffffff08") xsize 1920 ysize 3 at _travel_scan

    ## ── Vignette: dark wash on all four edges ──
    add Solid("#000000CC") xsize 1920 ysize 110 xpos 0 ypos 0
    add Solid("#000000CC") xsize 1920 ysize 110 xpos 0 yalign 1.0
    add Solid("#00000077") xsize 110 ysize 1080 xpos 0 ypos 0
    add Solid("#00000077") xsize 110 ysize 1080 xalign 1.0 ypos 0

    ## ── Thin outer border (dark maroon, 3px, all 4 sides) ──
    add Solid("#4a0e0e") xsize 1920 ysize 3   xpos 0      ypos 0
    add Solid("#4a0e0e") xsize 1920 ysize 3   xpos 0      yalign 1.0
    add Solid("#4a0e0e") xsize 3   ysize 1080 xpos 0      ypos 0
    add Solid("#4a0e0e") xsize 3   ysize 1080 xalign 1.0  ypos 0

    ## ── Outer corner brackets (warm gold, 110px arms, 8px thick) ──
    ## Top-left
    add Solid("#c8923a") xsize 110 ysize 8 xpos 0      ypos 0
    add Solid("#c8923a") xsize 8   ysize 110 xpos 0    ypos 0
    ## Top-right
    add Solid("#c8923a") xsize 110 ysize 8 xalign 1.0  ypos 0
    add Solid("#c8923a") xsize 8   ysize 110 xalign 1.0 ypos 0
    ## Bottom-left
    add Solid("#c8923a") xsize 110 ysize 8 xpos 0      yalign 1.0
    add Solid("#c8923a") xsize 8   ysize 110 xpos 0    yalign 1.0
    ## Bottom-right
    add Solid("#c8923a") xsize 110 ysize 8 xalign 1.0  yalign 1.0
    add Solid("#c8923a") xsize 8   ysize 110 xalign 1.0 yalign 1.0

    ## ── Corner squares at outer bracket tips (gold, 12×12) ──
    add Solid("#c8923a") xsize 12 ysize 12 xpos 0      ypos 0
    add Solid("#c8923a") xsize 12 ysize 12 xalign 1.0  ypos 0
    add Solid("#c8923a") xsize 12 ysize 12 xpos 0      yalign 1.0
    add Solid("#c8923a") xsize 12 ysize 12 xalign 1.0  yalign 1.0

    ## ── Inner corner brackets (maroon, 70px arms, 3px thick, inset 22px) ──
    ## Top-left
    add Solid("#a03030") xsize 70 ysize 3 xpos 22          ypos 22
    add Solid("#a03030") xsize 3  ysize 70 xpos 22         ypos 22
    ## Top-right  (1920 - 22 - 70 = 1828 | 1920 - 22 - 3 = 1895)
    add Solid("#a03030") xsize 70 ysize 3 xpos 1828        ypos 22
    add Solid("#a03030") xsize 3  ysize 70 xpos 1895       ypos 22
    ## Bottom-left  (1080 - 22 - 3 = 1055 | 1080 - 22 - 70 = 988)
    add Solid("#a03030") xsize 70 ysize 3 xpos 22          ypos 1055
    add Solid("#a03030") xsize 3  ysize 70 xpos 22         ypos 988
    ## Bottom-right
    add Solid("#a03030") xsize 70 ysize 3 xpos 1828        ypos 1055
    add Solid("#a03030") xsize 3  ysize 70 xpos 1895       ypos 988

    ## ── Top HUD strip: "◆ NAVIGATING ◆" ──
    frame:
        xalign 0.5
        ypos 10
        background "#00000000"
        padding (18, 4, 18, 4)
        hbox:
            spacing 10
            xalign 0.5
            text "◆" at _travel_dot_pulse:
                color "#c8923a"
                size 20
                yalign 0.5
            text "NAVIGATING":
                color "#2FA89A"
                size 30
                yalign 0.5
            text "◆" at _travel_dot_pulse:
                color "#c8923a"
                size 20
                yalign 0.5

    ## ── Destination card (slides up) ──
    frame at _travel_card_slidein:
        xalign 0.5
        yalign 0.87
        background "#000000AA"
        padding (48, 14, 48, 20)
        vbox:
            spacing 6
            xalign 0.5

            ## "DESTINATION" label with arrow indicators
            hbox:
                spacing 8
                xalign 0.5
                text "▶" at _travel_dot_pulse:
                    color "#e07070"
                    size 11
                    yalign 0.5
                text "DESTINATION":
                    color "#ffffff44"
                    size 11
                    yalign 0.5
                text "▶" at _travel_dot_pulse:
                    color "#e07070"
                    size 11
                    yalign 0.5

            ## Destination name
            text destination:
                xalign 0.5
                color "#ffffff"
                size 38
                bold True
                outlines [(2, "#000000AA", 1, 1)]

            ## Optional subtitle
            if subtitle:
                text subtitle:
                    xalign 0.5
                    color "#ffffff77"
                    size 14

            ## Staggered travel dots
            null height 2
            hbox:
                xalign 0.5
                spacing 10
                text "●" at _travel_tdot1:
                    color "#c8923a"
                    size 10
                text "●" at _travel_tdot2:
                    color "#c8923a"
                    size 10
                text "●" at _travel_tdot3:
                    color "#c8923a"
                    size 10

    ## ── Skip hint (bottom-right, inside corner bracket) ──
    text "[[ Click to skip ]]":
        xpos 1895
        xanchor 1.0
        ypos 1062
        color "#ffffff33"
        size 11
