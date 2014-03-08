from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist
 
engine = create_engine('sqlite:///mymusic.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# Create an artist
new_artist = Artist("Deadmau5")
new_artist.albums = [Album("Random Album Title", 
                           "Progressive House",
                           "Ultra Records", "CD")]
 
# add more albums
more_albums = [Album("For Lack Of A Better Name",
                     "Electro",
                     "Mau5trap Recordings, Virgin", "CD"),
               Album("4x4=12", 
                     "Tech House",
                     "Ultra Records", "CD")]                              
new_artist.albums.extend(more_albums)
 
# Add the record to the session object
session.add(new_artist)
# commit the record the database
session.commit()
 
# Add several artists
session.add_all([
    Artist("MXPX"),
    Artist("Kutless"),
    Artist("Thousand Foot Krutch")
    ])
session.commit()