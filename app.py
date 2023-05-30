from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('songs', user='banana', password='123', host='localhost', port='5432')

class BaseModel(Model):
  class Meta:
    database = db

class Song(BaseModel):
  song_name = CharField()
  artist_name = CharField()
  album = CharField()
  irsc = CharField()

db.connect()
db.drop_tables([Song])
db.create_tables([Song])

Song(song_name='SHAQ', artist_name='TRBLE', album='3:20', irsc= 'QZDA51930843').save()
Song(song_name='FameMiss', artist_name='TRBLE', album='3:20', irsc= 'QZDA51930842').save()
Song(song_name='Onto Something', artist_name='TRBLE', album='Onto Something', irsc= 'QZMWW2053469').save()
Song(song_name='FameMiss', artist_name='TRBLE', album='Social Studies', irsc= '').save()
Song(song_name='FameMiss', artist_name='TRBLE', album='Social Studies', irsc= '').save()
Song(song_name='FameMiss', artist_name='TRBLE', album='Social Studies', irsc= '').save()
Song(song_name='FameMiss', artist_name='TRBLE', album='Social Studies', irsc= '').save()
Song(song_name='FameMiss', artist_name='TRBLE', album='Social Studies', irsc= '').save()
Song(song_name='FameMiss', artist_name='TRBLE', album='Social Studies', irsc= '').save()
Song(song_name='FameMiss', artist_name='TRBLE', album='Social Studies', irsc= '').save()


app = Flask(__name__)

@app.route('/Song/', methods=['GET', 'POST'])
@app.route('/Song/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
  if request.method == 'GET':
    if id: 
       return jsonify(model_to_dict(Song.get(Song.id == id)))
    else:
      song_list = []
      for song in Song.select():
        song_list.append(model_to_dict(song))
      return jsonify(song_list)

  if request.method == 'POST':
    new_song = dict_to_model(song, request.get_json())
    new_song.save()
    return jsonify({'Success': True}) 
  
  if request.method == 'PUT':
    body = request.get_json()
    Song.update(body).where(Song.id == id).execute()
    return "Song " + str(id) + " has been updated."
  
  if request.method == 'DELETE':
    Song.delete().where(Song.id == id).execute()
    return "Song " + str(id) + " has been deleted."
    
@app.route('/')
def index():
  return 'I love music!'
     
app.run(debug=True, port=9000)