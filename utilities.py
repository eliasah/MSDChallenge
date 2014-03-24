import random, math
# if you want to use the print_result() function, please add your key and comment the next line
import echo_key 
from pyechonest import config,artist,song
# set API key
# config.ECHO_NEST_API_KEY="YOUR_ECHO_NEST_APIKEY"

def get_song_id(id):
    """ This function get the echonest if of the song from the songs file given the id of the song"""
    with open("data/kaggle_songs.txt") as file:
        for line in file:
            line = line.strip().split()
            if id == line[1]:
                return line[0]

def print_results():
    """ This function prints out the recommended song (name,artist) with their hotttnesss ranking according to the Echonest API """
    with open("result.txt",'r') as file:
        for line in file:
            list = line.strip().split()
            for song_id in list:
                try :
                    s = song.Song(str(song_id))
                    print "%s | %s - %s" % (s.song_hotttnesss,s, s.artist_name)
                except Exception as exception:
                    # print "Exception : %s. Can't get information about song %s" % (exception,song_id)
                    continue

def count_songs(file):
    """ This function counts the number of users that listens to each song """
    s = dict()
    with open(file,"r") as f:
        for line in f:
            _,song,_=line.strip().split('\t')
            try:
                s[song]+=1
            except:
                s[song]=1
    return s

def count_users(file):
    """ This functions count the users given a triplet input file """
    u = dict()
    with open(file,"r") as f:
        for line in f:
            user,_,_=line.strip().split('\t')
            try:
                u[user]+=1
            except:
                u[user]=1
    return u

def sort_dict(d):
    """ This function returns the given dictionnary d sorted by its keys"""
    return sorted(d.keys(),key=lambda s:d[s],reverse=True)

def song_to_users(file):
    """ This function loads user,song,play_count triplets and returns the dictionary of song with set of users that listens to that song """
    d = dict()
    with open(file,"r") as f:
        for line in f:
            user,song,_ = line.strip().split('\t')
            if song in d:
                d[song].add(user)
            else:
                d[song]=set([user])
    return d

def user_to_songs(file):
    """ This finctions loads user,song,play_count triplets and returns the dictionaryof users with the set of songs the user has listened to"""
    d = dict()
    with open(file,"r") as f:
        for line in f:
            user,song,_ = line.strip().split('\t')
            if user in d:
                d[user].add(song)
            else:
                d[user]=set([song])
    return d

def load_users(file):
    """ This function loads users from users file and returns list of users"""
    with open(file,"r") as f:
        u = map(lambda line: line.strip(),f.readlines())
    return u

def unique_users(file):
    """ This function returns a set of unique user
    - param:
          file : training file
    """
    u = set()
    with open(file,"r") as f:
        for line in f:
            user, _, _ = line.strip().split('\t')
            if user not in u:
                u.add(user)
    return u 

def save_recommendations(r, file):
    """ This function saves recommendation given in argument into file
    - param :
             r     list of songs to save
             file  output file
    """
    print "Saving recommendations"
    f = open(file,"w")
    for r_songs in r:
        out_line = [str(r_songs), '\n']
        f.writelines(out_line)
    f.close()
