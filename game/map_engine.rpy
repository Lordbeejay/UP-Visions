## ============================================================================
## MAP ENGINE — Point-and-click navigation with animated character walking
## ============================================================================

init python:
    import math
    from collections import deque

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

    ## ======================================================================
    ## ROAD WAYPOINT SYSTEM — keeps the character walking on roads only
    ## ======================================================================
    ## HOW TO ADJUST:
    ##   1. "waypoints" = list of (x, y) road intersection points (5000x5000 coords)
    ##      To convert from screen pixels: map_x = pixel_x / 0.384, map_y = pixel_y / 0.216
    ##   2. "edges" = pairs of waypoint indices that are connected by a road
    ##      e.g. (0, 1) means waypoint 0 and waypoint 1 have a road between them
    ##   3. Add your map key (same string you pass to map_screen) to enable road blocking
    ##   4. Maps NOT listed here have no blocking — character walks in a straight line
    ## ======================================================================

    MAP_ROAD_GRAPHS = {

        ## --- BANWA (Act 1 center map) ---
        ## Roads wrap AROUND the church — no path through the center.
        ## Character walks left road or right road to go top ↔ bottom.
        ##
        ##   Layout:
        ##       0 ===================== 1
        ##       |      [CHURCH]         |
        ##       2      [BLOCKED]        3 -- box1 area
        ##       |                       4
        ##       |                       |
        ##  exit 5 -- 6                  7 -- 8 exit
        ##       |                       |
        ##       9 ===== 10 ============ 11
        ##
        "maps/banwa.png": {
            "waypoints": [
                (1120, 450),   # 0   top-left intersection
                (3860, 450),   # 1   top-right intersection
                (1120, 1500),  # 2   left road, upper
                (3860, 1500),  # 3   right road, upper (box1)
                (3860, 2500),  # 4   right road, mid
                (100,  2500),  # 5   left edge exit (→ tindahan)
                (1120, 2500),  # 6   left road, mid
                (4900, 2500),  # 7   right edge exit (→ marillac)
                (1120, 4600),  # 8   bottom-left
                (2500, 4600),  # 9   bottom-center (Jaden)
                (3860, 4600),  # 10  bottom-right
            ],
            "edges": [
                ## top road — horizontal (same y=450)
                (0, 1),
                ## left vertical road (same x=1120)
                (0, 2), (2, 6), (6, 8),
                ## right vertical road (same x=3860)
                (1, 3), (3, 4), (4, 10),
                ## left exit — horizontal (same y=2500)
                (5, 6),
                ## right exit — horizontal (same y=2500)
                (4, 7),
                ## bottom road — horizontal (same y=4600)
                (8, 9), (9, 10),
            ],
        },

        ## --- TINDAHAN (Act 1 left map) ---
        ## Roads run between building blocks. No cutting through stores.
        ##
        ##   Layout:
        ##       0 ======= 1 ======= 2
        ##       |         |         |
        ##       3 == A == 4 == J == 5 -- 6 exit
        ##       |                   |
        ##       7 ================= 8
        ##
        "ui/overhead_tindahan.png": {
            "waypoints": [
                (520,  700),   # 0   top-left
                (2500, 700),   # 1   top-center
                (3780, 700),   # 2   top-right
                (520,  2400),  # 3   mid-left
                (1500, 2400),  # 4   mid — Aleng Maria
                (2800, 2400),  # 5   mid — Joseph Driver
                (3780, 2400),  # 6   mid-right
                (4900, 2400),  # 7   right exit (→ banwa)
                (520,  4700),  # 8   bottom-left
                (3780, 4700),  # 9   bottom-right
            ],
            "edges": [
                ## top road — horizontal (same y=700)
                (0, 1), (1, 2),
                ## left vertical (same x=520)
                (0, 3), (3, 8),
                ## center vertical (same x=2500)
                (1, 4),
                ## right vertical (same x=3780)
                (2, 6), (6, 9),
                ## mid road — horizontal (same y=2400)
                (3, 4), (4, 5), (5, 6), (6, 7),
                ## bottom road — horizontal (same y=4700)
                (8, 9),
            ],
        },

        ## --- MARILLAC (Act 1 right map) ---
        ## Right vertical road + top horizontal road + bottom connection.
        ## Building on the left side — can't walk through it.
        ##
        ##   Layout:
        ##       0 exit ============ 1
        ##                           |
        ##                           2  Manong Josh
        ##                           |
        ##                           3
        ##                           |
        ##                           4  Manong Chris
        ##                           |
        ##       6 ================= 5
        ##
        "ui/overhead_marillac.png": {
            "waypoints": [
                (325,  650),   # 0   top-left exit (→ banwa)
                (3650, 650),   # 1   top-right intersection
                (3650, 1500),  # 2   right road — Manong Josh
                (3650, 2500),  # 3   right road, mid
                (3650, 3500),  # 4   right road — Manong Chris
                (3650, 4400),  # 5   bottom-right
                (325,  4400),  # 6   bottom-left
            ],
            "edges": [
                ## top road — horizontal (same y=650)
                (0, 1),
                ## right vertical road (same x=3650)
                (1, 2), (2, 3), (3, 4), (4, 5),
                ## bottom road — horizontal (same y=4400)
                (5, 6),
            ],
        },
    }

    def find_nearest_waypoint(x, y, waypoints):
        """Find index of the closest waypoint to (x, y)."""
        best = 0
        best_d = float('inf')
        for i, (wx, wy) in enumerate(waypoints):
            d = (x - wx)**2 + (y - wy)**2
            if d < best_d:
                best_d = d
                best = i
        return best

    def find_road_path(sx, sy, ex, ey, map_name):
        """Return list of (x,y) points to walk through, following road waypoints.
        If the map has no road graph, returns a direct path."""
        if map_name not in MAP_ROAD_GRAPHS:
            return [(ex, ey)]

        graph = MAP_ROAD_GRAPHS[map_name]
        wps = graph["waypoints"]
        edges = graph["edges"]

        swp = find_nearest_waypoint(sx, sy, wps)
        ewp = find_nearest_waypoint(ex, ey, wps)

        if swp == ewp:
            return [(ex, ey)]

        # build adjacency
        adj = [[] for _ in range(len(wps))]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # BFS shortest path
        queue = deque([(swp, [swp])])
        visited = {swp}
        while queue:
            cur, path = queue.popleft()
            if cur == ewp:
                # return waypoint coords (include start wp so we walk to the road first)
                result = [wps[i] for i in path]
                result.append((ex, ey))
                return result
            for nb in adj[cur]:
                if nb not in visited:
                    visited.add(nb)
                    queue.append((nb, path + [nb]))

        # no path found — walk direct
        return [(ex, ey)]


