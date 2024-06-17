def get_deepest_element(data):
    if isinstance(data, (tuple, list)):
        for item in data:
            result = get_deepest_element(item)
            if result is not None:
                return result
    else:
        return data
    return None
