# CS 3050 Warmup Project
# Query Program
# Prompt user to provide query and return data
import string
import pyparsing as pp

# Prompt the user for input and call the query function until program manually terminated
def parser():
    # Boolean to continue prompting user
    done = False

    # Print welcome message
    print("Welcome ...")

    while done == False:
        # Store user input
        userInput = str(input("Enter query: "))
        inputList = userInput.split()

        # Process Input
        if userInput == "help":
            pass
        elif userInput == "quit":
            done = True
        else:
            typeParse = pp.Word(pp.alphas)  + pp.Word(pp.alphas)
            type = typeParse.parse_string(inputList[0] + " " + inputList[1])
            # Parsing logic
            template = (pp.QuotedString('"') | pp.Word(pp.alphas))[0, 7]
            parsed = template.parseString(userInput)

            # Error handling

            # Call query function



parser()

