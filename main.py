#!/usr/bin/env python
#  main.py
#
#  Copyright 2013 Jordan Hewitt <jordannh@sent.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade
import sys

# Import the local widgets
#import base_layout

class Base:

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        sys.exit()
        return False

    def __init__(self):
        gladefile = "./ui/remember-file-gtk_2_0.xml"
        gbuilder = gtk.Builder()
        gbuilder.add_from_file(gladefile)
	self.windowMain = gbuilder.get_object("window1")
	if (self.windowMain == None):
	    print "ERROR: Could not find main window."
	    sys.exit()
        self.windowMain.show_all()
        self.windowMain.connect("delete_event", self.delete_event)

    def main(self):
        gtk.main()

def main():
    gtk.main()
    return 0

if __name__=="__main__":
    b = Base()
    b.main()
    main();
