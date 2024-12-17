# MMDT: DECODING THE PRIVACY OF MULTIMODAL FOUNDATION MODELS

## Overview

This repo contains the source code of MMDT (Multimodal DecodingTrust).
This research endeavor is designed to help researchers and practitioners better understand the capabilities, limitations, and potential risks involved in deploying these state-of-the-art Multimodal foundation models (MMFMs).


## Getting Started

### Clone the repository

```bash
git clone https://github.com/AI-secure/MMDT.git && cd MMDT
```

### Install requirements

```bash
conda create --name mmdt python=3.9
conda activate mmdt
pip install -r requirements.txt
```

### Download MMDT dataset

We provide our dataset at [this URL](https://drive.google.com/file/d/1RLdkErIxyVuwEeVpVaC8eN0og2L3vwyM/view?usp=sharing). Please unzip the file and put the folder at the repository root `./data`. The directory will look like:

```
.
├── data
│   └── image-to-text
├── mmdt
├── scripts
├── README.md
└── requirements.txt
```

### Evaluate the privacy perspective

```bash
bash scripts/privacy-vispr.sh
```

## License
This project is licensed under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode)  - see the LICENSE file for details.

## Contact
Please reach out to us if you have any questions or suggestions. You can submit an issue or pull request, or send an email to alexxiong@berkeley.edu.

Thank you for your interest in MMDT. We hope our work will contribute to a more trustworthy, fair, and robust AI future.