from generate import generate_art

for x in range(1,11):
    image = generate_art()
    filelocation = "results/" + str(x) + ".jpg"
    image.save(filelocation)