# Stack Exchange Politics: Scraping and Analysis

This is a historical academic project exploring question tags, voting, answers, comments, user activity and reputation in a Stack Exchange Politics archive. It combines a **Scrapy spider** with a **pandas/statsmodels notebook** for exploratory analysis and OLS associations.

## Files

- `StackExPoliticsSpider.py` — standalone Scrapy spider. Accepts a question-listing URL at runtime and returns question metadata plus some author details.
- `StackExchangePoliticsSubforumProject.ipynb` — original coursework notebook for data cleaning, plots and regression. It expects a CSV called `stackexpoliticdata.csv`, which is **not included** in this repository.

The unused Scrapy project boilerplate has been removed from the current portfolio version. The standalone spider runs via `scrapy runspider` and does not need a `settings.py`, custom pipeline or item schema module.

## Run the spider

From the repository root, after installing the dependencies:

```bash
scrapy runspider StackExchangeAnalysis/StackExPoliticsSpider.py \\
  -a start_url=http://127.0.0.1:8080/politics.stackexchange.com_en_all_2023-11/questions \\
  -O stackexchange_questions.json
```

The original project used a *locally hosted November 2023 archive* at `127.0.0.1:8080`. That archive is **not supplied**, so this command needs a matching locally served snapshot or another permitted, reachable question-listing URL. For a current public site, follow robots.txt and its terms and check whether HTML selectors need updating.

## Tests

```bash
python -m unittest discover -s tests -v
```

These are **offline HTML-fixture tests** of extraction and pagination, not a live crawl or a rerun of the analysis notebook.

## Interpretation

The project demonstrates scraping, text and numeric cleaning, basic aggregation, visualisation and OLS modelling. Any observed relationship between question activity and reputation is an **association, not a causal effect**. Findings in the original notebook are specific to its historical sample and cannot be assumed to generalise to current Stack Exchange activity.

To rerun the notebook, provide `stackexpoliticdata.csv` with the expected fields. The new spider exports JSON with a related but not identical schema, so some data conversion and adaptation may be needed. Do not claim a complete notebook rerun solely from the working spider.
