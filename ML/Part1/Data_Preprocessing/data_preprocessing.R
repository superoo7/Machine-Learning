# Data Preprocessing

# import the data
dataset = read.csv('Data.csv')

# dealing with missing data
# method 1: delete the data
# method 2: take the mean of the data

# var$colName
# check wether is nil
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Salary)
View(dataset)

# Encoding categorical data
# Country
dataset$Country = factor(dataset$Country, 
                         levels = c('France','Spain','Germany'), 
                         labels = c(1,2,3)) #c is vector
# Purchased
dataset$Purchased = factor(dataset$Purchased, 
                         levels = c('No','Yes'), 
                         labels = c(0,1)) 



# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)

set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)


# Feature Scaling
# without [, 2:3] (Error in colMeans(x, na.rm = TRUE) : 'x' must be numeric)
training_set[, 2:3] =  scale(training_set[, 2:3])
test_set[, 2:3] = scale(test_set[, 2:3])
