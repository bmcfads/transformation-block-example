import argparse, os, shutil

# These are the three arguments that we get in
parser = argparse.ArgumentParser(description='Transformation block 1')
parser.add_argument('--in-directory', type=str, required=True)
parser.add_argument('--out-directory', type=str, required=True)

args, unknown = parser.parse_known_args()
in_dir = args.in_directory
out_dir = args.out_directory

# Verify that the input directory exists and create the output directory if needed
if not os.path.exists(in_dir):
    print('--in-directory argument', in_dir, 'does not exist', flush=True)
    exit(1)

# Remove the out-directory if it already exists
if  os.path.exists(out_dir):
    shutil.rmtree(out_dir)

# Copy files in in-directory to out-directory
shutil.copytree(in_dir, out_dir)

# Rename the files in the out-directory
for root, dirs, filenames in os.walk(out_dir):
    for filename in filenames:
        new_filename = filename.split('.')[0] + '_intermediate.jpeg'
        src = os.path.join(root, filename)
        dst = os.path.join(root, new_filename)
        os.rename(src, dst)
        print(f'Processed file: {filename} -> {new_filename}', flush=True)
