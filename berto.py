
import requests
from pathlib import Path
import json

def import_config(config_path, potential_match_threshold, auto_match_threshold):
    url = "http://localhost:8000/api/v1/config"
    with open(config_path) as f:
        model_dict = json.load(f)

    # Build the payload
    data = {
        "splink_settings": model_dict,
        "potential_match_threshold": potential_match_threshold,
        "auto_match_threshold": auto_match_threshold
    }

    # Send POST request
    response = requests.post(url, json=data)

    # Print response
    print("Status code:", response.status_code)
    print("Response body:", response.text)

def run(s3_uri, conf):
    #services/empi/empi_service.py
    url = "http://localhost:8000/api/v1/person-records/import"

    # Build the payload
    data = {
        "s3_uri": s3_uri,
        "config_id": conf
    }

    # Send POST request
    response = requests.post(url, json=data)

    # Print response
    print("Status code:", response.status_code)
    print("Response body:", response.text)

def get_persons():
    url = "http://localhost:8000/api/v1/persons"

    # Send GET request
    response = requests.get(url)

    # Print response
    print("Status code:", response.status_code)
    print("Response body:", response.text)

if __name__ == "__main__":
    import_config("backend/main/tests/resorces/tuva_synth/tuva_synth_model.json", potential_match_threshold=0.5, auto_match_threshold=1.0)
    #from backend/main/tests/resources/tuva_synth/tuva_synth_clean.csv
    run("s3://algorex-sandbox004-s3-it-filestaging-secure/2026-01-13/dad9049d11d41a05324d27cbe5d760be_18:56:08/fake_roster_20260109.csv","cfg_1")
    #get_persons()
    #TODO:
        #delete file function
        #export crosswalk function
    # connect to db container
    #sudo docker exec -it tuva-empi-db-1 /bin/bash
    # PGPASSWORD=tuva_empi psql -h db -U tuva_empi postgres
    # \l to see dbs
    # \c to connect to db
    # drop database tuva_empi to reset

