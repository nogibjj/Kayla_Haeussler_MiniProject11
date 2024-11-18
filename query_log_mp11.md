The operation is load data

The truncated output is: 

|    | forecastdate   | state   |   district |   special | candidate          | party   | incumbent   | model   |   win_probability |   voteshare |   p10_voteshare |   p90_voteshare |
|---:|:---------------|:--------|-----------:|----------:|:-------------------|:--------|:------------|:--------|------------------:|------------:|----------------:|----------------:|
|  0 | 2018-08-01     | AK      |          1 |       nan | Don Young          | R       | True        | classic |            0.7185 |       49.35 |           43.04 |           55.59 |
|  1 | 2018-08-01     | AK      |          1 |       nan | Alyse S. Galvin    | D       | False       | classic |            0.2815 |       44.11 |           37.77 |           50.39 |
|  2 | 2018-08-01     | AK      |          1 |       nan | Others             | nan     | False       | classic |            0      |        6.54 |            2.6  |           11.17 |
|  3 | 2018-08-01     | AL      |          1 |       nan | Bradley Byrne      | R       | True        | classic |            0.9993 |       64.9  |           59.71 |           69.94 |
|  4 | 2018-08-01     | AL      |          1 |       nan | Robert Kennedy Jr. | D       | False       | classic |            0.0007 |       35.1  |           30.06 |           40.29 |
|  5 | 2018-08-01     | AL      |          2 |       nan | Martha Roby        | R       | True        | classic |            0.9729 |       58.23 |           52.84 |           63.54 |
|  6 | 2018-08-01     | AL      |          2 |       nan | Tabitha Isner      | D       | False       | classic |            0.0271 |       41.77 |           36.46 |           47.16 |
|  7 | 2018-08-01     | AL      |          3 |       nan | Mike Rogers        | R       | True        | classic |            0.9972 |       62.27 |           57.14 |           67.42 |
|  8 | 2018-08-01     | AL      |          3 |       nan | Mallory Hagan      | D       | False       | classic |            0.0028 |       37.73 |           32.58 |           42.86 |
|  9 | 2018-08-01     | AL      |          4 |       nan | Robert B. Aderholt | R       | True        | classic |            1      |       76.32 |           71.05 |           81.54 |

```sql

    SELECT state, 
           party, 
           SUM(CASE WHEN incumbent = true THEN 1 ELSE 0 END) AS incumbent_count, 
           SUM(CASE WHEN incumbent = false THEN 1 ELSE 0 END) AS challenger_count
    FROM ids706_data_engineering.default.keh119_housedistricts
    GROUP BY state, party
    
```

```response from databricks
Query received, executing next...
```

```sql

    SELECT state, 
           party, 
           SUM(CASE WHEN incumbent = true THEN 1 ELSE 0 END) AS incumbent_count, 
           SUM(CASE WHEN incumbent = false THEN 1 ELSE 0 END) AS challenger_count
    FROM ids706_data_engineering.default.keh119_housedistricts
    GROUP BY state, party
    
```

```response from databricks
Error occurred: name 'spark' is not defined
```

The operation is load data

The truncated output is: 

|    | forecastdate   | state   |   district |   special | candidate          | party   | incumbent   | model   |   win_probability |   voteshare |   p10_voteshare |   p90_voteshare |
|---:|:---------------|:--------|-----------:|----------:|:-------------------|:--------|:------------|:--------|------------------:|------------:|----------------:|----------------:|
|  0 | 2018-08-01     | AK      |          1 |       nan | Don Young          | R       | True        | classic |            0.7185 |       49.35 |           43.04 |           55.59 |
|  1 | 2018-08-01     | AK      |          1 |       nan | Alyse S. Galvin    | D       | False       | classic |            0.2815 |       44.11 |           37.77 |           50.39 |
|  2 | 2018-08-01     | AK      |          1 |       nan | Others             | nan     | False       | classic |            0      |        6.54 |            2.6  |           11.17 |
|  3 | 2018-08-01     | AL      |          1 |       nan | Bradley Byrne      | R       | True        | classic |            0.9993 |       64.9  |           59.71 |           69.94 |
|  4 | 2018-08-01     | AL      |          1 |       nan | Robert Kennedy Jr. | D       | False       | classic |            0.0007 |       35.1  |           30.06 |           40.29 |
|  5 | 2018-08-01     | AL      |          2 |       nan | Martha Roby        | R       | True        | classic |            0.9729 |       58.23 |           52.84 |           63.54 |
|  6 | 2018-08-01     | AL      |          2 |       nan | Tabitha Isner      | D       | False       | classic |            0.0271 |       41.77 |           36.46 |           47.16 |
|  7 | 2018-08-01     | AL      |          3 |       nan | Mike Rogers        | R       | True        | classic |            0.9972 |       62.27 |           57.14 |           67.42 |
|  8 | 2018-08-01     | AL      |          3 |       nan | Mallory Hagan      | D       | False       | classic |            0.0028 |       37.73 |           32.58 |           42.86 |
|  9 | 2018-08-01     | AL      |          4 |       nan | Robert B. Aderholt | R       | True        | classic |            1      |       76.32 |           71.05 |           81.54 |

