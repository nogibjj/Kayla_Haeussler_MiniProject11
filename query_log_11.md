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
| AZ      | D                      |              3528 |               7056 |
| CA      | R                      |             14112 |              39984 |
| LA      | LIB                    |                 0 |               1176 |
| MI      | Working Class          |                 0 |               2352 |
| WV      | Mountain               |                 0 |               1176 |
| CA      | D                      |             45864 |              18816 |
| OR      | LIB                    |                 0 |               1176 |
| AL      | D                      |              1176 |               7056 |
| MO      | LIB                    |                 0 |               7056 |
| TX      | R                      |             23520 |              14112 |
| LA      |                        |                 0 |               3528 |
| PA      | R                      |              8232 |              11760 |
| MI      | US Taxpayers           |                 0 |               3528 |
| NJ      |                        |                 0 |               9408 |
| CA      | I                      |                 0 |               2352 |
| NC      | LIB                    |                 0 |               4704 |
| DE      | R                      |                 0 |               1176 |
| AL      | R                      |              7056 |                  0 |
| CO      | LIB                    |                 0 |                 96 |
| OH      | LIB                    |                 0 |               4704 |
| WI      | R                      |              4704 |               3528 |
| WI      | D                      |              3528 |               5880 |
| AR      | D                      |                 0 |               4704 |
| NE      | D                      |                 0 |               3528 |
| NE      | R                      |              3528 |                  0 |
| OK      | D                      |                 0 |               5880 |
| OR      |                        |                 0 |               2400 |
| OH      | GRE                    |                 0 |               2352 |
| OK      | I                      |                 0 |               1176 |
| SC      | AME                    |                 0 |               3528 |
| TN      | IND                    |                 0 |               5880 |
| MS      | R                      |              2352 |               1176 |
| IL      | R                      |              8232 |              12936 |
| OR      | GRE                    |                 0 |               1128 |
| IA      | LIB                    |                 0 |               1176 |
| MN      | Legal Marijuana Now    |                 0 |               1176 |
| MA      | IND                    |                 0 |               2352 |
| AR      | LIB                    |                 0 |               4704 |
| AZ      | G                      |                 0 |               2352 |
| IN      | R                      |              5880 |               4704 |
| TX      | IND                    |                 0 |               1176 |
| IL      | GRE                    |                 0 |               1176 |
| WY      |                        |                 0 |               1176 |
| KY      |                        |                 0 |               1176 |
| FL      | R                      |             14112 |              11760 |
| NH      |                        |                 0 |               2256 |
| AK      | R                      |              1176 |                  0 |
| MI      |                        |                 0 |               7056 |
| NV      |                        |                 0 |               3528 |
| KS      | R                      |              3528 |               1176 |
| MS      | D                      |              1176 |               3528 |
| ND      | IND                    |                 0 |               1176 |
| NY      | WOF                    |              1176 |                  0 |
| WY      | R                      |              1176 |                  0 |
| ID      |                        |                 0 |               1176 |
| KY      | D                      |              1176 |               5880 |
| MS      | REF                    |                 0 |               4704 |
| NJ      | LIB                    |                 0 |               1176 |
| ID      | D                      |                 0 |               2352 |
| CT      |                        |                 0 |               1176 |
| NJ      | R                      |              3528 |              10584 |
| VT      | D                      |              1176 |                  0 |
| WV      | R                      |              2352 |               1176 |
| NC      |                        |                 0 |               1176 |
| OR      | D                      |              4704 |               1176 |
| ME      | R                      |              1176 |               1176 |
| VT      |                        |                 0 |               1176 |
| NV      | D                      |              1176 |               3528 |
| MA      | R                      |                 0 |               5880 |
| OH      | R                      |             12936 |               5880 |
| OK      | R                      |              4704 |               1176 |
| MD      |                        |                 0 |               3528 |
| MT      | R                      |              1176 |                  0 |
| SD      | R                      |                 0 |               1176 |
| AK      | D                      |                 0 |               1176 |
| MO      |                        |                 0 |               2352 |
| OR      | IPO                    |                 0 |               1176 |
| KY      | IND                    |                 0 |               2352 |
| MO      | R                      |              7056 |               2352 |
| MI      | R                      |              9408 |               5880 |
| MD      | R                      |              1176 |               8232 |
| WA      | D                      |              7056 |               5880 |
| ME      |                        |                 0 |               1176 |
| LA      | I                      |                 0 |               2352 |
| KS      | LIB                    |                 0 |               2352 |
| MN      | R                      |              3528 |               5880 |
| UT      | LIB                    |                 0 |               1176 |
| NC      | CON                    |                 0 |               1176 |
| PA      | D                      |              5880 |              15288 |
| WI      | DPD                    |                 0 |               1176 |
| NM      | LIB                    |                 0 |               2352 |
| WA      | L                      |                 0 |               1176 |
| MS      |                        |                 0 |               1176 |
| MT      | D                      |                 0 |               1176 |
| HI      | D                      |              1176 |               1176 |
| MI      | D                      |              3528 |              12936 |
| NY      | R                      |             10584 |              14112 |
| VT      | R                      |                 0 |               1176 |
| WY      | D                      |                 0 |               1176 |
| ND      | R                      |                 0 |               1176 |
| NC      | R                      |             10584 |               4704 |
| RI      | D                      |              2352 |                  0 |
| TN      |                        |                 0 |               3528 |
| WA      | R                      |              3528 |               5880 |
| IA      |                        |                 0 |               3528 |
| NY      | Reform Party           |                 0 |               1176 |
| MN      | D                      |              2352 |               7056 |
| CT      | R                      |                 0 |               5880 |
| NV      | R                      |              1176 |               3528 |
| SC      | R                      |              4704 |               3528 |
| WV      | D                      |                 0 |               3528 |
| KS      | D                      |                 0 |               4704 |
| SD      |                        |                 0 |               1176 |
| TN      | D                      |              2352 |               8232 |
| UT      | D                      |                 0 |               4704 |
| NM      | R                      |                 0 |               3528 |
| SC      | CON                    |                 0 |               1176 |
| NC      | D                      |              3528 |              10584 |
| NY      | G                      |                 0 |               1176 |
| HI      | R                      |                 0 |               2352 |
| MT      | LIB                    |                 0 |               1176 |
| VA      | D                      |              4704 |               8232 |
| SC      | D                      |              1176 |               7056 |
| AR      | R                      |              4704 |                  0 |
| NY      |                        |                 0 |               5484 |
| MD      | LIB                    |                 0 |               5880 |
| LA      | D                      |              1176 |              12936 |
| NM      | D                      |              1176 |               2352 |
| PA      | L                      |                 0 |               2352 |
| GA      | D                      |              4704 |              10584 |
| CT      | D                      |              4704 |               1176 |
| IL      | IND                    |                 0 |               1176 |
| OR      | R                      |              1176 |               3576 |
| VA      | LIB                    |                 0 |               2352 |
| CA      | G                      |                 0 |               3528 |
| CO      | L                      |                 0 |                 48 |
| ID      | R                      |              1176 |               1176 |
| NH      | D                      |              1176 |               1176 |
| SD      | D                      |                 0 |               1176 |
| TN      | R                      |              4704 |               5880 |
| IL      | D                      |             11760 |               9408 |
| IN      | LIB                    |                 0 |               1176 |
| ND      | D                      |                 0 |               1176 |
| MA      | D                      |              8232 |               2352 |
| TX      |                        |                 0 |               5880 |
| TX      | D                      |             10584 |              31752 |
| CO      | D                      |              2352 |               5880 |
| OH      | D                      |              4704 |              14112 |
| NY      | Women's Equality Party |                 0 |                 48 |
| CT      | GRE                    |                 0 |               1176 |
| GA      | R                      |             11760 |               3528 |
| MD      | D                      |              7056 |               2352 |
| NH      | LIB                    |                 0 |                 96 |
| NY      | D                      |             18816 |              12936 |
| NH      | R                      |                 0 |               2352 |
| ME      | D                      |              1176 |               1176 |
| DE      | D                      |              1176 |                  0 |
| IA      | D                      |              1176 |               3528 |
| UT      | R                      |              4704 |                  0 |
| FL      | NPA                    |                 0 |               2352 |
| CO      | R                      |              4704 |               3528 |
| CO      |                        |                 0 |               5784 |
| FL      |                        |                 0 |               2352 |
| NY      | REF                    |                 0 |               2352 |
| FL      | D                      |             12936 |              18816 |
| MN      | Independence Party     |                 0 |               1176 |
| VA      | R                      |              5880 |               5880 |
| AK      |                        |                 0 |               1128 |
| NJ      | D                      |              8232 |               5880 |
| ME      | IND                    |                 0 |               1176 |
| WI      | I                      |                 0 |               2352 |
| NJ      | CON                    |                 0 |               1176 |
| AZ      | R                      |              4704 |               4704 |
| LA      | R                      |              4764 |               1176 |
| TX      | LIB                    |                 0 |              28224 |
| IN      | D                      |              2352 |               8232 |
| VA      | L                      |                 0 |               1176 |
| OK      |                        |                 0 |               1176 |
| KY      | R                      |              5880 |               1176 |
| KY      | LIB                    |                 0 |               1176 |
| NY      | GRE                    |                 0 |               2748 |
| SC      | GRE                    |                 0 |               1176 |
| RI      | R                      |                 0 |               2352 |
| IA      | R                      |              3528 |               1176 |
| MO      | D                      |              2352 |               7056 |
| UT      |                        |                 0 |               2352 |
| HI      |                        |                 0 |               1176 |
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
| AZ      | D                      |             10584 |              21168 |
| CA      | R                      |             42336 |             119952 |
| LA      | LIB                    |                 0 |               3528 |
| MI      | Working Class          |                 0 |               7056 |
| CA      | D                      |            137592 |              56448 |
| WV      | Mountain               |                 0 |               3528 |
| AL      | D                      |              3528 |              21168 |
| OR      | LIB                    |                 0 |               3528 |
| MO      | LIB                    |                 0 |              21168 |
| TX      | R                      |             70560 |              42336 |
| LA      |                        |                 0 |              10584 |
| PA      | R                      |             24696 |              35280 |
| MI      | US Taxpayers           |                 0 |              10584 |
| NJ      |                        |                 0 |              28224 |
| CA      | I                      |                 0 |               7056 |
| NC      | LIB                    |                 0 |              14112 |
| DE      | R                      |                 0 |               3528 |
| AL      | R                      |             21168 |                  0 |
| CO      | LIB                    |                 0 |                288 |
| OH      | LIB                    |                 0 |              14112 |
| WI      | R                      |             14112 |              10584 |
| AR      | D                      |                 0 |              14112 |
| WI      | D                      |             10584 |              17640 |
| NE      | D                      |                 0 |              10584 |
| NE      | R                      |             10584 |                  0 |
| OK      | D                      |                 0 |              17640 |
| OR      |                        |                 0 |               7200 |
| OH      | GRE                    |                 0 |               7056 |
| OK      | I                      |                 0 |               3528 |
| SC      | AME                    |                 0 |              10584 |
| TN      | IND                    |                 0 |              17640 |
| IL      | R                      |             24696 |              38808 |
| MS      | R                      |              7056 |               3528 |
| OR      | GRE                    |                 0 |               3384 |
| IA      | LIB                    |                 0 |               3528 |
| MN      | Legal Marijuana Now    |                 0 |               3528 |
| MA      | IND                    |                 0 |               7056 |
| AR      | LIB                    |                 0 |              14112 |
| AZ      | G                      |                 0 |               7056 |
| IN      | R                      |             17640 |              14112 |
| TX      | IND                    |                 0 |               3528 |
| IL      | GRE                    |                 0 |               3528 |
| KY      |                        |                 0 |               3528 |
| WY      |                        |                 0 |               3528 |
| FL      | R                      |             42336 |              35280 |
| NH      |                        |                 0 |               6768 |
| AK      | R                      |              3528 |                  0 |
| MI      |                        |                 0 |              21168 |
| NV      |                        |                 0 |              10584 |
| KS      | R                      |             10584 |               3528 |
| MS      | D                      |              3528 |              10584 |
| ND      | IND                    |                 0 |               3528 |
| NY      | WOF                    |              3528 |                  0 |
| WY      | R                      |              3528 |                  0 |
| ID      |                        |                 0 |               3528 |
| KY      | D                      |              3528 |              17640 |
| MS      | REF                    |                 0 |              14112 |
| ID      | D                      |                 0 |               7056 |
| NJ      | LIB                    |                 0 |               3528 |
| CT      |                        |                 0 |               3528 |
| NJ      | R                      |             10584 |              31752 |
| VT      | D                      |              3528 |                  0 |
| WV      | R                      |              7056 |               3528 |
| NC      |                        |                 0 |               3528 |
| ME      | R                      |              3528 |               3528 |
| OR      | D                      |             14112 |               3528 |
| VT      |                        |                 0 |               3528 |
| MA      | R                      |                 0 |              17640 |
| NV      | D                      |              3528 |              10584 |
| OH      | R                      |             38808 |              17640 |
| OK      | R                      |             14112 |               3528 |
| MD      |                        |                 0 |              10584 |
| AK      | D                      |                 0 |               3528 |
| MT      | R                      |              3528 |                  0 |
| SD      | R                      |                 0 |               3528 |
| MO      |                        |                 0 |               7056 |
| KY      | IND                    |                 0 |               7056 |
| MO      | R                      |             21168 |               7056 |
| OR      | IPO                    |                 0 |               3528 |
| MI      | R                      |             28224 |              17640 |
| MD      | R                      |              3528 |              24696 |
| WA      | D                      |             21168 |              17640 |
| ME      |                        |                 0 |               3528 |
| LA      | I                      |                 0 |               7056 |
| KS      | LIB                    |                 0 |               7056 |
| MN      | R                      |             10584 |              17640 |
| UT      | LIB                    |                 0 |               3528 |
| NC      | CON                    |                 0 |               3528 |
| PA      | D                      |             17640 |              45864 |
| WI      | DPD                    |                 0 |               3528 |
| NM      | LIB                    |                 0 |               7056 |
| WA      | L                      |                 0 |               3528 |
| MS      |                        |                 0 |               3528 |
| MT      | D                      |                 0 |               3528 |
| HI      | D                      |              3528 |               3528 |
| MI      | D                      |             10584 |              38808 |
| NY      | R                      |             31752 |              42336 |
| VT      | R                      |                 0 |               3528 |
| WY      | D                      |                 0 |               3528 |
| ND      | R                      |                 0 |               3528 |
| NC      | R                      |             31752 |              14112 |
| RI      | D                      |              7056 |                  0 |
| TN      |                        |                 0 |              10584 |
| WA      | R                      |             10584 |              17640 |
| IA      |                        |                 0 |              10584 |
| MN      | D                      |              7056 |              21168 |
| NY      | Reform Party           |                 0 |               3528 |
| CT      | R                      |                 0 |              17640 |
| KS      | D                      |                 0 |              14112 |
| NV      | R                      |              3528 |              10584 |
| SC      | R                      |             14112 |              10584 |
| WV      | D                      |                 0 |              10584 |
| SD      |                        |                 0 |               3528 |
| TN      | D                      |              7056 |              24696 |
| UT      | D                      |                 0 |              14112 |
| NM      | R                      |                 0 |              10584 |
| SC      | CON                    |                 0 |               3528 |
| HI      | R                      |                 0 |               7056 |
| NC      | D                      |             10584 |              31752 |
| NY      | G                      |                 0 |               3528 |
| MT      | LIB                    |                 0 |               3528 |
| VA      | D                      |             14112 |              24696 |
| SC      | D                      |              3528 |              21168 |
| AR      | R                      |             14112 |                  0 |
| NY      |                        |                 0 |              16452 |
| MD      | LIB                    |                 0 |              17640 |
| LA      | D                      |              3528 |              38808 |
| NM      | D                      |              3528 |               7056 |
| PA      | L                      |                 0 |               7056 |
| GA      | D                      |             14112 |              31752 |
| CT      | D                      |             14112 |               3528 |
| IL      | IND                    |                 0 |               3528 |
| OR      | R                      |              3528 |              10728 |
| VA      | LIB                    |                 0 |               7056 |
| CA      | G                      |                 0 |              10584 |
| CO      | L                      |                 0 |                144 |
| ID      | R                      |              3528 |               3528 |
| NH      | D                      |              3528 |               3528 |
| IL      | D                      |             35280 |              28224 |
| IN      | LIB                    |                 0 |               3528 |
| SD      | D                      |                 0 |               3528 |
| TN      | R                      |             14112 |              17640 |
| MA      | D                      |             24696 |               7056 |
| ND      | D                      |                 0 |               3528 |
| TX      |                        |                 0 |              17640 |
| CO      | D                      |              7056 |              17640 |
| TX      | D                      |             31752 |              95256 |
| OH      | D                      |             14112 |              42336 |
| NY      | Women's Equality Party |                 0 |                144 |
| CT      | GRE                    |                 0 |               3528 |
| GA      | R                      |             35280 |              10584 |
| MD      | D                      |             21168 |               7056 |
| NH      | LIB                    |                 0 |                288 |
| NY      | D                      |             56448 |              38808 |
| ME      | D                      |              3528 |               3528 |
| NH      | R                      |                 0 |               7056 |
| DE      | D                      |              3528 |                  0 |
| IA      | D                      |              3528 |              10584 |
| FL      | NPA                    |                 0 |               7056 |
| UT      | R                      |             14112 |                  0 |
| CO      | R                      |             14112 |              10584 |
| CO      |                        |                 0 |              17352 |
| FL      |                        |                 0 |               7056 |
| FL      | D                      |             38808 |              56448 |
| MN      | Independence Party     |                 0 |               3528 |
| NY      | REF                    |                 0 |               7056 |
| VA      | R                      |             17640 |              17640 |
| AK      |                        |                 0 |               3384 |
| ME      | IND                    |                 0 |               3528 |
| NJ      | D                      |             24696 |              17640 |
| WI      | I                      |                 0 |               7056 |
| AZ      | R                      |             14112 |              14112 |
| LA      | R                      |             14292 |               3528 |
| NJ      | CON                    |                 0 |               3528 |
| IN      | D                      |              7056 |              24696 |
| TX      | LIB                    |                 0 |              84672 |
| VA      | L                      |                 0 |               3528 |
| OK      |                        |                 0 |               3528 |
| KY      | R                      |             17640 |               3528 |
| KY      | LIB                    |                 0 |               3528 |
| NY      | GRE                    |                 0 |               8244 |
| SC      | GRE                    |                 0 |               3528 |
| IA      | R                      |             10584 |               3528 |
| MO      | D                      |              7056 |              21168 |
| RI      | R                      |                 0 |               7056 |
| UT      |                        |                 0 |               7056 |
| HI      |                        |                 0 |               3528 |
```

