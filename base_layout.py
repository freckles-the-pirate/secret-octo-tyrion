#!/usr/bin/env Python
import pygtk
pygtk.require('2.0')
import gtk

def_y_pad = 4
def_x_pad = 4

class BaseLayout:
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
        base_table = gtk.Table(6, 1, homogeneous=True)

        # Attach the next level of widgets.
        base_table.attach(main_menu_bar.MainMenuBar, 0, 1, 0, 1,
            xoptions=EXPAND, xpadding=def_x_pad, ypadding=def_y_pad)

        base_table.attach(main_menu_bar.MainMenuBar, 0, 1, 0, 1,
            xoptions=EXPAND, xpadding=def_x_pad, ypadding=def_y_pad)

        base_table.attach(actions_bar.ActionsBar(), 0, 1, 2, 3,
            xoptions=FILL, xpadding=def_x_pad, ypadding=def_y_pad)

        base_table.attach(scan_view.ScanView(), 0, 1, 3, 4,
            xoptions=FILL, xpadding=def_x_pad, ypadding=def_y_pad)

        base_table.attach(scan_view.LabelsBar(), 0, 1, 4, 5,
            xoptions=FILL, xpadding=def_x_pad, ypadding=def_y_pad)

        base_table.attach(scan_view.OutputBar(), 0, 1, 5, 6,
            xoptions=FILL, xpadding=def_x_pad, ypadding=def_y_pad)
