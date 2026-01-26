#docker exec -it myapp python berto.py

import requests
from pathlib import Path
import json

def move_to_s3():
    #is this necessary?
    #make s3 bucket
    print(
    """
    aws --endpoint-url=http://localhost:4566 s3 mb s3://albert-test
    """
    )
    # upload
    print(
    """
    aws --endpoint-url=http://localhost:4566 s3 cp backend/main/tests/resources/tuva_synth/tuva_synth_clean.csv s3://albert-test/tuva_synth_clean.csv
    """
    )
def import_config():
    url = "http://localhost:8000/api/v1/config"
    path = Path("backend/main/tests/resources/tuva_synth/tuva_synth_model.json")
    with path.open() as f:
        model_dict = json.load(f)
    # Build the payload
    data = {
        "splink_settings": model_dict,
        "potential_match_threshold": 0.5,
        "auto_match_threshold": 1
    }

    # Send POST request
    response = requests.post(url, json=data)

    # Print response
    print("Status code:", response.status_code)
    print("Response body:", response.text)

def import_data():
    url = "http://localhost:8000/api/v1/person-records/import"

    # Build the payload
    data = {
        "s3_uri": "s3://albert-test/tuva_synth_clean.csv",
        "config_id": "cfg_1"
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
    #move_to_s3()
    #import_config()
    #import_data()
    get_persons()

