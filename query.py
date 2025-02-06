# CS 3050 Warmup Project
# Query Program
# Prompt user to provide query and return data
import string
import pyparsing as pp
import query_engine
import database_config
import authentication

MAX_QUERY_LENGTH = 7


# Prompt the user for input and call the query function until program manually terminated
def parser():

    db = authentication.init_db()
    print("Connecting to database")

    # Boolean to continue prompting user
    done = False

    # Print welcome message
    print("Welcome ...")

    while not done:
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
            template = (pp.QuotedString('"') | pp.Word(pp.alphas))[0, MAX_QUERY_LENGTH]
            parsed = template.parseString(userInput)

            # Error handling
            valid = True

            if len(parsed) == 0:
                pass

            elif parsed[0].lower() == "get":
                type = ""
                col = []
                conditions = []
                if parsed[1].lower() in database_config.database_columns:
                    type = "getcol"
                    if parsed[2] == "of":
                        col = ["Name", parsed[1].lower().capitalize()]
                        conditions = getConditions(parsed[3:])

                elif parsed[1].lower() == "games":
                    pass
                else:
                    pass
                # Call query function
                result = query_engine.query(db, type, col, conditions)
                query_engine.print_query_result(result)


def getConditions(parsed):

    returnList = []
    try:
        for i in range(len(parsed)/4):
            if i == 0:
                if parsed[0].lower() != "where":
                    raise AssertionError
            else:
                if parsed[4 * i].lower() != "and":
                    raise AssertionError
                if parsed[4 * i + 1].lower() not in database_config.database_columns:
                    raise AssertionError
                if parsed[4 * i + 2].lower() not in database_config.database_comparators:
                    raise AssertionError
                tempTuple = (parsed[4 * i + 1], parsed[4 * i + 2], parsed[4 * i + 3])
                returnList.append(tempTuple)
        return returnList

    except IndexError or AssertionError:
        print("Invalid Input")
        return AssertionError("Invalid Input")




parser()
