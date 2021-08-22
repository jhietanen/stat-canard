<img src="references/img/StatCanard_logo.png" alt="logo" align="right" height="70"/>

# Stat Canard

Stat Canard is a data analysis project to explore and analyze [Official Statistics of Finland (OSF)](https://www.stat.fi/index_en.html) by using [PxWeb API](https://www.stat.fi/static/media/uploads/org_en/avoindata/px-web_api-help.pdf).

## Table of Content

- [Quick Guide](#quick-guide)
    - [Getting Data](#getting-data)
    - [Making Dataset](#making-dataset)
- [Project Structure](#project-structure)
- [References](#References)

## Quick Guide

Want to use this repo? Please review this quick guide. 

### Getting Data

Start searching data from [StatFin](https://pxnet2.stat.fi/PXWeb/pxweb/en/StatFin/) database. Choose table and variable you want to explore further and then *Show table*.

On the results page you can find *API query for this table*. Use following steps to retrieve data:
1. Create new subdirectory to `references/databases/StatFin/`. Use table name as a name for the subdirectory to keep things organized.
2. Create new JSON file to this subdirectory. Copy and paste the JSON query from *API query for this table* -> *JSON query* to this file.

Now you have saved the JSON query you want to use when retrieving the data from PxWeb API. Next we need to configure the whole data query.   

3. Configure `src/settings.py` file. Add new key to DATA_QUERIES dictionary. Use table name as a key to keep things organized.
4. Add new nested dictionary after newly created key and add keys "URL" and "JSON_QUERY" to this dictionary.
5. Copy and paste *API query for this table* -> *URL:* as value for the "URL" key and path to recently saved json file as value for the key "JSON_QUERY".
   
Here is an example:
```python
DATA_QUERIES = {
    'statfin_ksyyt_pxt_11bs.px': {
        'URL': 'http://pxnet2.stat.fi/PXWeb/api/v1/en/StatFin/ter/ksyyt/statfin_ksyyt_pxt_11bs.px',
        'JSON_QUERY': REFERENCES_PATHS['DATABASES'] / 'StatFin' / 'statfin_ksyyt_pxt_11bs.px' / 'json_query.json'
    },
}
```

After these steps, your JSON query has been saved and API query has been configured to settings.py file. Then you can use a script to get raw data dump.

6. Run script `python src/data/get_rawdata.py `in terminal and select the query you want to use (script will provide selection list containing all the configured data queries). Raw data dump will be saved to `data/raw/` with naming convention (table _ retrieval date)

### Making Dataset
API query response is in json-stat2 format. Before we can easily explore this data further (e.g. with pandas), we need to convert the file to another format. In this case, I have used CSV (comma-separated values).

Use following steps to convert to raw data dump to CSV format:
1. Run script `python src/data/make_dataset.py `in terminal. 
2. Select raw data dump you want to convert to CSV format (script will provide selection list containing all raw data dumps saved to `/data/raw/`). 
   
Data you selected will be converted to CSV format and saved to `/data/processed/` with naming convention (name of the table _ today's date)




## Project Structure


    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources. (placeholder)
    │   ├── interim        <- Intermediate data that has been transformed. (placeholder)
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                          and a short `-` delimited description, e.g.
    │                         `1.0-initial-data-exploration`.
    │
    ├── references         <- Data regarding PxWeb API databases and tables, manuals, assets etc.
    │   └── databases      
    │   │   └── tables
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── get_rawdata.py
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling (placeholder)
    │   │   └── build_features.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations (placeholder)
    │       └── visualize.py
    │
    └──  tests              <- Test cases.

--------

<p><small>Project structure based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

## References

Official Statistics of Finland (OSF): <https://www.stat.fi/index_en.html>  
StatFin Database: <https://pxnet2.stat.fi/PXWeb/pxweb/en/StatFin/>  
Cookiecutter Data Science Project Template: <https://drivendata.github.io/cookiecutter-data-science/>
