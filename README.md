# Time series forecasting tool
This is a scientific iniciation from [National Telecommunications Institute](inatel.br) titled "Development a Financial Time Series Forecasting Tool in a Massively Multiplayer Online Role-Playing Game".

## Abstract
This project aims to correlate two currencies values, the country currency (BRL, USD, EUR, TWD and CNY) and the World of Warcraft realm currency named wowtoken (Us, Eu, Ch, Kr and Tw), use the linear regression algorithm, and plot a graphic that show the past of curriencies and the future.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
First of all, we are using the [Python 3.7.4](https://www.python.org/downloads/release/python-374/). You can download this repository as a zip, and run the following command in to terminal to install the dependecies:

```pip install -r requirements.txt```
### Installing
You can run the ```install.py```(this code aren't ready) to setup your development env running. 

``` python install.py ```

- install.py
This script create the whole database that we will use in this project, the database's name is wow.db.

- database.py
This script is able to create the database that we'll use in the project named wow.db, collect the wowtoken value from [WoWTokenPrices.com](https://wowtokenprices.com) and the curriencies value from [Foreign exchange rates API](https://exchangeratesapi.io/) and adjust our data from the parameters that we need to plot (implements from cleanDatabase.py).

- cleanDatabase.py (REMOVE)
This one is capaple to organize the data that we have colleted before, and generate the maens values and average values from each currency and wowtoken, after this process, the script will create a new database named wow_az.db.

### Running
You can run the project with the ```run.py``` (aren't ready), it will plot the 2d graphics from our data, and will give the information abou correlation between our curency and wowtoken

- run.py
The function of this script is plot the data found in wow_az.db.

## Auxiliar tools

- [gdrive](https://github.com/prasmussen/gdrive): Upload automatically the database to my google drive.

## Libraries:

The following libraries were used in the project:
- [Pandas](https://pandas.pydata.org): Dataframes manipulation;
- [Requests](https://2.python-requests.org/en/master/): Send organic, grass-fed HTTP/1.1 requests, without the need for manual labor;
- [Numpy](https://www.numpy.org/): NumPy is the fundamental package for scientific computing with Python;
- [Matplotlib](https://matplotlib.org): Plotting 2D  graphics;
- [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/): Used for webscrapping.

## Authors
### Advisor
- Marcelo V. C. Aragão (https://github.com/marcelovca90)

### Students
- Rubens Cividati (https://github.com/cividati)

### Contributors
- Daniel Pontello (https://github.com/danielpontello)
- Isabella Capistrano
- Henrique B. Lang (https://github.com/henriqueblang)
