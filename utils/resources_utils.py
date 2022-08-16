def resources_list(**kwargs):
    res_dict = {}
    for res in kwargs:
        res_dict[res] = kwargs[res]

    return res_dict

