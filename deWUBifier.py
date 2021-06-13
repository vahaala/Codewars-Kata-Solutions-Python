test = "WUBWUBWUBWUBWUBTESTWUBYESWUB        WUBYESfjdsfhj WUBWUBWUB   NB S JDSJA   YESYESYWUB"
def song_decoder(song):
    new_song = " ".join(song.split("WUB")) #deletes WUBS
    final_songs = " ".join(new_song.split()) #removes excess spaces
    return final_songs #returns the new string
print(song_decoder(test))

