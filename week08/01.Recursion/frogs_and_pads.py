def create_state(n):
    left_side = ''
    right_side = ''
    for i in range(0, n):
        left_side = left_side + '>'
        right_side = right_side + '<'
    frogs_and_pads = left_side + '_' + right_side
    return frogs_and_pads


def swap(current_list, index1, index2):
    temp = current_list[index1]
    current_list[index1] = current_list[index2]
    current_list[index2] = temp
    return current_list


finded = []


def check_if_element_exist(elem, finded):
    for x in finded:
        if elem in finded:
            return True
        else:
            return False


def result_path_from_current_state(list_states):
    founded_states = []
    i = 0

    while i < len(list_states):
        if list_states[i] == '_':
            index_of_lilypad = i
            break
        i = i + 1

    if index_of_lilypad - 1 >= 0 and list_states[index_of_lilypad - 1] == '>':
        current_list = [x for x in list_states]
        result = swap(current_list, index_of_lilypad, index_of_lilypad - 1)
        founded_states.append(result)

    if index_of_lilypad - 2 >= 0 and list_states[index_of_lilypad - 2] == '>':
        current_list = [x for x in list_states]
        result = swap(current_list, index_of_lilypad, index_of_lilypad - 2)
        founded_states.append(result)

    if index_of_lilypad + 1 < len(list_states) and list_states[index_of_lilypad + 1] == '<':
        current_list = [x for x in list_states]
        result = swap(current_list, index_of_lilypad, index_of_lilypad + 1)
        founded_states.append(result)

    if index_of_lilypad + 2 < len(list_states) and list_states[index_of_lilypad + 2] == '<':
        current_list = [x for x in list_states]
        result = swap(current_list, index_of_lilypad, index_of_lilypad + 2)
        founded_states.append(result)
    return founded_states


def find_path(new_ones_states, start_state, end_state, flag):
    not_empty = []
    if flag is not True:
        new_ones_states.append(start_state)
        current_list = result_path_from_current_state(start_state)
        for res in current_list:
            if end_state == res:
                flag = True
                new_ones_states.append(end_state)
                return new_ones_states
                break
            if result_path_from_current_state(res) != []:
                not_empty.append(res)
        if not_empty != [] and flag is False:
            for elem in not_empty:
                if flag is True:
                    break
                else:
                    index = find_path(new_ones_states, elem, end_state, flag)
                    if index is not None:
                        return index
    else:
        return new_ones_states


def main():
    print('For Example -- if you choose 1 - >_<,2 - >>_<<')
    number = input('Number of frogs:')
    frogs = create_state(int(number))
    start_state = [frogs[i] for i in range(0, len(frogs))]
    end_state = start_state[::-1]
    path = []
    flag = False
    result = find_path(path, start_state, end_state, flag)
    for res in result:
        print(res)


if __name__ == '__main__':
    main()
