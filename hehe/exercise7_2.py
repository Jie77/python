# print ft_bones list
# delete "cuboid" from ft_bones
# delete "navicular" from list
# reprint list
# check for deletion of "cuboid" and "navicular"
ft_bones = ["calcaneus", "talus", "cuboid", "navicular",
            "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]

# using pop() to print the first and last items from the ft_bones list
print(ft_bones)

ft_bones.remove('cuboid')
del ft_bones[1]

print(ft_bones)

print(ft_bones.pop())
print(ft_bones[::-1].pop())
print(ft_bones.pop(2))
