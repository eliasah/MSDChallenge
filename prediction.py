#!/usr/bin/python
# -*- coding: utf-8 -*-

import math


class ItemBasedPrediction:
    """ This script implements the SongBasedPrediction class
    - References :
        * Item-Based Top-N Recommendation Algorithms - Mukund Deshpande, George Karypis
        * Evaluation of Item-Based Top-N Recommendation Algorithms - George Karypis
        * Finding Similar Items, Chapter 3 - Mining of Massive Datasets - Jeffery D. Ullman
    """

    def __init__(self, _R, _alpha=0.5, _sim=0):
        """ Initialize class Prediction
        - param :
                R      : train songs set
                alpha  : default equals 0.5
        """
        print("Creating Prediction")
        self.R = _R
        self.alpha = _alpha
        self.sim = _sim

    def cosine_similarity(self, i, j):
        """ Compute Cosine-Based Similarity between song i and song j
        - reference:
            * Item-Based Top-N Recommendation Algorithms - Mukund Deshpande, George Karypis (section 4.1.1.1)
        - param :
                i  : song i
                j  : song j
        """
        sim = 0
        freq_i = len(self.R[i])
        freq_j = len(self.R[j])
        freq_ij = float(len(self.R[i] & self.R[j]))

        # if sets of songs i and i are not disjoint
        if freq_ij > 0:
            sim = freq_ij / (math.pow(freq_i, self.alpha) * math.pow(freq_j, self.alpha))
        return sim

    def similarity(self, i, j):
        """ Compute Conditional Probability-based Similarity between song i and song j
        - reference:
            * Item-Based Top-N Recommendation Algorithms - Mukund Deshpande, George Karypis (section 4.1.1.2)
        - param :
                i  : song i
                j  : song j
        """
        sim = 0
        freq_i = len(self.R[i])
        freq_j = len(self.R[j])
        freq_ij = float(len(self.R[i] & self.R[j]))

        # if sets of songs i and i are not disjoint
        if freq_ij > 0:
            sim = freq_ij / (freq_i * math.pow(freq_j, self.alpha))
        return sim

    def score(self, user_songs, all_songs):
        """ compute scores for each song using similarity between user song and actual song
        - param:
                user_songs : user songs set
                all_songs  : training songs set
        """
        scores = dict()
        for song in all_songs:
            scores[song] = 0.0

            if not (song in self.R):
                continue

            for u_song in user_songs:
                if not (u_song in self.R):
                    continue
                if self.sim == 0:
                    sim = self.cosine_similarity(song, u_song)
                if self.sim == 1:
                    sim = self.similarity(song, u_song)
                # we fix the locality-sensitive param at 2
                scores[song] += math.pow(sim, 2)

                # if scores[song] > 0:
                #    print song,scores[song]

        return scores


class UserBasedPrediction:
    """ This script implements the UserBasedPrediction class 
    - Reference : 
        * Fouille de données et aide à la decision - Cours d'introduction au datamining - Anne-Claire Haury
    """

    def __init__(self, _M, _alpha=0):
        self.M = _M
        self.alpha = _alpha

    def score(self, user_songs, all_songs):
        """ This function computes scores for each each user using user based similarity 
        - param:
                user_songs : user songs vector
                all_songs  : training songs set
        """
        scores = dict()

        for user in self.M:
            if not user in self.M:
                continue

            # compute similarity
            w = float(len(self.M[user] & user_songs))
            if w > 0:
                freqi = len(user_songs)
                freqj = len(self.M[user])
                w /= (math.pow(freqi, self.alpha) * (math.pow(freqj, (1.0 - self.A))))

            # adding scores
            for s in self.M[user]:
                if s in scores:
                    scores[s] += w
                else:
                    scores[s] = w
        return scores
