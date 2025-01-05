# Description:
# Write a function to convert a name into initials. This kata strictly takes two words with one space in 
# between them.

# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F

# ==============

def abbrev_name(name):
    abbs = []
    name_list = name.split()
    for abb in name_list:
        abbs.append(abb[0].upper())
    return ".".join(abbs)