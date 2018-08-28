
# Description

&nbsp;

### Log analysis.

Analyze data from the logs of a web service to answer questions such as "What is the most popular page?" and "When was the error rate high?" using advanced SQL queries.


*This is project 3 of the [Udacity Full Stack Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) course.*

&nbsp;


## Dependencies

&nbsp;

| Python3 | PostgreSql | Psycopg2 | Vagrant | VirtualBox |
|:------------:|:------------:|:------------:| :------------:|:------------:|
| [Python 3.5.2](https://www.python.org/downloads/) | [PostgreSql 9.5.13](https://www.postgresql.org) | [Psycopg2 2.7.5](http://initd.org/psycopg/download/) | [Vagrant 2.1.1](https://www.vagrantup.com/) | [VirtualBox 5.2](https://www.virtualbox.org/) |

&nbsp;

## How-to

&nbsp;


- Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)<br>

- Clone this git repository or download it

- From your terminal, run the command `vagrant up`

-  When finished, run `vagrant ssh` to log in to your VM!

- Put the *Log_Analysis* folder into the shared vagrant directory.

- Load the database:
     `psql -d news -f newsdata.sql `

-  Run the *log_analysis.py* from your selected IDE or from the Terminal/Command Prompt.

&nbsp;
