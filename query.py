# CS 3050 Warmup Project
# Query Program
# Prompt user to provide query and return data
import string

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
            pass
        elif userInput == "quit":
            done = True
        else:
            # Parsing logic

            # Call query function



# Takes a type, the cols requested, and conditions and returns a list of objects from the database
# two types: getgames and getcol

def query(db, type: string, cols: list[string], conditions: list[tuple[string, string, string]]):
    #getgames
    if type == "getgames":
        # get a reference to the video_games collection
        vgs = db.collection('video_games')
        for i in range(len(conditions)):
            # for each condition specified
            vgs = vgs.where(conditions[i][0], conditions[i][1], conditions[i][2])
        docs = vgs.list_documents()
        games = []
        for doc in docs:
            games.append(doc.to_dict())
        return games
    elif type == "getcol":
        pass

parser()

