"""
Explicar el uso de:
    - Enumerate
    - Zip
    - Map
    - Filter
"""

def using_enumerate():
    """
    Enumerate
    It allows us to loop over something and have an automatic counter.
    """
    my_string = "Hello World, me llamo Pepe!"

    # Using Enumerate:
    for index, letter in enumerate(my_string):
        if index >= len(my_string)-5:
            print(f"Index: {index}, Letter: {letter}")

    # Using my own counter:
    index = 0
    for letter in my_string:
        print(f"Index: {index}, Letter: {letter}")
        index += 1

def using_zip():
    """
    Zip
    The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
    """
    # Simple zip() example with two lists
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]

    # Zipping the two lists together
    zipped = zip(names, ages)

    # Converting to list to display results
    zipped_list = list(zipped)
    print(zipped_list)

    # Transforming the zipped object to a dict
    print(dict(zipped_list))

def using_map():
    """
    Map
    The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
    """
    # Add text "I am a " to each element in the list
    words = ["cog", "dog", "elephant", "groundhog", "butterfly", "ox"]

    # Function to add text to each element
    def add_i_am(text: str) -> str:
        if (text[0].lower()) in ["a", "e", "i", "o", "u"]:
            return "I am an " + text
        return "I am a " + text

    # Using filter to get even numbers
    transformed_words = list(map(add_i_am, words))
    print("Words with 'I am' added:", transformed_words)

def using_filter():
    """
    Filter
    The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
    """
    # Filter even numbers from a list
    words = ["cog", "dog", "elephant", "groundhog", "butterfly", "ox"]

    # Function to check if number is even
    def contains_og(text: str) -> bool:
        return bool(text.find("og") != -1)

    # Using filter to get even numbers
    words_containing_og = list(filter(contains_og, words))
    print("Words that contain 'og':", words_containing_og)

if __name__ == "__main__":
    # using_enumerate()
    # using_zip()
    using_map()
    # using_filter()
