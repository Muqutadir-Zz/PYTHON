# info = {
#     "name" : "muqutadir" ,
#     "age" : "18"    
# }
# print(info)
# print(info["name"])

# null_dict = {}
# null_dict["name"] = "muqutadir" 
# print(null_dict)

# Nested Dict

# student  ={
#     "name" : "muquatdir",
#     "subjects" : {
#         "phy" : 99,
#         "mat" : 95,
#         "chem" : 90
#  }
# }

# student.update({"city" : "delhi"})
                   
# print(student)

# Set in Python

# collection = {1, 3, 3, 3, "yoooo", "yoooo"}
# print(collection)
# print(type(collection))

# collecion = {}
# print(type(collecion))

# collection = set()
# collection.add(1)
# collection.add("muquatdir")
# collection.add("yoooo")
# collection.remove(1)
# # collection.clear()
# print(collection.pop())
# print(collection)
# print(len(collection))

# Set Methods

# set1 = {1, 2, 3, 4}
# set2 = {2, 3, 4}

# print(set1.union(set2))

# Practice

# dictionary = {
#     "cat" : "a small animal",
#     "tabel" : ["a piece of furniture", "list of facts of facts & figures"]
# }
# print(dictionary)

# set1 = {"python", "jave", "C++", "javascript"}
# set2 = {"java", "python", "java", "C++", "C"}

# print(set1.unio(set2))   #  WRONG

# subjects = {
#   "python", "java", "C++", "javascript", "java", "python", "java", "C++", "C"
# }
# print(subjects)

marks = {}

x = int(input("enter phy : "))
marks.update({"phy": x}) # same for mat, chem etccc
print(marks)