```sql

    SELECT state, 
           party, 
           SUM(CASE WHEN incumbent = true THEN 1 ELSE 0 END) AS incumbent_count, 
           SUM(CASE WHEN incumbent = false THEN 1 ELSE 0 END) AS challenger_count
    FROM ids706_data_engineering.default.keh119_housedistricts
    GROUP BY state, party
    
```

```response from databricks
Query received, executing next...
```

```sql

    SELECT state, 
           party, 
           SUM(CASE WHEN incumbent = true THEN 1 ELSE 0 END) AS incumbent_count, 
           SUM(CASE WHEN incumbent = false THEN 1 ELSE 0 END) AS challenger_count
    FROM ids706_data_engineering.default.keh119_housedistricts
    GROUP BY state, party
    
```

```response from databricks
Error occurred: name 'spark' is not defined
```

The operation is load data

The truncated output is: 

|    | forecastdate   | state   |   district |   special | candidate          | party   | incumbent   | model   |   win_probability |   voteshare |   p10_voteshare |   p90_voteshare |
|---:|:---------------|:--------|-----------:|----------:|:-------------------|:--------|:------------|:--------|------------------:|------------:|----------------:|----------------:|
|  0 | 2018-08-01     | AK      |          1 |       nan | Don Young          | R       | True        | classic |            0.7185 |       49.35 |           43.04 |           55.59 |
|  1 | 2018-08-01     | AK      |          1 |       nan | Alyse S. Galvin    | D       | False       | classic |            0.2815 |       44.11 |           37.77 |           50.39 |
|  2 | 2018-08-01     | AK      |          1 |       nan | Others             | nan     | False       | classic |            0      |        6.54 |            2.6  |           11.17 |
|  3 | 2018-08-01     | AL      |          1 |       nan | Bradley Byrne      | R       | True        | classic |            0.9993 |       64.9  |           59.71 |           69.94 |
|  4 | 2018-08-01     | AL      |          1 |       nan | Robert Kennedy Jr. | D       | False       | classic |            0.0007 |       35.1  |           30.06 |           40.29 |
|  5 | 2018-08-01     | AL      |          2 |       nan | Martha Roby        | R       | True        | classic |            0.9729 |       58.23 |           52.84 |           63.54 |
|  6 | 2018-08-01     | AL      |          2 |       nan | Tabitha Isner      | D       | False       | classic |            0.0271 |       41.77 |           36.46 |           47.16 |
|  7 | 2018-08-01     | AL      |          3 |       nan | Mike Rogers        | R       | True        | classic |            0.9972 |       62.27 |           57.14 |           67.42 |
|  8 | 2018-08-01     | AL      |          3 |       nan | Mallory Hagan      | D       | False       | classic |            0.0028 |       37.73 |           32.58 |           42.86 |
|  9 | 2018-08-01     | AL      |          4 |       nan | Robert B. Aderholt | R       | True        | classic |            1      |       76.32 |           71.05 |           81.54 |

```sql

    SELECT state, 
           party, 
           SUM(CASE WHEN incumbent = true THEN 1 ELSE 0 END) AS incumbent_count, 
           SUM(CASE WHEN incumbent = false THEN 1 ELSE 0 END) AS challenger_count
    FROM ids706_data_engineering.default.keh119_housedistricts
    GROUP BY state, party
    
```

```response from databricks
Query received, executing next...
```

```sql

    SELECT state, 
           party, 
           SUM(CASE WHEN incumbent = true THEN 1 ELSE 0 END) AS incumbent_count, 
           SUM(CASE WHEN incumbent = false THEN 1 ELSE 0 END) AS challenger_count
    FROM ids706_data_engineering.default.keh119_housedistricts
    GROUP BY state, party
    
```

