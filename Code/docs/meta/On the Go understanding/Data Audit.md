### IPUMS data inspection and duplicate audit

  1. I audited the initial IPUMS inspection script written by Codex. The script reads the compressed .dat.gz file using
     the accompanying DDI XML metadata.

     DDI means Data Documentation Initiative. In this case, it is the XML codebook that specifies:
      - which variables are present;
      - where each variable begins and ends in each fixed-width record;
      - variable labels and meanings;
      - value codes and sample documentation.

  2. The initial inspection found 6,194,406 raw person-records. For the relevant fields, each record contains:

  YEAR, MONTH, CPSIDP, OCC

  where:

  - YEAR and MONTH identify the observation date;
  - CPSIDP is the IPUMS-linked person identifier;
  - OCC is the respondent’s occupation code.

  3. The initial script then grouped records by:

  (CPSIDP, YEAR, MONTH, OCC)

  It found:

  6,194,406 raw records
  5,808,614 unique extracted observations
  385,792 duplicate observations

  The term “unique” applies only to these four extracted fields. We have not compared every variable that might exist in
  the original CPS records.

  4. We then performed a source-aware audit to test the explanation for the duplicates.

     The DDI identifies ASECFLAG as the source indicator. We mapped its values as follows:

  1       ASEC
  2       March Basic
  blank   Unknown / ordinary monthly CPS record

  The source counts were:

  ASEC:          906,757
  March Basic:   475,160
  Unknown:     4,812,489
  Total:       6,194,406

  The “Unknown” category is not necessarily an error. It represents ordinary monthly CPS observations where ASECFLAG is
  blank.

  5. To test whether the duplicate observations arose from source overlap, we grouped records by:

  (CPSIDP, YEAR, MONTH, OCC)

  and asked whether the same key appeared under more than one source label.

  The result was:

  ASEC + March Basic: 385,792 keys
  ASEC + Unknown:           0 keys
  March Basic + Unknown:    0 keys

  Therefore, the duplicate explanation is directly supported:

  > The 385,792 duplicate extracted observations arise from the same person-month-occupation record appearing in both the  > ASEC and March Basic portions of the IPUMS extract.

### Edges Analysist

1. Of this 5.8m unique   (CPSIDP, YEAR, MONTH, OCC). We then counted unique  (CPSIDP), ONET suggests we consider these not as people until a further audit. 
2. Of these, codex then scanned for the number of times an ID was found across two consecutive months with a non empty OCC. This occured 1.6m times. 
3. This does not adress how this distribution exists across the different IDs. This is reserved for future analysis. 
4. It was found there existed 1,643,075 same-occupation links then split into:
  1,518,978 same-occupation links
  124,097 changed-occupation links
5. This was audited by checking for each ID.
    a.  When ID was seen, it was next seen in the data 4.2m times. 
    b.  Of these, the next time it was seen was a month apart 3.4m times. We use these consequtive month cases for simplicity for now. 
    c. Of the 3.4m 1.6m had valid occ end points and therefore can be consiered to have changed occupation. For now, we are keeping things simple. and we are exluding multiple, jumps and not referencing the employment data. we are using not in universe 0000 code as it is. not breaking this down using external data. 
    d. of these 1.6m, 200k moved jobs. 