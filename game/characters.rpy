## ============================================================================
## CHARACTER DEFINITIONS & PLAYER SPRITE ANIMATIONS

init python:
    def typing_sound(event, interact=True, **kwargs):
        if not interact:
            return
        # Start looping the click sound when text starts typing
        if event == "show":
            renpy.sound.play("audio/click2.mp3", loop=True)
        # Stop the sound when the text finishes appearing
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()
## ============================================================================

## --- NPC Character Definitions ---
## Color palette: warm earth tones matching Miagao pixel art

define player_char = Character("You", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define guard = Character("Manong Guard", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define driver = Character("Manong Driver", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define manongjosh = Character("Local", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define physician = Character("School Physician", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define dentist = Character("School Dentist", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define sir_ruel = Character("Sir Ruel", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define ms_santos = Character("Ms. Santos", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define sarah = Character("Sarah", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define mikhaela = Character("Sarah", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define jaden = Character("Jaden", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define caezar = Character("Caezar", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define dorm_mgr = Character("Dorm Manager", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define narrator_char = Character(None, what_color="#cccccc", callback=typing_sound)
define aleng_maria = Character("Aleng Maria", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define joseph_driver = Character("Joseph", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define manong_chris = Character("Manong Chris", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define manong_josh = Character("Manong Josh", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define joseph = Character("Joseph", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define ate_bea = Character("ate bea", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define kuya_mark = Character("kuya mark", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define maam_reyes = Character("maam reyes", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define sir_allan = Character("sir allan", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define sir_noel = Character("Sir Noel", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)

## --- Act 5 Characters ---
define prof_lena = Character("Prof. Lena", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")
define kuya_rico = Character("Kuya Rico", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")
define ate_grace = Character("Ate Grace", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")
define dan = Character("Dan", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")
define ria = Character("Ria", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")
define hsu_nurse = Character("Nurse Santos", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")
define prof_lena = Character("Prof. Lena", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define kuya_rico = Character("Kuya Rico", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define ate_grace = Character("Ate Grace", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define dan = Character("Dan", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)

## --- Act 6 Characters ---
define mika = Character("Mika", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define kuya_tomas = Character("Kuya Tomas", color="#6e1f2a", what_color="#ffffff", callback=typing_sound)
define ate_jenny = Character("Ate Jenny", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")
define coach_ramon = Character("Coach Ramon", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")

## --- Act 7 Characters ---
define ate_rosa = Character("Ate Rosa", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")
define kuya_neil = Character("Kuya Neil", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")
define prof_santos = Character("Prof. Santos", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")
define bea = Character("Bea", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")

## --- Act 8 Characters ---
define ate_linda = Character("Ate Linda", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")
define nanay_elena = Character("Nanay Elena", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")
define prof_reyes = Character("Prof. Reyes", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")

## --- Support Services Characters ---
define guidance_counselor = Character("Ma'am Garcia", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")
define tlrc_coord = Character("TLRC Coordinator", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")
define peer_tutor = Character("Peer Tutor", color="#6e1f2a", what_color="#ffffff", what_sound="audio/click.wav")

## --- NPC Sprite Images ---
## Ren'Py auto-names files in subdirectories with a space prefix (e.g. "npcs manong_guard").
## We define them explicitly here so `show manong_guard` works in dialogue scenes.
image manong_guard = "images/npcs/manong_guard.png"
image manong_driver = "images/npcs/manong_driver.png"
image physician = "images/npcs/physician.png"
image dentist = "images/npcs/dentist.png"
image sir_ruel = "images/npcs/sir_ruel.png"
image ms_santos = "images/npcs/ms_santos.png"
image sarah = "images/npcs/sarah.png"
image mikhaela = "images/npcs/sarah.png"
image jaden = "images/npcs/jaden.png"
image caezar = "images/npcs/caezar.png"
image dorm_mgr = "images/npcs/dorm_mgr.png"
image aleng_maria_sprite = "images/npcs/alengmaria.png"
image manong_josh = "images/npcs/manongjosh.png"      ## already have file, just add this
image manong_chris = "images/npcs/manongchris.png"
image joseph_driver = "images/npcs/manong_driver.png"
image ate_bea = "images/npcs/ate_bea.png"
image kuya_mark = "images/npcs/kuya_mark.png"
image maam_reyes = "images/npcs/maam_reyes.png"
image sir_allan = "images/npcs/sir_allan.png"
image sir_noel = "images/npcs/sir_allan.png"  ## placeholder — reuses sir_allan portrait

## --- Act 5 NPC Sprites ---
image prof_lena_sprite = "images/npcs/prof_lena.png"
image kuya_rico_sprite = "images/npcs/kuya_rico.png"
image ate_grace_sprite = "images/npcs/ate_grace.png"
image classmate_dan_sprite = "images/npcs/classmate_dan.png"
image ria_sprite = "images/npcs/ria.png"
image hsu_nurse_sprite = "images/npcs/hsu_nurse.png"

## --- Act 6 NPC Sprites ---
image mika_sprite = "images/npcs/mika.png"
image kuya_tomas_sprite = "images/npcs/kuya_tomas.png"
image ate_jenny_sprite = "images/npcs/ate_jenny.png"
image coach_ramon_sprite = "images/npcs/coach_ramon.png"

## --- Act 7 NPC Sprites ---
image ate_rosa_sprite = "images/npcs/ate_rosa.png"
image kuya_neil_sprite = "images/npcs/kuya_neil.png"
image prof_santos_sprite = "images/npcs/prof_santos.png"
image classmate_bea_sprite = "images/npcs/classmate_bea.png"

## --- Act 8 NPC Sprites ---
image jaden_sprite = "images/npcs/jaden.png"
image ate_linda_sprite = "images/npcs/ate_linda.png"
image nanay_elena_sprite = "images/npcs/nanay_elena.png"
image prof_reyes_sprite = "images/npcs/prof_reyes.png"

## --- Scene Backgrounds ---
image bg gate_entrance = Solid("#2a3a2a")
image bg miagao_campus = "images/ui/Entrance.png"
image bg Miagao = "images/ui/UI_Miagao.png"  
image bg act3_dialogue = "images/ui/act3_dialogue_bg.png"
## --- Player Sprite Images ---
## These use spritesheets from the Unity project's Player1 folder.
## Each spritesheet is a horizontal strip of 8 frames, 48x48 pixels each.
## We use im.Crop to extract individual frames from the spritesheet.
## Path prefix: "images/" because assets are in game/images/

## IDLE sprites (single frame from each directional spritesheet)
image player_idle_down = im.Crop("images/player/idle/Idle_Down.png", (0, 0, 48, 48))
image player_idle_up = im.Crop("images/player/idle/Idle_Up.png", (0, 0, 48, 48))
image player_idle_left = im.Crop("images/player/idle/Idle_Left_Down.png", (0, 0, 48, 48))
image player_idle_right = im.Crop("images/player/idle/Idle_Right_Down.png", (0, 0, 48, 48))

## WALK animations (cycling through frames from directional spritesheets)
image player_walk_down:
    im.Crop("images/player/walk/walk_Down.png", (0, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Down.png", (48, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Down.png", (96, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Down.png", (144, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Down.png", (192, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Down.png", (240, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Down.png", (288, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Down.png", (336, 0, 48, 48))
    0.12
    repeat

image player_walk_up:
    im.Crop("images/player/walk/walk_Up.png", (0, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Up.png", (48, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Up.png", (96, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Up.png", (144, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Up.png", (192, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Up.png", (240, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Up.png", (288, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Up.png", (336, 0, 48, 48))
    0.12
    repeat

image player_walk_left:
    im.Crop("images/player/walk/walk_Left.png", (0, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Left.png", (48, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Left.png", (96, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Left.png", (144, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Left.png", (192, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Left.png", (240, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Left.png", (288, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Left.png", (336, 0, 48, 48))
    0.12
    repeat

image player_walk_right:
    im.Crop("images/player/walk/walk_Right.png", (0, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Right.png", (48, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Right.png", (96, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Right.png", (144, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Right.png", (192, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Right.png", (240, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Right.png", (288, 0, 48, 48))
    0.12
    im.Crop("images/player/walk/walk_Right.png", (336, 0, 48, 48))
    0.12
    repeat

