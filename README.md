
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
 * vs. H<sub>1</sub> that there is significance in the difference.

#### (2) State the ideal data to address the business opportunity and clarify the rationale for needing specific data.

Ideal data to address the business opportunity includes for each transaction:

* date/time stamps of transaction
* user
* country of user
* subscription model
* resulting revenue

#### (3) Create a python script to extract relevant data from multiple data sources, automating the process of data ingestion.

TBD

From within a Python module there should be a function that reads in the data, attempts to catch common input errors and returns a feature matrix (NumPy array or Pandas DataFrame) that will subsequently be used as a starting point for EDA and modeling.

####  (4) Investigate the relationship between the relevant data, the target and the business metric.

TBD

Using the feature matrix and the tools abvailable to you through EDA spend some time to get to know the data.

#### (5) Articulate your findings using a deliverable with visualizations.

TBD

Summarize what you have learned in your investigations using visualizations.

## Part 2

TBD
