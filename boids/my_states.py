from state import State

class First(State):
    def on_event(self,event):
        if event =='second':
            return Second()
        return self

class Second(State):
    def on_event(self,event):
        if event =='first':
            return First()
        return  self

