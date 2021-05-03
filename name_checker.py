def name_scanner(names, friends):
    bad_friends = []
    for i in range(len(friends)):
        for j in range(len(friends[i])):
            if friends[i][j] not in names:
                bad_friends.append([names[i], j + 1])
    return bad_friends
