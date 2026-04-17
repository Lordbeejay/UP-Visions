## ============================================================================
## SUBQUEST INTERACTIVE MINI-GAME SCREENS
## 4 game types: Quiz, Sort, Timeline, GWA Calculator
## Pattern: state.setup() called in dialogue → call screen → $ _result = _return
## ============================================================================

## ============================================================================
## STATE CLASSES
## ============================================================================

init python:

    ## ── SQ QUIZ STATE ────────────────────────────────────────────────────────
    ## Reusable 3-question multiple choice. Questions passed via setup().
    ## Question format: (question_str, [(answer_str, is_correct_bool, feedback_str), ...])
    class SQQuizState:
        def __init__(self):
            self.title = "Quiz"
            self.subtitle = ""
            self.icon = "📋"
            self.questions = []
            self.current_q = 0
            self.score = 0
            self.done = False
            self.chosen = None
            self.is_correct = False
            self.feedback_text = ""
            self.show_feedback = False

        def setup(self, title, subtitle, icon, questions):
            import random
            self.title = title
            self.subtitle = subtitle
            self.icon = icon
            self.questions = [
                (q[0], random.sample(q[1], len(q[1])))
                for q in questions
            ]
            self.current_q = 0
            self.score = 0
            self.done = False
            self.chosen = None
            self.is_correct = False
            self.feedback_text = ""
            self.show_feedback = False

        def answer(self, ans_idx):
            if self.show_feedback or self.done:
                return
            q = self.questions[self.current_q]
            ans = q[1][ans_idx]
            self.chosen = ans_idx
            self.is_correct = ans[1]
            self.feedback_text = ans[2]
            if self.is_correct:
                self.score += 1
            self.show_feedback = True

        def retry(self):
            import random
            self.questions = [
                (q[0], random.sample(q[1], len(q[1])))
                for q in self.questions
            ]
            self.current_q = 0
            self.score = 0
            self.done = False
            self.chosen = None
            self.show_feedback = False

        def advance(self):
            self.show_feedback = False
            self.chosen = None
            self.current_q += 1
            if self.current_q >= len(self.questions):
                self.done = True

    sq_quiz_state = SQQuizState()


    ## ── SQ SORT STATE ────────────────────────────────────────────────────────
    ## Click a card to select it (highlighted), then click a bin to assign it.
    ## Item format:  (text_str, correct_bin_int, icon_str)
    ## Bin  format:  (label_str, color_hex_str, icon_str)
    class SQSortState:
        def __init__(self):
            self.title = "Sort Game"
            self.subtitle = ""
            self.items = []
            self.bins = []
            self.assignments = {}
            self.selected = None
            self.score = 0
            self.done = False

        def setup(self, title, subtitle, items, bins):
            self.title = title
            self.subtitle = subtitle
            self.items = list(items)
            self.bins = list(bins)
            self.assignments = {}
            self.selected = None
            self.score = 0
            self.done = False

        def select(self, idx):
            if idx not in self.assignments:
                self.selected = None if self.selected == idx else idx

        def assign(self, bin_idx):
            if self.selected is None:
                return
            correct = self.items[self.selected][1]
            self.assignments[self.selected] = bin_idx
            if bin_idx == correct:
                self.score += 1
            self.selected = None
            if len(self.assignments) >= len(self.items):
                self.done = True

        def unassign(self, idx):
            if idx in self.assignments:
                was_correct = (self.assignments[idx] == self.items[idx][1])
                if was_correct:
                    self.score -= 1
                del self.assignments[idx]
                self.done = False

        def retry(self):
            self.assignments = {}
            self.selected = None
            self.score = 0
            self.done = False

    sq_sort_state = SQSortState()


    ## ── SQ TIMELINE STATE ────────────────────────────────────────────────────
    ## Click historical events in chronological order (earliest first).
    ## Event format: (year_int, short_label_str, description_str, color_hex_str)
    class SQTimelineState:
        def __init__(self):
            self.events = []
            self.order = []
            self.score = 0
            self.done = False

        def setup(self, events):
            self.events = list(events)
            self.order = []
            self.score = 0
            self.done = False

        def pick(self, idx):
            if self.done or idx in self.order:
                return
            self.order.append(idx)
            if len(self.order) == len(self.events):
                correct = sorted(range(len(self.events)), key=lambda i: self.events[i][0])
                self.score = sum(1 for a, b in zip(self.order, correct) if a == b)
                self.done = True

        def undo(self):
            if self.order and not self.done:
                self.order.pop()

        def retry(self):
            self.order = []
            self.score = 0
            self.done = False

    sq_timeline_state = SQTimelineState()


    ## ── SQ GWA CALC STATE ────────────────────────────────────────────────────
    ## Click grade cells to cycle through UP grades; live GWA + scholarship shown.
    class SQGWACalcState:
        GRADE_STEPS = [1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 4.0, 5.0]

        def __init__(self):
            self.courses = [
                ("Kas 1 — Kasaysayan ng Pilipinas", 3),
                ("GE Mathematics (College Algebra)", 3),
                ("GE English (Writing and Reading)", 3),
                ("NSTP 1 (Civic Welfare Training)", 3),
                ("PE 1 (Physical Education)", 2),
            ]
            self.grades = {}
            self.challenge = "Reach University Scholar status (GWA \u2264 1.20)."
            self.challenge_gwa = 1.20

        def reset(self):
            self.grades = {}

        def cycle_grade(self, idx):
            if idx not in self.grades:
                self.grades[idx] = self.GRADE_STEPS[0]
            else:
                cur = self.GRADE_STEPS.index(self.grades[idx])
                self.grades[idx] = self.GRADE_STEPS[(cur + 1) % len(self.GRADE_STEPS)]

        def calc_gwa(self):
            if not self.grades:
                return None
            wu = sum(self.grades[i] * self.courses[i][1] for i in self.grades)
            tu = sum(self.courses[i][1] for i in self.grades)
            return round(wu / tu, 4) if tu else None

        def grade_color(self, g):
            if g is None:
                return "#888888"
            if g <= 1.75:
                return "#10b981"
            elif g <= 2.75:
                return "#fbbf24"
            elif g == 3.0:
                return "#fb923c"
            else:
                return "#f87171"

        def scholarship_for(self, gwa):
            if gwa is None:
                return ("Set all grades first", "#888888")
            if gwa <= 1.20:
                return ("\u2605 University Scholar", "#ffd700")
            elif gwa <= 1.45:
                return ("College Scholar", "#10b981")
            elif gwa <= 1.75:
                return ("Dean's List", "#6ee7b7")
            elif gwa <= 3.00:
                return ("Regular Standing", "#f1debf")
            else:
                return ("Academic Concern", "#f87171")

        def all_set(self):
            return len(self.grades) == len(self.courses)

    sq_gwa_state = SQGWACalcState()
    sq_gwa_state.reset()


