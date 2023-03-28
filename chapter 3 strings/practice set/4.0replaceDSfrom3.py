#wapp to replace double spaces with single spaces from 3
story="hello my name is Adit and I am improvising on the CodeWithHarry's modules  hope  you liked it. For  double  spaces  I am adding   double   spaces  randomly"
print(story.count("  "))
DoubleSpace=story.find("  ")
print(DoubleSpace)
story=story.replace("  "," ")
print(story)