import argparse
import sys
from pathlib import Path

import mlflow
import yaml

MAP = {
    "download": "get_data",
    "clean": "clean_data",
    "split": "split_data",
    "train": "train_model",
}


def go(args, config):
    if args.step == "test":
        sys.exit(0)
    else:
        directory = "data" if args.step != "train" else "model"

    abs_path = Path(__file__).parent
    dest_path = str(Path(abs_path, "src", MAP[args.step], directory))
    client = mlflow.tracking.MlflowClient(config["main"]["tracking_uri"])
    s3_path = config[args.step]["s3_path"]
    client.download_artifacts(args.run_id, s3_path, dest_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic artifact fetcher")
    parser.add_argument(
        "run_id", type=str, help="ID of a run from which to get artifact"
    )
    parser.add_argument("step", type=str, help="Name of the step")
    args = parser.parse_args()

    with open("config.yaml", "r") as fh:
        conf = yaml.safe_load(fh)

    go(args, conf)