## ============================================================================
## SCREEN: SQ QUIZ GAME
## call screen sq_quiz_game() → _return = score_int (0-3)
## ============================================================================
screen sq_quiz_game():
    on "show" action NullAction()
    modal True
    zorder 200

    add Solid("#0d0406") alpha 0.98

    $ _sq_total = len(sq_quiz_state.questions)
    $ _sq_cur   = sq_quiz_state.current_q

    if sq_quiz_state.done:
        ## ── RESULTS SCREEN ───────────────────────────────────────────────────
        frame:
            xalign 0.5
            yalign 0.5
            xsize 620
            padding (0, 0, 0, 0)
            background Solid("#1a0a0ef8")

            vbox:
                spacing 0

                frame:
                    background Solid("#2a0e0e")
                    xfill True
                    padding (24, 14, 24, 14)
                    vbox:
                        spacing 3
                        hbox:
                            spacing 8
                            text "[sq_quiz_state.icon]" size 18 yalign 0.5
                            text "[sq_quiz_state.title]" size 16 color "#ffd700" bold True yalign 0.5
                        text "[sq_quiz_state.subtitle]" size 11 color "#c8921888" italic True

                frame:
                    background Solid("#0d0406")
                    xfill True
                    padding (40, 32, 40, 36)
                    vbox:
                        spacing 16
                        xalign 0.5

                        text "\u2605 RESULT \u2605":
                            xalign 0.5
                            size 13
                            color "#c89218"
                            bold True

                        hbox:
                            xalign 0.5
                            spacing 4
                            text "[sq_quiz_state.score]":
                                size 60
                                color "#ffd700"
                                bold True
                                yalign 0.5
                            text "/[_sq_total]":
                                size 28
                                color "#f6d79d88"
                                yalign 1.0

                        if sq_quiz_state.score == _sq_total:
                            text "Perfect! Outstanding.":
                                xalign 0.5 size 15 color "#10b981"
                        elif sq_quiz_state.score >= 2:
                            text "Passed — good understanding.":
                                xalign 0.5 size 15 color "#6ee7b7"
                        else:
                            text "Review and try again.":
                                xalign 0.5 size 15 color "#f87171"

                        null height 8

                        if sq_quiz_state.score >= 2:
                            textbutton "Claim Reward  \u2605":
                                xalign 0.5
                                action Return(sq_quiz_state.score)
                                text_size 15
                                text_color "#ffd700"
                                background Solid("#5c1a1a")
                                hover_background Solid("#7c2222")
                                padding (24, 12, 24, 12)
                        else:
                            vbox:
                                spacing 10
                                xalign 0.5
                                textbutton "Try Again":
                                    xalign 0.5
                                    action Function(sq_quiz_state.retry)
                                    text_size 14
                                    text_color "#f6d79d"
                                    background Solid("#2a1018")
                                    hover_background Solid("#3c1828")
                                    padding (20, 10, 20, 10)
                                textbutton "Skip":
                                    xalign 0.5
                                    action Return(0)
                                    text_size 12
                                    text_color "#5a4a4a"
                                    background Solid("#1a0a0e")
                                    padding (16, 6, 16, 6)
    else:
        ## ── QUESTION SCREEN ──────────────────────────────────────────────────
        $ _q       = sq_quiz_state.questions[_sq_cur]
        $ _answers = _q[1]

        frame:
            xalign 0.5
            yalign 0.5
            xsize 860
            padding (0, 0, 0, 0)
            background Solid("#1a0a0ef8")

            vbox:
                spacing 0

                ## Header
                frame:
                    background Solid("#2a0e0e")
                    xfill True
                    padding (22, 12, 22, 12)
                    hbox:
                        xfill True
                        yalign 0.5
                        vbox:
                            spacing 3
                            hbox:
                                spacing 8
                                text "[sq_quiz_state.icon]" size 15 yalign 0.5
                                text "[sq_quiz_state.title]" size 14 color "#ffd700" bold True yalign 0.5
                            text "[sq_quiz_state.subtitle]" size 10 color "#c8921888" italic True
                        frame:
                            xalign 1.0
                            yalign 0.5
                            background Solid("#1a0a0e")
                            padding (12, 6, 12, 6)
                            text "Q [_sq_cur + 1] / [_sq_total]" size 13 color "#ffd700" bold True

                ## Progress dots
                frame:
                    background Solid("#130609")
                    xfill True
                    padding (20, 8, 20, 8)
                    hbox:
                        xalign 0.5
                        spacing 8
                        for _pi in range(_sq_total):
                            if _pi < _sq_cur:
                                frame:
                                    xysize (32, 6)
                                    background Solid("#f6d79d")
                            elif _pi == _sq_cur:
                                frame:
                                    xysize (32, 6)
                                    background Solid("#ffd700")
                            else:
                                frame:
                                    xysize (32, 6)
                                    background Solid("#2a1a1a")

                ## Question text
                frame:
                    background Solid("#0d0406")
                    xfill True
                    padding (28, 20, 28, 20)
                    text "[_q[0]]":
                        size 16
                        color "#ffffff"
                        line_spacing 4

                ## Feedback banner
                if sq_quiz_state.show_feedback:
                    frame:
                        xfill True
                        padding (24, 12, 24, 12)
                        background Solid("#10b98122" if sq_quiz_state.is_correct else "#f8717122")
                        vbox:
                            spacing 4
                            text ("✓  Correct!" if sq_quiz_state.is_correct else "✗  Not quite."):
                                size 14
                                color ("#10b981" if sq_quiz_state.is_correct else "#f87171")
                                bold True
                            text "[sq_quiz_state.feedback_text]":
                                size 13
                                color "#f1debf"
                                line_spacing 3

                ## Answer buttons — scrollable so all choices are reachable
                frame:
                    background Solid("#0d0406")
                    xfill True
                    padding (20, 12, 20, 4)

                    viewport:
                        id "choices_vp"
                        xfill True
                        ysize 240
                        mousewheel True
                        draggable True
                        scrollbars "vertical"

                        # Add an invisible frame to handle the spacing
                        frame:
                            background None
                            padding (0, 0, 16, 0)  # Adds 16px of padding on the right for the scrollbar
                            
                            vbox:
                                spacing 8
                                xfill True
                                # right_margin 12 <--- REMOVE THIS LINE

                                for _ai in range(len(_answers)):
                                    $ _atxt   = _answers[_ai][0]
                                    $ _acor   = _answers[_ai][1]
                                    $ _fb     = sq_quiz_state.show_feedback
                                    $ _picked = sq_quiz_state.chosen == _ai
                                    $ _lbls   = ["A", "B", "C", "D", "E", "F", "G", "H"]
                                    $ _lbl    = _lbls[_ai] if _ai < len(_lbls) else str(_ai + 1)

                                    if _fb:
                                        if _acor:
                                            frame:
                                                xfill True padding (14, 11, 14, 11)
                                                background Solid("#10b98133")
                                                hbox:
                                                    spacing 10 yalign 0.5
                                                    frame:
                                                        xysize (28, 28) yalign 0.5
                                                        background Solid("#10b981")
                                                        text "✓" size 13 color "#ffffff" xalign 0.5 yalign 0.5
                                                    text "[_atxt]" size 14 color "#10b981" yalign 0.5
                                        elif _picked:
                                            frame:
                                                xfill True padding (14, 11, 14, 11)
                                                background Solid("#f8717133")
                                                hbox:
                                                    spacing 10 yalign 0.5
                                                    frame:
                                                        xysize (28, 28) yalign 0.5
                                                        background Solid("#f87171")
                                                        text "✗" size 13 color "#ffffff" xalign 0.5 yalign 0.5
                                                    text "[_atxt]" size 14 color "#f87171" yalign 0.5
                                        else:
                                            frame:
                                                xfill True padding (14, 11, 14, 11)
                                                background Solid("#140810")
                                                hbox:
                                                    spacing 10 yalign 0.5
                                                    frame:
                                                        xysize (28, 28) yalign 0.5
                                                        background Solid("#1e1020")
                                                        text "[_lbl]" size 12 color "#3a2a3a" bold True xalign 0.5 yalign 0.5
                                                    text "[_atxt]" size 14 color "#3a2a3a" yalign 0.5
                                    else:
                                        button:
                                            xfill True padding (14, 11, 14, 11)
                                            background Solid("#1e0c18")
                                            hover_background Solid("#3c1a30")
                                            action Function(sq_quiz_state.answer, _ai)
                                            hbox:
                                                spacing 10 yalign 0.5
                                                frame:
                                                    xysize (28, 28) yalign 0.5
                                                    background Solid("#3c1a28")
                                                    text "[_lbl]" size 12 color "#c89218" bold True xalign 0.5 yalign 0.5
                                                text "[_atxt]" size 14 color "#f1debf" yalign 0.5

                ## Next / See Results button — outside the viewport
                if sq_quiz_state.show_feedback:
                    frame:
                        background Solid("#0d0406")
                        xfill True
                        padding (20, 4, 20, 16)
                        textbutton ("See Results \u2192" if _sq_cur + 1 >= _sq_total else "Next \u2192"):
                            xalign 1.0
                            action Function(sq_quiz_state.advance)
                            text_size 14
                            text_color "#ffd700"
                            background Solid("#5c1a1a")
                            hover_background Solid("#7c2222")
                            padding (18, 10, 18, 10)


