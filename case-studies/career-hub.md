# Career Hub — source aggregation and preference learning

**Personal project · Python · SQLite · local web application**

## Problem and workflow

Freelance assignments and employment offers arrive from several portals. Career Hub
collects them into separate inbox views, keeps source evidence and lets the owner
record decisions against the exact source snapshot.

![Workflow overview](../portfolio_assets/career-hub.png)

The application distinguishes verified source identities from unverified observations,
preserves history and quarantines reviewed inconsistencies. Genuine owner ratings
train separate freelance and employment preference models.

Activation depends on temporal validation and sufficient labelled data. Until validation
passes, the application uses newest-first ordering. Model scores are not probabilities
or evidence of improved matching quality.

The application also maintains versioned career materials and application packages.
Ratings and document preparation do not submit applications.

## Relevant client application

Build a review inbox for multiple agreed sources, preserve evidence, collect feedback
and evaluate whether a learned ordering improves on the agreed baseline.

## Evidence and limits

The project README and preference-validation documentation were reviewed on 2026-10-22.
This describes implemented workflow and guards, not measured recommendation quality.
The illustration is explanatory. The private application, live offers, documents,
account sessions and runtime database are not part of this public portfolio.
