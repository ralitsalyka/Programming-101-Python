def deep_find_dfs(key, data):
    if key in data:
        return data.get(key)
    for k in data:
        temp = data.get(k)
        if type(temp) is dict:
            return deep_find_dfs(key, temp)


def deep_find_bfs(key, data):
    visited = []
    for x in data:
        if type(data.get(x)) is dict:
            visited.append(data.get(x))
        elif x == key:
            return data.get(x)
    result = deep_find_bfs(key, visited[0])
    if result is not None:
        return result


def deep_find_all_dfs(key, data):
    found_values = []
    for k in data:
        if k == key:
            found_values.append(data[k])
        if type(data[k]) is dict:
            result = deep_find_all_dfs(key, data[k])
            for res in result:
                found_values.append(res)
    return found_values


def deep_find_all_bfs(key, data):
    visited = []
    found_values = []
    for k in data:
        if k == key:
            found_values.append(data[k])
        if type(data[k]) is dict:
            visited.append(data[k])
    for el in visited:
        result = deep_find_all_bfs(key, el)
        for res in result:
                found_values.append(res)
    return found_values


def deep_update(key, data, val):
    for k, v in data.items():
        if k == key:
            data[k] = val
        elif type(v) is dict:
            deep_update(key, v, val)
    return data
