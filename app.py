from flask import Flask, render_template, jsonify, request, Response, redirect
import feedparser
import csv
import io
from urllib.parse import quote_plus

app = Flask(__name__)

FEED_URL = "https://cloud.google.com/feeds/bigquery-release-notes.xml"

def get_release_notes():
    feed = feedparser.parse(FEED_URL)
    entries = []

    for entry in feed.entries[:20]:
        summary = entry.get("summary", "No description available")
        entries.append({
            "title": entry.get("title", "Untitled update"),
            "link": entry.get("link", "#"),
            "published": entry.get("published", entry.get("updated", "Date not available")),
            "summary": summary
        })

    return entries

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/refresh")
def refresh():
    return jsonify(get_release_notes())

@app.route("/api/notes")
def api_notes():
    return jsonify(get_release_notes())

@app.route("/tweet")
def tweet():
    text = request.args.get("text", "")
    url = request.args.get("url", "")
    tweet_url = "https://twitter.com/intent/tweet?text=" + quote_plus(text + " " + url)
    return redirect(tweet_url)

@app.route("/export/csv")
def export_csv():
    notes = get_release_notes()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Published Date", "Title", "Summary", "URL"])

    for note in notes:
        writer.writerow([
            note["published"],
            note["title"],
            note["summary"],
            note["link"]
        ])

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=bigquery_release_notes.csv"}
    )

if __name__ == "__main__":
    print("BigQuery Release Notes app is running!")
    print("Open browser: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
