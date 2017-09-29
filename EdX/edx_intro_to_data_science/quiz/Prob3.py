# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:28:54 2017

@author: lwang138
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    result_list=[]
    current_size=0
    songs_left=songs.copy()
    if songs[0][2]>max_size:
        return result_list
    else:
        result_list.append(songs[0][0])
        current_size+=songs[0][2]
        del(songs_left[0])
        songs_left.sort(key=lambda x:x[2])
        while len(songs_left)>0 and current_size+songs_left[0][2]<=max_size:
            current_size+=songs_left[0][2]
            result_list.append(songs_left[0][0])
            del(songs_left[0])
        return result_list