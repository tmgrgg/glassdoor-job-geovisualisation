from gdScraper import build_dataset
from gdHelper import build_csv

location_list = ['New York City', 'Los Angeles', 'San Francisco', 'Chicago', 'Houston', 'Philadelphia']

def autoscrape(job_title = 'Data Scientist' , locations=location_list):
    for location in locations:
        try:
            build_dataset(job_title, location)
            build_csv(job_title, location)
        except Exception as e:
            print(e)
            build_csv(job_title, location)
        

    