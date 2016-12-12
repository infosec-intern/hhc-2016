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


def get_tweets():
    config = read_config("config.json")
    client = Api(
        consumer_key=config["consumerKey"],
        consumer_secret=config["consumerSecret"],
        access_token=config["accessToken"],
        access_token_secret=config["accessSecret"]
    )
    response = client.api.statuses.user_timeline.get(screen_name=config["target"], count=200)
    print("\n".join([status["text"] for status in response]))
    with open("output.txt", "w") as ofile:
        ofile.write("\n".join([status["text"] for status in response]))
    last_id = response[-1]["id"]
    response = client.api.statuses.user_timeline.get(screen_name=config["target"], count=200, max_id=last_id)
    print("\n".join([status["text"] for status in response]))
    with open("output.txt", "a") as ofile:
        ofile.write("\n".join([status["text"] for status in response]))


if __name__ == '__main__':
    get_tweets()