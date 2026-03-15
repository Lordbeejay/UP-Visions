## ============================================================================
## MAP ENGINE — Point-and-click navigation with animated character walking
## ============================================================================

init python:
    import math

    class MapNode:
        """A clickable location on the map."""
        def __init__(self, name, x, y, target_label, tooltip="", locked=False, icon_color="#44cc44", icon_image=None, icon_zoom=0.12):
            self.name = name
            self.x = x
            self.y = y
            self.target_label = target_label
            self.tooltip = tooltip
            self.locked = locked
            self.icon_color = icon_color
            self.icon_image = icon_image
            self.icon_zoom = icon_zoom
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

    ## Key bindings for phone, inventory, encyclopedia — overlays so the map stays visible
    key "p" action If(phone_unlocked, Show("phone_screen"), NullAction())
    key "i" action If(inventory_unlocked, Show("inventory_screen"), NullAction())
    key "e" action If(inventory_unlocked, Show("encyclopedia_screen"), NullAction())

    ## Black background behind everything
    add Solid("#000000"):
        xysize (1920, 1080)

    ## Map background — scaled and centered with white border
    frame:
        background Solid("#ffffff")
        padding (4, 4, 4, 4)
        xalign 0.5
        yalign 0.5
        add ("images/" + map_bg):
            zoom map_scale

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
                            zoom getattr(node, "icon_zoom", 0.12)
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
                            zoom getattr(node, "icon_zoom", 0.12)
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
    $ _px = int(player_map_x * MAP_SCALE_X) - 60
    $ _py = int(player_map_y * MAP_SCALE_Y) - 100
    add ("player_idle_" + player_facing):
        xpos _px
        ypos _py
        zoom 2.5

    ## --- ACT + TASK LIST PANEL (top left) ---

    ## Outer glow border
    frame:
        xpos 14
        ypos 160
        xminimum 360
        xmaximum 520
        padding (3, 3, 3, 3)
        background Frame(Solid("#f6d79d22"), 0, 0)

        ## Main dark panel
        frame:
            xfill True
            padding (24, 18, 24, 18)
            background Frame(Solid("#1e0c12ee"), 0, 0)

            vbox:
                xfill True
                spacing 0

                ## Top ornament line
                hbox:
                    xalign 0.5
                    spacing 6

                    frame:
                        xsize 40
                        ysize 2
                        yalign 0.5
                        background Solid("#f6d79d66")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 8
                        ysize 8
                        yalign 0.5
                        background Solid("#f6d79d")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 80
                        ysize 2
                        yalign 0.5
                        background Solid("#f6d79d")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 8
                        ysize 8
                        yalign 0.5
                        background Solid("#f6d79d")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 40
                        ysize 2
                        yalign 0.5
                        background Solid("#f6d79d66")
                        padding (0, 0, 0, 0)

                null height 12

                ## Act title
                text "[get_act_title(current_act)]":
                    xalign 0.5
                    text_align 0.5
                    size 20
                    color "#ffd700"
                    outlines [(3, "#1e0c12", 0, 0), (1, "#8b6914aa", 1, 1)]

                null height 6

                ## Thin separator
                frame:
                    xalign 0.5
                    xsize 160
                    ysize 1
                    background Solid("#f6d79d44")
                    padding (0, 0, 0, 0)

                null height 10

                ## Task list
                for _task_label, _is_done, _is_unlocked in get_act_task_items(current_act):
                    if _is_done:
                        hbox:
                            spacing 8
                            text "★":
                                size 14
                                color "#b8e6b0"
                                outlines [(1, "#1e0c12", 0, 0)]
                                yalign 0.5
                            text "{s}[_task_label]{/s}":
                                size 16
                                color "#9fd19b88"
                                outlines [(1, "#1e0c12", 0, 0)]
                                yalign 0.5
                    elif _is_unlocked:
                        hbox:
                            spacing 8
                            at task_item_bob
                            text "◇":
                                size 14
                                color "#f6d79d"
                                outlines [(1, "#1e0c12", 0, 0)]
                                yalign 0.5
                            text "[_task_label]":
                                size 16
                                color "#f1debf"
                                outlines [(1, "#1e0c12", 0, 0)]
                                yalign 0.5
                    else:
                        hbox:
                            spacing 8
                            at task_item_bob
                            text "◇":
                                size 14
                                color "#9f8d7666"
                                outlines [(1, "#1e0c12", 0, 0)]
                                yalign 0.5
                            text "[_task_label]":
                                size 16
                                color "#9f8d7688"
                                outlines [(1, "#1e0c12", 0, 0)]
                                yalign 0.5

                    null height 4

                null height 8

                ## Bottom ornament line (mirrors top)
                hbox:
                    xalign 0.5
                    spacing 6

                    frame:
                        xsize 40
                        ysize 2
                        yalign 0.5
                        background Solid("#f6d79d66")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 8
                        ysize 8
                        yalign 0.5
                        background Solid("#f6d79d")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 80
                        ysize 2
                        yalign 0.5
                        background Solid("#f6d79d")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 8
                        ysize 8
                        yalign 0.5
                        background Solid("#f6d79d")
                        padding (0, 0, 0, 0)
                    frame:
                        xsize 40
                        ysize 2
                        yalign 0.5
                        background Solid("#f6d79d66")
                        padding (0, 0, 0, 0)

transform task_item_bob:
    yoffset 0
    block:
        easein 1.2 yoffset -1
        easeout 1.2 yoffset 0
        repeat


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
    $ _start_x = int(player_map_x * MAP_SCALE_X) - 60
    $ _start_y = int(player_map_y * MAP_SCALE_Y) - 100
    $ _end_x = int(target_node.x * MAP_SCALE_X) - 60
    $ _end_y = int(target_node.y * MAP_SCALE_Y) - 100

    show expression ("player_walk_" + _dir) as player_sprite:
        pos (_start_x, _start_y)
        zoom 2.5
        linear _dur pos (_end_x, _end_y)

    $ renpy.pause(_dur, hard=True)

    $ player_map_x = target_node.x
    $ player_map_y = target_node.y
    $ player_facing = _dir

    hide player_sprite
    $ target_node.mark_visited()

    return