import ppb

class Ship(ppb.BaseSprite):

      def on_update(self, update_event, signal):
          self.position += 0, -(4 * update_event.time_delta)

def setup(scene):
    scene.add(Ship(pos=(0, 3.5)))

ppb.run(setup=setup)

