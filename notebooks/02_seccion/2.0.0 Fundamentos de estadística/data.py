import pandas as pd

data_list = [("a","e","h","A"),
             ("a","e","i","C"),
             ("a","e","j","B"),
             ("a","f","h","A"),
             ("a","f","i","A"),
             ("a","g","h","A"),
             ("a","g","h","B"),
             ("b","e","i","B"),
             ("b","f","i","B"),
             ("b","f","j","B"),
             ("b","g","j","C"),
             ("c","e","i","C"),
             ("c","f","j","C"),
             ("c","g","h","B"),
             ("c","g","i","B"),
             ("c","g","j","C"),
             ("d","f","j","A"),
             ("d","g","j","A")
            ]
list_name = ["x1","x2","x3","y"]
data = pd.DataFrame(data_list, columns=list_name)