## ============================================================================
## SCREEN: SQ SORT GAME
## call screen sq_sort_game() → _return = "completed" or "skip"
## ============================================================================
screen sq_sort_game():
    on "show" action NullAction()
    modal True
    zorder 200

    add Solid("#0d0d20ee"):
        xysize (1920, 1080)

    if sq_sort_state.done:
        ## ── RESULTS ──────────────────────────────────────────────────────────
        $ _sq_n = len(sq_sort_state.items)
        frame:
            xalign 0.5 yalign 0.5 xsize 560
            padding (0, 0, 0, 0)
            background Solid("#1a0a0ef8")
            vbox:
                spacing 0
                frame:
                    background Solid("#2a0e0e") xfill True padding (24, 14, 24, 14)
                    text "[sq_sort_state.title]" size 18 color "#ffd700" bold True xalign 0.5
                frame:
                    background Solid("#0d0406") xfill True padding (40, 30, 40, 36)
                    vbox:
                        spacing 16 xalign 0.5
                        text "\u2605 SORTED \u2605" xalign 0.5 size 13 color "#c89218" bold True
                        hbox:
                            xalign 0.5 spacing 4
                            text "[sq_sort_state.score]":
                                size 56 color "#ffd700" bold True yalign 0.5
                            text "/[_sq_n]":
                                size 26 color "#f6d79d88" yalign 1.0
                        if sq_sort_state.score == _sq_n:
                            text "Perfect sorting!":
                                xalign 0.5 size 15 color "#10b981"
                        elif sq_sort_state.score >= (_sq_n * 2 // 3):
                            text "Good work!":
                                xalign 0.5 size 15 color "#6ee7b7"
                        else:
                            text "Review the categories.":
                                xalign 0.5 size 15 color "#f87171"
                        null height 8
                        if sq_sort_state.score >= (_sq_n * 2 // 3):
                            textbutton "Claim Reward  \u2605":
                                xalign 0.5 action Return("completed")
                                text_size 15 text_color "#ffd700"
                                background Solid("#5c1a1a") hover_background Solid("#7c2222")
                                padding (24, 12, 24, 12)
                        else:
                            vbox:
                                spacing 8 xalign 0.5
                                textbutton "Try Again":
                                    xalign 0.5 action Function(sq_sort_state.retry)
                                    text_size 14 text_color "#f6d79d"
                                    background Solid("#2a1018") hover_background Solid("#3c1828")
                                    padding (20, 10, 20, 10)
                                textbutton "Skip":
                                    xalign 0.5 action Return("skip")
                                    text_size 12 text_color "#5a4a4a"
                                    background Solid("#1a0a0e") padding (16, 6, 16, 6)
    else:
        ## ── GAME ─────────────────────────────────────────────────────────────
        vbox:
            xalign 0.5 yalign 0.5 spacing 14

            vbox:
                spacing 4 xalign 0.5
                text "[sq_sort_state.title]":
                    xalign 0.5 size 26 color "#ffd700" bold True
                    outlines [(2, "#1a0a0e", 0, 0)]
                text "[sq_sort_state.subtitle]":
                    xalign 0.5 size 13 color "#f1debf"
                    outlines [(1, "#1a0a0e", 0, 0)]

            hbox:
                spacing 28 yalign 0.5

                ## Cards column
                vbox:
                    spacing 6 xsize 500

                    text "ITEMS  ([len(sq_sort_state.assignments)] / [len(sq_sort_state.items)] sorted)":
                        size 12 color "#f6d79d" outlines [(1, "#1a0a0e", 0, 0)]

                    for _ci in range(len(sq_sort_state.items)):
                        $ _itm   = sq_sort_state.items[_ci]
                        $ _asgn  = _ci in sq_sort_state.assignments

                        if _asgn:
                            $ _bx      = sq_sort_state.assignments[_ci]
                            $ _correct = _itm[1]
                            $ _right   = _bx == _correct
                            $ _bcol    = sq_sort_state.bins[_bx][1]
                            button:
                                xsize 490 ysize 50 padding (12, 6, 12, 6)
                                background Solid(_bcol + "44")
                                hover_background Solid(_bcol + "66")
                                action Function(sq_sort_state.unassign, _ci)
                                hbox:
                                    spacing 8 yalign 0.5
                                    text ("✓" if _right else "✗"):
                                        size 15 color ("#10b981" if _right else "#f87171") yalign 0.5
                                    text "[_itm[2]]" size 17 yalign 0.5
                                    text "[_itm[0]]":
                                        size 13 color ("#10b981" if _right else "#f87171") yalign 0.5
                                    text "\u2192 [sq_sort_state.bins[_bx][0]]":
                                        size 11 color _bcol yalign 0.5

                        elif sq_sort_state.selected == _ci:
                            frame:
                                xsize 490 ysize 50 padding (12, 6, 12, 6)
                                background Solid("#5c3a10")
                                hbox:
                                    spacing 8 yalign 0.5
                                    text "\u25ba" size 14 color "#ffd700" yalign 0.5
                                    text "[_itm[2]]" size 17 yalign 0.5
                                    text "[_itm[0]]":
                                        size 13 color "#ffd700" bold True yalign 0.5
                                    text "(select a bin \u2192)":
                                        size 11 color "#ffd70088" yalign 0.5
                        else:
                            button:
                                xsize 490 ysize 50 padding (12, 6, 12, 6)
                                background Solid("#1e0c12")
                                hover_background Solid("#2e1c22")
                                action Function(sq_sort_state.select, _ci)
                                hbox:
                                    spacing 8 yalign 0.5
                                    text "[_itm[2]]" size 17 yalign 0.5
                                    text "[_itm[0]]":
                                        size 13 color "#f1debf" yalign 0.5

                ## Bins column
                vbox:
                    spacing 12 xsize 340 yalign 0.5

                    text ("← Click to assign" if sq_sort_state.selected is not None else "← Select an item first"):
                        size 13 outlines [(1, "#1a0a0e", 0, 0)]
                        color ("#ffd700" if sq_sort_state.selected is not None else "#555555")

                    for _bi in range(len(sq_sort_state.bins)):
                        $ _bin   = sq_sort_state.bins[_bi]
                        $ _bcnt  = sum(1 for v in sq_sort_state.assignments.values() if v == _bi)
                        $ _ready = sq_sort_state.selected is not None

                        if _ready:
                            button:
                                xsize 330 ysize 80 padding (16, 10, 16, 10)
                                background Solid(_bin[1] + "44")
                                hover_background Solid(_bin[1] + "77")
                                action Function(sq_sort_state.assign, _bi)
                                vbox:
                                    spacing 4 yalign 0.5
                                    hbox:
                                        spacing 8
                                        text "[_bin[2]]" size 20 yalign 0.5
                                        text "[_bin[0]]":
                                            size 16 color _bin[1] bold True yalign 0.5
                                    text "[_bcnt] item(s) here":
                                        size 11 color "#f6d79d88"
                        else:
                            frame:
                                xsize 330 ysize 80 padding (16, 10, 16, 10)
                                background Solid(_bin[1] + "1a")
                                vbox:
                                    spacing 4 yalign 0.5
                                    hbox:
                                        spacing 8
                                        text "[_bin[2]]" size 20 yalign 0.5
                                        text "[_bin[0]]":
                                            size 16 color _bin[1] + "88" bold True yalign 0.5
                                    text "[_bcnt] item(s) here":
                                        size 11 color "#f6d79d44"


## ============================================================================
## SCREEN: SQ SCENARIO GAME
## Guided chat-style scenario. Player clicks reply options to explore a topic.
## No right/wrong — each choice reveals a key fact. All paths teach.
## call screen sq_scenario_game() → _return = "completed"
## ============================================================================

init python:

    ## Step format: (speaker_text_str, [(choice_label_str, reveal_text_str), ...])
    ## Summary format: [(icon_str, bullet_text_str), ...]

    class SQScenarioState:
        def __init__(self):
            self.title        = ""
            self.icon         = "💬"
            self.speaker_name  = ""
            self.speaker_color = "#f1debf"
            self.steps        = []
            self.summary      = []
            self.current      = 0
            self.chosen_idx   = None
            self.reveal_text  = None
            self.done         = False

        def setup(self, title, icon, speaker_name, speaker_color, steps, summary):
            self.title         = title
            self.icon          = icon
            self.speaker_name  = speaker_name
            self.speaker_color = speaker_color
            self.steps         = list(steps)
            self.summary       = list(summary)
            self.current       = 0
            self.chosen_idx    = None
            self.reveal_text   = None
            self.done          = False

        def choose(self, idx):
            if self.reveal_text is not None:
                return
            choice = self.steps[self.current][1][idx]
            self.chosen_idx  = idx
            self.reveal_text = choice[1]

        def advance(self):
            self.current    += 1
            self.chosen_idx  = None
            self.reveal_text = None
            if self.current >= len(self.steps):
                self.done = True

    sq_scenario_state = SQScenarioState()


screen sq_scenario_game():
    on "show" action NullAction()
    modal True
    zorder 200

    add Solid("#070d18") alpha 0.98

    $ _sc_total = len(sq_scenario_state.steps)
    $ _sc_cur   = sq_scenario_state.current

    if sq_scenario_state.done:
        ## ── SUMMARY SCREEN ───────────────────────────────────────────────────
        frame:
            xalign 0.5 yalign 0.5 xsize 660
            padding (0, 0, 0, 0)
            background Solid("#0b1622f8")

            vbox:
                spacing 0

                ## Header
                frame:
                    background Solid("#0c2236")
                    xfill True padding (24, 14, 24, 14)
                    hbox:
                        spacing 10
                        text "[sq_scenario_state.icon]" size 18 yalign 0.5
                        text "[sq_scenario_state.title]" size 16 color "#4dd9f0" bold True yalign 0.5
                        text " — Done" size 13 color "#4dd9f066" yalign 0.5

                ## Summary body
                frame:
                    background Solid("#070d18")
                    xfill True padding (36, 26, 36, 30)
                    vbox:
                        spacing 12

                        text "WHAT YOU DISCOVERED":
                            size 11 color "#4dd9f0" bold True xalign 0.5
                            kerning 2

                        null height 4

                        for _si in range(len(sq_scenario_state.summary)):
                            $ _s_icon = sq_scenario_state.summary[_si][0]
                            $ _s_text = sq_scenario_state.summary[_si][1]
                            frame:
                                background Solid("#0c1e2e")
                                xfill True padding (14, 10, 14, 10)
                                hbox:
                                    spacing 14 yalign 0.5
                                    frame:
                                        xysize (32, 32) yalign 0.5
                                        background Solid("#102840")
                                        text "[_s_icon]" size 16 xalign 0.5 yalign 0.5
                                    text "[_s_text]":
                                        size 13 color "#c8e8f4" yalign 0.5 line_spacing 2

                        null height 10

                        textbutton "Claim Reward  ★":
                            xalign 0.5
                            action Return("completed")
                            text_size 15 text_color "#4dd9f0"
                            background Solid("#0c2236")
                            hover_background Solid("#163a50")
                            padding (28, 14, 28, 14)
    else:
        ## ── CONVERSATION SCREEN ──────────────────────────────────────────────
        $ _step    = sq_scenario_state.steps[_sc_cur]
        $ _choices = _step[1]

        frame:
            xalign 0.5 yalign 0.5 xsize 800
            padding (0, 0, 0, 0)
            background Solid("#0b1622f8")

            vbox:
                spacing 0

                ## Header
                frame:
                    background Solid("#0c2236")
                    xfill True padding (22, 12, 22, 12)
                    hbox:
                        xfill True yalign 0.5
                        hbox:
                            spacing 8
                            text "[sq_scenario_state.icon]" size 15 yalign 0.5
                            text "[sq_scenario_state.title]" size 14 color "#4dd9f0" bold True yalign 0.5
                        frame:
                            xalign 1.0 yalign 0.5
                            background Solid("#070d18")
                            padding (12, 6, 12, 6)
                            text "Step [_sc_cur + 1] / [_sc_total]" size 12 color "#4dd9f0"

                ## Progress bar
                frame:
                    background Solid("#060c16")
                    xfill True padding (20, 6, 20, 6)
                    hbox:
                        xalign 0.5 spacing 8
                        for _pi in range(_sc_total):
                            if _pi < _sc_cur:
                                frame:
                                    xysize (40, 5) background Solid("#4dd9f0")
                            elif _pi == _sc_cur:
                                frame:
                                    xysize (40, 5) background Solid("#9aecff")
                            else:
                                frame:
                                    xysize (40, 5) background Solid("#162030")

                ## Speaker message bubble
                frame:
                    background Solid("#070d18")
                    xfill True padding (28, 18, 28, 14)
                    vbox:
                        spacing 6
                        text "[sq_scenario_state.speaker_name]":
                            size 12 color "[sq_scenario_state.speaker_color]" bold True
                        frame:
                            background Solid("#0c1e30")
                            padding (18, 13, 18, 13)
                            xfill True
                            text "[_step[0]]":
                                size 15 color "#ddf0f8" line_spacing 5

                ## Reveal box — appears after a choice is clicked
                if sq_scenario_state.reveal_text is not None:
                    frame:
                        background Solid("#0a2018")
                        xfill True padding (24, 14, 24, 14)
                        vbox:
                            spacing 6
                            text "✓  Key fact:":
                                size 12 color "#4ded9a" bold True
                            text "[sq_scenario_state.reveal_text]":
                                size 14 color "#b8f0d0" line_spacing 4

                ## Choice buttons or Next button
                frame:
                    background Solid("#060c16")
                    xfill True padding (20, 14, 20, 14)

                    if sq_scenario_state.reveal_text is None:
                        ## Show clickable choice buttons
                        vbox:
                            spacing 8
                            text "How do you reply?":
                                size 11 color "#4dd9f066" xalign 0.5
                            null height 2
                            for _ci in range(len(_choices)):
                                $ _clabel = _choices[_ci][0]
                                textbutton "[_clabel]":
                                    xfill True
                                    action Function(sq_scenario_state.choose, _ci)
                                    text_size 13 text_color "#ddf0f8"
                                    background Solid("#101e30")
                                    hover_background Solid("#1a3040")
                                    padding (18, 12, 18, 12)
                    else:
                        ## Show the chosen reply (greyed) and Next button
                        vbox:
                            spacing 8
                            for _ci in range(len(_choices)):
                                $ _clabel = _choices[_ci][0]
                                if _ci == sq_scenario_state.chosen_idx:
                                    frame:
                                        xfill True padding (18, 12, 18, 12)
                                        background Solid("#0c2e20")
                                        hbox:
                                            spacing 8 yalign 0.5
                                            text "✓" size 14 color "#4ded9a" yalign 0.5
                                            text "[_clabel]":
                                                size 13 color "#4ded9a" yalign 0.5
                                else:
                                    frame:
                                        xfill True padding (18, 12, 18, 12)
                                        background Solid("#0a1218")
                                        text "[_clabel]":
                                            size 13 color "#3a5060"
                            textbutton ("See Summary →" if _sc_cur + 1 >= _sc_total else "Next →"):
                                xalign 1.0
                                action Function(sq_scenario_state.advance)
                                text_size 14 text_color "#4dd9f0"
                                background Solid("#0c2236")
                                hover_background Solid("#163a50")
                                padding (20, 10, 20, 10)


## ============================================================================
## STATES: SQ INBOX GAME + SQ FUNDING GAME
## ============================================================================

init python:

    ## ── SQ INBOX STATE ───────────────────────────────────────────────────────
    ## Route student cases to the right support service.
    ## case format:   (emoji, name, situation_text, correct_idx, hint_text)
    ## choice format: (label, icon, color_hex)

    class SQInboxState:
        def __init__(self):
            self.title      = ""
            self.icon       = "📬"
            self.cases      = []
            self.choices    = []
            self.current    = 0
            self.score      = 0
            self.chosen     = None
            self.is_correct = False
            self.phase      = "choose"   # "choose" | "feedback"
            self.done       = False

        def setup(self, title, icon, cases, choices):
            self.title   = title
            self.icon    = icon
            self.cases   = list(cases)
            self.choices = list(choices)
            self.current = 0
            self.score   = 0
            self.chosen  = None
            self.phase   = "choose"
            self.done    = False

        def choose(self, idx):
            if self.phase != "choose":
                return
            self.chosen     = idx
            self.is_correct = (idx == self.cases[self.current][3])
            if self.is_correct:
                self.score += 1
            self.phase = "feedback"

        def advance(self):
            self.current += 1
            self.chosen = None
            self.phase  = "choose"
            if self.current >= len(self.cases):
                self.done = True

    sq_inbox_state = SQInboxState()


    ## ── SQ FUNDING STATE ─────────────────────────────────────────────────────
    ## Apply financial programs to fill a student's budget gaps.
    ## student format: (emoji, name, situation, [(seg_label, prog_idx, color), ...])
    ## program format: (label, icon, color, short_blurb)

    class SQFundingState:
        def __init__(self):
            self.title    = ""
            self.icon     = "💰"
            self.students = []
            self.programs = []
            self.current  = 0
            self.filled   = set()   # set of (student_idx, seg_idx)
            self.done     = False

        def setup(self, title, icon, students, programs):
            self.title    = title
            self.icon     = icon
            self.students = list(students)
            self.programs = list(programs)
            self.current  = 0
            self.filled   = set()
            self.done     = False

        def activate(self, prog_idx):
            segs = self.students[self.current][3]
            for i, seg in enumerate(segs):
                if seg[1] == prog_idx:
                    self.filled.add((self.current, i))

        def is_applied(self, prog_idx):
            segs = self.students[self.current][3]
            return any(
                (self.current, i) in self.filled
                for i, seg in enumerate(segs)
                if seg[1] == prog_idx
            )

        def current_complete(self):
            segs = self.students[self.current][3]
            return all((self.current, i) in self.filled for i in range(len(segs)))

        def next_student(self):
            self.current += 1
            if self.current >= len(self.students):
                self.done = True

    sq_funding_state = SQFundingState()


## Bar fill animation — fades+slides in from left when a segment is filled
transform bar_fill_anim:
    alpha 0.0 xoffset -18
    ease 0.35 alpha 1.0 xoffset 0


## ============================================================================
## SCREEN: SQ INBOX GAME
## Route 5 student cases to the correct GCSU/Peer Facilitators resource.
## Clicking a routing button shows immediate visual status + hint text.
## call screen sq_inbox_game() → _return = "completed"
## ============================================================================

screen sq_inbox_game():
    on "show" action NullAction()
    modal True
    zorder 200

    add Solid("#070d18") alpha 0.98

    $ _in_n   = len(sq_inbox_state.cases)
    $ _in_i   = sq_inbox_state.current

    if sq_inbox_state.done:
        ## ── RESULTS ──────────────────────────────────────────────────────────
        frame:
            xalign 0.5 yalign 0.5 xsize 580
            padding (0, 0, 0, 0)
            background Solid("#0b1622f8")
            vbox:
                spacing 0
                frame:
                    background Solid("#0c2236") xfill True padding (24, 14, 24, 14)
                    hbox:
                        spacing 8
                        text "[sq_inbox_state.icon]" size 18 yalign 0.5
                        text "[sq_inbox_state.title]" size 16 color "#4dd9f0" bold True yalign 0.5
                frame:
                    background Solid("#070d18") xfill True padding (40, 32, 40, 36)
                    vbox:
                        spacing 18 xalign 0.5
                        text "★  CASES HANDLED  ★":
                            xalign 0.5 size 12 color "#4dd9f0" bold True kerning 2
                        hbox:
                            xalign 0.5 spacing 4
                            text "[sq_inbox_state.score]":
                                size 64 color "#4dd9f0" bold True yalign 0.5
                            text "/[_in_n]":
                                size 30 color "#4dd9f055" yalign 1.0
                        if sq_inbox_state.score == _in_n:
                            text "Perfect routing. Every student reached the right support.":
                                xalign 0.5 size 13 color "#4ded9a"
                        elif sq_inbox_state.score >= 3:
                            text "Good instincts. Review the cases you missed.":
                                xalign 0.5 size 13 color "#9aecff"
                        else:
                            text "The hints showed the right paths. Review them before you go.":
                                xalign 0.5 size 13 color "#f87171"
                        null height 8
                        textbutton "Claim Reward  ★":
                            xalign 0.5
                            action Return("completed")
                            text_size 15 text_color "#4dd9f0"
                            background Solid("#0c2236")
                            hover_background Solid("#163a50")
                            padding (28, 14, 28, 14)

    else:
        ## ── ACTIVE CASE ──────────────────────────────────────────────────────
        $ _case     = sq_inbox_state.cases[_in_i]
        $ _c_emoji  = _case[0]
        $ _c_name   = _case[1]
        $ _c_sit    = _case[2]
        $ _c_hint   = _case[4]
        $ _choices  = sq_inbox_state.choices

        vbox:
            xalign 0.5 yalign 0.5
            xsize 880
            spacing 10

            ## Header + progress pips
            frame:
                background Solid("#0b1622") xfill True padding (18, 10, 18, 10)
                hbox:
                    xfill True yalign 0.5
                    hbox:
                        spacing 8 yalign 0.5
                        text "[sq_inbox_state.icon]" size 16 yalign 0.5
                        text "[sq_inbox_state.title]" size 14 color "#4dd9f0" bold True yalign 0.5
                    hbox:
                        xalign 1.0 spacing 5
                        for _pi in range(_in_n):
                            if _pi < _in_i:
                                frame:
                                    xysize (24, 24) background Solid("#4dd9f0")
                                    text "✓" size 10 color "#070d18" xalign 0.5 yalign 0.5 bold True
                            elif _pi == _in_i:
                                frame:
                                    xysize (24, 24) background Solid("#9aecff")
                                    text "[_pi+1]" size 10 color "#070d18" xalign 0.5 yalign 0.5 bold True
                            else:
                                frame:
                                    xysize (24, 24) background Solid("#162030")
                                    text "[_pi+1]" size 10 color "#3a5060" xalign 0.5 yalign 0.5

            ## Case card
            frame:
                background Solid("#0b1622") xfill True padding (0, 0, 0, 0)
                vbox:
                    spacing 0

                    ## Student row
                    frame:
                        background Solid("#0c1e30") xfill True padding (20, 14, 20, 14)
                        hbox:
                            spacing 16 yalign 0.5
                            frame:
                                xysize (52, 52) background Solid("#102840")
                                text "[_c_emoji]" size 26 xalign 0.5 yalign 0.5
                            vbox:
                                spacing 3 yalign 0.5
                                text "[_c_name]" size 15 color "#9aecff" bold True
                                if sq_inbox_state.phase == "choose":
                                    text "● needs support" size 11 color "#f8717188"
                                elif sq_inbox_state.is_correct:
                                    text "✓  correctly routed" size 11 color "#4ded9a" bold True
                                else:
                                    text "✗  see correct path below" size 11 color "#f87171"

                    ## Situation text
                    frame:
                        background Solid("#070d18") xfill True padding (24, 16, 24, 16)
                        text "[_c_sit]":
                            size 14 color "#c8e8f4" line_spacing 5

                    ## Feedback box — visible after routing
                    if sq_inbox_state.phase == "feedback":
                        frame:
                            background Solid("#0a2018" if sq_inbox_state.is_correct else "#1e0c10")
                            xfill True padding (22, 13, 22, 13)
                            vbox:
                                spacing 5
                                text ("✓  Right call." if sq_inbox_state.is_correct else "✗  Not the best match — here's why:"):
                                    size 12
                                    color ("#4ded9a" if sq_inbox_state.is_correct else "#f87171")
                                    bold True
                                text "[_c_hint]":
                                    size 13 color "#b8f0d0" line_spacing 4

            ## Routing buttons — 2 × 2 grid
            frame:
                background Solid("#060c16") xfill True padding (14, 12, 14, 12)
                vbox:
                    spacing 8

                    if sq_inbox_state.phase == "choose":
                        text "Route to →":
                            size 11 color "#4dd9f044" xalign 0.5
                        null height 2

                    ## Row 1: choices 0 and 1
                    hbox:
                        xfill True spacing 8
                        for _ci in [0, 1]:
                            $ _ch      = _choices[_ci]
                            $ _ch_lbl  = _ch[0]
                            $ _ch_icon = _ch[1]
                            $ _ch_col  = _ch[2]
                            $ _chosen  = sq_inbox_state.chosen == _ci
                            $ _correct = _ci == _case[3]

                            if sq_inbox_state.phase == "choose":
                                button:
                                    xfill True padding (14, 14, 14, 14)
                                    background Solid("#101e30")
                                    hover_background Solid("#1a3040")
                                    action Function(sq_inbox_state.choose, _ci)
                                    hbox:
                                        spacing 12 yalign 0.5
                                        text "[_ch_icon]" size 26 yalign 0.5
                                        text "[_ch_lbl]" size 13 color "#ddf0f8" yalign 0.5
                            elif _chosen and sq_inbox_state.is_correct:
                                frame:
                                    xfill True padding (14, 14, 14, 14)
                                    background Solid("#0a2e18")
                                    hbox:
                                        spacing 12 yalign 0.5
                                        text "[_ch_icon]" size 26 yalign 0.5
                                        text "[_ch_lbl]" size 13 color "#4ded9a" bold True yalign 0.5
                            elif _chosen:
                                frame:
                                    xfill True padding (14, 14, 14, 14)
                                    background Solid("#2e0a10")
                                    hbox:
                                        spacing 12 yalign 0.5
                                        text "[_ch_icon]" size 26 yalign 0.5
                                        text "[_ch_lbl]" size 13 color "#f87171" yalign 0.5
                            elif _correct:
                                frame:
                                    xfill True padding (14, 14, 14, 14)
                                    background Solid("#0a2e18")
                                    hbox:
                                        spacing 12 yalign 0.5
                                        text "[_ch_icon]" size 26 yalign 0.5
                                        text "[_ch_lbl]" size 13 color "#4ded9a" yalign 0.5
                            else:
                                frame:
                                    xfill True padding (14, 14, 14, 14)
                                    background Solid("#0a1420")
                                    hbox:
                                        spacing 12 yalign 0.5
                                        text "[_ch_icon]" size 26 yalign 0.5
                                        text "[_ch_lbl]" size 13 color "#3a5060" yalign 0.5

                    ## Row 2: choices 2 and 3
                    hbox:
                        xfill True spacing 8
                        for _ci in [2, 3]:
                            $ _ch      = _choices[_ci]
                            $ _ch_lbl  = _ch[0]
                            $ _ch_icon = _ch[1]
                            $ _ch_col  = _ch[2]
                            $ _chosen  = sq_inbox_state.chosen == _ci
                            $ _correct = _ci == _case[3]

                            if sq_inbox_state.phase == "choose":
                                button:
                                    xfill True padding (14, 14, 14, 14)
                                    background Solid("#101e30")
                                    hover_background Solid("#1a3040")
                                    action Function(sq_inbox_state.choose, _ci)
                                    hbox:
                                        spacing 12 yalign 0.5
                                        text "[_ch_icon]" size 26 yalign 0.5
                                        text "[_ch_lbl]" size 13 color "#ddf0f8" yalign 0.5
                            elif _chosen and sq_inbox_state.is_correct:
                                frame:
                                    xfill True padding (14, 14, 14, 14)
                                    background Solid("#0a2e18")
                                    hbox:
                                        spacing 12 yalign 0.5
                                        text "[_ch_icon]" size 26 yalign 0.5
                                        text "[_ch_lbl]" size 13 color "#4ded9a" bold True yalign 0.5
                            elif _chosen:
                                frame:
                                    xfill True padding (14, 14, 14, 14)
                                    background Solid("#2e0a10")
                                    hbox:
                                        spacing 12 yalign 0.5
                                        text "[_ch_icon]" size 26 yalign 0.5
                                        text "[_ch_lbl]" size 13 color "#f87171" yalign 0.5
                            elif _correct:
                                frame:
                                    xfill True padding (14, 14, 14, 14)
                                    background Solid("#0a2e18")
                                    hbox:
                                        spacing 12 yalign 0.5
                                        text "[_ch_icon]" size 26 yalign 0.5
                                        text "[_ch_lbl]" size 13 color "#4ded9a" yalign 0.5
                            else:
                                frame:
                                    xfill True padding (14, 14, 14, 14)
                                    background Solid("#0a1420")
                                    hbox:
                                        spacing 12 yalign 0.5
                                        text "[_ch_icon]" size 26 yalign 0.5
                                        text "[_ch_lbl]" size 13 color "#3a5060" yalign 0.5

                    ## Next button — only after routing
                    if sq_inbox_state.phase == "feedback":
                        textbutton ("See Results →" if _in_i + 1 >= _in_n else "Next Case →"):
                            xalign 1.0
                            action Function(sq_inbox_state.advance)
                            text_size 14 text_color "#4dd9f0"
                            background Solid("#0c2236")
                            hover_background Solid("#163a50")
                            padding (20, 10, 20, 10)


## ============================================================================
## SCREEN: SQ FUNDING GAME
## Click program buttons to fill a student's budget gaps.
## Each program fills its specific segments with a bar-fill animation.
## call screen sq_funding_game() → _return = "completed"
## ============================================================================

screen sq_funding_game():
    on "show" action NullAction()
    modal True
    zorder 200

    add Solid("#07100a") alpha 0.98

    $ _fd_total = len(sq_funding_state.students)
    $ _fd_cur   = sq_funding_state.current

    if sq_funding_state.done:
        ## ── RESULTS ──────────────────────────────────────────────────────────
        frame:
            xalign 0.5 yalign 0.5 xsize 620
            padding (0, 0, 0, 0)
            background Solid("#091610f8")
            vbox:
                spacing 0
                frame:
                    background Solid("#0c2e1a") xfill True padding (24, 14, 24, 14)
                    hbox:
                        spacing 8
                        text "[sq_funding_state.icon]" size 18 yalign 0.5
                        text "[sq_funding_state.title]" size 16 color "#4ded9a" bold True yalign 0.5
                frame:
                    background Solid("#07100a") xfill True padding (40, 32, 40, 36)
                    vbox:
                        spacing 16 xalign 0.5
                        text "★  ALL STUDENTS FUNDED  ★":
                            xalign 0.5 size 12 color "#4ded9a" bold True kerning 2
                        null height 4
                        frame:
                            background Solid("#0c2e1a") xfill True padding (20, 16, 20, 16)
                            vbox:
                                spacing 10
                                for _pi in range(len(sq_funding_state.programs)):
                                    $ _p = sq_funding_state.programs[_pi]
                                    hbox:
                                        spacing 12 yalign 0.5
                                        frame:
                                            xysize (36, 36) background Solid(_p[2] + "66")
                                            text "[_p[1]]" size 18 xalign 0.5 yalign 0.5
                                        vbox:
                                            spacing 2 yalign 0.5
                                            text "[_p[0]]" size 14 color _p[2] bold True
                                            text "[_p[3]]" size 12 color "#9ad0b8"
                        null height 8
                        text "These three programs are not mutually exclusive.":
                            xalign 0.5 size 13 color "#c8e8d0" italic True
                        null height 4
                        textbutton "Claim Reward  ★":
                            xalign 0.5
                            action Return("completed")
                            text_size 15 text_color "#4ded9a"
                            background Solid("#0c2e1a")
                            hover_background Solid("#163a26")
                            padding (28, 14, 28, 14)

    else:
        ## ── ACTIVE STUDENT ───────────────────────────────────────────────────
        $ _stu     = sq_funding_state.students[_fd_cur]
        $ _s_emoji = _stu[0]
        $ _s_name  = _stu[1]
        $ _s_sit   = _stu[2]
        $ _s_segs  = _stu[3]

        vbox:
            xalign 0.5 yalign 0.5
            xsize 860
            spacing 10

            ## Header + student counter
            frame:
                background Solid("#091610") xfill True padding (18, 10, 18, 10)
                hbox:
                    xfill True yalign 0.5
                    hbox:
                        spacing 8 yalign 0.5
                        text "[sq_funding_state.icon]" size 16 yalign 0.5
                        text "[sq_funding_state.title]" size 14 color "#4ded9a" bold True yalign 0.5
                    hbox:
                        xalign 1.0 spacing 5
                        for _pi in range(_fd_total):
                            if _pi < _fd_cur:
                                frame:
                                    xysize (24, 24) background Solid("#4ded9a")
                                    text "✓" size 10 color "#07100a" xalign 0.5 yalign 0.5 bold True
                            elif _pi == _fd_cur:
                                frame:
                                    xysize (24, 24) background Solid("#9af4c8")
                                    text "[_pi+1]" size 10 color "#07100a" xalign 0.5 yalign 0.5 bold True
                            else:
                                frame:
                                    xysize (24, 24) background Solid("#102818")
                                    text "[_pi+1]" size 10 color "#3a6050" xalign 0.5 yalign 0.5

            ## Student profile
            frame:
                background Solid("#091610") xfill True padding (0, 0, 0, 0)
                vbox:
                    spacing 0
                    frame:
                        background Solid("#0c1e14") xfill True padding (20, 14, 20, 14)
                        hbox:
                            spacing 16 yalign 0.5
                            frame:
                                xysize (52, 52) background Solid("#102818")
                                text "[_s_emoji]" size 28 xalign 0.5 yalign 0.5
                            vbox:
                                spacing 3 yalign 0.5
                                text "[_s_name]" size 15 color "#9af4c8" bold True
                                text "[_s_sit]" size 12 color "#7ab898" line_spacing 3

            ## Budget gap bars
            frame:
                background Solid("#07100a") xfill True padding (22, 16, 22, 12)
                vbox:
                    spacing 6
                    text "BUDGET GAPS":
                        size 10 color "#4ded9a88" bold True kerning 2
                    null height 4
                    for _si in range(len(_s_segs)):
                        $ _seg       = _s_segs[_si]
                        $ _seg_lbl   = _seg[0]
                        $ _seg_prog  = _seg[1]
                        $ _seg_color = _seg[2]
                        $ _seg_prog_name = sq_funding_state.programs[_seg_prog][0]
                        $ _is_filled = (_fd_cur, _si) in sq_funding_state.filled

                        hbox:
                            xfill True spacing 10 yalign 0.5
                            frame:
                                xsize 230 ysize 44
                                background Solid("#0c1e14")
                                text "[_seg_lbl]":
                                    size 12 color "#7ab898" xalign 0.5 yalign 0.5
                            frame:
                                xfill True ysize 44
                                background Solid("#0c1810")
                                if _is_filled:
                                    frame:
                                        xfill True ysize 44
                                        background Solid(_seg_color)
                                        at bar_fill_anim
                                        hbox:
                                            xfill True yalign 0.5
                                            text "✓  [_seg_prog_name]":
                                                size 13 color "#ffffff" xalign 0.5 yalign 0.5 bold True

            ## Program buttons
            frame:
                background Solid("#060e08") xfill True padding (18, 14, 18, 14)
                vbox:
                    spacing 8
                    text "APPLY PROGRAMS  →  click to fill the gaps":
                        size 10 color "#4ded9a55" xalign 0.5 kerning 1
                    null height 2
                    hbox:
                        xalign 0.5 spacing 12
                        for _pi in range(len(sq_funding_state.programs)):
                            $ _prog       = sq_funding_state.programs[_pi]
                            $ _prog_lbl   = _prog[0]
                            $ _prog_icon  = _prog[1]
                            $ _prog_color = _prog[2]
                            $ _prog_blurb = _prog[3]
                            $ _applied    = sq_funding_state.is_applied(_pi)

                            if _applied:
                                frame:
                                    xsize 240 ysize 72
                                    background Solid(_prog_color + "33")
                                    padding (14, 10, 14, 10)
                                    vbox:
                                        spacing 4 xalign 0.5 yalign 0.5
                                        hbox:
                                            spacing 8 xalign 0.5
                                            text "[_prog_icon]" size 20
                                            text "[_prog_lbl]" size 14 color _prog_color bold True
                                        text "✓  Applied" size 11 color _prog_color xalign 0.5
                            else:
                                button:
                                    xsize 240 ysize 72
                                    background Solid("#0c1810")
                                    hover_background Solid(_prog_color + "22")
                                    action Function(sq_funding_state.activate, _pi)
                                    padding (14, 10, 14, 10)
                                    vbox:
                                        spacing 4 xalign 0.5 yalign 0.5
                                        hbox:
                                            spacing 8 xalign 0.5
                                            text "[_prog_icon]" size 20
                                            text "[_prog_lbl]" size 14 color "#7ab898" bold True
                                        text "[_prog_blurb]" size 10 color "#3a6050" xalign 0.5

                    ## Funded indicator + Next button
                    if sq_funding_state.current_complete():
                        null height 6
                        frame:
                            background Solid("#0a2818") xfill True padding (18, 12, 18, 12)
                            hbox:
                                xfill True yalign 0.5
                                vbox:
                                    spacing 3
                                    text "✓  [_s_name] is funded.":
                                        size 14 color "#4ded9a" bold True
                                    text "All three programs are active — none cancel each other out.":
                                        size 12 color "#7ab898"
                                textbutton ("See Results →" if _fd_cur + 1 >= _fd_total else "Next Student →"):
                                    xalign 1.0 yalign 0.5
                                    action Function(sq_funding_state.next_student)
                                    text_size 14 text_color "#4ded9a"
                                    background Solid("#0c2e1a")
                                    hover_background Solid("#163a26")
                                    padding (20, 10, 20, 10)


## ============================================================================
## SCREEN: SQ TIMELINE GAME
## call screen sq_timeline_game() → _return = score_int
## ============================================================================
screen sq_timeline_game():
    on "show" action NullAction()
    modal True
    zorder 200

    add Solid("#0d0d20ee"):
        xysize (1920, 1080)

    if sq_timeline_state.done:
        ## ── RESULTS ──────────────────────────────────────────────────────────
        $ _tl_n       = len(sq_timeline_state.events)
        $ _tl_correct = sorted(range(_tl_n), key=lambda i: sq_timeline_state.events[i][0])

        frame:
            xalign 0.5 yalign 0.5 xsize 640
            padding (0, 0, 0, 0)
            background Solid("#1a0a0ef8")
            vbox:
                spacing 0
                frame:
                    background Solid("#2a0e0e") xfill True padding (24, 14, 24, 14)
                    text "HERITAGE TIMELINE — RESULT" size 16 color "#ffd700" bold True xalign 0.5

                frame:
                    background Solid("#0d0406") xfill True padding (28, 20, 28, 28)
                    vbox:
                        spacing 12 xalign 0.5

                        hbox:
                            xalign 0.5 spacing 4
                            text "[sq_timeline_state.score]":
                                size 52 color "#ffd700" bold True yalign 0.5
                            text "/[_tl_n] in correct position":
                                size 17 color "#f6d79d88" yalign 1.0

                        text "Correct chronological order:":
                            size 12 color "#c89218" xalign 0.5

                        for _oi in range(_tl_n):
                            $ _ei  = _tl_correct[_oi]
                            $ _ev  = sq_timeline_state.events[_ei]
                            $ _pp  = sq_timeline_state.order.index(_ei) if _ei in sq_timeline_state.order else -1
                            $ _ok  = _pp == _oi

                            frame:
                                xfill True padding (12, 7, 12, 7)
                                background Solid("#10b98133" if _ok else "#f8717122")
                                hbox:
                                    spacing 10 yalign 0.5
                                    text str(_oi + 1) + "." size 13 color "#f6d79d88" xsize 20 yalign 0.5
                                    text str(_ev[0]):
                                        size 14 color _ev[3] bold True yalign 0.5 xsize 50
                                    text "[_ev[1]]":
                                        size 13 color "#f1debf" yalign 0.5
                                    text ("✓" if _ok else ("(you: #" + str(_pp + 1) + ")" if _pp >= 0 else "?")):
                                        xalign 1.0 yalign 0.5 size 12
                                        color ("#10b981" if _ok else "#f87171")

                        null height 8
                        if sq_timeline_state.score >= _tl_n - 1:
                            textbutton "Claim Reward  \u2605":
                                xalign 0.5 action Return(sq_timeline_state.score)
                                text_size 15 text_color "#ffd700"
                                background Solid("#5c1a1a") hover_background Solid("#7c2222")
                                padding (24, 12, 24, 12)
                        else:
                            vbox:
                                spacing 8 xalign 0.5
                                textbutton "Try Again":
                                    xalign 0.5 action Function(sq_timeline_state.retry)
                                    text_size 14 text_color "#f6d79d"
                                    background Solid("#2a1018") hover_background Solid("#3c1828")
                                    padding (20, 10, 20, 10)
                                textbutton "Skip":
                                    xalign 0.5 action Return(0)
                                    text_size 12 text_color "#5a4a4a"
                                    background Solid("#1a0a0e") padding (16, 6, 16, 6)
    else:
        ## ── GAME ─────────────────────────────────────────────────────────────
        vbox:
            xalign 0.5 yalign 0.5 spacing 14

            vbox:
                spacing 4 xalign 0.5
                text "HERITAGE TIMELINE":
                    xalign 0.5 size 28 color "#ffd700" bold True
                    outlines [(2, "#1a0a0e", 0, 0)]
                text "Click events in CHRONOLOGICAL ORDER — earliest to latest":
                    xalign 0.5 size 14 color "#f1debf"
                    outlines [(1, "#1a0a0e", 0, 0)]

            hbox:
                xalign 0.5 spacing 20

                ## Order slots (left column)
                vbox:
                    spacing 6 xsize 72 yalign 0.5
                    for _si in range(len(sq_timeline_state.events)):
                        frame:
                            xsize 66 ysize 66 yalign 0.5
                            background Solid("#1e0c12")
                            vbox:
                                xalign 0.5 yalign 0.5 spacing 2
                                text str(_si + 1) + ".":
                                    size 11 color "#c89218" xalign 0.5
                                if _si < len(sq_timeline_state.order):
                                    $ _ev_sl = sq_timeline_state.events[sq_timeline_state.order[_si]]
                                    text str(_ev_sl[0]):
                                        size 15 color _ev_sl[3] bold True xalign 0.5
                                else:
                                    text "?":
                                        size 20 color "#2a1a1a" xalign 0.5

                ## Event cards (right column)
                vbox:
                    spacing 8 xsize 720

                    for _ei in range(len(sq_timeline_state.events)):
                        $ _ev      = sq_timeline_state.events[_ei]
                        $ _pos     = sq_timeline_state.order.index(_ei) if _ei in sq_timeline_state.order else -1

                        if _pos >= 0:
                            frame:
                                xsize 710 ysize 66 padding (14, 8, 14, 8)
                                background Solid(_ev[3] + "33")
                                hbox:
                                    spacing 12 yalign 0.5
                                    frame:
                                        xysize (30, 30) yalign 0.5
                                        background Solid(_ev[3])
                                        text str(_pos + 1):
                                            size 15 color "#ffffff" bold True xalign 0.5 yalign 0.5
                                    vbox:
                                        spacing 2 yalign 0.5
                                        text "[_ev[1]]":
                                            size 15 color _ev[3] bold True
                                        text "[_ev[2]]":
                                            size 11 color "#9a8a8a"
                        else:
                            button:
                                xsize 710 ysize 66 padding (14, 8, 14, 8)
                                background Solid("#1e0c12")
                                hover_background Solid("#2e1c22")
                                action Function(sq_timeline_state.pick, _ei)
                                hbox:
                                    spacing 12 yalign 0.5
                                    frame:
                                        xysize (30, 30) yalign 0.5
                                        background Solid("#2a1a2a")
                                        text "?" size 16 color "#5a4a5a" xalign 0.5 yalign 0.5
                                    vbox:
                                        spacing 2 yalign 0.5
                                        text "[_ev[1]]":
                                            size 15 color "#f1debf" bold True
                                        text "[_ev[2]]":
                                            size 11 color "#7a6a7a"

            hbox:
                xalign 0.5 spacing 20
                textbutton "\u21a9 Undo Last":
                    action Function(sq_timeline_state.undo)
                    text_size 13 text_color "#f6d79d"
                    background Solid("#2a1018") hover_background Solid("#3c1828")
                    padding (14, 8, 14, 8)
                text "[len(sq_timeline_state.order)] / [len(sq_timeline_state.events)] placed":
                    size 13 color "#c89218" yalign 0.5
                    outlines [(1, "#1a0a0e", 0, 0)]


## ============================================================================
## SCREEN: SQ GWA CALCULATOR GAME
## call screen sq_gwa_calc_game() → _return = "completed" or "partial"
## Click grade cells to cycle through UP grades; live GWA + scholarship shown.
## ============================================================================
screen sq_gwa_calc_game():
    on "show" action Function(sq_gwa_state.reset)
    modal True
    zorder 200

    add Solid("#0d0d20ee"):
        xysize (1920, 1080)

    $ _gwa           = sq_gwa_state.calc_gwa()
    $ _sch, _scol    = sq_gwa_state.scholarship_for(_gwa)
    $ _all           = sq_gwa_state.all_set()

    vbox:
        xalign 0.5 yalign 0.5 spacing 14

        vbox:
            spacing 4 xalign 0.5
            text "GWA CALCULATOR":
                xalign 0.5 size 28 color "#ffd700" bold True
                outlines [(2, "#1a0a0e", 0, 0)]
            text "Click a course row to cycle its grade  (1.00 \u2192 1.25 \u2192 ... \u2192 5.00 \u2192 repeat)":
                xalign 0.5 size 13 color "#f1debf"
                outlines [(1, "#1a0a0e", 0, 0)]

        hbox:
            xalign 0.5 spacing 22 yalign 0.5

            ## Course table
            frame:
                xsize 620 padding (0, 0, 0, 0)
                background Solid("#1a0a0ef8")
                vbox:
                    spacing 0
                    frame:
                        background Solid("#2a0e0e") xfill True padding (16, 10, 16, 10)
                        hbox:
                            xfill True
                            text "COURSE" size 13 color "#ffd700" bold True xsize 360
                            text "UNITS" size 13 color "#ffd700" bold True xsize 80 text_align 0.5
                            text "GRADE" size 13 color "#ffd700" bold True xsize 160 text_align 0.5

                    for _ci in range(len(sq_gwa_state.courses)):
                        $ _cname, _cunit = sq_gwa_state.courses[_ci]
                        $ _has  = _ci in sq_gwa_state.grades
                        $ _gval = sq_gwa_state.grades.get(_ci, None)
                        $ _gcol = sq_gwa_state.grade_color(_gval)

                        button:
                            xfill True padding (16, 12, 16, 12)
                            background Solid(_gcol + "22" if _has else "#0d0406")
                            hover_background Solid(_gcol + "33" if _has else "#1e1020")
                            action Function(sq_gwa_state.cycle_grade, _ci)
                            hbox:
                                xfill True yalign 0.5
                                text "[_cname]":
                                    size 13 color "#f1debf" yalign 0.5 xsize 360
                                text "[_cunit]u":
                                    size 13 color "#f6d79d88" yalign 0.5 xsize 80 text_align 0.5
                                if _has:
                                    frame:
                                        xsize 150 ysize 38 yalign 0.5
                                        background Solid(_gcol + "44")
                                        text ("%.2f" % _gval):
                                            xalign 0.5 yalign 0.5 size 20 color _gcol bold True
                                else:
                                    frame:
                                        xsize 150 ysize 38 yalign 0.5
                                        background Solid("#2a1a2a")
                                        text "click \u2192":
                                            size 12 color "#5a4a5a" xalign 0.5 yalign 0.5

                    frame:
                        background Solid("#130609") xfill True padding (16, 8, 16, 8)
                        hbox:
                            xfill True
                            text "TOTAL UNITS SET":
                                size 11 color "#c89218" bold True xsize 360
                            text "":
                                xsize 80
                            text "[sum(sq_gwa_state.courses[i][1] for i in sq_gwa_state.grades)] / [sum(c[1] for c in sq_gwa_state.courses)] units":
                                size 11 color "#f6d79d88" xsize 160 text_align 0.5

            ## GWA panel
            frame:
                xsize 300 padding (0, 0, 0, 0)
                background Solid("#1a0a0ef8")
                vbox:
                    spacing 0
                    frame:
                        background Solid("#2a0e0e") xfill True padding (16, 10, 16, 10)
                        text "LIVE GWA" size 15 color "#ffd700" bold True xalign 0.5

                    frame:
                        background Solid("#0d0406") xfill True padding (20, 22, 20, 22)
                        vbox:
                            spacing 10 xalign 0.5

                            if _gwa is not None:
                                text ("%.4f" % _gwa):
                                    xalign 0.5 size 50 color _scol bold True
                            else:
                                text "\u2014":
                                    xalign 0.5 size 50 color "#3a2a3a" bold True

                            frame:
                                xfill True padding (10, 8, 10, 8)
                                background Solid(_scol + "33")
                                text "[_sch]":
                                    xalign 0.5 size 13 color _scol bold True

                    frame:
                        background Solid("#130609") xfill True padding (14, 10, 14, 10)
                        vbox:
                            spacing 4
                            text "GRADE SCALE" size 10 color "#c89218" bold True xalign 0.5
                            null height 3
                            python:
                                _grade_scale = [
                                    ("\u2264 1.20", "Univ. Scholar", "#ffd700"),
                                    ("\u2264 1.45", "College Scholar", "#10b981"),
                                    ("\u2264 1.75", "Dean's List", "#6ee7b7"),
                                    ("\u2264 3.00", "Regular", "#f1debf"),
                                    ("> 3.00",  "Concern", "#f87171"),
                                ]
                            for _ref in _grade_scale:
                                hbox:
                                    spacing 6
                                    text _ref[0] size 11 color "#f6d79d88" xsize 56
                                    text _ref[1] size 11 color _ref[2]

                    frame:
                        background Solid("#0d0406") xfill True padding (14, 12, 14, 14)
                        vbox:
                            spacing 8
                            text "CHALLENGE" size 10 color "#c89218" bold True xalign 0.5
                            text "[sq_gwa_state.challenge]":
                                size 12 color "#f6d79d" text_align 0.5 xalign 0.5

                            if _all:
                                if _gwa is not None and _gwa <= sq_gwa_state.challenge_gwa:
                                    vbox:
                                        spacing 6
                                        text "\u2713 Challenge met!" size 13 color "#10b981" bold True xalign 0.5
                                        textbutton "Claim Reward \u2605":
                                            xalign 0.5 action Return("completed")
                                            text_size 14 text_color "#ffd700"
                                            background Solid("#5c1a1a") hover_background Solid("#7c2222")
                                            padding (16, 8, 16, 8)
                                else:
                                    vbox:
                                        spacing 6
                                        text "Adjust grades to meet challenge." size 11 color "#f6d79d" xalign 0.5 text_align 0.5
                                        textbutton "Submit Anyway":
                                            xalign 0.5 action Return("partial")
                                            text_size 11 text_color "#888888"
                                            background Solid("#1a0a0e") padding (14, 6, 14, 6)
                            else:
                                text "Set all 5 grades to continue.":
                                    size 11 color "#888888" xalign 0.5

        text "Click any row to advance to the next grade value  |  Rows cycle: 1.00 \u2192 1.25 \u2192 ... \u2192 5.00 \u2192 1.00":
            xalign 0.5 size 11 color "#c8921866"
            outlines [(1, "#1a0a0e", 0, 0)]


## ============================================================================
## ACT 6 MINIGAME — Guided Breathing Exercise (GCSU Scene)
## Triggered after Ma'am Garcia's "Slow breath with me. In... hold... and out."
## Player follows 3 breath cycles: Inhale (4s) → Hold (2s) → Exhale (4s).
## Dan's stress meter drops after each cycle; Continue unlocks after all 3.
## ============================================================================

## ── ATL: Circle animates per phase ──────────────────────────────────────────

transform breath_inhale:
    ## Expands from small to full over 4 seconds
    zoom 0.45 alpha 0.65
    linear 4.0 zoom 1.0 alpha 1.0

transform breath_hold_pulse:
    ## Gentle slow pulse at full size over 2 seconds
    zoom 1.0 alpha 1.0
    ease 1.0 zoom 1.07 alpha 0.90
    ease 1.0 zoom 1.0 alpha 1.0
    repeat

transform breath_exhale:
    ## Contracts from full to small over 4 seconds
    zoom 1.0 alpha 1.0
    linear 4.0 zoom 0.45 alpha 0.65

transform breath_done_glow:
    ## Soft steady glow when all cycles complete
    alpha 0.85
    ease 1.5 alpha 1.0
    ease 1.5 alpha 0.85
    repeat


## ── Screen ───────────────────────────────────────────────────────────────────

screen breathing_exercise_screen():
    modal True
    zorder 200

    ## Per-call screen state
    default bphase = "in"    ## "in" | "hold" | "out"
    default bcycle = 0       ## cycles completed (0–2)
    default bdone  = False   ## True after the 3rd exhale

    ## ── Phase-advance timers ────────────────────────────────────────────────
    ## Each timer fires once, then the screen re-renders with the new phase,
    ## which creates the next timer. Chain stops when bdone becomes True.
    if not bdone:
        if bphase == "in":
            timer 4.0 action SetScreenVariable("bphase", "hold")
        elif bphase == "hold":
            timer 2.0 action SetScreenVariable("bphase", "out")
        elif bphase == "out":
            if bcycle < 2:
                ## More cycles remain — reset to inhale and increment counter
                timer 4.0 action [
                    SetScreenVariable("bcycle", bcycle + 1),
                    SetScreenVariable("bphase", "in"),
                ]
            else:
                ## 3rd exhale complete — mark done
                timer 4.0 action SetScreenVariable("bdone", True)

    ## ── Background ──────────────────────────────────────────────────────────
    add Solid("#050c12") alpha 0.98

    ## ── Central layout ──────────────────────────────────────────────────────
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 28

        ## Header
        frame:
            xalign 0.5
            background Solid("#0c1d2a")
            padding (32, 14, 32, 14)
            vbox:
                spacing 5
                text "Guided Breathing":
                    size 21
                    color "#a8d8ea"
                    bold True
                    xalign 0.5
                    outlines [(1, "#050c12", 1, 1)]
                text "Follow the rhythm with Dan":
                    size 12
                    color "#4e7f92"
                    italic True
                    xalign 0.5

        ## Breathing circle container
        fixed:
            xsize 270
            ysize 270
            xalign 0.5

            ## Soft outer ring (always visible)
            frame:
                xsize 270
                ysize 270
                xalign 0.5
                yalign 0.5
                background Solid("#ffffff06")

            ## Animated inner circle — swapped per phase so ATL restarts
            if bdone:
                frame:
                    xsize 190
                    ysize 190
                    xalign 0.5
                    yalign 0.5
                    background Solid("#4aad78")
                    at breath_done_glow
            elif bphase == "in":
                frame:
                    xsize 190
                    ysize 190
                    xalign 0.5
                    yalign 0.5
                    background Solid("#3e8fb5")
                    at breath_inhale
            elif bphase == "hold":
                frame:
                    xsize 190
                    ysize 190
                    xalign 0.5
                    yalign 0.5
                    background Solid("#4aad78")
                    at breath_hold_pulse
            elif bphase == "out":
                frame:
                    xsize 190
                    ysize 190
                    xalign 0.5
                    yalign 0.5
                    background Solid("#8a62a0")
                    at breath_exhale

            ## Phase label (centred inside circle)
            if bdone:
                text "":
                    xalign 0.5 yalign 0.5 size 15 color "#ffffff"
            elif bphase == "in":
                text "Breathe in...":
                    xalign 0.5 yalign 0.5 size 15 color "#ffffff" bold True
                    outlines [(1, "#00000088", 1, 1)]
            elif bphase == "hold":
                text "Hold...":
                    xalign 0.5 yalign 0.5 size 15 color "#ffffff" bold True
                    outlines [(1, "#00000088", 1, 1)]
            elif bphase == "out":
                text "Breathe out...":
                    xalign 0.5 yalign 0.5 size 15 color "#ffffff" bold True
                    outlines [(1, "#00000088", 1, 1)]

        ## ── Cycle progress pips (fill as each cycle finishes) ───────────────
        python:
            _filled_pips = bcycle + (1 if bdone else 0)
        hbox:
            xalign 0.5
            spacing 12
            for _pip in range(3):
                frame:
                    xsize 22
                    ysize 22
                    background Solid("#5ab3d0" if _pip < _filled_pips else "#0e2030")

        ## ── Dan's stress meter (decreases each cycle) ───────────────────────
        python:
            _stress_bars = 3 - bcycle - (1 if bdone else 0)
        vbox:
            spacing 8
            xalign 0.5
            text "Dan's stress:":
                size 11
                color "#4e7f92"
                xalign 0.5
            hbox:
                spacing 8
                xalign 0.5
                for _bar in range(3):
                    frame:
                        xsize 54
                        ysize 16
                        background Solid("#c84040" if _bar < _stress_bars else "#0e1e16")

        ## ── Done state — calm message + Continue ────────────────────────────
        if bdone:
            vbox:
                spacing 14
                xalign 0.5
                text "Dan feels calmer.":
                    size 15
                    color "#8fd4a8"
                    bold True
                    xalign 0.5
                    outlines [(1, "#050c12", 1, 1)]
                textbutton "Continue":
                    xalign 0.5
                    action Return()
                    text_size 14
                    text_color "#a8d8ea"
                    background Solid("#0c2233")
                    hover_background Solid("#163344")
                    padding (30, 10, 30, 10)


## ============================================================================
## ACT 5 MINIGAME — Find Your Classroom (Navigation Puzzle)
## Triggered at the "Attend your first class" node in act5_first_class.
## Player decodes 3 schedule entries to find the correct building + floor.
## Reinforces Kuya Rico's room-numbering lesson: prefix = building, first
## digit of room number = floor.
## ============================================================================

init python:

    class ClassroomFinderState:

        BUILDINGS = [
            "CAS Building",
            "CM Building",
            "CFOS Building",
        ]
        BUILDINGS_SUB = [
            "College of Arts & Sciences",
            "College of Management",
            "Fisheries & Ocean Sciences",
        ]
        FLOORS = [
            "Ground Floor  (1xx)",
            "2nd Floor  (2xx)",
            "3rd Floor  (3xx)",
        ]

        ## Each challenge: the formatted schedule entry the player sees,
        ## the explanation shown after, and the correct building/floor indices.
        CHALLENGES = [
            dict(
                entry    = "ENG 1  \u00b7  MWF 09:00\u201310:00  \u00b7  CAS 105",
                explain  = "\"CAS\" \u2192 CAS Building   |   Room 105: first digit 1 \u2192 Ground Floor",
                building = 0,   ## CAS
                floor    = 0,   ## 1xx = Ground
            ),
            dict(
                entry    = "KAS 1  \u00b7  TTh 13:00\u201314:30  \u00b7  CAS 203",
                explain  = "\"CAS\" \u2192 CAS Building   |   Room 203: first digit 2 \u2192 2nd Floor",
                building = 0,   ## CAS
                floor    = 1,   ## 2xx = 2nd
            ),
            dict(
                entry    = "MATH 11  \u00b7  MWF 11:00\u201312:00  \u00b7  CM 301",
                explain  = "\"CM\" \u2192 CM Building   |   Room 301: first digit 3 \u2192 3rd Floor",
                building = 1,   ## CM
                floor    = 2,   ## 3xx = 3rd
            ),
        ]

        def __init__(self):
            self.reset()

        def reset(self):
            self.round        = 0
            self.phase        = "building"  ## "building" | "floor" | "result"
            self.sel_building = None
            self.sel_floor    = None
            self.bld_ok       = None
            self.flr_ok       = None
            self.done         = False

        def pick_building(self, idx):
            if self.phase != "building":
                return
            self.sel_building = idx
            self.bld_ok       = (idx == self.CHALLENGES[self.round]["building"])
            self.phase        = "floor"

        def pick_floor(self, idx):
            if self.phase != "floor":
                return
            self.sel_floor = idx
            self.flr_ok    = (idx == self.CHALLENGES[self.round]["floor"])
            self.phase     = "result"

        def advance(self):
            self.round += 1
            if self.round >= len(self.CHALLENGES):
                self.done = True
            else:
                self.phase        = "building"
                self.sel_building = None
                self.sel_floor    = None
                self.bld_ok       = None
                self.flr_ok       = None

        def retry(self):
            self.phase        = "building"
            self.sel_building = None
            self.sel_floor    = None
            self.bld_ok       = None
            self.flr_ok       = None

    classroom_finder_state = ClassroomFinderState()


## ── Screen ───────────────────────────────────────────────────────────────────

screen classroom_finder_screen():
    modal True
    zorder 200

    add Solid("#080d18") alpha 0.98

    python:
        _cf    = classroom_finder_state
        _total = len(_cf.CHALLENGES)
        _ch    = _cf.CHALLENGES[_cf.round] if not _cf.done else None

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 22

        ## ── Header ──────────────────────────────────────────────────────────
        frame:
            xalign 0.5
            background Solid("#0e1a2c")
            padding (36, 14, 36, 14)
            vbox:
                spacing 5
                text "Find Your Classroom":
                    size 21
                    color "#f6d7a0"
                    bold True
                    xalign 0.5
                    outlines [(1, "#080d18", 1, 1)]
                text "Read the schedule entry \u2192 pick the right building \u2192 pick the right floor":
                    size 11
                    color "#8a7a5a"
                    italic True
                    xalign 0.5

        ## ── Round progress pips ─────────────────────────────────────────────
        hbox:
            xalign 0.5
            spacing 12
            for _pip in range(_total):
                frame:
                    xsize 22
                    ysize 22
                    background Solid("#c89218" if (_pip < _cf.round or _cf.done) else "#1e1408")

        if not _cf.done:

            ## ── Schedule entry card ─────────────────────────────────────────
            frame:
                xalign 0.5
                background Solid("#10203a")
                padding (32, 18, 32, 18)
                vbox:
                    spacing 8
                    text ("CLASS  " + str(_cf.round + 1) + " / " + str(_total)):
                        size 10
                        color "#4a6a8a"
                        bold True
                        xalign 0.5
                    text (_ch["entry"]):
                        size 17
                        color "#e8d4a0"
                        bold True
                        xalign 0.5
                        outlines [(1, "#080d18", 1, 1)]

            ## ── Step 1 — Choose building ────────────────────────────────────
            if _cf.phase == "building":
                vbox:
                    spacing 12
                    xalign 0.5
                    text "Step 1 \u2014 Which building?":
                        size 13
                        color "#c8a84a"
                        bold True
                        xalign 0.5
                    hbox:
                        spacing 14
                        xalign 0.5
                        for _bi in range(len(_cf.BUILDINGS)):
                            textbutton _cf.BUILDINGS[_bi]:
                                action Function(_cf.pick_building, _bi)
                                text_size 13
                                text_color "#e8d4a0"
                                background Solid("#0e1a2c")
                                hover_background Solid("#1c3050")
                                padding (20, 10, 20, 10)

            ## ── Step 2 — Choose floor ───────────────────────────────────────
            elif _cf.phase == "floor":
                vbox:
                    spacing 12
                    xalign 0.5

                    ## Show building result badge
                    frame:
                        xalign 0.5
                        background Solid("#0a1420" if _cf.bld_ok else "#1a0a0a")
                        padding (16, 8, 16, 8)
                        hbox:
                            spacing 10
                            xalign 0.5
                            yalign 0.5
                            text ("\u2713" if _cf.bld_ok else "\u2717"):
                                size 15
                                color ("#10b981" if _cf.bld_ok else "#ef4444")
                                yalign 0.5
                            text (_cf.BUILDINGS[_cf.sel_building]):
                                size 13
                                color "#e8d4a0"
                                yalign 0.5

                    text "Step 2 \u2014 Which floor?":
                        size 13
                        color "#c8a84a"
                        bold True
                        xalign 0.5
                    hbox:
                        spacing 12
                        xalign 0.5
                        for _fi in range(len(_cf.FLOORS)):
                            textbutton _cf.FLOORS[_fi]:
                                action Function(_cf.pick_floor, _fi)
                                text_size 12
                                text_color "#e8d4a0"
                                background Solid("#0e1a2c")
                                hover_background Solid("#1c3050")
                                padding (18, 9, 18, 9)

            ## ── Result phase ────────────────────────────────────────────────
            elif _cf.phase == "result":
                python:
                    _both_ok = _cf.bld_ok and _cf.flr_ok

                vbox:
                    spacing 12
                    xalign 0.5

                    ## Building row
                    frame:
                        xalign 0.5
                        background Solid("#0a1420" if _cf.bld_ok else "#1a0a0a")
                        padding (16, 8, 16, 8)
                        hbox:
                            spacing 10
                            xalign 0.5
                            yalign 0.5
                            text ("\u2713" if _cf.bld_ok else "\u2717"):
                                size 15
                                color ("#10b981" if _cf.bld_ok else "#ef4444")
                                yalign 0.5
                            text (_cf.BUILDINGS[_cf.sel_building]):
                                size 13
                                color "#e8d4a0"
                                yalign 0.5
                            if not _cf.bld_ok:
                                text (" \u2192 " + _cf.BUILDINGS[_ch["building"]]):
                                    size 12
                                    color "#10b981"
                                    yalign 0.5

                    ## Floor row
                    frame:
                        xalign 0.5
                        background Solid("#0a1420" if _cf.flr_ok else "#1a0a0a")
                        padding (16, 8, 16, 8)
                        hbox:
                            spacing 10
                            xalign 0.5
                            yalign 0.5
                            text ("\u2713" if _cf.flr_ok else "\u2717"):
                                size 15
                                color ("#10b981" if _cf.flr_ok else "#ef4444")
                                yalign 0.5
                            text (_cf.FLOORS[_cf.sel_floor]):
                                size 13
                                color "#e8d4a0"
                                yalign 0.5
                            if not _cf.flr_ok:
                                text (" \u2192 " + _cf.FLOORS[_ch["floor"]]):
                                    size 12
                                    color "#10b981"
                                    yalign 0.5

                    ## Explanation note
                    frame:
                        xalign 0.5
                        background Solid("#0a1810" if _both_ok else "#120a08")
                        padding (18, 10, 18, 10)
                        text (_ch["explain"]):
                            size 11
                            color ("#90c890" if _both_ok else "#c89060")
                            italic True
                            xalign 0.5

                    if _both_ok:
                        text "Room found! \u2605":
                            size 15
                            color "#f6d700"
                            bold True
                            xalign 0.5
                            outlines [(1, "#080d18", 1, 1)]
                        textbutton "Next Class \u2192":
                            xalign 0.5
                            action Function(_cf.advance)
                            text_size 13
                            text_color "#f6d7a0"
                            background Solid("#183a0e")
                            hover_background Solid("#28581a")
                            padding (26, 9, 26, 9)
                    else:
                        text "Not quite \u2014 check the schedule notation.":
                            size 12
                            color "#f87171"
                            xalign 0.5
                        textbutton "Try Again":
                            xalign 0.5
                            action Function(_cf.retry)
                            text_size 13
                            text_color "#f6d7a0"
                            background Solid("#2a0e0e")
                            hover_background Solid("#3a1616")
                            padding (26, 9, 26, 9)

        ## ── Done state ──────────────────────────────────────────────────────
        else:
            vbox:
                spacing 18
                xalign 0.5
                text "All classrooms found!":
                    size 20
                    color "#f6d700"
                    bold True
                    xalign 0.5
                    outlines [(1, "#080d18", 1, 1)]
                text "You know your way around. Time for that first class.":
                    size 13
                    color "#a0c8a0"
                    italic True
                    xalign 0.5
                textbutton "Attend First Class":
                    xalign 0.5
                    action Return()
                    text_size 14
                    text_color "#f6d7a0"
                    background Solid("#183a0e")
                    hover_background Solid("#28581a")
                    padding (30, 10, 30, 10)
