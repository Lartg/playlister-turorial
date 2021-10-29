from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists


from flask import Flask
from flask import render_template

app = Flask(__name__)

playlists = [
  {'title': 'Chess Videos', 'description': 'Top games from TCEC'},
  {'title': 'chill vibes', 'description': 'Resonance'}
]

@app.route('/')
def playlist_index():
  """Show all playlists"""
  return render_template('playlists_index.html', playlists = playlists)

if __name__ == "__main__":
  app.run(debug=True)