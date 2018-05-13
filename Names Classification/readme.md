# Ethnic Name Classifier 
### Problem Statement:
Given a data set of first names belonging to one particular
ethnic group, we want to create a classifier that can classify the
first names of that particular ethnicity from all other ethnicities.
This problem is different from regular multi class classification
problem since here we have training data belonging to only one
class, we can evaluate it using some samples from other
“negative” classes, but there is no practical way to collect or
even stipulate data from all possible classes.

### Data Sets
hindu_baby_names.txt: This data set contains baby names of
our target ethnicity.

Create a classifier that given an input string will output “True” if
the input string corresponds to this ethnicity, for all other
ethnicities it will output “False.
negative_class_1.txt, negative_class_2.txt :
Sample data sets from two other ethnicities, namely American
baby names and Arabic baby names against which you can
evaluate your classifier but at test time we will randomly select
a data set of baby names from any possible ethnicity (may be
Nordic, Somali, Japanese etc.)

### Approach:
1- One hot encoding each name using tokens created of varying lengths
2- Word2Vec approach for catching underlying sequence structure of names by using the context of the tokens.
3 - KMeans clustering. A threshold to maybe filter out names that are farther atleast this much from their assigned cluster centers
