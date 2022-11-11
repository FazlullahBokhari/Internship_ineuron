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