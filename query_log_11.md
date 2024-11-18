```sql

    SELECT state, 
           party, 
           SUM(CASE WHEN incumbent = true THEN 1 ELSE 0 END) AS incumbent_count, 
           SUM(CASE WHEN incumbent = false THEN 1 ELSE 0 END) AS challenger_count
    FROM election_data
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
    FROM election_data
    GROUP BY state, party
    
```

```response from databricks
Error occurred: [TABLE_OR_VIEW_NOT_FOUND] The table or view `election_data` cannot be found. Verify the spelling and correctness of the schema and catalog.
If you did not qualify the name with a schema, verify the current_schema() output, or qualify the name with the correct schema and catalog.
To tolerate the error on drop use DROP VIEW IF EXISTS or DROP TABLE IF EXISTS. SQLSTATE: 42P01; line 6 pos 9;
'Aggregate ['state, 'party], ['state, 'party, 'SUM(CASE WHEN ('incumbent = true) THEN 1 ELSE 0 END) AS incumbent_count#1647, 'SUM(CASE WHEN ('incumbent = false) THEN 1 ELSE 0 END) AS challenger_count#1648]
+- 'UnresolvedRelation [election_data], [], false

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
| state   | party                  |   incumbent_count |   challenger_count |
|:--------|:-----------------------|------------------:|-------------------:|
| AZ      | D                      |              2646 |               5292 |
| CA      | R                      |             10584 |              29988 |
| LA      | LIB                    |                 0 |                882 |
| MI      | Working Class          |                 0 |               1764 |
| WV      | Mountain               |                 0 |                882 |
| CA      | D                      |             34398 |              14112 |
| OR      | LIB                    |                 0 |                882 |
| AL      | D                      |               882 |               5292 |
| MO      | LIB                    |                 0 |               5292 |
| TX      | R                      |             17640 |              10584 |
| LA      |                        |                 0 |               2646 |
| PA      | R                      |              6174 |               8820 |
| MI      | US Taxpayers           |                 0 |               2646 |
| NJ      |                        |                 0 |               7056 |
| CA      | I                      |                 0 |               1764 |
| NC      | LIB                    |                 0 |               3528 |
| DE      | R                      |                 0 |                882 |
| AL      | R                      |              5292 |                  0 |
| CO      | LIB                    |                 0 |                 72 |
| OH      | LIB                    |                 0 |               3528 |
| WI      | R                      |              3528 |               2646 |
| WI      | D                      |              2646 |               4410 |
| AR      | D                      |                 0 |               3528 |
| NE      | D                      |                 0 |               2646 |
| NE      | R                      |              2646 |                  0 |
| OK      | D                      |                 0 |               4410 |
| OR      |                        |                 0 |               1800 |
| OH      | GRE                    |                 0 |               1764 |
| OK      | I                      |                 0 |                882 |
| SC      | AME                    |                 0 |               2646 |
| TN      | IND                    |                 0 |               4410 |
| MS      | R                      |              1764 |                882 |
| IL      | R                      |              6174 |               9702 |
| OR      | GRE                    |                 0 |                846 |
| IA      | LIB                    |                 0 |                882 |
| MN      | Legal Marijuana Now    |                 0 |                882 |
| MA      | IND                    |                 0 |               1764 |
| AR      | LIB                    |                 0 |               3528 |
| AZ      | G                      |                 0 |               1764 |
| IN      | R                      |              4410 |               3528 |
| TX      | IND                    |                 0 |                882 |
| IL      | GRE                    |                 0 |                882 |
| WY      |                        |                 0 |                882 |
| KY      |                        |                 0 |                882 |
| FL      | R                      |             10584 |               8820 |
| NH      |                        |                 0 |               1692 |
| AK      | R                      |               882 |                  0 |
| MI      |                        |                 0 |               5292 |
| NV      |                        |                 0 |               2646 |
| KS      | R                      |              2646 |                882 |
| MS      | D                      |               882 |               2646 |
| ND      | IND                    |                 0 |                882 |
| NY      | WOF                    |               882 |                  0 |
| WY      | R                      |               882 |                  0 |
| ID      |                        |                 0 |                882 |
| KY      | D                      |               882 |               4410 |
| MS      | REF                    |                 0 |               3528 |
| NJ      | LIB                    |                 0 |                882 |
| ID      | D                      |                 0 |               1764 |
| CT      |                        |                 0 |                882 |
| NJ      | R                      |              2646 |               7938 |
| VT      | D                      |               882 |                  0 |
| WV      | R                      |              1764 |                882 |
| NC      |                        |                 0 |                882 |
| OR      | D                      |              3528 |                882 |
| ME      | R                      |               882 |                882 |
| VT      |                        |                 0 |                882 |
| NV      | D                      |               882 |               2646 |
| MA      | R                      |                 0 |               4410 |
| OH      | R                      |              9702 |               4410 |
| OK      | R                      |              3528 |                882 |
| MD      |                        |                 0 |               2646 |
| MT      | R                      |               882 |                  0 |
| SD      | R                      |                 0 |                882 |
| AK      | D                      |                 0 |                882 |
| MO      |                        |                 0 |               1764 |
| OR      | IPO                    |                 0 |                882 |
| KY      | IND                    |                 0 |               1764 |
| MO      | R                      |              5292 |               1764 |
| MI      | R                      |              7056 |               4410 |
| MD      | R                      |               882 |               6174 |
| WA      | D                      |              5292 |               4410 |
| ME      |                        |                 0 |                882 |
| LA      | I                      |                 0 |               1764 |
| KS      | LIB                    |                 0 |               1764 |
| MN      | R                      |              2646 |               4410 |
| UT      | LIB                    |                 0 |                882 |
| NC      | CON                    |                 0 |                882 |
| PA      | D                      |              4410 |              11466 |
| WI      | DPD                    |                 0 |                882 |
| NM      | LIB                    |                 0 |               1764 |
| WA      | L                      |                 0 |                882 |
| MS      |                        |                 0 |                882 |
| MT      | D                      |                 0 |                882 |
| HI      | D                      |               882 |                882 |
| MI      | D                      |              2646 |               9702 |
| NY      | R                      |              7938 |              10584 |
| VT      | R                      |                 0 |                882 |
| WY      | D                      |                 0 |                882 |
| ND      | R                      |                 0 |                882 |
| NC      | R                      |              7938 |               3528 |
| RI      | D                      |              1764 |                  0 |
| TN      |                        |                 0 |               2646 |
| WA      | R                      |              2646 |               4410 |
| IA      |                        |                 0 |               2646 |
| NY      | Reform Party           |                 0 |                882 |
| MN      | D                      |              1764 |               5292 |
| CT      | R                      |                 0 |               4410 |
| NV      | R                      |               882 |               2646 |
| SC      | R                      |              3528 |               2646 |
| WV      | D                      |                 0 |               2646 |
| KS      | D                      |                 0 |               3528 |
| SD      |                        |                 0 |                882 |
| TN      | D                      |              1764 |               6174 |
| UT      | D                      |                 0 |               3528 |
| NM      | R                      |                 0 |               2646 |
| SC      | CON                    |                 0 |                882 |
| NC      | D                      |              2646 |               7938 |
| NY      | G                      |                 0 |                882 |
| HI      | R                      |                 0 |               1764 |
| MT      | LIB                    |                 0 |                882 |
| VA      | D                      |              3528 |               6174 |
| SC      | D                      |               882 |               5292 |
| AR      | R                      |              3528 |                  0 |
| NY      |                        |                 0 |               4113 |
| MD      | LIB                    |                 0 |               4410 |
| LA      | D                      |               882 |               9702 |
| NM      | D                      |               882 |               1764 |
| PA      | L                      |                 0 |               1764 |
| GA      | D                      |              3528 |               7938 |
| CT      | D                      |              3528 |                882 |
| IL      | IND                    |                 0 |                882 |
| OR      | R                      |               882 |               2682 |
| VA      | LIB                    |                 0 |               1764 |
| CA      | G                      |                 0 |               2646 |
| CO      | L                      |                 0 |                 36 |
| ID      | R                      |               882 |                882 |
| NH      | D                      |               882 |                882 |
| SD      | D                      |                 0 |                882 |
| TN      | R                      |              3528 |               4410 |
| IL      | D                      |              8820 |               7056 |
| IN      | LIB                    |                 0 |                882 |
| ND      | D                      |                 0 |                882 |
| MA      | D                      |              6174 |               1764 |
| TX      |                        |                 0 |               4410 |
| TX      | D                      |              7938 |              23814 |
| CO      | D                      |              1764 |               4410 |
| OH      | D                      |              3528 |              10584 |
| NY      | Women's Equality Party |                 0 |                 36 |
| CT      | GRE                    |                 0 |                882 |
| GA      | R                      |              8820 |               2646 |
| MD      | D                      |              5292 |               1764 |
| NH      | LIB                    |                 0 |                 72 |
| NY      | D                      |             14112 |               9702 |
| NH      | R                      |                 0 |               1764 |
| ME      | D                      |               882 |                882 |
| DE      | D                      |               882 |                  0 |
| IA      | D                      |               882 |               2646 |
| UT      | R                      |              3528 |                  0 |
| FL      | NPA                    |                 0 |               1764 |
| CO      | R                      |              3528 |               2646 |
| CO      |                        |                 0 |               4338 |
| FL      |                        |                 0 |               1764 |
| NY      | REF                    |                 0 |               1764 |
| FL      | D                      |              9702 |              14112 |
| MN      | Independence Party     |                 0 |                882 |
| VA      | R                      |              4410 |               4410 |
| AK      |                        |                 0 |                846 |
| NJ      | D                      |              6174 |               4410 |
| ME      | IND                    |                 0 |                882 |
| WI      | I                      |                 0 |               1764 |
| NJ      | CON                    |                 0 |                882 |
| AZ      | R                      |              3528 |               3528 |
| LA      | R                      |              3573 |                882 |
| TX      | LIB                    |                 0 |              21168 |
| IN      | D                      |              1764 |               6174 |
| VA      | L                      |                 0 |                882 |
| OK      |                        |                 0 |                882 |
| KY      | R                      |              4410 |                882 |
| KY      | LIB                    |                 0 |                882 |
| NY      | GRE                    |                 0 |               2061 |
| SC      | GRE                    |                 0 |                882 |
| RI      | R                      |                 0 |               1764 |
| IA      | R                      |              2646 |                882 |
| MO      | D                      |              1764 |               5292 |
| UT      |                        |                 0 |               1764 |
| HI      |                        |                 0 |                882 |
```

