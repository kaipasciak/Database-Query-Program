import string
import authentication


# Takes a type, the cols requested, and conditions and returns a list of objects from the database
# two types: getgames and getcol
def query(db, type: string, cols: list[string], conditions: list[tuple[string, string, any]]):
    # get a reference to the video_games collection
    vgs = db.collection('video_games')
    games = []
    for i in range(len(conditions)):
        # for each condition specified add a where clause to our query
        vgs = vgs.where(conditions[i][0], conditions[i][1], conditions[i][2])

    docs = vgs.stream()
    for doc in docs:
        games.append(doc.to_dict())
    #getgames
    if type == "getgames":
        # if we're getting games, return all games
        return games
    elif type == "getcol":
        ret_game = {}
        if games:
            for col in cols:
                ret_game[col] = games[0][col]
            return [ret_game]
        else:
            return []

def print_query_result(result: list[dict[string,any]]):
    header = ""
    if 'name' in result[0].keys():
        header += "Name".center(46) + "|"
    if 'year' in result[0].keys():
        header += "Year".center(8) + "|"
    if 'platform' in result[0].keys():
        header += "Platform".center(12) + "|"
    if 'sales' in result[0].keys():
        header += "Global_Sales (millions)".center(27)
    print(header.format("","","",""))
    for row in result:
        row_output = ""
        keys = row.keys()
        if 'name' in keys:
            row_output += row['name'].ljust(46) + "|"
        if 'year' in keys:
            row_output += str(row['year']).center(8) + "|"
        if 'platform' in keys:
            row_output += row['platform'].center(12) + "|"
        if 'sales' in keys:
            row_output += str(row['sales']).center(27)
        print(row_output)
        print()
