lettres_trouvées = ['.']
mot = 'lol'
guess = input('entrez une lettre: ')
guess = guess.lower()

for letter in mot:
    if guess == letter:
        print('haha')
        lettres_trouvées.append(guess)
    else:
        print('raté')
devine = []

for a in lettres_trouvées:
    for b in lettres_trouvées:
        if a == b:
            del b


for letter in mot and (moi in lettres_trouvées):
    if letter == moi:
        devine.append(lettre)
    else:
        devine.append('*')