def convert_units_array(names, heights, weights):
    new_hts = heights * 0.39370
    new_wts = weights * 2.20462
    people_data = {}
    for i,name in enumerate(names):
        people_data[name] = (new_hts[i], new_wts[i])
    return people_data