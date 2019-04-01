# Maryland Energy Administration Incentive Program Analysis
Short analysis of Maryland Energy Administration data on a statewide consumption incentive program.

The Maryland Energy Administration (MEA) publishes data surrounding state-wide initiatives aimed at reducing energy consumption - this dataset was made available via data.gov. 

# Background

The MEA's stated mission is to "promote affordable, reliable and cleaner energy for the benefit of all Marylanders," doing so through a mix of grant and loan offerings across multiple economic verticals (residential, commercial, agriculture, etc.) and actors.
The group maintains a public database, DSIRE, as a source of information surrounding specific policy and incentive programs.
MEA is led by Mary Beth Tung.

# Exploration

The dataset provided consists of 1,724 observations, each with 7 features: Program, County, Savings (electricity consumption reduction in kwh), MEA Contribution, Total Project Cost, Location (longitude/latitude coordinates), and Program Link (url to respective program webpage). The dataset contains no null values.

Every observation is tied to the Home Performance Rebate with Energy Star Program, an incentive designed to offer homeowners rebates in return for making energy efficient upgrades. 

There's a bit more variation when it comes to county. 23 unique counties are included in the data, with a range of observations attributed to each from 1 (Allegany, Somerset) to 799 (Montgomery). 

Let's take a look at the three numerical data points. Using a 'describe' call, we can see that the average electricity reduction comes out to 3.345 kwh (with a standard deviation of 1.98). There does appear to be some outliers, as the max saving value is listed at 23.3 kwh - just over ten standard deviations above the average. MEA contribution is capped at $3,100, and 94 entries hit this max contribution. Total Project Cost appears to have a linear relation with Savings based off of visualization. 

# Regression
Can MEA contribution and total project cost be used to predict savings in kwh? 
Fit a linear regression model after splitting the dataset 75/25 into train/test holdouts. 

Model Coefficients: 
  
  Contribution: -7.541044425177233e-08
 
  Project Cost: 0.0007000140248282455

Performance Metrics:

MAE: 0.00022005286360234918

MSE: 7.448671681375386e-08

MAPE: 0.89%

So, total project cost appears to be positively correlated with reduction in elictricity consumption, while MEA contribution seems to have a smaller effect.  
