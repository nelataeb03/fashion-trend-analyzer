def fix_category_paths(category_file, output_file):
    with open(category_file, 'r') as f:
        lines = f.readlines()
    
    with open(output_file, 'w') as f:
        f.write(lines[0])  # Write the first line (number of images)
        f.write(lines[1])  # Write the second line (header)
        for line in lines[2:]:
            fixed_line = line.replace('img/', 'img_highres_subset/')
            f.write(fixed_line)

if __name__ == '__main__':
    category_file = 'deepfashion/list_eval_partition.txt'
    output_file = 'deepfashion/list_eval_partition_fixed.txt'
    fix_category_paths(category_file, output_file)