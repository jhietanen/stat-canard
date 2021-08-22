# -*- coding: utf-8 -*-
import click
import logging
import requests
import json
from datetime import date

from pathlib import Path
from src import settings

@click.command()
@click.option('--table', prompt=True, type=click.Choice(settings.DATA_QUERIES),)
def main(table):
    """ Runs scripts to retrieve data from StatFin API.
        Returns json-stat file which will be saved to /data/raw/.
    """


    # Get URL and json-query data for selected table from settings
    query_dict = settings.DATA_QUERIES[table]

    # Read JSON_QUERY saved for this table
    with open(query_dict['JSON_QUERY']) as file:
        json_query = json.load(file)

    # Use POST Request with JSON query to retrieve data from PxWeb API
    logging.info(f'Retrieving {table} data from API')
    r = requests.post(query_dict['URL'], json=json_query)
    data = r.json()

    # Save json-stat file to /data/raw/ directory, configure filename and path
    filename = table.split('.')[0]+'_'+str(date.today())  # Naming convention ([table]_[retrieval date])
    suffix = '.json'
    path = Path(settings.DATA_PATHS['RAW'], filename).with_suffix(suffix)

    with open(path, 'w') as json_file:
        json.dump(data, json_file)

    logging.info(f'Saved file {filename} to {settings.DATA_PATHS["RAW"]}')

    return data

if __name__ == '__main__':

    # Configure logging
    log_fmt = '%(asctime)s:%(levelname)s:%(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt, force=True)

    main()
