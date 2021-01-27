def remove_duplicates(input_list):
    """Removes duplicated elements from a list"""
    
    temp_list = [] 
    [temp_list.append(element) for element in input_list if element not in temp_list]
    
    return temp_list