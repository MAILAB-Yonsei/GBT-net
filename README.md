# GBT-net
This GitHub repository is created to share the model weights developed during the **GBT-net** project.

![GBT-net Architecture](assets/foundation_models.png)  

---

## Requirements
| Package        | Version |
|----------------|---------|
| Python         | ≥ 3.8   |
| PyTorch        |  2.2.2  |
| monai          |  1.3.0  |

---

## Pre-training Dataset Overview

| Dataset                          | Modality               | Clinical Status             | Total # of Data (each contrast)      | Train (# subj) | Valid (# subj) | Test (# subj) |
|----------------------------------|------------------------|-----------------------------|--------------------------------------|---------------|---------------|---------------|
| *Pre-training*                   |                        |                             |                                      |               |               |               |
| ADNI-1                           | T1                     | AD, MCI, NC                 | 1 179                                | 782           | 196           | 201           |
| AIBL                             | T1                     | AD, MCI, NC                 | 1 281                                | 1 280         | –             | –             |
| BraTS 2023                       | T1, T1C, T2, FLAIR     | Brain Tumor                 | 5 004 (1 251 × 4)                    | 3 328 (832)   | 832 (208)     | 844 (211)     |
| IXI                              | T1, T2, PD, MRA        | Normal                      | 2 307 (581, 578, 578, 570)           | 2 307         | –             | –             |
| *Fine-tuning*                    |                        |                             |                                      |               |               |               |
| TCGA                             | T1, T1C, T2, FLAIR     | IDH-mutant, IDH-wildtype    | 800 (200 × 4)                        | 800 (200)     | –             | –             |
| UCSF                             | T1, T1C, T2, FLAIR     | IDH-mutant, IDH-wildtype    | 1 908 (477 × 4)                      | 1 908 (477)   | –             | –             |
| In-house (Sinchon Severance)     | T1, T1C, T2, FLAIR     | IDH-mutant, IDH-wildtype    | 4 212 (1 053 × 4)                    | 2 804 (701)   | 704 (176)     | 704 (176)     |
| FLARE 23                         | Abdomen CT             | Normal                      | 4 000                                | 4 000         | –             | –             |
| In-house (Gangnam Severance)     | Abdomen CT             | Acute Diseases              | 15 317                               | 15 317        | –             | –             |
| **Total**                        | —                      | —                           | **36 008**                           | **32 526**    | **1 732**     | **1 749**     |

> **Note:** DTI images from the IXI dataset and ADC images from the in-house dataset were excluded due to low quality.  
> **Abbreviations:**  
> **NC** – Normal Cognition &nbsp;•&nbsp; **MCI** – Mild Cognitive Impairment &nbsp;•&nbsp; **AD** – Alzheimer’s Disease &nbsp;•&nbsp; **MRA** – Magnetic Resonance Angiography  
> **IDH** – Isocitrate Dehydrogenase &nbsp;•&nbsp; **TCGA** – The Cancer Genome Atlas &nbsp;•&nbsp; **UCSF** – University of California, San Francisco  
> **subj** – subject (unique patient/scan)

---
## Downstream Task Evaluation

| Method            | Backbone         | Modality               | Training Token Size (B) | Model Params      | ADNI (AUC)            | BraTS2023 (DSC)              | MSD04 (DSC)                  | OASIS-1 (AUC)        |
|-------------------|------------------|------------------------|-------------------------|-------------------|-----------------------|------------------------------|------------------------------|----------------------|
|  –                | UNETR            | –                      | –                       | 249 M (E: 88 M)   | 0.615                 | 82.17                        | 80.17                        | 0.739                |
|  –                | Swin-UNETR       | –                      | –                       | 62 M (E: 8 M)     | 0.699                 | 83.83                        | 80.55                        | 0.635                |
|  –                | Swin-UNETR-v2    | –                      | –                       | 73 M (E: 18 M)    | 0.875                 | 83.69                        | 81.23                        | 0.778                |
| Swin-UNETR        | Swin-UNETR       | CT                     | 15                      | 62 M (E: 8 M)     | **0.950**             | 83.17                        | 80.78                        | 0.878                |
| VoCo              | Swin-UNETR-v2    | CT                     | 333                     | 73 M (E: 18 M)    | 0.938                 | 83.64                        | 81.67                        | 0.843                |
| SuPreM            | Swin-UNETR       | CT                     | 28                      | 62 M (E: 8 M)     | 0.910                 | **84.25**                    | 80.76                        | 0.843                |
| Universal Model   | Swin-UNETR       | Multi (CT, Text)       | 12                      | 62 M (E: 8 M)     | 0.893                 | 83.61                        | **81.99**                    | 0.752                |
| MedCoss           | UNETR            | Multi (CT, MRI, Text)  | 0.14                    | 249 M (E: 88 M)   | 0.846                 | 82.26                        | 78.96                        | 0.809                |
| **GBT-net**       | Swin-UNETR-v2    | CT, MR                 | 32 K                    | 73 M (E: 18 M)    | <ins>0.949</ins>      | <ins>83.85</ins>             | 81.16                        | **0.943**            |

> **E**: encoder parameters  
> **Bold** indicates the best score in each column  
> Token sizes are in billions (B) or thousands (K) as indicated.  

## Model Weights
The trained model weights for **GBT-net** are provided below.  
Replace the placeholder links with your actual download URLs.

| Version | Description                                 | Download Link |
|---------|---------------------------------------------|---------------|
| v1.0    | Pre-trained on MRI & CT (full pre-training) | `[Download .pth](https://github.com/yourname/yourrepo/releases/download/v1.0/gbt-net_pretrain_v1.0.pth)` |
| v1.1    | Fine-tuned on IDH mutation classification   | `[Download .pth](https://github.com/yourname/yourrepo/releases/download/v1.1/gbt-net_finetune_v1.1.pth)` |
| v2.0    | Updated architecture with attention module  | `[Download .pth](https://github.com/yourname/yourrepo/releases/download/v2.0/gbt-net_attention_v2.0.pth)` |


## Usage
Please refer to the [GBT-net Model Loading Notebook](load_model_weight.ipynb) for detailed instructions on how to load and run both the segmentation and classification models.

---

## License 
See the [LICENSE](LICENSE) file for more details.
