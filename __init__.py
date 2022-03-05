from mycroft import MycroftSkill, intent_file_handler


class LostWorld(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('world.lost.intent')
    def handle_world_lost(self, message):
        self.speak_dialog('world.lost')


def create_skill():
    return LostWorld()

