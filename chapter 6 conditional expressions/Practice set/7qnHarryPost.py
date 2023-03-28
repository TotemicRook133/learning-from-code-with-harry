#Wapp to find out whether a given post is talking about "Harry"or not

post="harry hello everyone, today we are going to talk about HaRRY "
if("harry" in post.capitalize() or "Harry" in post.capitalize()):
    print("yes the given post is talking about harry and it is: \n")
    print('"'+post+'"')
else:
    print("no the given post is not talking about harry and it is: \n")
    print(post.capitalize())
