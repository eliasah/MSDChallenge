#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This scripts implements the Recommender class for Item-Based Recommendation Algorithms:
- References :
* Item-Based Top-N Recommendation Algorithms - Mukund Deshpande, George Karypis
* Evaluation of Item-Based Top-N Recommendation Algorithms - George Karypis
* Content-Based Recommendations, Chapter 9.2 - Mining of Massive Datasets - Jeffery D. Ullman
"""

import utilities


class Recommender:
    def __init__(self, _all_songs, _predictor, _k=10):
        """ This is the recommender constructor with default k = 10"""
        print("Initialize recommender")
        self.predictor = _predictor
        self.all_songs = _all_songs
        self.k = _k

    def recommend(self, user, u_s):
        """ This function builds the recommendation for a given user over the dictionary of u_s (user-set_of_songs)
        - References :
            * Item-Based Top-N Recommendation Algorithms, 4.2 Applying the model - Mukund Deshpande, George Karypis.
        """
        songs_sorted = list()
        p = self.predictor
        print("Building recommendation - Fetching top items (ordered)")
        if user in u_s:
            s_songs = utilities.sort_dict(p.score(u_s[user], self.all_songs))
        else:
            # if user not in the matrix we recommend the best songs
            s_songs = list(self.all_songs)

        cleaned_songs = list()
        for x in s_songs:
            if len(cleaned_songs) >= self.k:
                break
            if x not in u_s[user]:
                cleaned_songs.append(x)

        songs_sorted += [cleaned_songs]

        r = list()
        ii = [0]

        # Top-K items
        while len(r) < self.k:
            s = songs_sorted[0][ii[0]]
            if s in r:
                continue
            else:
                r.append(s)
            ii[0] += 1

        return r
