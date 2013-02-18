#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
class ScanView:
    def __init__(self):
        self.scrolled_window = gtk.ScrolledWindow()
        for i in range(0, 20):
            self.scrolled_window.add(gtk.Label("String %d\n" % (i)))

    def get(self):
        return self.scrolled_window

    def main(self):
        gtk.main()
