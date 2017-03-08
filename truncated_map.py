#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This scripts provides functions for computing the Mean Average Precision 
 - reference to the formulas used in this script :
 The Million Song Dataset Challenge - Thierry Bertin-Mahieux, Brian McFee """
import numpy as np


def average_precision(rec_songs, M, k=50):
    """ This function computes the average precision at each recall point
    - param :
             rec_songs : list of recommended songs
             M : user-song matrix
    """
    np = len(M)
    # print "np:", np
    nc = 0.0
    mapr_user = 0.0
    for j, s in enumerate(rec_songs):
        if j >= k:
            break
        if s in M:
            nc += 1.0
            mapr_user += nc / (j + 1)
    mapr_user /= min(np, k)
    return mapr_user


def mean_average_precision(l_users, l_rec_songs):
    """ This function computes the mean average precision
    - reference to the mAP formula:
    The Million Song Dataset Challenge - Thierry Bertin-Mahieux, Brian McFee
    - param :
           l_users     : list of users
           l_rec_songs : list of lists of recommended songs for users
    - return:
           the mean average precision
    """
    return np.mean([average_precision(l_users, l_rec_songs) for l_users, l_rec_songs in zip(l_users, l_rec_songs)])
