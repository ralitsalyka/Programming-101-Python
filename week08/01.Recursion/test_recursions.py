from recursions import *
import unittest


data1 = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': 'val3'
}

data2 = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': {
        'inner_key1': 'val1',
        'inner_key2': 'val2'
    },
    'key4': 'val4'
}

data3 = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': {
        'inner_key1': 'val1_inner',
        'inner_key2': 'val2_inner',
        'inner_key3': {
            'more_inner_key1': 'val1_more_inner',
            'more_inner_key2': 'val2_more_inner'
        }
    }
}

data4 = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': {
        'inner_key1': 'val1_inner',
        'more_inner_key2': 'val2_inner',
        'inner_key3': {
            'more_inner_key1': 'val1_more_inner',
            'more_inner_key2': 'val2_more_inner'
        }
    }
}

data5 = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': {
        'inner_key1': 'val1',
        'key2': 'val2'
    },
    'key4': 'val4'
}
data6 = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': 'val3'
}


class TestRecursiveFucntion_deep_find_dfs(unittest.TestCase):
    def test_deep_find_dfs_function_if_it_is_normal_dict(self):
        result = deep_find_dfs('key2', data1)
        self.assertEqual(result, 'val2')

    def test_deep_find_dfs_function_if_it_is_more_than_one_dictionary(self):
        result = deep_find_dfs('inner_key2', data2)
        self.assertEqual(result, 'val2')

    def test_deep_find_dfs_function_if_it_is_more_than_one_dictionary_data3(self):
        result = deep_find_dfs('more_inner_key2', data3)
        self.assertEqual(result, 'val2_more_inner')


class TestRecursiveFucntion_deep_find_bfs(unittest.TestCase):
    def test_deep_find_bfs_function_if_it_is_normal_dict(self):
        result = deep_find_bfs('key2', data1)
        self.assertEqual(result, 'val2')

    def test_deep_find_bfs_function_if_it_is_more_than_one_dictionary(self):
        result = deep_find_bfs('inner_key2', data2)
        self.assertEqual(result, 'val2')

    def test_deep_find_bfs_function_if_it_is_more_than_one_dictionary_data3(self):
        result = deep_find_bfs('more_inner_key2', data3)
        self.assertEqual(result, 'val2_more_inner')


class Test_Recursive_Fucntion_deep_find_all_dfs(unittest.TestCase):
    def test_deep_find_all_dfs_function_if_it_is_normal_dict(self):
        result = deep_find_all_dfs('key2', data1)
        self.assertEqual(result, ['val2'])

    def test_deep_find_all_dfs_function_if_it_is_more_than_one_dictionary_data3(self):
        result = deep_find_all_dfs('more_inner_key2', data4)
        self.assertEqual(result, ['val2_inner', 'val2_more_inner'])



class Test_Recursive_Fucntion_deep_all_find_bfs(unittest.TestCase):
    def test_deep_find_all_bfs_function_if_it_is_normal_dict(self):
        result = deep_find_all_bfs('key2', data1)
        self.assertEqual(result, ['val2'])

    def test_deep_find_all_bfs_function_if_it_is_more_than_one_dictionary_data3(self):
        result = deep_find_all_bfs('more_inner_key2', data4)
        self.assertEqual(result, ['val2_inner', 'val2_more_inner'])


class TestRecursiveFucntion_deep_update(unittest.TestCase):
    def test_deep_update_fucntion_for_one_dict(self):
        result = deep_update('key2', data6, 'fff')
        self.assertEqual(result, {'key1': 'val1', 'key2': 'fff', 'key3': 'val3'})

    def test_deep_update_fucntion_for_more_than_one_dict(self):
        result = deep_update('key2', data5, 'fff')
        self.assertEqual(result, {'key1': 'val1', 'key2': 'fff', 'key3': {'inner_key1': 'val1', 'key2': 'fff'}, 'key4': 'val4'})


if __name__ == '__main__':
    unittest.main()
