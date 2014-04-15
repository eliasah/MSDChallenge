MSDChallenge
============

Abstract 
--------

MSDChallenge is music recommendation engine created for the Million Song Dataset challenge. 
It offers, considering a log listening history ,for a specific user a set of recommended songs.

We focused on a collaborative filtering approach based on the content, "Item-based Collaborative Filtering" (CF), because this approach is able to handle large data sets efficiently. 

We also studied functions for target similarities between songs, assigning scores for each song (using these functions) and the recommendation of songs for a user.

# Introduction

With the expansion of the distribution of digital content, people now have access to music collections on an unprecedented scale. Commercial music libraries have several million songs [1] , far beyond the ability to listen to every single person (one million songs take more than seven years of non-stop listening ). 
To help users cope with the rapid expansion of music available, many academic studies have been made to automate the search, annotation and search for music content [2].

Clearly, the advancement of technology information retrieval music can have a significant impact on commercial music recommendation systems such as Google, Apple and Amazon, among others. However, as for now, the vast majority of academic efforts focused on simple tasks related to the assessment of similarity, either between users or between songs.

Content-based algorithms use the set of user history to generate a prediction. These systems employ statistical techniques to find a set of users known as neighbors, who have already agreed with the active user (ie they tend to listen to a similar set of items). Once this set of users is formed, these systems use different algorithms to combine the preferences of neighbors to produce a prediction or top-N recommendation for the active user. 

One of the techniques used, and that we also used for the project is collaborative filtering (CF), which is one of the most popular techniques used in practice.

# Methods


In this section, we will discuss the statistical methods and algorithms that we used in the project. At first, we describe the data that has served us as a model for the recommendation engine, the type of data storage, the programming language we used and libraries that we have chosen followed by the data mining techniques that we used.


## Million Song Dataset 

### Data: Collection, Encoding and description 
The Million Song Dataset [3] is an audio collection of over one million pieces of popular music available freely. We also used data collection "Taste Profile Subset" also provides the Million Song Dataset site. 

The taste subset is composed of more than 48 million triplets (user, song, listening frequency) recovered from the listening user histories. Data were provided from several applications, where each user can listen to the music he wanted. Data from 1.2 million users listening to 380,000 songs.

[1]: http://en.wikipedia.org/wiki/List_of_online_music_databases  "List of online music databases"
[2]: http://en.wikipedia.org/wiki/International_Society_for_Music_Information_Retrieval "ISMIR - The International Society for Music Information retreival"
[3]: http://cosmal.ucsd.edu/~gert/papers/msdc.pdf "The Million Song Dataset Challenge - B. McFee, T. Bertin-Mahieux, D. Ellis and G. Lanckriet, AdMIRe"


