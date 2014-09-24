# -*- coding: utf-8 -*-
# [{time: value(button)}{}]
#time 함수 해서time 저장 
class Database(object):
    def __init__(self):
        self.music_database = []
#button은 키코드, timing은 현재시간. 
    def start_music(self,button, timing):
    	self.music_database.append({timing: button}) 




    def put(self, storage):
        self.database.append(storage)

    def 

    def out(self):
        return self.database

def start_music(button, timing, db):
	db.append({timing:button})
music_database=[]
start_music(85,"10:00:01",music_database)
start_music(90,"10:00:04",music_database)
print music_database