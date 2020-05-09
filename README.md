# All-MPs-and-Lords-Members-Bio-Page-Links

## Category
Web scraping/data collection

## Purpose
Collect URLs from UK Parliament website for all House of Commons MPs and House of Lords Members.

## User needs
A script developed to help our performance analyst run SEO/Performance checks in batches for all Bio pages (1427 URLs) using Lighthouse. Links to bio pages are collected in .csv file.

## Data collected
Pages parsed for URLs
* [URLs to pages for all House of Commons MPs](https://www.parliament.uk/mps-lords-and-offices/mps/)
* [URLs to pages for all Members of the House of Lords](https://www.parliament.uk/mps-lords-and-offices/lords/)

**NOTE: UK Parliament is getting a new website. New page structure means that this scraper will break and will need to be modified in the future**

.csv file contains
- House name (Commons/Lords)
- Name of MP/Lords Member
- Link to Bio Page

## Dependencies
Built with Python 3.6.4 and the following modules
- requests_html
- urllib
- re
- time
- datetime
- csv

## Developed by
Kostas Koutoupis ([@kkoutoup](https://github.com/kkoutoup)) for the Web and Publications Unit (WPU) of the Chambers and Committee Office (CCT), House of Commons
