#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 12:50:52 2017

@author: kevinryan
"""
import media, fresh_tomatoes


toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print toy_story.storyline

avatar = media.Movie("Avatar", "A marine on an alien planet", 
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", 
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

#print avatar.storyline

#avatar.show_trailer()


castaway = media.Movie("Cast Away", 
                      "The story of one man's love for his volley ball",
                      "https://upload.wikimedia.org/wikipedia/en/a/a7/Cast_away_film_poster.jpg",
                      "https://www.youtube.com/embed/PJvosb4UCLs?start=10&end=30&autoplay=1&version=3")

#castaway.show_trailer()

school_of_rock = media.Movie("School of Rock", "Using rock music to learn", "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris", "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors", "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", "https://www.youtube.com/watch?v=BYRWfS2s2v4")


movies = [toy_story, avatar, castaway, school_of_rock, ratatouille, midnight_in_paris]

fresh_tomatoes.open_movies_page(movies)