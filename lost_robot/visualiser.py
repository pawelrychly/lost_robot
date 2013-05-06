__author__ = 'Pawel Rychly, Maciej Trojan'

import gtk
import cairo
from world import World
class Board(gtk.DrawingArea):

    def __init__(self, world):
        super(Board, self).__init__()

        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0, 0, 0))
        self.set_size_reqsuest(world.get_width(), world.get_height())
        self.connect("expose-event", self.expose)

    def on_key_down(self, event):

        key = event.keyval

        if key == gtk.keysyms.Left:
            print "left"

        if key == gtk.keysyms.Right:
            print "right"

        if key == gtk.keysyms.Up:
            print "up"

        if key == gtk.keysyms.Down:
            print "down"

class WorldVisualisation(gtk.Window):

    def __init__(self, world):
        super(WorldVisualisation, self).__init__()

        self.set_title('lost robot')
        self.set_size_request(world.get_width(), world.get_height())
        self.set_resizable(False)
        self.set_position(gtk.WIN_POS_CENTER)

        self.board = Board(world)
        self.connect("key-press-event", self.on_key_down)

        self.add(self.board)

        self.connect("destroy", gtk.main_quit)
        self.show_all()


    def on_key_down(self, widget, event):
        key = event.keyval
        self.board.on_key_down(event)

    def expose(self, widget, event):

        cr = widget.window.cairo_create()


        cr.set_source_rgb(0, 0, 0)
        cr.paint()

        cr.set_source_surface(self.apple, self.apple_x, self.apple_y)
        cr.paint()

        for z in range(self.dots):
            if (z == 0):
                cr.set_source_surface(self.head, x[z], y[z])
                cr.paint()
            else:
                cr.set_source_surface(self.dot, x[z], y[z])
                cr.paint()



world = World(500,300)
WorldVisualisation(world)
gtk.main()

