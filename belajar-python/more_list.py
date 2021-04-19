test_list = [{"id" : 1, "data" : "HappY"}, 
             {"id" : 2, "data" : "BirthDaY"}, 
             {"id" : 3, "data" : "Rash"}] 

res = [i for i in test_list if not (i["id"] == 2)]

print(test_list)

print(res)