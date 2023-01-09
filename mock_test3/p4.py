def f(d):
    went_in = []
    came_out = []
    currently_in = []
    for set in d:
        if set[1] == 'in':
            went_in.append(set[0])
        else:
            came_out.append(set[0])

    for a in range(len(went_in)):
        if went_in[a] not in came_out:
            currently_in.append(went_in[a])
        else:
            came_out.remove(went_in[a])


    return currently_in


cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],["BA111","in"],["BA123","out"],["KR234","in"]]


print(f(cars))