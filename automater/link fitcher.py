import gkeepapi
import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials  # Import the correct class

# Define the scope
SCOPES = ['https://www.googleapis.com/auth/keep']

def authenticate():
    creds = None
    # The file token.json stores the user's access and refresh tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)  # Correct method

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('/home/sagar/Downloads/cred.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def main():
    # Authenticate and get credentials
    creds = authenticate()

    # Initialize Google Keep client
    keep = gkeepapi.Keep()
    print("Authenticating...")
    keep.login(creds)

    print("Retrieving all notes...")
    notes = keep.all()

    # Open file to write notes
    with open('google-keep-notes.csv', 'w', encoding='utf-8') as f:
        f.write("Title,Text\n")
        for note in notes:
            # Write note title and text to CSV (escape quotes by doubling them)
            title = note.title.replace('"', '""') if note.title else ''
            text = note.text.replace('"', '""') if note.text else ''
            f.write(f'"{title}","{text}"\n')

            # Delete the note from Google Keep
            print(f"Deleting note: {title or '(no title)'}")
            keep.delete(note)

    # Sync to apply deletions
    print("Syncing deletions with Google Keep server...")
    keep.sync()

    print("All notes exported and deleted successfully.")

if __name__ == "__main__":
    main()
