class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.map = scene_map

    def play(self):
        next_scene = self.map.opening_scene()
        while next_scene:
            next_scene = self.map.next_scene(next_scene)



class Death(Scene):

    def enter(self):
        print('You died...')

class CentralCorridor(Scene):

    def enter(self):
        print('in central corridor')
        return 'laser_weapon_armory'


class LaserWeaponArmory(Scene):

    def enter(self):
        print('in laser armory')
        return 'the_bridge'

class TheBridge(Scene):

    def enter(self):
        print('in the bridge')
        return 'escape_pod'

class EscapePod(Scene):

    def enter(self):
        print('in escape pod')


class Map(object):

    def __init__(self, start_scene):
        self.start = start_scene
        self.scenes = {
            'central_corridor': CentralCorridor(),
            'laser_weapon_armory': LaserWeaponArmory(),
            'the_bridge': TheBridge(),
            'escape_pod': EscapePod()
        }

    def next_scene(self, scene_name):
        return self.scenes[scene_name]

    def opening_scene(self):
        return self.next_scene(self.start)
        

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

