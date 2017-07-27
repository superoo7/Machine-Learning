# Chapter 1 Data Preprocessing
* Python: [Data Preprocessing Template](./predata.py)
* R: [Data Preprocessing Template](./predata.r)

## 1) Import Files

## 2) Create Matrix 
* X,Y

## 3) Dealing with missing data 
* Strategy used: mean
* based on strategy replaced the missing val

## 4) Encode categorical data 
* make names into data
* To resolve one name higher/superior than another use dummy val

## 5) Split data into Training and Test set
* normally test_size is .2-.3 (train_size+test_size = 1)

## 6) Feature Scaling 
* fit and transform dummy variables? 
	* dummy value consist of 0s and 1s, depends on the context, depends how much you want to keep interpretation in your models
	* If scaled, everything will be same scale, good for prediction
	* Lose interpretation for knowing which observation belongs to which source
	* It wont break the model
* feature scaling on dependable variable? (Y)
	* No (Regression)
