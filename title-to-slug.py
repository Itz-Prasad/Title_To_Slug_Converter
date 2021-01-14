
# Title to slug converter - Program

Title = str(input("Enter Title : "))  #Takes title as input

Splitted_Title = Title.split(" ")  # Splits words apart which have spaces within

# print(Splitted_Title)  # Prints list of the Splitted_Title

Lower_Case_Title = [items.lower() for items in Splitted_Title]  # Gives list of words in lower case

# print(Lower_Case_Title) # Prints list of words in title all with lower case

Slug = ("-").join(Lower_Case_Title)  # Joins words in list with "-" to make a slug

print(Slug)  # Prints slug as a final result
