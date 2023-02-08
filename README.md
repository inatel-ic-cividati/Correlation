# Correlation Analysis between Real Currency Fluctuations and Virtual Currency of an MMORPG
This repository contains code about a scientific initiation from [National Telecommunications Institute](https://inatel.br/home/) located in Santa Rita do Sapucaí, Brazil titled "Correlation Analysis between Real Currency Fluctuations and Virtual Currency of an MMORPG". You can download the full documentation [here](https://github.com/Cividati/tsft/blob/master/files/article.pdf).

## Abstract
This work proposes the collection of data from the MMORPG World of Warcraft’s virtual currency and real-world exchange rates variations in order to perform a correlation analysis, to identify similarities and differences between these contexts and to point out possible explanations for such relationships. 

## Example
This Graphics shows us the correlation between two datasets, the China's real currency in red(Renminbi - Cny) and the World of Warcraft coin, WoW Token in blue.

![Graphics](https://raw.githubusercontent.com/Cividati/tsft/master/files/plot_ch_rmb.png)

Comparing and correlating each real currency with each respective realm, we got the follow correlation table. Where the columns ```Pearson, Kendall and Spearman``` show the method used for correlation.

Region     | Currency | Pearson | Kendall | Spearman |
------------|-------|---------|---------|----------|
Américas    | BRL   |  0,81   |  0,47   |  0,65    |
Europa      | Eur   |  0,55   |  0,28   |  0,46    |
China       | Cny   |  0,74   |  0,36   |  0,56    |
Coreia      | Krw   | -0,10   | -0,05   | -0,09    |

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
First of all, we are using the [Python 3.7.4](https://www.python.org/downloads/release/python-374/). You can download this repository as a zip, and run the following command in to terminal to install the dependecies:

```pip install -r requirements.txt```

### Running
You can run the whole project with the [main.py](https://github.com/Cividati/IC-wow/blob/master/main.py), for a while it isn't plotting any graphics.

```python main.py```

### Directory Structure
This project is comprised of the following directories:

- **code**: Contains all codes used for correlate and plot;
- **files**: Contains pictures and documentations archives.

## Auxiliar tools

- [gdrive](https://github.com/prasmussen/gdrive): Upload automatically the database to my google drive.

## Libraries

The following libraries were used in the project:
- [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/): Used for webscrapping;
- [Matplotlib](https://matplotlib.org): Plotting 2D graphics;
- [Numpy](https://www.numpy.org/): NumPy is the fundamental package for scientific computing with Python;
- [Pandas](https://pandas.pydata.org): Dataframes manipulation;
- [Requests](https://2.python-requests.org/en/master/): Send organic, grass-fed HTTP/1.1 requests, without the need for manual labor;
- [SciPy](https://www.scipy.org/): Python-based ecosystem of open-source software for mathematics, science, and engineering;
- [Statsmodels](https://www.statsmodels.org/stable/index.html): Module that provides classes and functions for the estimation of many different statistical models.

## Authors
| Name                 	| Role        	| Github 	|
|----------------------	|-------------	|--------	|
| Rubens Cividati      	| Author      	|  [Github](https://github.com/cividati)  	|
| Marcelo V. C. Aragão 	| Advisor     	|  [Github](https://github.com/marcelovca90)      	|
| Isabella Capistrano  	| Contributor 	|   -     	|

## Presentation
[Incitel XXXII 2020](https://www.youtube.com/watch?v=dULSdxkL1xc)
