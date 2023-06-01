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
Song(song_name='Intro', artist_name='TRBLE', album='Social Studies', irsc= 'QZHNB1906815').save()
Song(song_name='Deadman', artist_name='TRBLE', album='Social Studies', irsc= 'QZHNB1906816').save()
Song(song_name='Diamonds', artist_name='TRBLE', album='Social Studies', irsc= 'QZHNB1906817').save()
Song(song_name='Champions', artist_name='TRBLE', album='Social Studies', irsc= 'QZHNB1906818').save()
Song(song_name='Real Thing', artist_name='TRBLE', album='Social Studies', irsc= 'QZHNB1906819').save()
Song(song_name='S X T (Space & Time)', artist_name='TRBLE', album='Social Studies', irsc= 'QZHNB1906820').save()
Song(song_name='Gone Till November', artist_name='TRBLE', album='Social Studies', irsc= 'QZHNB1906821').save()
Song(song_name='Rewind', artist_name='TRBLE', album='Social Studies', irsc= 'QZHNB1906822').save()
Song(song_name='Prayer', artist_name='TRBLE', album='Social Studies', irsc= 'QZHNB1906823').save()
Song(song_name='Go Tina', artist_name='TRBLE', album='Go Tina', irsc= 'QZFYZ2008014').save()
Song(song_name='Permanently Phakin\' Love', artist_name='TRBLE', album='The Lost Baker-EP', irsc= 'QZDA51929539').save()
Song(song_name='F U G I', artist_name='TRBLE', album='The Lost Baker-EP', irsc= 'QZDA51929540').save()
Song(song_name='Lil Secret', artist_name='TRBLE', album='The Lost Baker-EP', irsc= 'QZDA51929541').save()
Song(song_name='Untitled Changes', artist_name='TRBLE', album='The Lost Baker-EP', irsc= 'QZDA51929542').save()
Song(song_name='Karma', artist_name='TRBLE', album='The Lost Baker-EP', irsc= 'QZDA51929543').save()
Song(song_name='Check', artist_name='TRBLE', album='Check-Single', irsc= 'QZFZ52191493').save()
Song(song_name='Dear Father', artist_name='TRBLE', album='Dear Father-Single', irsc= 'QZNB82092242').save()
Song(song_name='Tht Side', artist_name='TRBLE', album='Tht Side-Single', irsc= '').save()
Song(song_name='Bad Guy', artist_name='TRBLE', album='Bad Guy-Single', irsc= '').save()
Song(song_name='Love Me', artist_name='TRBLE', album='Love Me-Single', irsc= '').save()


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

@app.route('/song/<id>')
def index():
  return 

@app.route('/Song/<id>', methods=['GET', 'PUT', 'DELETE'])
def index(id=None):
  if request.method == 'GET':
    if id: 
       return jsonify(model_to_dict(Song.get(Song.id == id)))
    else:
      song_list = []
      for song in Song.select():
        song_list.append(model_to_dict(song))
      return jsonify(song_list)

@app.route('/')
def index():
  return 'I love music!'

@app.route('/')
def index():
  return 'I love music!'
     
app.run(debug=True, port=9000)