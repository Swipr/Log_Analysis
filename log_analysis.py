#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def main():
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()

    '''Execute/load the view statements.'''
    create_views = open("create_views.sql").read()
    c.execute(create_views)

    '''Return the three most popular articles of all time.'''

    pop_articles = '''
            select articles.title, count(log.path) as views
            from articles, log
            where log.path = concat('/article/', articles.slug)
            group by articles.title
            order by views desc
            limit 3;
            '''
    c.execute(pop_articles)
    print("1. What are the most popular three articles of all time?" + "\n")
    for (title, views) in c.fetchall():
        print(title + " -- " + str(views) + " views")
    print("\n" + "\n")

    '''Return the most popular article authors of all time.'''

    pop_authors = '''
            select authors.name, count(log.path) as views
            from articles, log, authors
            where log.path = concat('/article/', articles.slug)
             and articles.author = authors.id
            group by authors.name
            order by views desc;
            '''
    c.execute(pop_authors)
    print("2. Who are the most popular article authors of all time?" + "\n")
    for (name, views) in c.fetchall():
        print(name + " -- " + str(views) + " views")
    print("\n" + "\n")

    '''Return on which days did more than 1% of requests lead to errors.'''

    pop_authors = '''
            select to_char(date:: DATE, 'Mon dd, yyyy') as date, error_final
            from error_perc
            where error_final > 1.0
            order by error_final desc;
            '''
    c.execute(pop_authors)
    print("3. On which days "
          "did more than 1% of requests lead to errors?" + "\n")
    for (date, error_final) in c.fetchall():
        print(date + " -- " + str(error_final) + "% errors")

    db.close()


if __name__ == "__main__":
    main()
