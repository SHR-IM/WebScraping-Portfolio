# Python Web Scraping and Exploratory Data Analysis Portfolio

Academic Python exercises covering **data collection, cleaning, exploratory analysis, regression and graph search**. These are historical coursework demonstrations and **not** continuously maintained data services or validated production systems.

## Choose a project

| Project | What it demonstrates | How to inspect |
| --- | --- | --- |
| [Economic Data Extraction & Analysis](EconomicDataExtraction%26Analysis/) | Python requests/lxml scraping, pandas cleaning, exploratory charts, statsmodels OLS | Read the notebook and project README |
| [StackExchange Analysis](StackExchangeAnalysis/) | Scrapy extraction, tags, engagement analysis, user-level OLS | Read the notebook, or run the standalone spider below |
| [Walk the World](WalkTheWorld/) | Wikipedia data extraction and breadth-first search (BFS) | Read the notebook; treat route output as **illustrative**, not travel guidance |

**Portfolio highlight:** The economic indicators project most directly combines the author's economics background with Python data science. StackExchange adds a distinct scraping-and-analysis workflow.

## Setup

Use Python 3.11 or newer:

    python -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt

On Windows, activate using `.venv\Scripts\activate`.

Notebooks can be opened with Jupyter. Their data acquisition code requires network access, and their HTML selectors were developed against historical page structures; current Wikipedia/StackExchange HTML may differ. No external web calls are made when running the offline test suite.

### Scrapy spider

The original project used a **locally hosted 2023 Stack Exchange archive** at 127.0.0.1:8080. That archive is not included here, so we do not claim the original spider is runnable against it without a local copy.

A standalone spider has been provided with explicit URL input:

    scrapy runspider StackExchangeAnalysis/StackExPoliticsSpider.py \
      -a start_url=http://127.0.0.1:8080/politics.stackexchange.com_en_all_2023-11/questions \
      -O stackexchange_questions.json

You must supply a reachable page. For publicly hosted sites, check robots.txt and the site's terms before collecting data. Markup changes may require selector adjustments.

The spider exports question title, URL, excerpt, tags, vote and answer counts, comments, and user data when present. It may contain missing fields where the HTML does not expose them.

### Reproducing the notebooks

- `EconomicDataExtraction&Analysis/EconomicDataExtraction.ipynb` generates `countries_data.csv` from Wikipedia; collecting this dataset requires internet access and the notebook's historical selectors may need adjustments.
- `StackExchangeAnalysis/StackExchangePoliticsSubforumProject.ipynb` references `stackexpoliticdata.csv`. **That dataset is not committed**; provide or regenerate a compatible export before running the analysis cells. Scraped schemas may need mapping before using new exports in that older notebook.
- `WalkTheWorld/WalktheWorld.ipynb` builds an adjacency graph from a Wikipedia article and applies BFS. This does **not** validate real-world pedestrian travel, visas, ferry connections, or current border accessibility.

## Verification

    python -m unittest discover -s tests -v

Offline unit tests use synthetic HTML fixtures and cover spider initialization, pagination, legacy and modern question extraction, vote/answer counts and detail parsing. These tests do not verify current live-site compatibility or reproduce every analysis result.

## Interpretation and limitations

- The OLS analyses describe *associations* in scraped observational data; they cannot establish causal effects of GDP, HDI, user activity, or reputation.
- Wikipedia data varies by update date and source; missing values and changing page HTML can affect results.
- A shortest path in a country adjacency graph minimizes **border crossings**, not walking distance or actual travel feasibility.
- This repository retains the original analysis notebooks as academic records and makes targeted fixes to increase clarity and reproducibility.

*Portfolio maintenance: November 2026.*
