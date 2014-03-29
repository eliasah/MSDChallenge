#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import utilities,recommender,prediction

def main():
    # opt : cosine => cosine-based similarity
    # opt : prob => conditional probability-based similarity 
    user_id, opt = sys.argv[1:]
    user_id = int(user_id)
    opt = str(opt)
    
    print "Building recommendation for user : %d" % (user_id)
    
    # TRIPLETS FILE
    file_tt = "data/train_triplets_sub.txt"
    # We used kaggle evaluation triplets since they are different from our training
    file_tev = "data/kaggle_visible_evaluation_triplets.txt"
    
    print "Load Users from users list"
    users = list(utilities.load_users("data/kaggle_users.txt"))

    print "Ordering song by popularity"
    songs_ordered = utilities.sort_dict(utilities.count_songs(file_tt))

    print "Load unique Users indexes"
    uniq_users = utilities.unique_users(file_tt)

    print "Enumerate User with indexes"
    Ui = dict()
    for i,u in enumerate(uniq_users):
        Ui[u] = i
        
    print "Loading MSD training triplets"
    Su = utilities.song_to_users(file_tt)

    print "Converting Users indexes"
    for s in Su:
        s_set = set()
        for u in Su[s]:
            s_set.add(Ui[u])
        Su[s]=s_set

    del Ui

    # creating prediction
    if opt == "cosine":
        opt = 0
        print "Using cosine based similarity prediction"
    if opt == "prob":
        opt = 1
        print "Using cond-prob based similarity prediction"
    
    pr = prediction.SongBasedPrediction(Su, _sim = opt)
    # pr = prediction.UserBasedPrediction( )

    print "Loading users evaluation triplets"
    # Us : dict of users with the set of songs the user has listened to (user vector)
    Us = utilities.user_to_songs(file_tev)

    rec = recommender.Recommender(songs_ordered,pr)

    res = rec.recommend(users[user_id],Us)
    utilities.save_recommendations(res,"result.txt")

    # Evalutation
    # yp = np.array([]) 
    # precision_recall_fscore_support(yt,yp,average="weighted")

    utilities.print_results()

if __name__ == "__main__":
    main()
