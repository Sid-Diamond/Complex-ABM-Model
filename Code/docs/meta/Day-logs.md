09/09/2026:

  - Established that O*NET can create a static occupational similarity network, but does not contain observed worker
    transitions or meaningful time evolution.

  - Evaluated JobHop as a possible transition dataset, but identified serious limitations: resume-derived data, Flemish
    population, ESCO coding, selection bias, and extraction/classification noise.

  - Chose IPUMS-CPS as a more defensible candidate because it is based on the U.S. Current Population Survey and provides
    survey weights and person linkages.

  - Created an IPUMS extract covering 2020–2026 monthly/ASEC data.
  - Discovered that the extract contains current occupation (OCC) and linked person IDs (CPSIDP), but not a direct
    previous-year occupation variable.

  - Built a preliminary inspection script.
  - Found 6.19 million records, 1.54 million linked IDs, 56 months, and approximately 1.64 million valid adjacent-month
    observations.

  - Detected and corrected 385,792 duplicate March observations caused by overlapping ASEC/Basic records.
  - Estimated 124,097 occupation changes across 37,689 directed edges.
  - Added Data/ to .gitignore so raw IPUMS and O*NET data remain local.

  The transition figures are preliminary. They are not yet a publishable network because we still need to validate
  linkage quality, duplicate handling, weights, occupation coding, and the interpretation of a month-to-month change.