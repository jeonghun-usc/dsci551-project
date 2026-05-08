from flask import Flask, jsonify, send_from_directory
import os
import duckdb


app = Flask(__name__)
@app.route("/")
def index():
    return send_from_directory(os.getcwd(), "index.html")

def get_con():
    return duckdb.connect("music.db", read_only=True)

@app.route("/api/audio-trends")
def audio_trends():
    con = get_con()
    result = con.execute("""
        SELECT track_genre,
               ROUND(AVG(energy), 3) AS avg_energy,
               ROUND(AVG(danceability), 3) AS avg_danceability
        FROM tracks
        GROUP BY track_genre
        ORDER BY avg_energy DESC
    """).df()
    con.close()
    return jsonify(result.to_dict(orient="records"))

@app.route("/api/genre-popularity")
def genre_popularity():
    con = get_con()
    result = con.execute("""
        SELECT track_genre,
               ROUND(AVG(popularity), 2) AS avg_popularity,
               COUNT(*) AS track_count
        FROM tracks
        GROUP BY track_genre
        ORDER BY avg_popularity DESC
    """).df()
    con.close()
    return jsonify(result.to_dict(orient="records"))

@app.route("/api/top-artists")
def top_artists():
    con = get_con()
    result = con.execute("""
        SELECT artists,
               track_genre,
               ROUND(AVG(popularity), 2) AS avg_popularity,
               COUNT(*) AS track_count
        FROM tracks
        GROUP BY artists, track_genre
        ORDER BY avg_popularity DESC
        LIMIT 20
    """).df()
    con.close()
    return jsonify(result.to_dict(orient="records"))

@app.route("/api/duration-loudness")
def duration_loudness():
    con = get_con()
    result = con.execute("""
        SELECT track_genre,
               ROUND(AVG(duration_ms) / 1000, 2) AS avg_duration_sec,
               ROUND(AVG(loudness), 3) AS avg_loudness
        FROM tracks
        GROUP BY track_genre
        ORDER BY avg_duration_sec DESC
    """).df()
    con.close()
    return jsonify(result.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)