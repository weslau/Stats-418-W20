file = r'C:\Users\lauw02\Desktop\stats 418\cifar-10-python.tar\cifar-10-python\cifar-10-batches-py\data_batch_1'

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

print(unpickle(file))