## ============================================================================
## MAP SCREEN
## ============================================================================

screen map_screen(map_bg, nodes, task_text="", map_scale=1.0, player_zoom=2.5):

    predict False

    ## Key bindings for phone, inventory, encyclopedia — overlays so the map stays visible
    key "p" action If(phone_unlocked, Show("phone_screen"), NullAction())
    key "e" action Show("encyclopedia_screen")
    key "d" action Show("dictionary_screen")

    ## Full-screen map background — stretches to fill 1920x1080
    add ("images/" + map_bg):
        xpos 0
        ypos 0
        xsize 1920
        ysize 1080
        fit "cover"

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
                background Solid("#00000000")
                hover_background Solid("#00000000")

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
                background Solid("#00000000")

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
        zoom player_zoom
        xanchor 0.5
        yanchor 0.5

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

    ## --- QUICK-ACCESS TOOLBAR (top center) ---
    ## Same construction as the task box above: outer glow + dark panel + gold ornaments.

    frame:
        xalign 0.5
        ypos 14
        padding (3, 3, 3, 3)
        background Frame(Solid("#f6d79d22"), 0, 0)

        frame:
            xfill True
            padding (20, 10, 20, 10)
            background Frame(Solid("#1e0c12ee"), 0, 0)

            vbox:
                xfill True
                spacing 0

                ## Top ornament line
                hbox:
                    xalign 0.5
                    spacing 6

                    frame:
                        xsize 30 ysize 2 yalign 0.5
                        background Solid("#f6d79d66") padding (0, 0, 0, 0)
                    frame:
                        xsize 6 ysize 6 yalign 0.5
                        background Solid("#f6d79d") padding (0, 0, 0, 0)
                    frame:
                        xsize 60 ysize 2 yalign 0.5
                        background Solid("#f6d79d") padding (0, 0, 0, 0)
                    frame:
                        xsize 6 ysize 6 yalign 0.5
                        background Solid("#f6d79d") padding (0, 0, 0, 0)
                    frame:
                        xsize 30 ysize 2 yalign 0.5
                        background Solid("#f6d79d66") padding (0, 0, 0, 0)

                null height 8

                ## Button row
                hbox:
                    xalign 0.5
                    spacing 20

                    ## [E]ncyclopedia
                    button:
                        background Solid("#00000000")
                        hover_background Solid("#f6d79d14")
                        insensitive_background Solid("#00000000")
                        padding (10, 4, 10, 4)
                        action Show("encyclopedia_screen")

                        hbox:
                            spacing 5
                            yalign 0.5
                            frame:
                                xsize 18 ysize 18 yalign 0.5
                                padding (0, 0, 0, 0)
                                background Solid("#5c1a1a")
                                text "E":
                                    xalign 0.5 yalign 0.5
                                    size 11 bold True
                                    color "#ffd700"
                                    outlines [(1, "#1e0c12", 0, 0)]
                            text "ncyclopedia":
                                yalign 0.5 size 15
                                color "#f1debf"
                                outlines [(2, "#1e0c12", 0, 0)]

                    ## Thin gold divider
                    frame:
                        xsize 1 ysize 20 yalign 0.5
                        background Solid("#f6d79d44") padding (0, 0, 0, 0)

                    ## [D]ictionary
                    button:
                        background Solid("#00000000")
                        hover_background Solid("#f6d79d14")
                        insensitive_background Solid("#00000000")
                        padding (10, 4, 10, 4)
                        action Show("dictionary_screen")

                        hbox:
                            spacing 5
                            yalign 0.5
                            frame:
                                xsize 18 ysize 18 yalign 0.5
                                padding (0, 0, 0, 0)
                                background Solid("#5c1a1a")
                                text "D":
                                    xalign 0.5 yalign 0.5
                                    size 11 bold True
                                    color "#ffd700"
                                    outlines [(1, "#1e0c12", 0, 0)]
                            text "ictionary":
                                yalign 0.5 size 15
                                color "#f1debf"
                                outlines [(2, "#1e0c12", 0, 0)]

                    ## Thin gold divider
                    frame:
                        xsize 1 ysize 20 yalign 0.5
                        background Solid("#f6d79d44") padding (0, 0, 0, 0)

                    ## [P]hone
                    button:
                        background Solid("#00000000")
                        hover_background Solid("#f6d79d14")
                        insensitive_background Solid("#00000000")
                        padding (10, 4, 10, 4)
                        action If(phone_unlocked, Show("phone_screen"), NullAction())
                        sensitive phone_unlocked

                        hbox:
                            spacing 5
                            yalign 0.5
                            frame:
                                xsize 18 ysize 18 yalign 0.5
                                padding (0, 0, 0, 0)
                                background Solid("#5c1a1a")
                                text "P":
                                    xalign 0.5 yalign 0.5
                                    size 11 bold True
                                    color "#ffd700"
                                    outlines [(1, "#1e0c12", 0, 0)]
                            text "hone":
                                yalign 0.5 size 15
                                color ("#f1debf" if phone_unlocked else "#f1debf44")
                                outlines [(2, "#1e0c12", 0, 0)]

                null height 8

                ## Bottom ornament line (mirrors top)
                hbox:
                    xalign 0.5
                    spacing 6

                    frame:
                        xsize 30 ysize 2 yalign 0.5
                        background Solid("#f6d79d66") padding (0, 0, 0, 0)
                    frame:
                        xsize 6 ysize 6 yalign 0.5
                        background Solid("#f6d79d") padding (0, 0, 0, 0)
                    frame:
                        xsize 60 ysize 2 yalign 0.5
                        background Solid("#f6d79d") padding (0, 0, 0, 0)
                    frame:
                        xsize 6 ysize 6 yalign 0.5
                        background Solid("#f6d79d") padding (0, 0, 0, 0)
                    frame:
                        xsize 30 ysize 2 yalign 0.5
                        background Solid("#f6d79d66") padding (0, 0, 0, 0)

