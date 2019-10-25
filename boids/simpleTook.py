from my_states import First


class SimpleTook(object):
    def __init__(self):
        self.state = First()
    def on_event(self,event):
        self.state = self.state.on_event(event)
