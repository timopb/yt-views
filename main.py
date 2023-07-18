from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from bs4 import BeautifulSoup
import requests

# TODO: Apply your own Sheet ID here
SPREADSHEET_ID = '1ypg-aT4fVPMarFrU4SlvafBXVT6knGwxBBVcxDlJQ2U'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
URL_RANGE = 'Views!A2:A'    # range where we get the URLs from
DATA_RANGE = 'Views!B2:B'   # range where we put the view count

def authenticate():
  """Handles the authentication"""
  print("Auhtenticating... ", end = '')
  creds = None
  if os.path.exists('token.json'):
      creds = Credentials.from_authorized_user_file('token.json', SCOPES)
  if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
          creds.refresh(Request())
      else:
          flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
          creds = flow.run_local_server(port=0)
      with open('token.json', 'w') as token:
          token.write(creds.to_json())
  print("success!")
  return creds

def get_ytdata(url):
    print("Getting data for %s... " % url, end = '')
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    views = s.select_one('meta[itemprop="interactionCount"]')['content']
    data = {'views': views}
    print("%s views" % data['views'])
    return data

def parse_sheet(creds, spredsheet_id):
  """Parses the sheet row by row"""
  try:
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.get(spreadsheetId=spredsheet_id,ranges=[URL_RANGE],fields="sheets/data/rowData/values/hyperlink").execute()
    rowData = result["sheets"][0]["data"][0]["rowData"]
    update = []
    for row in rowData:
      url = row["values"][0]['hyperlink']
      data = get_ytdata(url)
      update.append([data["views"]])

    value_input_option = 'USER_ENTERED'
    print("Updating data... ", end ='')
    result = sheet.values().update(spreadsheetId=spredsheet_id, range=DATA_RANGE, valueInputOption=value_input_option, body={"values": update}).execute()
    print("done")
  except HttpError as err:
    print(err)

def main():
  print("Updating sheet https://docs.google.com/spreadsheets/d/%s" % SPREADSHEET_ID)
  creds = authenticate()
  if not creds:
    print("Got no credentials!")
    return
  
  parse_sheet(creds, SPREADSHEET_ID)

if __name__ == '__main__':
    main()