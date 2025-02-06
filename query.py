# CS 3050 Warmup Project
# Query Program
# Prompt user to provide query and return data
import string
import pyparsing as pp
import query_engine
import database_config
import authentication
import warnings

MAX_QUERY_LENGTH = 100 #high number because we need a maximum word count


# Prompt the user for input and call the query function until program manually terminated
def parser():
    # suppress warnings
    warnings.filterwarnings("ignore", category=UserWarning)

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
                  "\'Get {column} of {game title}\' to find the sales, release year or platform \n"
                  "of a specific game.\n The platforms and Names of games are CASE-SENSITIVE.\n\n"
                  "OR\n\'Get games where {condition}...\' to filter results\n"
                  "Condition Syntax:\n"
                  "\'where platform is {platform name}\'\n"
                  "\'where sales is greater/less than {sale amount}\'\n"
                  "\'released before/after {year}\'\n"
                  "NOTE:\n - For game or platform names with multiple words, use"
                  " double quotes.\n - Multiple conditions may be added and separated"
                  "by \'and\'.\n")
            print("Recognized Columns:")
            print(database_config.database_columns)
            print("\nRecognized Comparators:")
            print(database_config.database_comparators)
            print()

        elif userInput == "quit":
            done = True
        else:
            # Parsing logic
            template = (pp.QuotedString('"') | pp.Word(pp.alphanums+"=<>"))[0, MAX_QUERY_LENGTH]
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
                    if parsed[2].lower() == "of":
                        #queries of this form must have exactly 4 words
                        if len(parsed) > 4:
                            print("Incorrect Syntax. Type 'help' for more information")
                            valid = False
                        col = ["name", parsed[1].lower()]
                        conditions.append(("name", "==", parsed[3]))

                elif parsed[1].lower() == "games":
                    type = "getgames"
                    #get the conditions, starting with "where"
                    conditions = getConditions(parsed[2:])
                    if conditions == "INVALID":
                        print("Incorrect Syntax. Type 'help' for more information")
                        valid = False

                else:
                    print("Incorrect Syntax. Type 'help' for more information")
                    valid = False
                # Call query function
                if valid:
                    result = query_engine.query(db, type, col, conditions)
                    if len(result) == 0:
                        print("No Results Found. Check your spelling and try again.")
                    else:
                        query_engine.print_query_result(result)
            else:
                print("Incorrect Syntax. Type 'help' for more information")


def getConditions(parsed):

    returnList = []
    try:
        #must have a multiple of 4 words
        #phrases are in the form "where"/"and", {column}, {operator}, {value}
        #the last three of each phrase are passed on as conditions
        if len(parsed) % 4 != 0:
            raise AssertionError
        for i in range(len(parsed)//4):
            if i == 0:
                if parsed[0].lower() != "where":
                    raise AssertionError
            elif parsed[4 * i].lower() != "and":
                raise AssertionError

            if parsed[4 * i + 1].lower() not in database_config.database_columns:
                raise AssertionError
            if parsed[4 * i + 2].lower() not in database_config.database_comparators:
                raise AssertionError

            # Handle the case where the value we compare is numeric.
            user_argument = parsed[4 * i + 3]
            if parsed[4 * i + 3].isnumeric():
                user_argument = float(parsed[4 * i + 3])

            tempTuple = (parsed[4 * i + 1], parsed[4 * i + 2], user_argument)
            returnList.append(tempTuple)
        return returnList

    except AssertionError:
        return "INVALID"




parser()
