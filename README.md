# bids-mri-eval-loop

BIDS -> MRIQC -> one-page evaluation summary for clinical brain MRI.

## Features

- Run MRIQC on BIDS datasets and collect IQMs
- Generate one-page summary (HTML/Markdown)
- BIDS App-style CLI

## Quickstart

```bash
# example (paths are placeholders)
docker run --rm -v $PWD/demo_data:/data:ro -v $PWD/outputs:/out nipreps/mriqc:latest /data /out participant
python -m src.cli /data /out group --report-format html
```