```response from databricks
Error occurred: name 'spark' is not defined
```

The operation is load data

The truncated output is: 

|    | forecastdate   | state   |   district |   special | candidate          | party   | incumbent   | model   |   win_probability |   voteshare |   p10_voteshare |   p90_voteshare |
|---:|:---------------|:--------|-----------:|----------:|:-------------------|:--------|:------------|:--------|------------------:|------------:|----------------:|----------------:|
|  0 | 2018-08-01     | AK      |          1 |       nan | Don Young          | R       | True        | classic |            0.7185 |       49.35 |           43.04 |           55.59 |
|  1 | 2018-08-01     | AK      |          1 |       nan | Alyse S. Galvin    | D       | False       | classic |            0.2815 |       44.11 |           37.77 |           50.39 |
|  2 | 2018-08-01     | AK      |          1 |       nan | Others             | nan     | False       | classic |            0      |        6.54 |            2.6  |           11.17 |
|  3 | 2018-08-01     | AL      |          1 |       nan | Bradley Byrne      | R       | True        | classic |            0.9993 |       64.9  |           59.71 |           69.94 |
|  4 | 2018-08-01     | AL      |          1 |       nan | Robert Kennedy Jr. | D       | False       | classic |            0.0007 |       35.1  |           30.06 |           40.29 |
|  5 | 2018-08-01     | AL      |          2 |       nan | Martha Roby        | R       | True        | classic |            0.9729 |       58.23 |           52.84 |           63.54 |
|  6 | 2018-08-01     | AL      |          2 |       nan | Tabitha Isner      | D       | False       | classic |            0.0271 |       41.77 |           36.46 |           47.16 |
|  7 | 2018-08-01     | AL      |          3 |       nan | Mike Rogers        | R       | True        | classic |            0.9972 |       62.27 |           57.14 |           67.42 |
|  8 | 2018-08-01     | AL      |          3 |       nan | Mallory Hagan      | D       | False       | classic |            0.0028 |       37.73 |           32.58 |           42.86 |
|  9 | 2018-08-01     | AL      |          4 |       nan | Robert B. Aderholt | R       | True        | classic |            1      |       76.32 |           71.05 |           81.54 |

```sql

    SELECT state, 
           party, 
           SUM(CASE WHEN incumbent = true THEN 1 ELSE 0 END) AS incumbent_count, 
           SUM(CASE WHEN incumbent = false THEN 1 ELSE 0 END) AS challenger_count
    FROM ids706_data_engineering.default.keh119_housedistricts
    GROUP BY state, party
    
```

```response from databricks
Query received, executing next...
```

```sql

    SELECT state, 
           party, 
           SUM(CASE WHEN incumbent = true THEN 1 ELSE 0 END) AS incumbent_count, 
           SUM(CASE WHEN incumbent = false THEN 1 ELSE 0 END) AS challenger_count
    FROM ids706_data_engineering.default.keh119_housedistricts
    GROUP BY state, party
    
```

```response from databricks
Error occurred: name 'spark' is not defined
```

The operation is load data

The truncated output is: 

|    | forecastdate   | state   |   district |   special | candidate          | party   | incumbent   | model   |   win_probability |   voteshare |   p10_voteshare |   p90_voteshare |
|---:|:---------------|:--------|-----------:|----------:|:-------------------|:--------|:------------|:--------|------------------:|------------:|----------------:|----------------:|
|  0 | 2018-08-01     | AK      |          1 |       nan | Don Young          | R       | True        | classic |            0.7185 |       49.35 |           43.04 |           55.59 |
|  1 | 2018-08-01     | AK      |          1 |       nan | Alyse S. Galvin    | D       | False       | classic |            0.2815 |       44.11 |           37.77 |           50.39 |
|  2 | 2018-08-01     | AK      |          1 |       nan | Others             | nan     | False       | classic |            0      |        6.54 |            2.6  |           11.17 |
|  3 | 2018-08-01     | AL      |          1 |       nan | Bradley Byrne      | R       | True        | classic |            0.9993 |       64.9  |           59.71 |           69.94 |
|  4 | 2018-08-01     | AL      |          1 |       nan | Robert Kennedy Jr. | D       | False       | classic |            0.0007 |       35.1  |           30.06 |           40.29 |
|  5 | 2018-08-01     | AL      |          2 |       nan | Martha Roby        | R       | True        | classic |            0.9729 |       58.23 |           52.84 |           63.54 |
|  6 | 2018-08-01     | AL      |          2 |       nan | Tabitha Isner      | D       | False       | classic |            0.0271 |       41.77 |           36.46 |           47.16 |
|  7 | 2018-08-01     | AL      |          3 |       nan | Mike Rogers        | R       | True        | classic |            0.9972 |       62.27 |           57.14 |           67.42 |
|  8 | 2018-08-01     | AL      |          3 |       nan | Mallory Hagan      | D       | False       | classic |            0.0028 |       37.73 |           32.58 |           42.86 |
|  9 | 2018-08-01     | AL      |          4 |       nan | Robert B. Aderholt | R       | True        | classic |            1      |       76.32 |           71.05 |           81.54 |

