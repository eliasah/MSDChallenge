#!/usr/bin/python

""" This script implements the Prediction class for Song-Based Recommendation Algorithms
- References :
* Item-Based Top-N Recommendation Algorithms - Mukund Deshpande, George Karypis
* Evalluation of Item-Based Top-N Recommendation Algorithms - George Karypis
* Finding Similar Items, Chapter 3 - Mining of Massive Datasets - Anand Rajaraman, Jeffery D. Ullman
"""

import utilities, math
import numpy as np

class SongBasedPrediction:
   
    def __init__(self, _R, _alpha = 0.5, _sim = 0):
        """ Initialize class Prediction
        - param :
                R      : train songs set
                alpha  : default equals 0.5
        """
        print "Creating Prediction"
        self.R = _R
        self.alpha = _alpha
        self.sim = _sim
        
    def cosine_similarity(self,i,j):
        """ Compute Cosine-Based Similarity between song i and song j
        - reference:
        Item-Based Top-N Recommendation Algorithms - Mukund Deshpande, George Karypis (section 4.1.1.1)
        - param :
                i  : song i
                j  : song j
        """
        sim    = 0
        freq_i = len(self.R[i])
        freq_j = len(self.R[j])
        freq_ij =  float(len(self.R[i] & self.R[j]))

        # if sets of songs i and i are not disjoint
        if freq_ij > 0:
            sim = freq_ij / (math.pow(freq_i,self.alpha) * math.pow(freq_j,self.alpha))
        return sim


    def similarity(self,i,j):
        """ Compute Conditional Probabiliry-based Similarity between song i and song j
        - reference:
        Item-Based Top-N Recommendation Algorithms - Mukund Deshpande, George Karypis (section 4.1.1.2)
        - param :
                i  : song i
                j  : song j
        """
        sim    = 0
        freq_i = len(self.R[i])
        freq_j = len(self.R[j])
        freq_ij =  float(len(self.R[i] & self.R[j]))

        # if sets of songs i and i are not disjoint
        if freq_ij > 0:
            sim = freq_ij / (freq_i * math.pow(freq_j,self.alpha))
        return sim

    def score(self,user_songs, all_songs):
        """ compute scores for each song using similarity
        between user song and actuall song
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
                    sim = self.cosine_similarity(song,u_song)
                if self.sim == 1:
                    sim = self.similarity(song,u_song)
                # we fix the locality-sensitive param at 2
                scores[song] += math.pow(sim,2)
            
            # if scores[song] > 0:
            #    print song,scores[song]
        
        return scores

class UserBasedPrediction():
    """ This class implements the User Based Prediction """
    def __init__(self, _M, _alpha = 0):
        self.M = _M
        self.alpha = _alpha

    def score(self,user_songs,  all_songs):
        scores= dict()

        for u_tr in self.M:
            print u_tr
            if not u_tr in self.M:
                continue
            w = float(len(self.M[u_tr] & user_songs))
            if w > 0:
                freqi = len(user_songs)
                freqj = len(self.M[u_tr])
                w /= (math.pow(freqi,self.alpha) * (math.pow(freqj,(1.0 - self.A))))
            for s in self.M[u_tr]:
                if s in scores:
                    scores[s]+=w
                else:
                    scores[s]=w
        return scores
