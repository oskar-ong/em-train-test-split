import argparse


if __name__ == "main":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', '-d', help="dataset file", required=True)

    args = parser.parse_args()
    dataset = args.data

    if(dataset == "musicbrainz"):
        pass