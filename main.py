#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

import prediction
import recommender
import utilities
# import numpy as np


def main():
    # usage python main [userId] [cosine|prod](cosine by default)
    # opt : cosine => cosine-based similarity
    # opt : prob => conditional probability-based similarity 
    user_id, opt = sys.argv[1:]
    user_id = int(user_id)
    opt = str(opt)

    print("Building recommendation for user : {:d}".format(user_id))
    # TRIPLETS FILE
    file_tt = "data/train_triplets_sub.txt"
    # We used kaggle evaluation triplets since they are different from our training
    file_tev = "data/kaggle_visible_evaluation_triplets.txt"

    print("Load Users from users list")
    users = list(utilities.load_users("data/kaggle_users.txt"))

    print("Ordering song by popularity")
    songs_ordered = utilities.sort_dict(utilities.count_songs(file_tt))

    print("Load unique Users indexes")
    uniq_users = utilities.unique_users(file_tt)

    print("Enumerate User with indexes")
    u_i = dict()
    for i, u in enumerate(uniq_users):
        u_i[u] = i

    print("Loading MSD training triplets")
    s_u = utilities.song_to_users(file_tt)

    print("Converting Users indexes")
    for s in s_u:
        s_set = set()
        for u in s_u[s]:
            s_set.add(u_i[u])
        s_u[s] = s_set

    del u_i

    # creating prediction
    if opt == "cosine":
        opt = 0
        print("Using cosine based similarity prediction")
    if opt == "prob":
        opt = 1
        print("Using cond-prob based similarity prediction")

    pr = prediction.ItemBasedPrediction(s_u, _sim=opt)
    # pr = prediction.UserBasedPrediction( )

    print("Loading users evaluation triplets")
    # u_s : dict of users with the set of songs the user has listened to (user vector)
    u_s = utilities.user_to_songs(file_tev)

    rec = recommender.Recommender(songs_ordered, pr)

    res = rec.recommend(users[user_id], u_s)
    utilities.save_recommendations(res, "result.txt")

    # Evaluation
    # yp = np.array([])
    # precision_recall_fscore_support(yt, yp, average="weighted")
    # utilities.print_results()


if __name__ == "__main__":
    main()
