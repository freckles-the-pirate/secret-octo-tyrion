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

# Import the local widgets
import main_menu_bar
import scan_view

class Base:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.add(BaseLayout())
        self.window.show()

    def main(self):
        self.mmb.main()
        self.scanview.main()
        gtk.main()

def main():
    gtk.main()
    return 0

if __name__=="__main__":
    b = Base()
    b.main()
    main();
