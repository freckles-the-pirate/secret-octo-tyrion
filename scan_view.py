#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
class ScanView(gtk.ScrolledWindow):
    def __init__(self):
        for i in range(0, 20):
            self.add(gtk.Label("String %d\n" % (i)))

    def main(self):
        gtk.main()
