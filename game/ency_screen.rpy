# Default variable to track which entry the player is looking at
default current_ency_entry = None

screen encyclopedia():
    tag menu
    style_prefix "game_menu"
    
    # Use parallax background as the base
    add "gui/main_menu/layer7.png"
    add Solid("#000000aa") # Darken for readability

    hbox:
        align (0.5, 0.4)
        spacing 40
        xsize 1600

        # LEFT PANEL: Entry List (entryListContainer from my Unity shit)
        vbox:
            xsize 450
            label _("ENTRIES") style "main_menu_title" text_size 40
            
            viewport:
                scrollbars "vertical"
                mousewheel True
                vbox:
                    spacing 10
                    for entry_id, entry in all_entries.items():
                        if entry_id in persistent.encyclopedia_unlocks:
                            textbutton entry.name:
                                action SetVariable("current_ency_entry", entry)
                                style "custom_menu_button"
                        else:
                            textbutton "???" action None style "custom_menu_button"

        # RIGHT PANEL: Details (titleText/descriptionText from my Unity shit)
        vbox:
            xsize 1100
            if current_ency_entry:
                if current_ency_entry.icon:
                    add current_ency_entry.icon xalign 0.5
                
                text current_ency_entry.name style "main_menu_title" size 70
                text current_ency_entry.category color "#ffcc00" size 24
                null height 20
                text current_ency_entry.desc style "say_dialogue"
            else:
                text _("Select an entry to learn more about Visions.") align (0.5, 0.5) style "say_dialogue"

    # Return button
    textbutton _("RETURN"):
        align (0.5, 0.95)
        action Return()
        style "custom_menu_button"
        text_size 45