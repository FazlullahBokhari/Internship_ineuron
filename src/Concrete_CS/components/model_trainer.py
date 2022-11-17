import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import RandomizedSearchCV
from Concrete_CS.entity import ModelTrainerConfig
from Concrete_CS import logger

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config= config
        logger.info("Uploading testing data...")
        self.testing_features= pd.read_csv(self.config.testing_features_path)
        self.real_values= pd.read_csv(self.config.testing_target_path).iloc[:,1]
        logger.info("test data uploaded!")
    def load_training_data(self):
        logger.info("uploading training data...")
        features_set= pd.read_csv(self.config.training_features_path)
        logger.info("training data uploaded!")
        target_set= pd.read_csv(self.config.training_target_path)
        logger.info("with pandas create data for training the model.")
        features_set[target_set.columns]=target_set
        logger.info("training data created!")
        return features_set
    def by_linear_regression(self):
        logger.info("training model by linear regression.")
        linear_reg= LinearRegression()
        linear_reg.fit(self.load_training_data().iloc[:,:-1], self.load_training_data().iloc[:,-1])
        logger.info("model trained by linear regression!")
        predicted_values= pd.DataFrame(linear_reg.predict(self.testing_features))
        squared_error= mean_squared_error(predicted_values, self.real_values)
        logger.info("model error...")
        error= np.sqrt(squared_error)
        return linear_reg
    def by_random_forest(self):
        logger.info("model training by Random Forest")
        rf= RandomForestRegressor()
        n_estimators= self.config.n_estimators
        max_features= self.config.max_features
        max_depth= self.config.max_depth
        min_samples_split= self.config.min_samples_split
        min_samples_leaf= self.config.min_samples_leaf
        random_grid= {
                      "n_estimators": n_estimators,
                      "max_features": max_features,
                      "max_depth": max_depth,
                      "min_samples_split": min_samples_split,
                      "min_samples_leaf": min_samples_leaf
                     }
        scoring= self.config.scoring
        n_iter= self.config.n_iter
        cv= self.config.cv
        verbose= self.config.verbose
        random_state= self.config.random_state
        RF_Random= RandomizedSearchCV(
                                      estimator= rf,
                                      param_distributions= random_grid,
                                      scoring= scoring,
                                      n_iter= n_iter,
                                      cv= cv,
                                      verbose= verbose,
                                      random_state= random_state
                                     )
        RF_Random.fit(self.load_training_data().iloc[:,:-1], self.load_training_data().iloc[:,-1])
        logger.info("Model is trained by Random Forest.")
        predicted_values= pd.DataFrame(RF_Random.predict(self.testing_features))
        squared_error= mean_squared_error(predicted_values, self.real_values)
        logger.info("error came out from trained model.")
        error= np.sqrt(squared_error)
        return RF_Random
    def save_file(self):
        logger.info("saving the model in pickle file...")
        random_forest= self.by_random_forest()
        file= open(self.config.saved_file, "wb")
        pickle.dump(random_forest, file)
        logger.info(f"Model is saved at {self.config.root_dir}")