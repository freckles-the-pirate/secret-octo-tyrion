#!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk
import controllers.main_menu_bar_controller


class MainMenuBar:
    def __init__(self):
        self.uimanager = gtk.UIManager()
        self.accelGroup = self.uimanager.get_accel_group()
        self.merge_id = self.uimanager.add_ui_from_file("./ui/main_menu.xml")

    def get(self):
        return self.accelGroup

    def main(self):
        gtk.main()
