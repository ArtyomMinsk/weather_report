# Weather Report

## Description

Create a Python application that will pull data from multiple Weather Underground API endpoints and present a weather report to the user.

## Files

The `endpoints` directory contains the following files:

  - `weater.py` - Main file with imported endpoints
  - `conditions.py` - Current conditions at that location
  - `forecast.py` - 10 day forecast for that location
  - `astronomy.py` - Sunrise and sunset times
  - `alerts.py` - Any current weather alerts
  - `hurricanes.py` - A list of all active hurricanes (anywhere)

`requirements.txt` - list of environment requirements

## Motivation

The motivation of this project is to:

- Understand the purpose and structure of Web APIs
- Understand JSON structure
- Be able to access an API using a token
- Be able to make HTTP requests via requests
- Be able to pull and merge information from multiple API endpoints
- Be able to write tests that mock API responses

## Special Instructions

User must import the following libraries:

- requests
- requests-mock
