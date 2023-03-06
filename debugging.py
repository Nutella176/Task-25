def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])  # k replaced by key


# Double quotation marks replaced with single quotation marks and escape \ added. Also exclamation mark added after d'oh
# Another option was to keep double quotation with no need of the escape character as below:
# simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh", "maggie": "(Pacifier Suck)"}
simpson_catch_phrases = {
    "lisa": "BAAAAAART!",
    "bart": "Eat My Shorts!",
    "marge": "Mmm~mmmmm",
    "homer": "d'oh!",
    "maggie": "(Pacifier Suck)",
}

# Square brackets added around the keys
print_values_of(simpson_catch_phrases, ["lisa", "bart", "homer"])

"""
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

"""
