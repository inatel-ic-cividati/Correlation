# Time Series Forecasting Tool
This is a scientific iniciation from [National Telecommunications Institute](https://inatel.br/home/) titled "Development a Financial Time Series Forecasting Tool in a Massively Multiplayer Online Role-Playing Game".

## Abstract
This project aims to correlate two currencies values, the country currency (BRL, USD, EUR, TWD and CNY) and the World of Warcraft realm currency named wowtoken (Us, Eu, Ch, Kr and Tw), use the linear regression algorithm, and plot a graphic that show the past of curriencies and the future.

## Example
This Graphics shows us the comparation between two datasets, the European currency (Euro) and the World of Warcraft European server's currency (Europe). The correlation between the two graphics looks like 70.42% and the covariance is about 0.06%.
![Graphics](https://i.imgur.com/U8mW7ts.png)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
First of all, we are using the [Python 3.7.4](https://www.python.org/downloads/release/python-374/). You can download this repository as a zip, and run the following command in to terminal to install the dependecies:

```pip install -r requirements.txt```

### Running
You can run the project with the [main.py](https://github.com/Cividati/IC-wow/blob/master/main.py), for a while it isn't plotting any graphics, but it's collecting the whole data needed for it.

```python main.py```

### Scripts
- [database.py](https://github.com/Cividati/IC-wow/blob/master/database.py): 
This script have all functinos that we need to collect the wowtoken value from [WoW Token Prices](https://wowtokenprices.com) and the curriencies value from [Foreign exchange rates API](https://ratesapi.io), adjust our data from the parameters that we need to plot. Plot isn't ready.

- (in development) [main.py](https://github.com/Cividati/IC-wow/blob/master/main.py): 
Run the functions sequencially.
- (in development) [analytics.py](https://github.com/Cividati/IC-wow/blob/master/analytics.py): 
Contains our functions that calculate the correlation index and the auto regression.

- (in development) [view.py](https://github.com/Cividati/IC-wow/blob/master/view.py): 
This code contains the functions that's able to plot our data.

## Auxiliar tools

- [gdrive](https://github.com/prasmussen/gdrive): Upload automatically the database to my google drive.

## Libraries:

The following libraries were used in the project:
- [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/): Used for webscrapping;
- [Matplotlib](https://matplotlib.org): Plotting 2D  graphics;
- [Numpy](https://www.numpy.org/): NumPy is the fundamental package for scientific computing with Python;
- [Pandas](https://pandas.pydata.org): Dataframes manipulation;
- [Requests](https://2.python-requests.org/en/master/): Send organic, grass-fed HTTP/1.1 requests, without the need for manual labor;
- [Statsmodels](https://www.statsmodels.org/stable/index.html): Module that provides classes and functions for the estimation of many different statistical models;
- [SciPy](https://www.scipy.org/): Python-based ecosystem of open-source software for mathematics, science, and engineering.

## Authors
### Advisors
- Marcelo V. C. Aragão (https://github.com/marcelovca90)
- Renzo Mesquita

### Students
- Rubens Cividati (https://github.com/cividati)

### Contributors
- Daniel Pontello (https://github.com/danielpontello)
- Isabella Capistrano
- Henrique B. Lang (https://github.com/henriqueblang)
- Gabriel Claret (https://github.com/claret1)
