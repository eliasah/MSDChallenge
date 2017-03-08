#!/usr/bin/python
# -*- coding: utf-8 -*-

from scipy.sparse import dok_matrix


def build_graph():
    """ This function reads the triplet dataset file and convert it into a bipartite graph
    and returns the number of songs and users in the graph
    -> useful for bipartite links recommendation
    """
    users_count = 0
    dataset_count = 0
    udict = dict()  # users dictionary
    sdict = dict()  # songs dictionary

    songs_count = 0
    links = 0

    file_nodes = open('data/graph.n', 'w')
    file_graph = open('data/graph.txt', 'w')
    file_songs = open('data/songs.txt', 'w')
    file_users = open('data/users.txt', 'w')
    dataset_file = open('data/train_triplets_sub.txt', 'r')

    # missing = {}
    # for lines in dataset_file:
    while 1:
        lines = dataset_file.readlines(1000000)
        if not lines:
            break
        for line in lines:
            # strip line
            line = line.strip()
            # split into triplet
            (user, song, play_count) = line.split()

            user = user.strip()
            song = song.strip()
            play_count = int(play_count.strip())

            # we will not check that for the moment since the number of access for EchoNest is restricted
            # to 120 access/minute
            # check if song_id exists in EchoNest
            # try :
            #    try:
            #        missing[song]
            #    except KeyError:
            #        artist.Song(str(song))
            #        time.sleep(1) # solve access excess on EchoNest API
            # except Exception as exception:
            #    missing[song] = 1
            #    print("Exception : %s. (%d already added)" %  (exception,songs_count))
            #    continue

            # check if user already exists and add it if not
            try:
                udict[user]
            except KeyError:
                udict[user] = users_count
                out_line = [str(user), '\n']
                file_users.writelines(out_line)
                users_count += 1

            # check if song already exists and add it if not
            try:
                sdict[song]
            except KeyError:
                sdict[song] = songs_count
                out_line = [str(song), " ", str(songs_count), '\n']
                file_songs.writelines(out_line)
                songs_count += 1

            out_line = [str(udict[user]), " ", str(sdict[song]), " ", str(play_count), '\n']
            file_graph.writelines(out_line)

    out_line = [str(songs_count), '\n']
    file_nodes.writelines(out_line)

    # close files
    dataset_file.close()
    file_songs.close()
    file_users.close()
    file_graph.close()
    file_nodes.close()

    return songs_count, users_count


def load_graph(links, nodes):
    """ Create a bipartite weighted graph from dataset_file and store it into
    graph.data. """
    print("creating user-song sparse matrix (%d,%d)" % (links, nodes))
    M = dok_matrix((links, nodes))
    f = open('data/graph.txt', 'r')
    print("populating matrix")
    for line in f:
        line = line.strip()
        (user, song, play_count) = line.split()
        user = int(user.strip())
        song = int(song.strip())
        # play_count = int(play_count.strip())
        M[user, song] = 1
    print(M)


def main():
    print("data pretreatment")
    n, m = build_graph()
    print("n = {}, m = {}".format(n, m))


if __name__ == "__main__":
    print("encoding train_triplets data")
    main()
