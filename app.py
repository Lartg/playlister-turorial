from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

playlists = [
  {'title': 'Chess Videos', 'description': 'Top games from TCEC'},
  {'title': 'chill vibes', 'description': 'Resonance'}
]

@app.route('/')
def playlist_index():
  """Show all playlists"""
  return render_template('playlists_index.html', playlists = playlists)

@app.route('/playlists/new')
def playlists_new():
  return render_template('playlists_new.html')

@app.route('/playlists', methods=['POST'])
def playlists_submit():
  playlist = {
    'title': request.form.get('title'),
    'description': request.form.get('description')
  }
  playlists.append(playlist)
  return redirect(url_for('playlist_index'))

if __name__ == "__main__":
  app.run(debug=True)