#!/usr/bin/env Python
import pygtk
pygtk.require('2.0')
import gtk

## Import local widgets
import main_menu_bar
import icon_bar
import actions_bar
import scan_view
import labels_bar
import output_bar

def_y_pad = 4
def_x_pad = 4

class BaseLayout(gtk.Table):
    def __init__(self):
        # Create the table.
        # The table will be single-columned with each collumn as
        # follows:
        #   1) Main menu bar
        #   2) Icon bar (quick access save, new, etc.)
        #   3) Actions Bar (search, mainly)
        #   4) ScanView bar (scrolling page of scanned docs)
        #   5) Labels bar
        #   6) Info output bar.

        # Attach the next level of widgets.
        mmb = main_menu_bar.MainMenuBar()
        self.attach(mmb, 0, 1, 0, 1, xoptions=gtk.EXPAND,
            xpadding=def_x_pad, ypadding=def_y_pad)

        ibar = icon_bar.IconBar()
        self.attach(ibar, 0, 1, 1, 2, xoptions=gtk.EXPAND,
            xpadding=def_x_pad, ypadding=def_y_pad)

        abar = actions_bar.ActionsBar()
        self.attach(abar, 0, 1, 2, 3, xoptions=gtk.FILL,
            xpadding=def_x_pad, ypadding=def_y_pad)

        sv = scan_view.ScanView()
        self.attach(sv, 0, 1, 3, 4, xoptions=gtk.FILL,
            xpadding=def_x_pad, ypadding=def_y_pad)

        lb = labels_bar.LabelsBar()
        self.attach(lb, 0, 1, 4, 5, xoptions=gtk.FILL,
            xpadding=def_x_pad, ypadding=def_y_pad)

        ob = output_bar.OutputBar()
        self.attach(ob, 0, 1, 5, 6, xoptions=gtk.FILL,
            xpadding=def_x_pad, ypadding=def_y_pad)
