# Quicklinks

## Repositories
* Repositories: https://github.com/westurner?tab=repositories
* Repositories: https://github.com/search?l=&q=user%3Awesturner&ref=advsearch&type=Repositories&utf8=%E2%9C%93

## Activity

* Activity: https://github.com/westurner?tab=activity
* Contributions: Past Month: https://github.com/westurner?tab=contributions&period=monthly
* Contributions: Past Week: https://github.com/westurner?tab=contributions&period=weekly
* Mentions: https://www.google.com/search?q=site%3Agithub.com+"%40westurner"

## Pull Requests

* Pull Requests (Open): https://github.com/dashboard/pulls?direction=desc&page=1&sort=created&state=open
* Pull Requests (Closed): https://github.com/dashboard/pulls?direction=desc&page=1&sort=created&state=closed

## Issues

* Issues (Open): https://github.com/dashboard/issues?direction=desc&page=1&repos=true&sort=created&state=open
* Issues (Closed): https://github.com/dashboard/issues?direction=desc&page=1&repos=true&sort=created&state=closed
* Issues: https://github.com/search?l=&q=user%3Awesturner&ref=advsearch&type=Issues&utf8=%E2%9C%93
* Issue Mentions: https://github.com/search?q=mentions%3Awesturner&ref=searchresults&type=Issues&utf8=%E2%9C%93

## Archive

* http://www.githubarchive.org/
* https://github.com/igrigorik/githubarchive.org/tree/master/bigquery
* https://github.com/nikitos3000/congruence/tree/master/history
* https://bigquery.cloud.google.com/ (project:githubarchive)

### My Activity

```sql
SELECT actor, repository_url, created_at, payload_action, url, type
FROM [githubarchive:github.timeline]
WHERE
  actor=="westurner"
LIMIT 1000
```

### My Activity (-WatchEvent)

```sql
SELECT actor, repository_url, created_at, payload_action, url, type
FROM [githubarchive:github.timeline]
WHERE
  actor=="westurner"
  and
  type!="WatchEvent"
ORDER BY created_at
LIMIT 1000
```

### My Activity (Starred / Started Following)

```sql
SELECT repository_url, created_at
FROM [githubarchive:github.timeline]
WHERE
  actor=="westurner"
  AND
  payload_action=="started"
ORDER BY created_at
LIMIT 500
```