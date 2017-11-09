from collections import OrderedDict
import sys

def merge(*objs, **kw):
    result = objs[0]
    for obj in objs[1:]:
        result = merge_obj(result, obj, kw.get('position'))
    return result

def move_to_start(result, key):
    result_copy = result.copy()
    result.clear()
    result[key] = result_copy.pop(key)
    result.update(result_copy)

def merge_obj(result, obj, position=None):
    if not isinstance(result, dict):
        result = OrderedDict() if position else {}

    if not isinstance(obj, dict):
        return obj

    if position:
        if position not in ('first', 'last'):
            raise ValueError("position can either be first or last")
        if not isinstance(result, OrderedDict) or not isinstance(obj, OrderedDict):
            raise ValueError("If using position all dicts need to be OrderedDicts")

    for key, value in obj.items():
        if isinstance(value, dict):
            target = result.get(key)
            if isinstance(target, dict):
                merge_obj(target, value, position)
                continue
            result[key] = OrderedDict() if position else {}
            if position and position == 'first':
                if sys.version_info >= (3, 2):
                    result.move_to_end(key, False)
                else:
                    move_to_start(result, key)
            merge_obj(result[key], value, position)
            continue
        if value is None:
            result.pop(key, None)
            continue
        if key not in result and position == 'first':
            result[key] = value
            if sys.version_info >= (3, 2):
                result.move_to_end(key, False)
            else:
                move_to_start(result, key)
        else:
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

