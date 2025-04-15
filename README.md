SEO Rank Tracker
A Flask-based tool to track Google search rankings, store data in CSVs, and analyze trends using Microsoft's Phi-3 model via Ollama. Features a clean UI for single/batch searches, history, LLM analysis, and visualizations.

Features

Scrape Google for rank, title, and URL per keyword.
Batch search with progress tracking.
Store and export ranking history as CSVs.
Analyze ranking trends with Phi-3 (e.g., rank changes, title/URL shifts).
Dashboard with stats (total searches, average rank).
Trends visualization using Chart.js.
Robust error handling for scraping and LLM calls.

Visuals 

![image](https://github.com/user-attachments/assets/81e17d61-93cb-47c3-9265-a28cdfc5963e)


![image](https://github.com/user-attachments/assets/6fd67406-e885-43d6-87dd-5ff3646a1ecc)


![image](https://github.com/user-attachments/assets/2874816b-22f8-459c-afe0-9370e5fee0f8)


![image](https://github.com/user-attachments/assets/686c2127-d613-4b55-be7e-d3d558567e8e)



Project Structure
WebRanking/
├── ranking_data/         # CSVs for keyword rankings
├── search_results/       # Temporary HTML from scraping
├── templates/            # Flask HTML templates
│   ├── dashboard.html
│   ├── index.html
│   └── trends.html
├── app.py                # Main Flask app
├── init_app.py           # Blueprint setup
├── routes.py             # Dashboard/trends routes
├── run.py                # App entry point
└── README.md

Pipeline

Scraping: Selenium scrapes Google (random.uniform(2, 5) sleep), BeautifulSoup parses results.
Storage: CSVs in ranking_data/ (pandas, portalocker for thread safety).
LLM Analysis:
Chunk CSVs (10 records).
Prompt Phi-3 via Ollama for trend analysis.
Retry failed calls (3 attempts, 2s delay).


UI: Flask with Jinja2, Chart.js, Select2; tabs for search, history, analysis.

Technologies

Backend: Python, Flask, Selenium, BeautifulSoup, pandas, requests, retrying.
Frontend: HTML/CSS/JS, Chart.js, Select2, jQuery.
AI: Ollama, Phi-3 Mini (3.8B).
Other: ChromeDriver, Git.

Setup

Clone Repo:git clone https://github.com/Amiradha/AgenticAI_WebRanking
cd webreinvent-seo-tracker


Virtual Environment:python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


Install Dependencies:pip install flask selenium beautifulsoup4 pandas requests retrying portalocker webdriver-manager


Setup Ollama:ollama pull phi3
ollama serve
ollama run phi3

Run App:python run.py

Open http://localhost:5000.

Usage

Single Search: Enter keyword (e.g., "Laravel development company"), view rank.
Batch Search: Input multiple keywords, track progress.
History: View/export past searches.
LLM Analysis: Select keyword, see Phi-3 analysis (e.g., "Rank stable at 15-18").
Dashboard/Trends: View stats and ranking charts.

Future Work

Add database (SQLite).
Cache LLM responses.
Schedule automated searches.
Enhance UI with filters.

Contributing
Fork, branch, commit, and submit a pull request. Report issues on GitHub.
License
MIT License. Phi-3 model under Microsoft’s MIT License.
Author: Amiradha Satsangi Date: April 2025
