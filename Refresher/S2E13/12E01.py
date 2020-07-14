friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne", "John"}

# This will test the equal items and remove them
local_friends = friends.difference(abroad)
print(local_friends)
friends_together = friends.union(abroad)
print(friends_together)
both = friends.intersection(abroad)
print(both)