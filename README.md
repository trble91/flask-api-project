# Flask-api-Project

A project, designed to build an api. This is a RESTful api using CRUD functionality.

### Song Schema

``` py
Song(song_name='Space & Time', artist_name='TRBLE', track_time=180, album='Social Studies').save()
Song(song_name='FameMiss', artist_name='TRBLE', track_time=135, album='3:20').save()

app = Flask(__name__)

@app.route('/Song/', methods=['GET', 'POST'])
@app.route('/Song/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
  if request.method == 'GET':q
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

### Seed

Once the file has been seeded and accessed in postgresql it should appear like the image below:

![ALT](/seed%20data%20update.png)



