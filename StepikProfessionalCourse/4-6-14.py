import pickle


def filter_dump(filename, objects, typename):
    with open(filename, 'wb') as bf:
        pickle.dump([i for i in objects if type(i) is typename], bf)


filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)