---
date: 2017-02-23
title: "Project 2: Classification with Health Records"
---

**Due October 30**

Posted: 10/10/2017  
Last Update: 10/10/2017  

# Task

We will use data from the following Kaggle dataset: https://www.kaggle.com/joniarroba/noshowappointments.

The goal here is to predict patients that will not show up for medical appointments based on their medical records. You should read
the dataset and task prediction in Kaggle to familiarize yourself as much as possible with the task and data.

# Part I: Data prep

- Fork my project skeleton github repo on github
- Download the dataset from [{{< baseurl >}}data/noshowappointments.zip]({{< baseurl >}}data/noshowappointments.zip). Unzip and copy the csv file on to the `data` directory in the project.
- Rename file `partI_shell.ipynb` to `partI.ipynb`
- Complete the `partI.ipynb` notebook

This includes:

- Reading in data csv file 
- Cleanup data column names
- Remove records with erroneous entries (e.g., negative ages, look at what people have done in Kaggle)
- Create a test set of 100k records that you won't touch again for the reminder of this project until Part III. Use stratified sampling on the `No-show` variable to ensure
test set and training set class proportions are the same. Save the train and test sets as csv files in the `processed_data` directory.
- Plot the `No-show` variable against the other variables in the dataset as part of Exploratory Data Analysis (USE THE TRAINING SET FOR THIS!!)
- Create a preprocessing pipeline using `scikit` to prepare the data for the ML algorithms we will use. At a minimum, standardize numerical variables, transform categorical variables into one or more numerical values. You may apply other transformations that you think would be useful (e.g., logarithmic transformations).

Push your changes to github and submit part I on ELMS on Monday Oct. 16 11:59pm

A lot of what you will do here is covered in the introduction notebook posted earlier this semester [{{< baseurl >}}/notebooks/intro_lab.html]({{< baseurl >}}/notebooks/intro_lab.html). Feel free to use that code for inspiration.

# Part II: Classification Methods

# Part III: Ensembles and Final Result