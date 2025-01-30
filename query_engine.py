import string


# Takes a type, the cols requested, and conditions and returns a list of objects from the database
# two types: getgames and getcol
def query(db, type: string, cols: list[string], conditions: list[tuple[string, string, string]]):
    # get a reference to the video_games collection
    vgs = db.collection('video_games')
    games = []
    for i in range(len(conditions)):
        # for each condition specified add a where clause to our query
        vgs = vgs.where(conditions[i][0], conditions[i][1], conditions[i][2])
        docs = vgs.list_documents()
        for doc in docs:
            games.append(doc.to_dict())
    #getgames
    if type == "getgames":
        # if we're getting games, return all games
        return games
    elif type == "getcol":
        pass