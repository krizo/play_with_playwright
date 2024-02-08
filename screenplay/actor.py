
class Actor:
    def __init__(self, name: str, abilities: dict):
        self.name = name
        self.abilities = abilities

    def perform(self, task):
        task.perform(self)
