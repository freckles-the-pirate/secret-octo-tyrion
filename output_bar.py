#!/usr/bin/env Python
import pygtk
pygtk.require('2.0')
import gtk

class OutputBar(gtk.Widget):
    def __init__(self):
        print "Show some text"
