
# Predict Sports Wagering Revenue


## **Problem Statement**

The State Legislature of Connecticut is reviewing a bill to legalize sports wagering within the state. The State Legislature must carefully weigh pros and cons when deciding pass or reject the bill. If they pass the bill, the bill moves on to the Sentate for final approval. If the Senate approves, Connecticut would become the 12th state in the United States where sports wagering has been legalized.

A major consideration by the State Legislature is the potential revenue gain in the State General fund. All sources of gaming share revenue with the state and make transfers into the State General fund at the end of the fiscal year. While sports wagering itself is likely to bring in new revenue for the state, the state must consider reductions in other revenue streams that the new sports wagering revenue stream may cause.

Using West Virginia has a protype, we will build a time series model that will predict tax revenue broken down on a weekly basis. After building a baseline model, we will gridsearch to find the most optimal parameters to use, leading us to select an ARIMAX time series model. After modeling, we will use root mean squared error to measure the model's succes. If our ARIMAX model's Root Mean Squared Error is less than our baseline model's Root Mean Squared Error, we can conclude that our model does improve predictions than a standard baseline model would. If it does beat the baseline, we can consider using the model to lead to a recommendation for the State Legislature in Connecticut.

## **Executive Summary**

We were told that the State Legislature needs help in making their decision. They don't want to approve a bill to the Senate to approve of sports wagering without having a sense of what amount of taxable revenue the state could expect to bring in over a period of time if the state does legalize sports wagering. Several states have gone through the same process before, and sports wagering reports are available to the public to analyze. While each state's report does include taxable revenue, the additional features that each state provides in their reports vary greatly. Given that West Virgina makes public sports wagering reports that include interesting features that we expect to help predict taxable revenue beyond the actual taxable revenue feature, we have chosen West Virginia as our prototype, therefore, West Virginia's sports wagering reports will be analyzed and used as data to train our model on. Since the data is broken out into weekly time periods, where one observation includes one week of data, we know a time series model will be appropriate.

We begin our analysis by importing in our sports wagering annual report. The report includes 52 weeks of data, 26 weeks taken from a 2019 fiscal year report, and 26 weeks taken from a 2020 fiscal year report, the total, being our combined report that we read in. Our next step is to do some high level checks. We take a closer look at the data by looking at the info, columns, shape, a description, data types, and null values that the data includes. That leads us to some cleaning where we fill null values when appropriate, and clean feature titles by stripping out blank spaces when necessary. We then look at the relationships of our features. Some basic scatterplots will show sometimes interesting, sometimes obvious relationships. It becomes obvious that some features are calculations of others, when correlations of 1 are found, for example. After getting a feel for our features and how they are related or unrelated, we focus on the times series aspect of the data. We start seeing that there aren't many obvious trends of our taxable revenue (which West Virginia defines as "total_taxable_receipts" over the time period of our data. Unfortunately, we only have one year of data. More data would help determine if seasonality occurs. 

We then move on to preprocessing, a step needed before we can model. To improve our model, we expect that exogenous features would be useful to include. We look at Autocorrelation and Partial Autocorrelation Functions, which show us that most of our data falls within the 95% confidence interval. Once again, we see seasonality cannot be proven. This leads us to do outside research, to gain more confidence in our modeling selection. We conduct outside research, leading us to believe the upwards trend in taxable revenue may be caused by more sports wagering options, in the forms of professional sporting events, may be available to sports wagerers. For example, in the fall, where taxable revenue increased in West Virginia, the NFL season is underway and the NBA season is getting ready to begin. Therefore, we leverage and read in NFL and NBA data sets which leads us to adding new features (to be used as exogenous features in our model), to our data. We then train-test split our data, splitting our data as a necessary means of modeling.

We create a basic baseline model based on the mean of total taxable receipts of our train data. After calculating the Root Mean Squared Error of that model, we now have something to try and beat with a new model. We gridsearch to find the optimal parameters, that will lead us to a select a model. The results lead us to select an ARIMAX model that only includes an Autoregressive component, as well as exogenous features. After building that model, we calculate the Root Mean Squared Error of that model too. We also look at residuals, to see how closely our model can predict. If the RMSE value is closer to zero than it is in our baseline model, we can conclude that the ARIMAX model does a better job than a baseline model does, and therefore, select the ARIMAX model as our final model.


## **Conclusions and Recommendations**


We would love to be able to tell the State Legislature that they should either expect X amount of taxable revenue in a year if they approve sports wagering to the Senate and the Senate, in turn, passest the bill. Leveraging our ARIMAX model, we are able to come up with predicted weekly values of taxable revenue. However, to give the State Legislature a confident yes or no, we really need more data. Given that we were only able to leverage 52 weeks of data and observations, we can't conclude if seasonality exists. The State Legislature would benefit from knowing of seasonality.  Additionally, while our ARIMAX model does outperform a standard baseline model, it doesn't come very close in predicting values based on what we trained the model on.  At certain points in time within the data time period, it made reasonable predictions. At other times, it was way off. We'd like more time to tune our model and possibly bring in additional exogenous features.

We recommend leveraging more resources to continue our analysis. We would like more years of data, more features, and a better idea from the State Legislature how exactly they determine success. All we were told is that they want to decide on whether to approve the bill or not to the Senate. We don't know what is important to them, if there is a certain taxable revenue amount they want to see to approve the bill, etc.

In conclusion, we would like the State Legislature to work more closely with us, for them to help us define "success", to provide us more resources, and more time to conduct a more comprehensive analysis.


## **Sources**

- West Virginia Sports Wagering Reports:https://wvlottery.com/secured-portal-reporting/?hash=5be9f594

- US Sports Betting Revenue And Handle: https://www.legalsportsreport.com/sports-betting/revenue/

- How to Grid Search SARIMA Hyperparameters for Time Series Forecasting by
Jason Brownlee: https://machinelearningmastery.com/how-to-grid-search-sarima-model-hyperparameters-for-time-series-forecasting-in-python/

- 2019 NFL Season Schedule: https://www.pro-football-reference.com/years/2019/games.htm

- 2019-2020 NBA Season Schedule:
https://www.basketball-reference.com/leagues/NBA_2020_games.html

