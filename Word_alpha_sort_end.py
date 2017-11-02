# file locations
# C:\Users\W113400\Documents\Coding\python\random text.txt

# import timeit and string modules for use in the code
import string, timeit

start_time = timeit.default_timer()

with open("C:/Users/W113400/Documents/Coding/python/random text.txt", "r") as f:
    content = f.read()  # read contents of file and store in variable called content
    f.close()  # close the file (now that we have stored content in variable)
    table = str.maketrans(dict.fromkeys(string.punctuation))  # make translation table
    content = content.translate(table).lower()  # reset content variable with text body having had the punctuation removed and case set to lower
    words = content.split()  # split contents into list of individual words


# function to sort text based on last character
def sort_last_letter(strings):
    def last_letter(s):
        return s[-1]

    return sorted(strings, key=last_letter)


# print the words sorted by last letter
print(sort_last_letter(words))
# print the time taken to run
print("\nTime to run: ", timeit.default_timer() - start_time)


# checkout design patterns to see if someone else has created something that can be used