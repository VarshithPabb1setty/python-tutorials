lucky_numbers = [17, 34, 81, 7, 56, 6]
friends = ["Ruthvik", "Saikiran", "Pruthvi", "Varshith", "Harsha", "Sohan"]

# friends.extend(lucky_numbers)
friends.append("Shankar")
friends.insert(1, "Varshith")
friends.remove("Shankar")
friends.pop()
print(friends.index("Pruthvi"))
print(friends.count("Varshith"))
friends.sort()
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(friends)
friends2 = friends.copy()
print(lucky_numbers)
