#Create a list called destination using the data stored in travel_plans.txt.
# Each element of the list should contain a line from the file that lists a country and cities inside that country.
# Hint: each line that has this information also has a colon : in it.
file = open ('travel_plans.txt','r')
destination = []

lines = file.readlines()
for line in lines :
    printed = lines
    words = line.split(':')
    check = words [0]
    letters = check.split()
    length = len(letters)
    if length == 1:
        destination.append(line)
print(destination[:])


#Create a list called j_emotions that contains every word in emotion_words.txt that begins with the letter “j”.
file = open ('emotion_words.txt','r')
lines = file.readlines()
j_emotions = []
for line in lines :
    words = line.split()
    for word in words :
        letters = word.split()
        for letter in letters :
            if letter[0] == 'j':
                j_emotions.append(word)
            else :
                continue
   