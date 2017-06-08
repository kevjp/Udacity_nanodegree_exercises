#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 12:50:52 2017

@author: kevinryan

Generate Movie instances for each movie to be posted to the Movie trailer
website
"""
import media
import fresh_tomatoes

# toy_story instance
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

# print toy_story.storyline

# avatar instance
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

# castaway instance
castaway = media.Movie("Cast Away",
                       "The story of one man's love for his volley ball",
                       "https://upload.wikimedia.org/wikipedia/en/a/a7/Cast_away_film_poster.jpg",  # NOQA
                       "https://www.youtube.com/embed/PJvosb4UCLs?start=10&end=30&autoplay=1&version=3"   # NOQA
                       )

# castaway.show_trailer()

# school_of_rock instance
school_of_rock = media.Movie("School of Rock",
                            "Using rock music to learn",
                            "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

# ratatouille instance
ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk"  # NOQA
                          )

# midnight_in_paris instance
midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4"  # NOQA
                                )


# Group all the above instances in a list
movies = [toy_story, avatar, castaway, school_of_rock,
          ratatouille, midnight_in_paris]

# Run open_movies_page function from fresh_tomatoes module providing
# movies list
fresh_tomatoes.open_movies_page(movies)

# Test print statements below ....
# print media.Movie.VALID_RATINGS
# print media.Movie.__doc__
# print media.Movie.__name__
# print media.Movie.__module__
