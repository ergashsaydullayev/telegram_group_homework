from read_data import read_data as read

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    f=[]
    for i in data["messages"]:
        if "actor_id" in i and i["actor_id"] not in f and "channel" not in i["actor_id"]:
            f.append(i["actor_id"])
        elif "from_id" in i and i["from_id"] not in f and "channel" not in i["from_id"]:
            f.append(i["from_id"])
    return f
b=read("data/result.json")
print(find_all_users_id(b))