```sql

    SELECT state, 
           party, 
           SUM(CASE WHEN incumbent = true THEN 1 ELSE 0 END) AS incumbent_count, 
           SUM(CASE WHEN incumbent = false THEN 1 ELSE 0 END) AS challenger_count
    FROM ids706_data_engineering.default.keh119_housedistricts
    GROUP BY state, party
    
```

```response from databricks
Query received, executing next...
```

```sql

    SELECT state, 
           party, 
           SUM(CASE WHEN incumbent = true THEN 1 ELSE 0 END) AS incumbent_count, 
           SUM(CASE WHEN incumbent = false THEN 1 ELSE 0 END) AS challenger_count
    FROM ids706_data_engineering.default.keh119_housedistricts
    GROUP BY state, party
    
```

```response from databricks
Error occurred: name 'spark' is not defined
```

The operation is load data

The truncated output is: 

|    | forecastdate   | state   |   district |   special | candidate          | party   | incumbent   | model   |   win_probability |   voteshare |   p10_voteshare |   p90_voteshare |
|---:|:---------------|:--------|-----------:|----------:|:-------------------|:--------|:------------|:--------|------------------:|------------:|----------------:|----------------:|
|  0 | 2018-08-01     | AK      |          1 |       nan | Don Young          | R       | True        | classic |            0.7185 |       49.35 |           43.04 |           55.59 |
|  1 | 2018-08-01     | AK      |          1 |       nan | Alyse S. Galvin    | D       | False       | classic |            0.2815 |       44.11 |           37.77 |           50.39 |
|  2 | 2018-08-01     | AK      |          1 |       nan | Others             | nan     | False       | classic |            0      |        6.54 |            2.6  |           11.17 |
|  3 | 2018-08-01     | AL      |          1 |       nan | Bradley Byrne      | R       | True        | classic |            0.9993 |       64.9  |           59.71 |           69.94 |
|  4 | 2018-08-01     | AL      |          1 |       nan | Robert Kennedy Jr. | D       | False       | classic |            0.0007 |       35.1  |           30.06 |           40.29 |
|  5 | 2018-08-01     | AL      |          2 |       nan | Martha Roby        | R       | True        | classic |            0.9729 |       58.23 |           52.84 |           63.54 |
|  6 | 2018-08-01     | AL      |          2 |       nan | Tabitha Isner      | D       | False       | classic |            0.0271 |       41.77 |           36.46 |           47.16 |
|  7 | 2018-08-01     | AL      |          3 |       nan | Mike Rogers        | R       | True        | classic |            0.9972 |       62.27 |           57.14 |           67.42 |
|  8 | 2018-08-01     | AL      |          3 |       nan | Mallory Hagan      | D       | False       | classic |            0.0028 |       37.73 |           32.58 |           42.86 |
|  9 | 2018-08-01     | AL      |          4 |       nan | Robert B. Aderholt | R       | True        | classic |            1      |       76.32 |           71.05 |           81.54 |

```sql

    SELECT state, 
           party, 
           SUM(CASE WHEN incumbent = true THEN 1 ELSE 0 END) AS incumbent_count, 
           SUM(CASE WHEN incumbent = false THEN 1 ELSE 0 END) AS challenger_count
    FROM ids706_data_engineering.default.keh119_housedistricts
    GROUP BY state, party
    
```

```response from databricks
Query received, executing next...
```

```sql

    SELECT state, 
           party, 
           SUM(CASE WHEN incumbent = true THEN 1 ELSE 0 END) AS incumbent_count, 
           SUM(CASE WHEN incumbent = false THEN 1 ELSE 0 END) AS challenger_count
    FROM ids706_data_engineering.default.keh119_housedistricts
    GROUP BY state, party
    
```

```response from databricks
Error occurred: name 'spark' is not defined
```

