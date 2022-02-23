import argparse
from XmlResultParser import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="List verification time of all methods in the given Dafny xml output")
    parser.add_argument(metavar="XMLFILE", dest="xml_file", type=str)
    args = parser.parse_args()

    xml_parser = XmlResultParser()
    xml_results = xml_parser.parse(open(args.xml_file))
    finished_methods = [{"name": r["name"], "duration": r["duration"]} for r in xml_results["methods"] if r["finished"]]
    unfinished_methods = [{"name": r["name"]} for r in xml_results["methods"] if not r["finished"]]

    finished_methods = sorted(finished_methods, key=lambda m: m["duration"], reverse=True)

    max_name_length = max([len(r["name"]) for r in finished_methods + unfinished_methods])
    print("\n".join(["{} {}".format(r["name"].ljust(max_name_length), r["duration"]) for r in finished_methods]))
    print("\n".join(["{} not finished".format(r["name"].ljust(max_name_length)) for r in unfinished_methods]))
