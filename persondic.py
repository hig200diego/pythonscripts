person = [['name', 'Jared'], ['job', 'Musician'], ['city', 'Bern']]

answer = {k:v for k,v in person}
print(answer)


#Outras soluções

# answer = {thing[0]:thing[1] for thing in person}

# answer = dict(person)!!!!!!!!!!!!!!!!!!!!!!!!!!!