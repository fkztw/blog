#/usr/bin/env python3

import json
import os
import pathlib
import re
from collections import defaultdict
from datetime import datetime, timedelta

from python_graphql_client import GraphqlClient


GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

root = pathlib.Path(__file__).resolve().parents[2]
client = GraphqlClient(endpoint="https://api.github.com/graphql")


def make_fetch_tils_query(start_time_str, after_cursor=None):
    query = """
        query {
          viewer {
            repository(name: "m157q.github.io") {
              issues(
                orderBy: {field: CREATED_AT, direction: ASC},
                filterBy: {
                  states: OPEN,
                  since: "START_TIME",
                  createdBy: "M157q"
                },
                first: 100,
                after: AFTER
              )
              {
                pageInfo {
                  hasNextPage
                  endCursor
                }
                nodes {
                  title
                  body
                  createdAt
                  labels(first: 1) {
                    nodes {
                      name
                    }
                  }
                }
              }
            }
          }
        }
    """.replace(
        "START_TIME", start_time_str
    ).replace(
        "AFTER", '"{}"'.format(after_cursor) if after_cursor else "null"
    )

    print(query)
    return query


def fetch_tils(oauth_token, start_time, end_time):
    tils = defaultdict(list)
    has_next_page = True
    after_cursor = None
    start_time_str = start_time.strftime('%Y-%m-%dT%H:%M:%S%z')
    print(f"start_time_str: {start_time_str}")

    while has_next_page:
        data = client.execute(
            query=make_fetch_tils_query(start_time_str, after_cursor),
            headers={"Authorization": "Bearer {}".format(oauth_token)},
        )
        print()
        print(json.dumps(data, indent=4))
        print()

        for til in data["data"]["viewer"]["repository"]["issues"]["nodes"]:
            if datetime.strptime(til["createdAt"], "%Y-%m-%dT%H:%M:%S%z") < start_time:
                continue

            if datetime.strptime(til["createdAt"], "%Y-%m-%dT%H:%M:%S%z") > end_time:
                print(til["title"], til["createdAt"])
                has_next_page = False
                break

            print(len(til["labels"]["nodes"]))
            print(til)
            category = til["labels"]["nodes"][0]["name"]

            # til["body"]
            """
            <url>

            text
            text
            ...
            """
            # Get first line and strip '<' and '>' to get url
            url = til["body"].split('\n')[0].strip()[1:-1]
            # til["body"].split('\n')[1] is an empty string
            text_lines = til["body"].split('\n')[2:]

            tils[category].append(
                {
                    "title": til["title"],
                    "url": url,
                    "text_lines": text_lines,
                }
            )

        has_next_page = data["data"]["viewer"]["repository"]["issues"]["pageInfo"]["hasNextPage"]
        after_cursor = data["data"]["viewer"]["repository"]["issues"]["pageInfo"]["endCursor"]
    return tils


if __name__ == "__main__":
    # Make sure running this script at anytime of this week
    # will get the same result because it gathers issues only from "last week"
    # No matter what time you execute this script at this week.
    timezone_str = "+0800"
    timezone = datetime.strptime(timezone_str, '%z').tzinfo
    now = datetime.now(tz=timezone)

    target_year, target_week, _ = (now - timedelta(days=7)).isocalendar()
    start_time = datetime.strptime(
        '{}-{}-1 {}'.format(target_year, target_week, timezone_str),
        '%G-%V-%u %z',
    )
    end_time = start_time + timedelta(days=7)
    print(f"now: {now}")
    print(f"start_time: {start_time}")
    print(f"end_time: {end_time}")
    print()

    post = {}
    post['title'] = "Y{}W{}".format(
        start_time.isocalendar()[0],
        start_time.isocalendar()[1],
    )
    post['slug'] = post['title'].lower()
    post['date'] = now.strftime('%Y-%m-%d %H:%M:%S')
    post['authors'] = 'M157q'
    post['category'] = 'Weekly'
    post['summary'] = "Collections of {} ({} ~ {})".format(
        post['title'],
        start_time.strftime('%Y-%m-%d %a %H:%M:%S%z'),
        end_time.strftime('%Y-%m-%d %a %H:%M:%S%z'),
    )

    # Fetch TILs from GitHub
    tils = fetch_tils(GITHUB_TOKEN, start_time, end_time)
    print()
    print(f"len of tils: {len(tils)}")
    print(f"tils: {tils}")
    print()

    post['tags'] = ', '.join(sorted(tils.keys()))

    post['content'] = ''
    for tag, post_data in sorted(tils.items()):
        post['content'] += f"## {tag}  \n"

        for post_datum in post_data:
            if post_datum['title'] and post_datum['url']:
                post['content'] += '- [{}]({})  \n'.format(
                    post_datum['title'], post_datum['url'],
                )
            if post_datum['text_lines']:
                for line in post_datum['text_lines']:
                    if line and post_datum['title'] and post_datum['url']:
                        post['content'] += (
                            '{}  \n'
                        ).format(line.strip())
                post['content'] += "\n"
        post['content'] += "---\n\n"

    # Write a new blog post
    new_post_filename = f"{post['slug']}.md"
    new_weekly_post_path = root / "content" / "posts" / new_post_filename
    post_template = """Title: {title}
Slug: {slug}
Date: {date}
Authors: {authors}
Category: {category}
Tags: {tags}
Summary: {summary}


{content}
"""

    with open(new_weekly_post_path, 'w') as f:
        f.write(post_template.format(**post))
