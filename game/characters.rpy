## ============================================================================
## CHARACTER DEFINITIONS & PLAYER SPRITE ANIMATIONS
## ============================================================================

## --- NPC Character Definitions ---
## Color palette: warm earth tones matching Miagao pixel art
define player_char = Character("You", color="#88ccff", what_color="#ffffff")
define guard = Character("Manong Guard", color="#c8ffc8", what_color="#ffffff")
define driver = Character("Manong Driver", color="#ffd700", what_color="#ffffff")
define manongjosh = Character("Local", color="#ff9999", what_color="#ffffff")
define physician = Character("School Physician", color="#99ccff", what_color="#ffffff")
define dentist = Character("School Dentist", color="#99ffcc", what_color="#ffffff")
define sir_ruel = Character("Sir Ruel", color="#ff8866", what_color="#ffffff")
define ms_santos = Character("Ms. Santos", color="#cc99ff", what_color="#ffffff")
define sarah = Character("Sarah", color="#ffcc99", what_color="#ffffff")
define mikhaela = Character("Mikhaela", color="#ff99cc", what_color="#ffffff")
define jaden = Character("Jaden", color="#99ccff", what_color="#ffffff")
define caezar = Character("Caezar", color="#ccff99", what_color="#ffffff")
define dorm_mgr = Character("Dorm Manager", color="#ffaa77", what_color="#ffffff")
define narrator_char = Character(None, what_color="#cccccc")
define aleng_maria = Character("Aleng Maria", color="#ffaa88", what_color="#ffffff")
define joseph_driver = Character("Joseph", color="#ffd700", what_color="#ffffff")
define manong_chris = Character("Manong Chris", color="#aaddff", what_color="#ffffff")
define manong_josh = Character("Manong Josh", color="#ffd7a0", what_color="#ffffff")
define joseph = Character("Joseph", color="#ffd700", what_color="#ffffff")
define ate_bea = Character("ate bea", color="#ffd700", what_color="#ffffff")
define kuya_mark = Character("kuya mark", color="#aaddff", what_color="#ffffff")
define maam_reyes = Character("maam reyes", color="#ffd7a0", what_color="#ffffff")
define sir_allan = Character("sir allan", color="#ffd700", what_color="#ffffff")
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
image mikhaela = "images/npcs/mikhaela.png"
image jaden = "images/npcs/jaden.png"
image caezar = "images/npcs/caezar.png"
image dorm_mgr = "images/npcs/dorm_mgr.png"
image aleng_maria_sprite = "images/npcs/alengmaria.png"
image manong_josh = "images/npcs/manongjosh.png"      ## already have file, just add this
image manong_chris = "images/npcs/manong_chris.png"
image joseph_driver = "images/npcs/joseph_driver.png"
image ate_bea = "images/npcs/ate_bea.png"
image kuya_mark = "images/npcs/kuya_mark.png"
image maam_reyes = "images/npcs/maam_reyes.png"
image sir_allan = "images/npcs/sir_allan.png"
## --- Scene Backgrounds ---
image bg gate_entrance = Solid("#2a3a2a")
image bg miagao_campus = "images/ui/Entrance.png"
image bg Miagao = "images/ui/UI_Miagao.png"  
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

