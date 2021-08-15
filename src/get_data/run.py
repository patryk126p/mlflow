#!/usr/bin/env python
"""
Download dataset
"""
import argparse
import logging
import os

import mlflow
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):
    logger.info(f"Downloading {args.uri}")
    data = requests.get(args.uri).content.decode("utf-8")
    file_path = os.path.join("data", args.file_name)
    with open(file_path, "w") as fh:
        fh.write(data)
    logger.info(f"Uploading {args.file_name} to artifact store")
    mlflow.log_artifact(file_path, args.s3_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download URL to a local destination")
    parser.add_argument("uri", type=str, help="URI of file to download")
    parser.add_argument("file_name", type=str, help="Name of the downloaded file")
    parser.add_argument("s3_path", type=str, help="Destination in artifact store")
    args = parser.parse_args()

    go(args)
