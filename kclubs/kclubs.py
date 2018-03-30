from clubs import akc
from clubs import ankc
from clubs import ckc
from clubs import kc
from clubs import ukc
import multiprocessing as mp
import os


def fetch_all_data(data_dir):
    processes = [
        mp.Process(target=akc.fetch_data, args=(data_dir,)),
        mp.Process(target=ankc.fetch_data, args=(data_dir,)),
        mp.Process(target=ckc.fetch_data, args=(data_dir,)),
        mp.Process(target=kc.fetch_data, args=(data_dir,)),
        mp.Process(target=ukc.fetch_data, args=(data_dir,))
    ]
    for p in processes:
        p.start()


if __name__ == '__main__':
    data_dir = os.path.join(
        os.path.split(os.path.dirname(os.path.realpath(__file__)))[0], 'data')
    fetch_all_data(data_dir)
