# Engineering Intelligence System

## Overview
This system generates structured weekly engineering insights by combining data from multiple sources (Git, work items, spreadsheets) and using AI for summarization.

## Problem
Engineering managers spend significant time manually collecting and summarizing fragmented data across tools.

## Solution
A lightweight AI-assisted system that:
- Ingests engineering activity data
- Computes key delivery metrics
- Generates structured summaries using LLMs
- Validates outputs with evidence-backed guardrails

## Features
- Multi-source data ingestion (Git, Excel/CSV, work items)
- Deterministic metric computation
- AI-generated summaries (structured JSON)
- Validation layer to reduce hallucinations
- Markdown + email report generation
- Historical tracking for trend analysis

## Tech Stack
- Python
- OpenAI API
- Pandas
- SQLite
- Pydantic

## Run
```bash
python src/main.py
