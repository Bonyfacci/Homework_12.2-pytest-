def get_val(collection, key, default='git'):
    if key in collection.keys():
        return collection[key]
    else:
        return default
