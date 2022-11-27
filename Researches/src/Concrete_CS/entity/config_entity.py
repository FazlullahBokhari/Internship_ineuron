from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    data_validation_path: Path
    updated_data_validation_path: Path
    simple_imputer_strategy: str

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_transformation_path: Path
    train_dataset_features_path: Path
    train_dataset_target_path: Path
    test_dataset_features_path: Path
    test_dataset_target_path: Path
    test_size: float
    random_state: int

@dataclass(frozen= True)
class ModelTrainerConfig:
    root_dir: Path
    training_features_path: Path
    training_target_path: Path
    testing_features_path: Path
    testing_target_path: Path
    saved_file: Path
    n_estimators: list
    max_features: list
    max_depth: list
    min_samples_split: list
    min_samples_leaf: list
    scoring: str
    n_iter: int
    cv: int
    verbose: int
    random_state: int