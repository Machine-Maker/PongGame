class Scene(object):
    def __init__(self):
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError


class SceneManager(object):
    def __init__(self, next_scene):
        self.scene = None
        self.go_to(next_scene)

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self
