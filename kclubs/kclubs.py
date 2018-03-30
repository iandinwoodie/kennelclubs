from clubs import akc
from clubs import ankc
from clubs import ckc
from clubs import kc
from clubs import ukc
import os


def fetch_all_data(data_dir):
    akc.fetch_data(data_dir)
    ankc.fetch_data(data_dir)
    ckc.fetch_data(data_dir)
    kc.fetch_data(data_dir)
    ukc.fetch_data(data_dir)


if __name__ == '__main__':
    data_dir = os.path.join(
        os.path.split(os.path.dirname(os.path.realpath(__file__)))[0], 'data')
    fetch_all_data(data_dir)
