
def merge(*objs):
    result = objs[0]
    for obj in objs[1:]:
        result = merge_obj(result, obj)
    return result

def merge_obj(result, obj):
    if not isinstance(result, dict):
        result = {}

    if not isinstance(obj, dict):
        return obj

    for key, value in obj.items():
        if isinstance(value, dict):
            target = result.get(key)
            if isinstance(target, dict):
                merge_obj(target, value)
                continue
            result[key] = {}
            merge_obj(result[key], value)
            continue
            
        if value is None:
            result.pop(key, None)
            continue
        result[key] = value
    return result

def create_patch(source, target):
    return create_patch_obj(source, target)

def create_patch_obj(source, target):
    if not isinstance(target, dict) or not isinstance(source, dict):
        return target

    result = {}

    for key in set(source.keys()) - set(target.keys()):
        result[key] = None

    for key, value in target.items():
        if key not in source:
            result[key] = value
            continue
        if value == source[key]:
            continue
        result[key] = create_patch_obj(source[key], value)
    return result

