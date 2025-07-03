# GBT-net
This GitHub repository is created to share the model weights developed during the **GBT-net** project.

![GBT-net Architecture](assets/foundation_models.png)  

---

## Requirements
| Package        | Version |
|----------------|---------|
| Python         | ≥ 3.8   |
| PyTorch (`torch`) | ≥ 2.0 |
| torchvision    | ≥ 0.15  |
| numpy          | ≥ 1.24  |
| pandas         | ≥ 2.0   |
| scikit-learn   | ≥ 1.3   |
| matplotlib     | ≥ 3.8   |
| tqdm           | ≥ 4.66  |

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

## Model Weights
The trained model weights for **GBT-net** are provided below.  
Replace the placeholder links with your actual download URLs.

| Version | Description                                 | Download Link |
|---------|---------------------------------------------|---------------|
| v1.0    | Pre-trained on MRI & CT (full pre-training) | `[Download .pth](https://github.com/yourname/yourrepo/releases/download/v1.0/gbt-net_pretrain_v1.0.pth)` |
| v1.1    | Fine-tuned on IDH mutation classification   | `[Download .pth](https://github.com/yourname/yourrepo/releases/download/v1.1/gbt-net_finetune_v1.1.pth)` |
| v2.0    | Updated architecture with attention module  | `[Download .pth](https://github.com/yourname/yourrepo/releases/download/v2.0/gbt-net_attention_v2.0.pth)` |


## Usage
Please refer to the [GBT-net Model Loading Notebook](gbt_net_model_loading.ipynb) for detailed instructions on how to load and run both the segmentation and classification models.

---


## License
Distributed under the MIT License.  
See the [LICENSE](LICENSE) file for more details.
