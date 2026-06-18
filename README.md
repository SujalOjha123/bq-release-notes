# BigQuery Release Notes Flask App

A simple Flask web application that fetches and displays BigQuery release notes from the official Google Cloud release notes feed.

## Features

- Fetches BigQuery release notes from the official XML feed
- Displays release notes as clean cards
- Refresh button to reload the feed
- Spinner while loading
- Tweet button for sharing a selected update
- Copy to Clipboard button for each release note
- Export to CSV button
- Light/Dark mode toggle

## Tech Stack

- Python
- Flask
- Feedparser
- HTML
- CSS
- JavaScript

## Feed Source

https://cloud.google.com/feeds/bigquery-release-notes.xml

## Project Structure

bq-release-notes/
- app.py
- requirements.txt
- README.md
- .gitignore
- templates/
  - index.html

## Setup Instructions

1. Install dependencies:

py -m pip install -r requirements.txt

2. Run the app:

py app.py

3. Open in browser:

http://127.0.0.1:5000

## Routes

- / : Main web page
- /api/notes : Returns release notes as JSON
- /refresh : Returns release notes as JSON
- /tweet : Opens Twitter/X sharing URL
- /export/csv : Downloads release notes as CSV

## Notes

This project was created as part of the Day 2 Antigravity CLI practice task.
