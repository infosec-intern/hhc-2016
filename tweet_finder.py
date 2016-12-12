"""Script to access a specific Twitter user's tweets"""
import json
from twypy.api import Api


def read_config(filename):
    """
    Read a JSON file for info about the Twitter API
    Input
        filename: Path to the JSON config file
    No Output
    """
    with open(filename, "r") as ifile:
        return json.loads(ifile.read())


if __name__ == '__main__':
    config = read_config("config.json")
    client = Api(
        consumer_key=config["consumerKey"],
        consumer_secret=config["consumerSecret"],
        access_token=config["accessToken"],
        access_token_secret=config["accessSecret"]
    )
    statuses = []
    response = client.api.statuses.user_timeline.get(screen_name=config["target"])
    print("\n".join([status["text"] for status in response]))
