import argparse

from collection_persistence import load_collection, store_collection
from util import make_matrix
from vbs import find_n_vbs_results


class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Make n-VBS")
        parser.add_argument(metavar="COLLECTION_IN", dest="results_collection_in", type=str)
        parser.add_argument(metavar="COLLECTION_OUT", dest="results_collection_out", type=str)
        parser.add_argument(metavar="P", dest="p", type=int)
        self.args = parser.parse_args()

    def run(self):
        df = load_collection(self.args.results_collection_in)
        vbs_results = find_n_vbs_results(df, self.args.p)
        vbs_matrix = make_matrix(vbs_results)
        store_collection(self.args.results_collection_out, vbs_matrix)


if __name__ == '__main__':
    Main().run()
