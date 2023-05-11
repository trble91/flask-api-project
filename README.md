# Flask-api-Project'

### Songs
This was a mini project, designed to guide us through building an api. This is a RESTful api using CRUD functionality.

``` py
Song(song_name='Space & Time', artist_name='TRBLE', track_time=180, album='Social Studies').save()
Song(song_name='FameMiss', artist_name='TRBLE', track_time=135, album='3:20').save()

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
```

Please free to comment and/or commit. Something my wife used to say :()
