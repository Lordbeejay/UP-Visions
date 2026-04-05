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
                                    text "[\u2192 [sq_sort_state.bins[_bx][0]]]":
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
                            for _ref in [("\u2264 1.20", "Univ. Scholar", "#ffd700"),
                                         ("\u2264 1.45", "College Scholar", "#10b981"),
                                         ("\u2264 1.75", "Dean's List", "#6ee7b7"),
                                         ("\u2264 3.00", "Regular", "#f1debf"),
                                         ("> 3.00",  "Concern", "#f87171")]:
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
