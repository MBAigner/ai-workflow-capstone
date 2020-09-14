
# IBM AI Enterprise Workflow Capstone Project

This repository contains my solution for the IBM AI Enterprise Workflow Captstone project.
The task is provided in https://github.com/aavail/ai-workflow-capstone and is additionally
documented [here](https://github.com/MBAigner/ai-workflow-capstone/blob/master/documentation/description.md).


## Part 1

#### (1) Assimilate the business scenario and articulate testable hypotheses.

* H<sub>0</sub>: There will be no difference between the revenue of the new model an the old one.
* H<sub>1</sub>: The revenue will increase using the new model.

Another alternative hypothesis is that the revenue goes down when using the new model.
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

#### (3) Re-train your model on all of the data using the selected approach and prepare it for deployment.

This is again provided in the final version of the script ``model.py``.

#### (4) Articulate your findings in a summary report.

The summary report is provided in ``documentation/part_2_report.pdf``.

## Part 3

TBD

#### (1) Build a draft version of an API with train, predict, and logfile endpoints.

TBD

#### (2) Using Docker, bundle your API, model, and unit tests.

TBD

#### (3) Using test-driven development iterate on your API in a way that anticipates scale, load, and drift.

TBD

#### (4) Create a post-production analysis script that investigates the relationship between model performance and the business metric.

TBD

#### (5) Articulate your summarized findings in a final report.

The summary report is provided in ``documentation/part_3_report.pdf``.

