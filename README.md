
# IBM AI Enterprise Workflow Capstone Project

This repository contains my solution for the IBM AI Enterprise Workflow Captstone project.
The task is provided in https://github.com/aavail/ai-workflow-capstone and is additionally
documented [here](https://github.com/MBAigner/ai-workflow-capstone/blob/master/documentation/description.md).

# Project Structure and API

## API

After starting ``app.py`` locally or over the provided ``Dockerfile``, predictions, trainings and logs work over REST calls, described in the following.
The REST calls can be done over the address 0.0.0.0:8080.

The following POST options are present. All of them get a dictionary as input via post. Additionally, the response is always a dictionary (despite of log files).
* ``0.0.0.0:8080/predict``
  * Parameters:
    * ``country``: all or name of the country
    * ``test``: true or false
  * Return: ``prediction``, ``probability``, ``status`` (if error, additionally ``error_message``)
* ``0.0.0.0:8080/train``
  * Parameters: 
    * ``country:`` all or name of the country
    * ``test``: true or false
  * Return: ``status`` (if error, additionally ``error_message``)
* ``0.0.0.0:8080/get_log``
  * Parameters: ``type``: "predict" or "train"
  * return: log file (in CSV Format) or in case of errors a dictonary with ``status`` and ``error_message``

## Docker

Execute the following commands to build and run the docker container:

```
docker build -t ai-workflow-capstone .
docker run ai-workflow-capstone
```

The container now runs at port 8080 on localhost.

## Testing

All tests can be run with ``python3 run-tests.py``.

Single tests for either API, logging or model can be found in the directory ``unittests``.
There, ``DEBUG`` can be set to True for single tests (either API, Log or Model).

Logging for tests is done with test models and an according flag for tests in the log files.
Thus, production and test logs can be distinguished.

## Monitoring

A monitoring script for obtaining prediction errors and comparing actual versus predicted values (also to the baseline) is available in ``monitoring.py``.

## Reports

The reports for all three parts can be found in the directory ``documentation``.


# Solution

## Part 1

#### (1) Assimilate the business scenario and articulate testable hypotheses.

* H<sub>0</sub>: There will be no difference between the revenue of the new model an the old one.
* H<sub>1</sub>: The revenue prediction will increase using the new model.

Another alternative hypothesis is that the revenue prediction performance goes down when using the new model.
Alternatively, the same can be assumed country-wise:

* A further hypothesis H<sub>0</sub> is that there are no differences in the distribution of monthly revenues of the then top countries,
 * vs. H<sub>1</sub> that there is s significant difference.

#### (2) State the ideal data to address the business opportunity and clarify the rationale for needing specific data.

Ideal data to address the business opportunity includes for each transaction:

* date/time stamps of transaction
* user
* country of user
* subscription model
* resulting revenue

#### (3) Create a python script to extract relevant data from multiple data sources, automating the process of data ingestion.

The extraction of the relevant data from multiple input files is based on the script given in the solution guidance
 ``solution-guidance/cslib.py``.
 
The extracted Pandas DataFrames have been used as a basis for the subsequent EDA tasks (4) and (5).

####  (4) Investigate the relationship between the relevant data, the target and the business metric.

The data exploration and the determination of relationships has been done in the Jupyter notebook
 ``scripts/part_1.ipynb``.

#### (5) Articulate your findings using a deliverable with visualizations.

The visualizations have been again built in the notebook ``scripts/part_1.ipynb``.
The findings are summarized in the part 1 report in the documentation folder 
``documentation/part1_report.pdf``.

## Part 2

#### (1) State the different modeling approaches that you will compare to address the business opportunity.

In order to address the business opportunity, the following models will be compared:

* A supervised ensemble approach, namely the **Random Forest Regressor**
* A simple **Least Squares Regressor**
* A time-series model (TBD)

#### (2) Iterate on your suite of possible models by modifying data transformations, pipeline architectures, hyperparameters and other relevant factors.

The suitablilty of data transformations, pipeline architectures, hyperparameters and other relevant factors has been established. 
This is done in the python script ``model.py``.

For all of the models, different parameter settings and transformations have been compared.

#### (3) Re-train your model on all of the data using the selected approach and prepare it for deployment.

This is again provided in the final version of the script ``model.py``.
The decision is argued in the summary report.

#### (4) Articulate your findings in a summary report.

The summary report is provided in ``documentation/part_2_report.pdf``.

## Part 3


#### (1) Build a draft version of an API with train, predict, and logfile endpoints.

The API draft and endpoints are written in the file ``app.py``.

#### (2) Using Docker, bundle your API, model, and unit tests.

The Docker file is stored as ``Dockerfile`` in the root directory of this repository and bundles the API, model and unit tests.


#### (3) Using test-driven development iterate on your API in a way that anticipates scale, load, and drift.

All tests can be started using ``run-test.py`` and have been stored in the directory ``unittests``.
The consist of

* Tests for training and predicting using the model for different countries and dates.
* Tests for the logging utility.
* Testing for the API endpoints

#### (4) Create a post-production analysis script that investigates the relationship between model performance and the business metric.

A post-production analysis is provided in the script ``monitoring.py``.
There, the actual values are compared to the predictions.
Additionally, the predictions are compared to a baseline, i.e. always predicting the mean as revenue for the next days.

Furthermore, the current RMSE of the model and of the baseline are shown.

#### (5) Articulate your summarized findings in a final report.

The summary report is provided in ``documentation/part_3_report.pdf``.
Additionally, the REST interfaces are explained there.

