"""
Assignment 5: Dictionaries

1.  Create a dictionary to store information about a book. Include keys for "title", "author", and "year_published".
2.  Print the dictionary.
3.  Update the "year_published" to a new value and print the dictionary again.
4.  Add a new key-value pair for "genre" and print the final dictionary.
"""

print("\n== Assignment 5: Dictionaries == ") 

book1= {"Title": "The Hare Who Wouldn't Share",  "Author" :"Steve Small" , "year_published": "2024"} # Creating a Dictionary

print("1. Dictionary Creation")

print(f" Book 1: {book1}")    # Print the dictionary

book1["year_published"] = "2025"  # Modifying exsiting
print(f" Book 1: {book1}")

print("\n== Modifying Dictionary")
book1["Genre"]= "Kids Book for Adults"  # Add a new Key-value "Genre"
print(f"Final Dictionary: {book1}")




