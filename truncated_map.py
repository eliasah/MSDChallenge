#!/usr/bin/python
""" This scripts provides functions for computing the Mean Average Precision 
 - reference to the formulas used in this script :
 The Million Song Dataset Challenge - Thierry Bertin-Mahieux, Brian McFee """
import numpy as np

def average_precision(rec_songs, Msu, k = 20 ):
    """ This function computes the average precision at each recall point"""
    """ rec_songs : list of recommended songs """
   
    np = len(Msu)
    print "np:", np
    nc = 0.0
    mapr_user = 0.0
    for j,s in enumerate(l_rec):
        if j >= k:
            break
        if s in Msu:
            nc += 1.0
            mapr_user += nc/(j+1)
    mapr_user /= min(np,k)
    return mapr_user


def mean_average_precision(l_users, l_rec_songs, u2s, k = 10):
    """ This function computes the mean average precision
    - reference to the mAP formula:
    The Million Song Dataset Challenge - Thierry Bertin-Mahieux, Brian McFee
    - param :
           l_users     : list of users
           l_rec_songs : list of lists of recommended songs for users
    - return:
           the mean average precision
    """
    return np.mean([average_precision(l_users,l_rec_songs) for l_users,l_rec_songs in zip(l_users,l_rec_songs)])

