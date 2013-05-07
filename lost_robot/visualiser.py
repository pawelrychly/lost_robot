__author__ = 'Pawel Rychly, Maciej Trojan'

import gtk
import cairo
import math
import glib
from particle_filter import ParticleFilter

from world import World
class Board(gtk.DrawingArea):

    def __init__(self, world, particle_filter):
        super(Board, self).__init__()
        self.world = world
        self.particle_filter = particle_filter
        self.robot = world.get_robot()
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0, 0, 0))
        self.connect("expose-event", self.expose)
        glib.timeout_add(50, self.on_timer)



    def on_key_down(self, event):

        key = event.keyval

        if key == gtk.keysyms.Left:
            self.robot.change_direction(0.1)
            self.particle_filter.next_step(0.1)
            print "left"

        if key == gtk.keysyms.Right:
            self.robot.change_direction(-0.1)
            self.particle_filter.next_step(-0.1)
            print "right"

    def on_timer(self):
        self.world.run()
        self.particle_filter.next_step(0)
        self.queue_draw()
        return True


    def _draw_direction_arrow(self, cr):
        arrow_length = 30
        arrow_x = (math.cos(self.robot.get_direction()) * arrow_length)
        arrow_y = (math.sin(self.robot.get_direction()) * arrow_length)
        cr.move_to(0, 0)
        cr.line_to(arrow_x, arrow_y);
        cr.move_to(0, 0)

    def _draw_landmarks(self, cr):
        landmarks = self.world.get_landmarks()
        for lm in landmarks:
            cr.save()
            self._draw_circle(cr, lm)
            cr.set_source_rgb(0.4, 0.8, 0.4)
            cr.fill()
            cr.restore()


    def _draw_circle(self, cr, position):
        cr.translate(position["x"], position["y"])
        cr.move_to(0, 0)
        cr.arc(0, 0, 5, 0, 2 * math.pi)
        cr.stroke_preserve()
        cr.move_to(0, 0)


    def _draw_filter(self, cr):
        particles = self.particle_filter.get_particles()
        for particle in particles:
            cr.save()
            #self._draw_circle(cr, particle.get_position())

            cr.translate(particle.get_position()["x"], particle.get_position()["y"])
            cr.move_to(0, 0)
            cr.arc(0, 0, 1, 0, 2 * math.pi)
            cr.stroke_preserve()
            cr.move_to(0, 0)
            cr.set_source_rgb(0.4, 0.8, 0.8)
            cr.fill()
            cr.restore()

    def expose(self, widget, event):
        position = self.robot.get_position()
        cr = widget.window.cairo_create()
        self._draw_landmarks(cr)
        cr.set_source_rgb(0.7, 0.2, 0.0)
        cr.save()
        cr.translate(position["x"], position["y"])
        self._draw_direction_arrow(cr)
        cr.arc(0, 0, 5, 0, 2 * math.pi)
        cr.stroke_preserve()
        cr.set_source_rgb(0.3, 0.4, 0.6)
        cr.fill()
        cr.restore()
        self._draw_filter(cr)



class WorldVisualisation(gtk.Window):

    def __init__(self, world, particle_filter):
        super(WorldVisualisation, self).__init__()

        self.set_title('lost robot')
        self.set_size_request(world.get_width(), world.get_height())
        self.set_resizable(False)
        self.set_position(gtk.WIN_POS_CENTER)

        self.board = Board(world, particle_filter)
        self.connect("key-press-event", self.on_key_down)

        self.add(self.board)

        self.connect("destroy", gtk.main_quit)
        self.show_all()


    def on_key_down(self, widget, event):
        key = event.keyval
        self.board.on_key_down(event)



world = World(500,300)
particle_filter = ParticleFilter(world)
WorldVisualisation(world, particle_filter)
gtk.main()
world.run()

