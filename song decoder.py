import math
def song_decoder(song):
    song=song.split('WUB')
    for i in range(len(song)):
        if '' in song:
            song.remove('')
    return ' '.join(song)
def is_square(n): 
    if n>=0 and len(str(math.sqrt(n)).split('.')[1])==1:
                    return True
    return False # fix me
    
    
    
