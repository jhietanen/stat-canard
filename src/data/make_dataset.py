# -*- coding: utf-8 -*-
import click
import logging
import json

from pyjstat import pyjstat
from pathlib import Path
from src import settings

RAW_DATA = [x.name for x in settings.DATA_PATHS['RAW'].iterdir() if x.is_file() and x.name.endswith('.json')]

@click.command()
@click.option('--datafile', prompt=True, type=click.Choice(RAW_DATA),)
def main(datafile):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """

    # Read RAW data file
    with open(settings.DATA_PATHS['RAW'] / datafile) as file:
        json_stat = json.load(file)

    # Convert RAW data to pandas DataFrame
    logging.info(f'Converting {datafile} to CSV')
    df = pyjstat.from_json_stat(json_stat)[0]

    # Save pandas dataframe as CSV to /data/processed/ directory, configure filename and path
    filename = datafile
    suffix = '.csv'
    path = Path(settings.DATA_PATHS['PROCESSED'], filename).with_suffix(suffix)

    # Save pandas DataFrame as CSV -file
    df.to_csv(path)
    logging.info(f'CSV file saved to {path}')

    return df


if __name__ == '__main__':

    # Configure logging
    log_fmt = '%(asctime)s:%(levelname)s:%(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt, force=True)

    main()
