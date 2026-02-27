## ============================================================================
## MAP ENGINE — Point-and-click navigation with animated character walking
## ============================================================================

init python:
    import math

    class MapNode:
        """A clickable location on the map."""
        def __init__(self, name, x, y, target_label, tooltip="", locked=False, icon_color="#44cc44", icon_image=None):
            self.name = name
            self.x = x
            self.y = y
            self.target_label = target_label
            self.tooltip = tooltip
            self.locked = locked
            self.icon_color = icon_color
            self.icon_image = icon_image
            self.visited = False

        def unlock(self):
            self.locked = False

        def mark_visited(self):
            self.visited = True

    def calc_walk_duration(x1, y1, x2, y2, speed=400.0):
        """Calculate walk time in seconds based on pixel distance."""
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return max(0.3, dist / speed)

    def get_direction(x1, y1, x2, y2):
        """Determine walk direction for sprite selection."""
        dx = x2 - x1
        dy = y2 - y1
        if abs(dx) > abs(dy):
            return "right" if dx > 0 else "left"
        else:
            return "down" if dy > 0 else "up"

    ## Scale factors: map coords (5000x5000) -> screen coords (1920x1080)
    MAP_SCALE_X = 1920.0 / 5000.0
    MAP_SCALE_Y = 1080.0 / 5000.0

    def map_to_screen(mx, my):
        """Convert map coordinates (5000x5000 space) to screen pixels (1920x1080)."""
        return (int(mx * MAP_SCALE_X), int(my * MAP_SCALE_Y))


## ============================================================================
## MAP SCREEN
## ============================================================================

screen map_screen(map_bg, nodes, task_text="", map_scale=1.0):

    predict False

    ## Map background — displayed at full screen size (1920x1080 image, no zoom)
    add ("images/" + map_bg):
        xpos 0
        ypos 0
        xsize 1920
        ysize 1080

    ## Node markers — positioned using screen coordinates
    for node in nodes:
        ## Convert map coords (5000x5000) to screen coords (1920x1080)
        $ _sx = int(node.x * MAP_SCALE_X)
        $ _sy = int(node.y * MAP_SCALE_Y)

        if not node.locked:
            button:
                xpos _sx - 40
                ypos _sy - 70
                xysize (80, 90)
                action Return(("walk", node))
                background None
                hover_background None

                vbox:
                    xalign 0.5
                    spacing 2

                    if getattr(node, "icon_image", None):
                        add ("npcs/" + node.icon_image):
                            zoom 0.12
                            xalign 0.5
                    else:
                        frame:
                            xalign 0.5
                            xysize (20, 20)
                            background Solid(node.icon_color if not node.visited else "#666666")
                            padding (3, 3, 3, 3)
                            add Solid("#ffffff"):
                                xysize (14, 14)

                    text node.tooltip:
                        size 12
                        color "#ffffff"
                        outlines [(3, "#000000", 0, 0)]
                        text_align 0.5
                        xalign 0.5

        else:
            frame:
                xpos _sx - 40
                ypos _sy - 70
                xysize (80, 90)
                background None

                vbox:
                    xalign 0.5
                    spacing 2

                    if getattr(node, "icon_image", None):
                        add ("npcs/" + node.icon_image):
                            zoom 0.12
                            xalign 0.5
                            matrixcolor BrightnessMatrix(-0.5)
                    else:
                        frame:
                            xalign 0.5
                            xysize (18, 18)
                            background Solid("#33333388")
                            padding (3, 3, 3, 3)
                            add Solid("#55555588"):
                                xysize (12, 12)

                    text "🔒":
                        size 12
                        xalign 0.5

    ## Player sprite — also converted to screen coords
    $ _px = int(player_map_x * MAP_SCALE_X) - 24
    $ _py = int(player_map_y * MAP_SCALE_Y) - 48
    add ("player_idle_" + player_facing):
        xpos _px
        ypos _py
        zoom 2.0

    ## --- TASK DISPLAY BAR (top center) ---
    if task_text:
        frame:
            xalign 0.5
            ypos 10
            padding (30, 10, 30, 10)
            background Solid("#000000cc")
            has hbox:
                spacing 10
            text "📋" size 20
            text task_text:
                size 20
                color "#ffd700"
                outlines [(2, "#000000", 0, 0)]
                text_align 0.5

    ## --- ACT DISPLAY (bottom left) ---
    frame:
        xpos 10
        ypos 680
        padding (16, 6, 16, 6)
        background Solid("#000000cc")
        text get_act_title(current_act):
            size 16
            color "#ffd700"
            outlines [(2, "#000000", 0, 0)]

    ## --- HELP TEXT (bottom right) ---
    frame:
        xalign 1.0
        ypos 685
        padding (12, 4, 12, 4)
        background Solid("#00000088")
        text "Click a marker to walk there":
            size 13
            color "#aaaaaa"


## ============================================================================
## WALK LABEL
## ============================================================================

label walk_to_node(target_node, map_bg="maps/banwa.png"):
    ## Show the map background so it stays visible during the walk animation
    scene expression ("images/" + map_bg):
        xpos 0
        ypos 0
        xsize 1920
        ysize 1080

    $ _dir = get_direction(player_map_x, player_map_y, target_node.x, target_node.y)
    $ _dur = calc_walk_duration(player_map_x, player_map_y, target_node.x, target_node.y)

    ## Calculate screen positions for walk animation
    $ _start_x = int(player_map_x * MAP_SCALE_X) - 24
    $ _start_y = int(player_map_y * MAP_SCALE_Y) - 48
    $ _end_x = int(target_node.x * MAP_SCALE_X) - 24
    $ _end_y = int(target_node.y * MAP_SCALE_Y) - 48

    show expression ("player_walk_" + _dir) as player_sprite:
        pos (_start_x, _start_y)
        zoom 2.0
        linear _dur pos (_end_x, _end_y)

    $ renpy.pause(_dur, hard=True)

    $ player_map_x = target_node.x
    $ player_map_y = target_node.y
    $ player_facing = _dir

    hide player_sprite
    $ target_node.mark_visited()

    return