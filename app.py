from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb+srv://Admin:kHwGiTilGkc8OEq4@cluster0.anqw0.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.get_default_database()
playlists = db.playlists

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def video_url_creator(id_list):
  videos = []
  for vid_id in id_list:
    video = 'https://youtube.com/embed/' + vid_id
    videos.append(video)
  return videos

@app.route('/')
def playlist_index():
  """Show all playlists"""
  return render_template('playlists_index.html', playlists = playlists.find())

@app.route('/playlists/<playlist_id>')
def display_playlist(playlist_id):
  playlist = playlists.find_one({'_id': ObjectId(playlist_id)})
  return render_template('playlists_show.html', playlist = playlist)

@app.route('/playlists/<playlist_id>/edit')
def playlist_editor(playlist_id):
  playlist = playlists.find_one({'_id': ObjectId(playlist_id)})
  return render_template('playlists_edit.html', playlist=playlist, title="Edit Playlist")

@app.route('/playlists/<playlist_id>', methods=['POST'])
def update_playlist(playlist_id):
  video_ids = request.form.get('video_ids').split()
  videos = video_url_creator(video_ids)
  updated_playlist = {
    'title': request.form.get('title'),
    'description': request.form.get('description'),
    'videos': videos,
    'video_ids': video_ids
    }
  playlists.update_one(
    {'_id': ObjectId(playlist_id)},
    {'$set': updated_playlist})
  return redirect(url_for('display_playlist', playlist_id=playlist_id))
  

@app.route('/playlists/new')
def playlists_new():
  playlist = {}
  return render_template('playlists_new.html', playlist=playlist,title="New Playlist")

@app.route('/playlists', methods=['POST'])
def playlists_submit():
  video_ids =  request.form.get('video_ids').split()
  videos = video_url_creator(video_ids)
  playlist = {
    'title': request.form.get('title'),
    'description': request.form.get('description'),
    'videos': videos,
    'video_ids': video_ids
  }
  playlists.insert_one(playlist)
  return render_template('playlists_show.html', playlist = playlist)

@app.route('/playlists/<playlist_id>/delete', methods=['POST'])
def delete_playlist(playlist_id):
  playlists.delete_one({'_id': ObjectId(playlist_id)})
  return redirect(url_for('playlist_index'))

if __name__ == "__main__":
  app.run(debug=True)
  