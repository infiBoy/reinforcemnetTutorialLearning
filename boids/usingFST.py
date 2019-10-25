from fysom import  *

fsm = Fysom({'initial':'sleep','final':'red','events':[
    {'name':'wake','src':'sleeping','dst':'awake'},
    {'name': 'sleep', 'src': 'awake', 'dst': 'sleeping'},
]})

print(fsm.current)
fsm.sleep()
print(fsm.current)
