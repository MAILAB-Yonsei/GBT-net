# GBT-net

# Dataset Overview

| Dataset                            | Modality               | Clinical Status             | Total # of Data (each contrast)       | Train (# of subj) | Valid (# of subj) | Test (# of subj) |
|------------------------------------|------------------------|-----------------------------|--------------------------------------|-------------------|-------------------|------------------|
| *Pre-training*                     |                        |                             |                                      |                   |                   |                  |
| ADNI-1                             | T1                     | AD, MCI, NC                 | 1179                                 | 782               | 196               | 201              |
| AIBL                               | T1                     | AD, MCI, NC                 | 1281                                 | 1280              | –                 | –                |
| BraTS2023                          | T1, T1C, T2, FLAIR     | Brain Tumor                 | 5004 (1251, 1251, 1251, 1251)        | 3328 (832)        | 832 (208)         | 844 (211)        |
| IXI                                | T1, T2, PD, MRA        | Normal                      | 2307 (581, 578, 578, 570)            | 2307              | –                 | –                |
| *Fine-tuning*                      |                        |                             |                                      |                   |                   |                  |
| TCGA                               | T1, T1C, T2, FLAIR     | IDH-mutant, IDH-wildtype    | 800 (200, 200, 200, 200)             | 800 (200)         | –                 | –                |
| UCSF                               | T1, T1C, T2, FLAIR     | IDH-mutant, IDH-wildtype    | 1908 (477, 477, 477, 477)            | 1908 (477)        | –                 | –                |
| In-house (Sinchon Severance)       | T1, T1C, T2, FLAIR     | IDH-mutant, IDH-wildtype    | 4212 (1053 × 4)                      | 2804 (701)        | 704 (176)         | 704 (176)        |
| FLARE 23                           | Abdomen CT             | Normal                      | 4000                                 | 4000              | –                 | –                |
| In-house (Gangnam Severance)       | Abdomen CT             | Acute Diseases              | 15317                                | 15317             | –                 | –                |
| **Total**                          |                        |                             | **36,008**                           | **32,526**        | **1,732**         | **1,749**        |

> **Note:** DTI images from the IXI dataset and ADC images from the in-house dataset were excluded due to low quality.  
> **Abbreviations:**  
> NC: Normal Cognition; MCI: Mild Cognitive Impairment; AD: Alzheimer’s Disease; MRA: Magnetic Resonance Angiography;  
> IDH: Isocitrate Dehydrogenase; TCGA: The Cancer Genome Atlas; UCSF: University of California, San Francisco; subj: subject.
