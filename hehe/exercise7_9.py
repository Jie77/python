# .sort() in place
# .sort() - orders a list in place
quiz_scores = [20, 19, 20, 15, 20, 20, 20, 18, 18, 18, 19]
print("before sort(): ",quiz_scores)
quiz_scores.sort()
print("after sort(): ", quiz_scores)

# sorted() copy
# sorted() - creates an ordered list copy
game_points = [3, 14, 0, 8, 21, 1, 3, 8]
print("before sorted(): ", game_points)
sorted_points = sorted(game_points)
print("after sorted(): ", game_points)

print(sorted_points)
