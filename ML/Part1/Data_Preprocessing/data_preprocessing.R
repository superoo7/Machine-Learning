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
dataset$Country = factor(dataset$Country, 
                         levels = c('France','Spain','Germany'), 
                         labels = c(1,2,3)) #c is vector