transform task_item_bob:
    yoffset 0
    block:
        easein 1.2 yoffset -1
        easeout 1.2 yoffset 0
        repeat

screen map_nodes_overlay(nodes):
    for node in nodes:
        $ _sx = int(node.x * MAP_SCALE_X)
        $ _sy = int(node.y * MAP_SCALE_Y)

        if not node.locked:
            if getattr(node, "icon_image", None):
                add ("npcs/" + node.icon_image):
                    zoom getattr(node, "icon_zoom", 0.12)
                    xpos _sx - 40
                    ypos _sy - 70
            text node.tooltip:
                xpos _sx - 40
                ypos _sy - 10
                size 12
                color "#ffffff"
                outlines [(3, "#000000", 0, 0)]
        else:
            if getattr(node, "icon_image", None):
                add ("npcs/" + node.icon_image):
                    zoom getattr(node, "icon_zoom", 0.12)
                    xpos _sx - 40
                    ypos _sy - 70
                    matrixcolor BrightnessMatrix(-0.5)
            text "🔒":
                xpos _sx - 40
                ypos _sy - 10
                size 12

## ============================================================================
## WALK LABEL
## ============================================================================

label walk_to_node(target_node, map_bg=None, nodes=None, player_zoom=2.5):
    ## Use the global current_map_bg if no explicit map_bg is passed
    if map_bg is None:
        $ map_bg = current_map_bg

    ## Show the map background so it stays visible during the walk animation
    # Use map_scale=0.5 for Act 5 CL3, otherwise default to 1.0
    python:
        _map_scale = 1.0
        _use_black_bg = False
        _fit_cover = False
        if map_bg == "maps/CL3.png" or map_bg == "ui/CAS_Overworld(F).png" or map_bg == "ui/Diwata.png":
            _fit_cover = True
    if map_bg == "maps/CL3.png":
        # Remove black/white border for CL3, use fit cover for consistency
        pass
    if _fit_cover:
        show expression ("images/" + map_bg) as walk_map_bg:
            xpos 0
            ypos 0
            xsize 1920
            ysize 1080
            fit "cover"
    else:
        show expression ("images/" + map_bg) as walk_map_bg:
            xalign 0.5
            yalign 0.5
            zoom _map_scale

    if nodes is not None:
        show screen map_nodes_overlay(nodes)

    ## Get road-aware path (list of waypoints to walk through)
    $ _road_path = find_road_path(player_map_x, player_map_y, target_node.x, target_node.y, map_bg)

    ## Walk through each segment of the path
    $ _walk_i = 0
    while _walk_i < len(_road_path):
        $ _wp_x, _wp_y = _road_path[_walk_i]
        $ _seg_dist = math.sqrt((player_map_x - _wp_x)**2 + (player_map_y - _wp_y)**2)

        if _seg_dist < 30:
            ## Skip tiny segments (already there)
            $ player_map_x = _wp_x
            $ player_map_y = _wp_y
            $ _walk_i += 1
        else:
            $ _dir = get_direction(player_map_x, player_map_y, _wp_x, _wp_y)
            $ _dur = calc_walk_duration(player_map_x, player_map_y, _wp_x, _wp_y)
            $ _sx = int(player_map_x * MAP_SCALE_X) - 60
            $ _sy = int(player_map_y * MAP_SCALE_Y) - 100
            $ _ex = int(_wp_x * MAP_SCALE_X) - 60
            $ _ey = int(_wp_y * MAP_SCALE_Y) - 100

            show expression ("player_walk_" + _dir) as player_sprite:
                pos (_sx, _sy)
                zoom player_zoom
                xanchor 0.5
                yanchor 0.5
                linear _dur pos (_ex, _ey)

            $ renpy.pause(_dur, hard=True)
            $ player_map_x = _wp_x
            $ player_map_y = _wp_y
            $ player_facing = _dir
            $ _walk_i += 1

    hide player_sprite
    hide walk_map_bg
    hide screen map_nodes_overlay
    $ target_node.mark_visited()

    return