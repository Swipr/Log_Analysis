
# Description
---
&nbsp;

### Log analysis.
*This is project 3 of the [Udacity Full Stack Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) course.*

&nbsp;


## Dependencies
---
&nbsp;

| *Required* | *Required* | Optional |
|:------------:|:------------:|:------------:|
| [Python 3.5.2](https://www.python.org/downloads/) | [PostgreSql 9.5.13](https://www.postgresql.org) | [Psycopg2 2.7.5](http://initd.org/psycopg/download/) |
&nbsp;
## How-to
---
&nbsp;

 - Clone this git repository or download it
-  Create views in the given order then run the *log_analysis.py* from your SELECTed IDE or from the Terminal/Command Prompt.

&nbsp;
### Create views:
```sql
CREATE VIEW all_code AS
SELECT date(log.time),count(log.status) AS all_status_code
FROM log
GROUP BY date(log.time)
ORDER BY all_status_code DESC;
```
```sql
CREATE VIEW most_errors AS
SELECT date(log.time),count(log.status) AS errors
FROM log
where log.status = '404 NOT FOUND'
GROUP BY date(log.time)
ORDER BY errors DESC;
```
```sql
CREATE VIEW error_perc AS
SELECT all_code.date,
 round(100*most_errors.errors::numeric/all_code.all_status_code::numeric,2)
 AS error_final
FROM all_code, most_errors
where most_errors.date = all_code.date
ORDER BY error_final DESC;
```
&nbsp;
