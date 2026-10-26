# Preserved access evidence

`medicaid-sample-0-2047.bin` contains exactly the first 2,048 bytes returned by the public HHS Medicaid CSV server. `medicaid-sample-metadata.json` records the source URL, HTTP Range request, response status/headers, and NPPES lookup response for the anomalous identifier. The copied sample path is relative to this folder. Original acquisition path is retained separately.

This tiny sample proves access and exposes an initial data-validation problem. It does not characterize the full dataset or demonstrate provider fraud. Do not rank the dataset by raw paid amounts before validation.
