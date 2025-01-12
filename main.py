def longest_career(albums):

    artist_span = {}

    for artist, _, year in albums:
        if artist not in artist_span:
            artist_span[artist] = [year, year]

        else:
            min_year = artist_span[artist][0]
            max_year = artist_span[artist][1]

            if year < min_year:
                artist_span[artist][0] = year

            if year > max_year:
                artist_span[artist][1] = year

    max_duration = None
    best_artist = None

    for artist, duration in artist_span.items():
        current_duration = duration[1] - duration[0]

        if max_duration is None or current_duration > max_duration:

            max_duration = current_duration
            best_artist = artist

    print(best_artist, max_duration)
    return (best_artist, max_duration)



longest_career([
    ("Rodrigo y Gabriela", "9 Dead Alive", 2014),
    ("Shakira", "El Dorado", 2017),
    ("Janelle Monáe", "The ArchAndroid", 2010),
    ("Shakira", "Magia", 1991),
    ("Shakira", "She Wolf", 2009),
    ("Rodrigo y Gabriela", "11:11", 2009),
    ("Rodrigo y Gabriela", "Rodrigo y Gabriela", 2006),
    ("Rodrigo y Gabriela", "Mettavolution", 2019),
    ("Janelle Monáe", "Dirty Computer", 2018)
])



# Test cases
albums_1 = [
    ("Rodrigo y Gabriela", "9 Dead Alive", 2014),
    ("Shakira", "El Dorado", 2017),
    ("Janelle Monáe", "The ArchAndroid", 2010),
    ("Shakira", "Magia", 1991),
    ("Shakira", "She Wolf", 2009),
    ("Rodrigo y Gabriela", "11:11", 2009),
    ("Rodrigo y Gabriela", "Rodrigo y Gabriela", 2006),
    ("Rodrigo y Gabriela", "Mettavolution", 2019),
    ("Janelle Monáe", "Dirty Computer", 2018)
]
assert longest_career(albums_1) == ("Shakira", 26)


albums_2 = [
    ("Skylar Kergil", "Tell Me a Story", 2015),
    ("Lil Nas X", "Old Town Road", 2018),
    ("Skylar Kergil", "Thank You", 2013),
    ("Lil Nas X", "Montero", 2021),
]
assert longest_career(albums_2) == ("Lil Nas X", 3)

print("All test cases passed!")
print("Finished early? Discuss time & space complexity")
