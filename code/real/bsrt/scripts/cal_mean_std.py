import torch
import numpy as np
from tqdm import tqdm

from datasets.burstsr_dataset import BurstSRDataset, flatten_raw_image
from datasets.synthetic_burst_train_set import SyntheticBurst
from datasets.zurich_raw2rgb_dataset import ZurichRAW2RGB
import argparse
import os

def main(dataset_root):
    train_zurich_raw2rgb = ZurichRAW2RGB(root=dataset_root, split='train')
    train_data = SyntheticBurst(train_zurich_raw2rgb, burst_size=14, crop_sz=384)
    means = []
    stds = []

    for data in tqdm(train_data):
        print(data.shape)
        break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate mean and std of dataset')
    parser.add_argument(
        '--root',
        type=str,
        default=os.path.join('datasets', 'burstsr', 'synthetic'),
        help='path to synthetic BurstSR dataset'
    )
    args = parser.parse_args()

    main(args.root)
