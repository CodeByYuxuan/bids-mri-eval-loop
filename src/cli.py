# src/cli.py
import argparse, pathlib


def main():
    p = argparse.ArgumentParser()
    p.add_argument("bids_dir")
    p.add_argument("output_dir")
    p.add_argument("analysis_level", choices=["participant", "group"])
    p.add_argument("--report-format", choices=["html", "md"], default="html")
    args = p.parse_args()

    bids = pathlib.Path(args.bids_dir).resolve()
    out = pathlib.Path(args.output_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)

    # 这里先占位: 读取 MRIQC 产出的 group-level CSV，生成一页摘要
    # 后续接入: fMRIPrep、SynthSR/SMORE、MONAI 指标
    print(f"[OK] inputs: {bids} → outputs: {out} level={args.analysis_level}")


if __name__ == "__main__":
    main()
