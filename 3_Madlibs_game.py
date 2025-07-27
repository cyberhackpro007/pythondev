# Mad libs game
# word game where you create a story
# by filling in the blanks with random words

adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb1 = input("Enter a verb: ")


print(f"Today is a {adjective1} Day.")
print (f"I was at Mall and I saw {noun1}")
print (f"The {noun1} was wearing {adjective2} cap and {verb1} at me")


def play_mad_libs():
    """Plays a simple Mad Libs game."""

    story_template = "Once upon a time, a {adjective} {animal} decided to {verb} through the {place} while carrying a {object}."

    print("Welcome to Mad Libs! Please provide the following words:")

    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb (past tense): ")
    place = input("Enter a place: ")
    object_name = input("Enter an object: ")

    final_story = story_template.format(
        adjective=adjective,
        animal=animal,
        verb=verb,
        place=place,
        object=object_name
    )

    print("\nHere's your Mad Libs story:")
    print(final_story)

if __name__ == "__main__":
    play_mad_libs()
