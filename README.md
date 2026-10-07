# Daniel Jaroszewski

Data Scientist at Wakacje.pl, previously Data Analyst at LPP. I help turn CSV/Excel exports and API data into repeatable reports using Python, SQL and Google Cloud Platform.

For freelance projects, we agree on the sources, output and acceptance checks. You receive a working solution and instructions for the next run. Availability: 5–10 hours per week. Document processing with human review is a second service.

## Selected existing projects

### Multi-source listing research

**Problem:** several sources show overlapping listings, changing prices and incomplete information. Flat Hunter collects listings, keeps their history in SQLite, deduplicates records and presents a ranked shortlist with source evidence in a local web panel.

**Result:** one view for comparing candidates, investigating missing facts and seeing source failures. Python handles collection and ranking; local model-assisted text and photo review supports investigation.

[See the workflow and an illustrative input/output example](case-studies/flat-hunter.md).

**Client application:** monitoring an agreed set of sources, tracking changes and preparing a reviewable shortlist. Personal project; source code and collected data are private.

### Document and reporting automation

[ksiegowy-ai](https://github.com/ahZe667/ksiegowy-ai) is an existing public Python project for structured document parsing and reporting. Its modules cover invoice XML, JPK and bank CSV exports, with a workflow in which a person controls official submissions. This demonstrates the separation of deterministic processing from AI-assisted preparation.

**Client application:** turn a defined document or export format into validated records and a repeatable report.

**Evidence:** [an executed synthetic CSV example](case-studies/document-data.md) shows the existing parser turning an export into normalized records. Public version 0.4.0 also includes local PDF OCR on macOS. This is a personal software project; accounting or tax advisory services are outside my freelance offer.

### Personalized recommendations

[playlist_recommender](https://github.com/ahZe667/playlist_recommender) is a Flask application for generating music recommendations from user ratings. Its documented workflow includes duplicate handling, feature preparation, clustering, positive and negative feedback, and diversity-aware ranking.

**Client application:** prototype a recommendation workflow and make its inputs and results available through a small web interface.

**Project type:** personal recommendation application. Relevant to recommendation prototypes and data science work.

### Documents to a reviewable report

Deal Hunter is a personal tool for researching used IT offers. Its documented pipeline extracts information from native HTML, PDF, XLSX and DOCX, preserves source locations, records price history and produces review reports. Missing information and insufficient evidence remain explicit.

**Client application:** convert a defined set of documents into structured information, with traceability and items that need a person's review.

**Limits:** the repository is private. Scanned documents are flagged for review; OCR is not implemented. Financial calculations are scenarios with explicit assumptions, not evidence of realised investment returns.

## Professional experience

### Data Scientist at Wakacje.pl

Work on data products including recommendation ranking and monitoring, forecasting, conversion modelling and automated reporting. Confirmed contributions include changes to recommendation monitoring and Power BI reporting, forecast data integration and Google Sheets exports, and development and maintenance of conversion-value pipelines connected to advertising workflows.

I also work with customer-return modelling projects. These are contributions to employer-owned team projects.

### Data Analyst at LPP

Prepared e-commerce reports and analyses of sales, inventory, returns, costs and profitability. Worked with data on Google Cloud Platform using SQL and BigQuery, Python and Looker, and analysed GA4 funnels and A/B tests.

## Additional public code

- [Agent Relay](https://github.com/ahZe667/agent-relay): a FastAPI and SQLite coursework project demonstrating authenticated task delivery, leases and retries.
- [Household Chores](https://github.com/ahZe667/household-chores): a Django coursework application for shared household tasks.
- [LeagueTable](https://github.com/ahZe667/leaguetable): a sports scoreboard coursework application.

The examples above are labelled coursework. Employer code and data are not published.

## Contact

[Useme profile](https://useme.com/pl/roles/contractor/daniel-jaroszewski,625497/) · [Upwork profile](https://www.upwork.com/freelancers/~01f870aecc168381a1) · [GitHub](https://github.com/ahZe667)
