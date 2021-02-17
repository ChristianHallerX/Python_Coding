def convert_units(names, heights, weights):
    new_hts = [ht * 0.39370  for ht in heights]
    new_wts = [wt * 2.20462  for wt in weights]
    people_data = {}
    for i,name in enumerate(names):
        people_data[name] = (new_hts[i], new_wts[i])
    return people_data