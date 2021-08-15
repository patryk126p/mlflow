import os

import mlflow
import yaml

_steps = [
    "download",
    "clean",
    "split",
    "train",
]


def go(config: dict):
    mlflow.set_tracking_uri(config["main"]["tracking_uri"])
    mlflow.set_experiment(config["main"]["experiment_name"])

    # Steps to execute
    steps_par = config["main"]["steps"]
    active_steps = steps_par.split(",") if steps_par != "all" else _steps

    if "download" in active_steps:
        _ = mlflow.run(
            os.path.join("src", "get_data"),
            "main",
            parameters={
                "uri": config["download"]["uri"],
                "file_name": config["download"]["file_name"],
                "s3_path": config["download"]["s3_path"],
            },
        )

    if "clean" in active_steps:
        _ = mlflow.run(
            os.path.join("src", "clean_data"),
            "main",
            parameters={
                "raw_data": config["clean"]["raw_data"],
                "file_name": config["clean"]["file_name"],
                "col_names": config["clean"]["col_names"],
                "s3_path": config["clean"]["s3_path"],
            },
        )

    if "split" in active_steps:
        _ = mlflow.run(
            os.path.join("src", "split_data"),
            "main",
            parameters={
                "clean_data": config["split"]["clean_data"],
                "test_size": config["split"]["test_size"],
                "random_seed": config["split"]["random_seed"],
                "file_names": config["split"]["file_names"],
                "s3_path": config["split"]["s3_path"],
            },
        )

    if "train" in active_steps:
        _ = mlflow.run(
            os.path.join("src", "train_model"),
            "main",
            parameters={
                "train_data": config["train"]["train_data"],
                "target": config["train"]["target"],
                "model_config": config["train"]["model_config"],
                "model_name": config["train"]["model_name"],
                "s3_path": config["train"]["s3_path"],
            },
        )


if __name__ == "__main__":
    with open("config.yaml", "r") as fh:
        conf = yaml.safe_load(fh)

    go(conf)
