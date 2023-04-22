db = connect("root:root@localhost:27017/admin");
db = db.getSiblingDB('spotify_songs');
db.createUser({
'user': "spotify_songs",
'pwd': "sp123",
'roles': [{
    'role': 'dbOwner',
    'db': 'spotify_songs'}]});
// user created

conn = connect("spotify_songs:sp123@localhost:27017/spotify_songs");
db = db.getSiblingDB('spotify_songs');
db.test.insertOne(
    {
      title: "The Favourite",
      genres: [ "Drama", "History" ],
      runtime: 121,
      rated: "R",
      year: 2018,
      directors: [ "Yorgos Lanthimos" ],
      cast: [ "Olivia Colman", "Emma Stone", "Rachel Weisz" ],
      type: "movie"
    }
)
// add new collection