#a data structure in Python that is a mutable, or changeable, ordered sequence of elements.
friends = ["Nid", "Vid", "Mis", "Pri", "Ani", "Sam", "Viv", "Apr"]
lucky_nos = [1, 3, 5, 7, 9, 0]
friends.extend(lucky_nos)
friends.append("Creed")
friends.insert(0, "Shreya")
friends.remove("Shreya")
friends.pop()
print(friends)
print(friends.count("Nid"))
lucky_nos.sort()
lucky_nos.reverse()
print(lucky_nos)
friends2 = friends.copy()
print(friends2)
