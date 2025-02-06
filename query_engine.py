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
        for col in cols:
            ret_game[col] = games[0][col]
        return [ret_game]

def print_query_result(result: list[dict[string,any]]):
    header = ""
    if 'Name' in result[0].keys():
        header += "Name".center(46) + "|"
    if 'Year' in result[0].keys():
        header += "Year".center(8) + "|"
    if 'Platform' in result[0].keys():
        header += "Platform".center(12) + "|"
    if 'Global_Sales' in result[0].keys():
        header += "Global_Sales (millions)".center(27)
    print(header.format("","","",""))
    for row in result:
        row_output = ""
        keys = row.keys()
        if 'Name' in keys:
            row_output += row['Name'].ljust(46) + "|"
        if 'Year' in keys:
            row_output += str(row['Year']).center(8) + "|"
        if 'Platform' in keys:
            row_output += row['Platform'].center(12) + "|"
        if 'Global_Sales' in keys:
            row_output += str(row['Global_Sales']).center(27)
        print(row_output)

db = authentication.init_db()
print_query_result(query(db, "getgames", ["Name", "Year", "Platform"], []))