import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exeption import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    '''
    This class handles the data transformation process for the machine learning pipeline.
    It creates preprocessing pipelines for both numerical and categorical features,
    combines them using ColumnTransformer, and provides methods to transform datasets.
    
    The class handles:
    - Missing value imputation for numerical and categorical features
    - Scaling/normalization of numerical features
    - One-hot encoding of categorical features
    - Saving and loading preprocessor objects
    '''
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        try:
            numerical_columns = ['writing_score', 'reading_score']
            categorical_columns = [
                'gender', 
                'race_ethnicity', 
                'parental_level_of_education', 
                'lunch', 
                'test_preparation_course'
            ]

            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),  # Handle missing values with median
                ('scaler', StandardScaler())                    # Standardize numerical features
            ])
            
            # Create pipeline for categorical features
            cat_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy="most_frequent")),  # Handle missing values with mode
                ("one_hot_encoder", OneHotEncoder()),                  # Convert categories to binary columns
                ("scaler", StandardScaler(with_mean=False))            # Scale the encoded features
            ])

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            # Combine both pipelines using ColumnTransformer
            preprocessor = ColumnTransformer([
                ("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipeline", cat_pipeline, categorical_columns)
            ])

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)