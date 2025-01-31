# CS 3050 Warmup Project
# Query Program
# Prompt user to provide query and return data
import string
import pyparsing as pp
import query_engine.py

# Prompt the user for input and call the query function until program manually terminated
def parser():
    # Boolean to continue prompting user
    done = False

    # Print welcome message
    print("Welcome ...")

    while done == False:
        # Store user input
        userInput = str(input("Enter query: "))

        # Process Input
        if userInput == "help":
            # Print help menu
            print("--- Help Menu ---\n"
                  "Enter queries in the form:\n"
                  "\'Get {value} of {game title}\' to find the sales, release year or platform \n"
                  "of a specific game.\n\n"
                  "OR\n\'Get games where {condition}...\' to filter results\n"
                  "Condition Syntax:\n"
                  "\'where platform is {platform name}\'\n"
                  "\'where sales is greater/less than {sale amount}\'\n"
                  "\'released before/after {year}\'\n"
                  "NOTE:\n - For game or platform names with multiple words, use"
                  " double quotes.\n - Multiple conditions may be added separated"
                  "by \'and\'.\n")

        elif userInput == "quit":
            done = True
        else:
            # Parsing logic
            template = (pp.QuotedString('"') | pp.Word(pp.alphas))[0, 7]
            parsed = template.parseString(userInput)

            # Error handling

            # Call query function


parser()

