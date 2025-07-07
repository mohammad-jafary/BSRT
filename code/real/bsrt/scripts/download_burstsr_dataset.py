import os
import urllib.request
import zipfile
import shutil
import argparse


def download_burstsr_dataset(download_path):
    out_dir = os.path.join(download_path, 'burstsr_dataset')

    # Download train folders
    for i in range(9):
        if not os.path.isfile(os.path.join(out_dir, f'train_{i:02d}.zip')):
            print('Downloading train_{:02d}'.format(i))

            urllib.request.urlretrieve(
                f'https://data.vision.ee.ethz.ch/bhatg/BurstSRChallenge/train_{i:02d}.zip',
                os.path.join(out_dir, 'tmp.zip'),
            )

            os.rename(
                os.path.join(out_dir, 'tmp.zip'),
                os.path.join(out_dir, f'train_{i:02d}.zip'),
            )

    # Download val folder
    if not os.path.isfile(os.path.join(out_dir, 'val.zip')):
        print('Downloading val')

        urllib.request.urlretrieve(
            'https://data.vision.ee.ethz.ch/bhatg/BurstSRChallenge/val.zip',
            os.path.join(out_dir, 'tmp.zip'),
        )

        os.rename(os.path.join(out_dir, 'tmp.zip'), os.path.join(out_dir, 'val.zip'))

    # Unpack train set
    for i in range(9):
        print('Unpacking train_{:02d}'.format(i))
        with zipfile.ZipFile(os.path.join(out_dir, f'train_{i:02d}.zip'), 'r') as zip_ref:
            zip_ref.extractall(out_dir)

    # Move files to a common directory
    os.makedirs(os.path.join(out_dir, 'train'), exist_ok=True)

    for i in range(9):
        file_list = os.listdir(os.path.join(out_dir, f'train_{i:02d}'))

        for b in file_list:
            source_dir = os.path.join(out_dir, f'train_{i:02d}', b)
            dst_dir = os.path.join(out_dir, 'train', b)

            if os.path.isdir(source_dir):
                shutil.move(source_dir, dst_dir)

    # Delete individual subsets
    for i in range(9):
        shutil.rmtree(os.path.join(out_dir, f'train_{i:02d}'))

    # Unpack val set
    print('Unpacking val')
    with zipfile.ZipFile(os.path.join(out_dir, 'val.zip'), 'r') as zip_ref:
        zip_ref.extractall(out_dir)


def main():
    parser = argparse.ArgumentParser(description='Downloads and unpacks BurstSR dataset')
    parser.add_argument('path', type=str, help='Path where the dataset will be downloaded')

    args = parser.parse_args()

    download_burstsr_dataset(args.path)


if __name__ == '__main__':
    main()


