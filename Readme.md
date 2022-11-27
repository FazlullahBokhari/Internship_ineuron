
# Concrete Compressive Strength

This project helps to predict the compressive strength of concrete after a given time at any time which in general takes 28 days time by the industry. The proposed Machine Learning Project is a time saver.


## Acknowledgements

 - [Final Deployment](https://concrete.herokuapp.com/)
 - [GitHUB Repository](https://github.com/FazlullahBokhari/Internship_ineuron/tree/master/Code)
 - [DagsHUB Repository](https://dagshub.com/Amir47/ML_Intern)

## Appendix

The Concrete compressive strength model is a Machine Learning project which predicts Concrete compressive strength on the basis of raw materials and age of the concrete.

## Authors

- [Amir Khan](https://github.com/Amir4786/)
- [Fazlullah Bokhari](https://github.com/FazlullahBokhari/)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`


## Configuration Setup

#### Command to the whole setup from scratch

#### For Virtual Environment and Requirements installation

```
  bash init_setup.sh
```



#### Activate the Environment

```
  conda activate ./env
```


#### Data Ingestion Step

```
  python src/Concrete_CS/pipeline/stage_01_data_ingestion.py
```


#### Data Validation Step

```
  python src/Concrete_CS/pipeline/stage_02_data_validation.py
```


#### Data Transformation Step

```
  python src/Concrete_CS/pipeline/stage_03_data_transformation.py
```


#### Model Trainer Step

```
  python src/Concrete_CS/pipeline/stage_04_model_trainer.py
```


## DVC

#### Used to know the Model Flow

#### To initialize DVC

```
  dvc init
```

#### To run the Pipeline

```
  dvc repro
```