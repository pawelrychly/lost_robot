__author__ = 'Pawel Rychly, Maciej Trojan'

import gtk
import cairo
import math
import glib

from world import World
class Board(gtk.DrawingArea):

    def __init__(self, world):
        super(Board, self).__init__()
        self.world = world
        self.robot = world.get_robot()
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0, 0, 0))
        self.connect("expose-event", self.expose)
        glib.timeout_add(10, self.on_timer)


    def on_key_down(self, event):

        key = event.keyval

        if key == gtk.keysyms.Left:
            self.robot.change_direction(0.1)
            print "left"

        if key == gtk.keysyms.Right:
            self.robot.change_direction(-0.1)
            print "right"

    def on_timer(self):
        self.world.run()
        self.queue_draw()
        return True


    def _draw_direction_arrow(self, cr):
        arrow_length = 30
        arrow_x = (math.cos(self.robot.get_direction()) * arrow_length)
        arrow_y = (math.sin(self.robot.get_direction()) * arrow_length)
        cr.move_to(0, 0)
        cr.line_to(arrow_x, arrow_y);
        cr.move_to(0, 0)


    def expose(self, widget, event):

        position = self.robot.get_real_position()
        cr = widget.window.cairo_create()
        cr.set_source_rgb(0.7, 0.2, 0.0)

        cr.translate(position["x"], position["y"])
        self._draw_direction_arrow(cr)
        cr.arc(0, 0, 5, 0, 2 * math.pi)

        cr.stroke_preserve()
        cr.set_source_rgb(0.3, 0.4, 0.6)
        cr.fill()


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



world = World(500,300)
WorldVisualisation(world)
gtk.main()
world.run()

