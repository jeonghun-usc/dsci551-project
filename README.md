# Music Trend Analytics Dashboard
**DSCI 551 Course Project — Spring 2026**
Jeong Hun Lee | USC ID: 1240-693-517

A web-based analytics dashboard that explores audio patterns across music genres using the Spotify Tracks Dataset. The backend is powered by DuckDB, an embedded analytical database that uses columnar storage and vectorized execution to run aggregation queries efficiently.

---

## Project Structure

```
dsci551_project/
├── app.py                        # Flask backend with API endpoints
├── index.html                    # Frontend dashboard (Chart.js)
├── Spotify_music_analytics.ipynb # Data loading and exploration notebook
├── dataset.csv                   # Spotify Tracks Dataset (114,000 rows)
├── music.db                      # DuckDB database file (auto-generated)
└── README.md                     # This file
```

---

## Requirements

- Python 3.9 or higher (tested on Python 3.13)
- Anaconda or Miniconda (recommended)

---

## Environment Setup

### Step 1 — Create and activate a conda environment

```bash
conda create -n dsci551 python=3.13 -y
conda activate dsci551
```

### Step 2 — Install dependencies

```bash
pip install duckdb flask pandas
```

---

## Dataset Setup

The dataset used is the **Spotify Tracks Dataset** from Kaggle (~114,000 tracks, 21 columns).

The file `dataset.csv` is included in this repository. No additional download is needed.

If you prefer to download it directly from Kaggle:
1. Go to: https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset
2. Download and unzip the file
3. Place `dataset.csv` in the project root directory

---

## Loading the Data into DuckDB

Before running the app, load the dataset into DuckDB by running the Jupyter notebook:

```bash
jupyter lab
```

Open `Spotify_music_analytics.ipynb` and run the first cell. This creates `music.db` with the `tracks` table loaded from `dataset.csv`.

Alternatively, you can run this directly in Python:

```python
import duckdb
con = duckdb.connect("music.db")
con.execute("""
    CREATE TABLE IF NOT EXISTS tracks AS
    SELECT * FROM read_csv_auto('dataset.csv')
""")
con.close()
```

---

## Running the Application

Make sure you are in the project directory and the conda environment is active:

```bash
conda activate dsci551
cd dsci551_project
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

The dashboard will load with four tabs:
- **Audio Features** — average energy and danceability by genre
- **Genre Popularity** — genres ranked by average popularity score
- **Top Artists** — top 20 artists by average popularity
- **Duration & Loudness** — average track duration and loudness by genre

---

## Secret Keys and Credentials

This project does not use any secret keys, API keys, or external credentials. The application runs entirely locally using DuckDB and Flask with no external service dependencies.

---

## Reproducing Results

1. Clone the repository
2. Set up the conda environment and install dependencies (see above)
3. Load the dataset into DuckDB using the notebook or the Python snippet above
4. Run `python app.py`
5. Open `http://127.0.0.1:5000` in your browser

All query results are computed live from `music.db` on each page load. Results are deterministic and will match the charts shown in the project report.

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Database | DuckDB 0.10 |
| Backend | Python, Flask |
| Frontend | HTML, JavaScript, Chart.js |
| Data | Spotify Tracks Dataset (Kaggle) |

---

## References

1. Raasveldt, M., & Muehleisen, H. (2019). DuckDB: an embeddable analytical database. ACM SIGMOD 2019. https://doi.org/10.1145/3299869.3320212
2. DuckDB Documentation. Internals Overview. https://duckdb.org/docs/internals/overview
3. Maharjan, A. (2023). Spotify Tracks Dataset. Kaggle. https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset
