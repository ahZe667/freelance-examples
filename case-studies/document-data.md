# Document data — export to normalized records

**Personal project · existing ksiegowy-ai parser · synthetic data**

An export can contain localized decimal separators, headings and inconsistent spacing. The existing `mbank` parser in [ksiegowy-ai](https://github.com/ahZe667/ksiegowy-ai) reads a defined bank CSV format and produces dated, normalized transaction records.

## Input

[Download the synthetic input](document-data/input.csv). It contains three invented transactions, no account numbers and no personal identifiers.

## Executed output

[See the generated records](document-data/output.json). The demonstration executes the existing public parser, rather than asking a model to invent values. The verification notes record the source commit and the checks performed.

## Client application

Turn a specified export format into structured data that can feed a repeatable report. A first milestone defines the columns, amount/date conventions and expected rows, then checks the result against a sample.

## Boundaries

This example covers CSV parsing, not scanned invoice extraction. The current parser skips rows that do not match its date/amount pattern; a client workflow must separately account for rejected rows. It does not demonstrate complete reconciliation or accuracy across arbitrary formats. The public project also has macOS PDF OCR, whose transcripts require review against the original.
