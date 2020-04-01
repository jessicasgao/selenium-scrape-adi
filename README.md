# selenium-scrape-adi

The Area Deprivation Index (ADI) is a national and statewide index that ranks neighborhoods (FIPS and zip codes) by level of socioeconomic disadvantage. The ADI is increasingly found in literature and used by healthcare researchers to evaluate equity in health outcomes by geographic location.

Unfortunately, getting each state's zip code level data requires a separate download process. This repo uses Python selenium to automate the entire process:
- Log into the website
- Navigate to data downloads page
- Download each of the 50 states' zipped data file
- Unzip all files to a specified location and check for completion
- Append each state's data into a single .csv file for easy data analysis; and
- Remove separate state files.

## Getting Started

Make sure to use best practices when editing the repository:
- [pipenv](https://github.com/pypa/pipenv)
- [git flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [semantic commit messages](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)

Before launching the data scraper, make sure to create an account on the [ADI website](https://www.hipxchange.org/ADI). 

## Running the script

After editing the config file to reflect your local paths and login information, open git bash in the root directory:

```
pipenv run python main.py
```

Voila! Check your output folder for your final csv. 

## Authors

Jessica Gao
