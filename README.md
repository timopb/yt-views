# YTViews
Extracts the youtube video view count based on a list of video URLs from a Google Docs Spreadhseet.

## Requirements
- a Google account
- Python 3.10.7 or newer. Download [here](https://www.python.org/).

## Preparation
1. Install requirements
```sh
pip install -r requirements.txt
```
2. Follow instructions on the [Google Workspace Python quickstart guide](https://developers.google.com/docs/api/quickstart/python) to ensure API access. Download your **credentials.json** file and place it in the root folder of the project.
3. Head to [Google Docs Spreadsheets](https://docs.google.com/spreadsheets/) and create your own sheet or clone the [sample sheet](https://docs.google.com/spreadsheets/d/1ypg-aT4fVPMarFrU4SlvafBXVT6knGwxBBVcxDlJQ2U).
4. Extract the sheet ID from your Sheet URL. The sheet ID is the bold part of the following example: docs.google.com/spreadsheets/d/**1ypg-aT4fVPMarFrU4SlvafBXVT6knGwxBBVcxDlJQ2U**/edit#gid=0
5. Apply the ID to the [appropriate line](https://github.com/timopb/yt-views/blob/ec4d29a819aad0a5dfbe178c13adf2635a56937a/main.py#L14C24-L14C63) in main.py

## Running the script
```sh
python main.py
```
## Demo

https://github.com/timopb/yt-views/assets/3785547/4b00686a-2cb3-4aca-a73e-647708906a65

## Relevant URLs:
* [Google Cloud Console](https://console.cloud.google.com/)
* [Google Workspace Python quickstart guide](https://developers.google.com/docs/api/quickstart/python)
* [Sample Sheet](https://docs.google.com/spreadsheets/d/1ypg-aT4fVPMarFrU4SlvafBXVT6knGwxBBVcxDlJQ2U)
