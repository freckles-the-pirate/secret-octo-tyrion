#!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk
import controllers.main_menu_bar_controller


class MainMenuBar(gtk.Widget):
    def __init__(self):
        uimanager = gtk.UIManager()
        accelGroup = uimanager.get_accel_group()
        merge_id = uimanager.add_ui_from_file("./ui/main_menu.xml")
        self = uimanager.get_widget("/MainMenu")

    def main(self):
        gtk.main()
