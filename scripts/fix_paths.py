input_file = 'deepfashion/list_attr_img.txt'
output_file = 'deepfashion/list_attr_img_fixed.txt'

with open(input_file, 'r') as f:
    lines = f.readlines()

with open(output_file, 'w') as f:
    for line in lines[:2]:  # Copy the header lines
        f.write(line)
    for line in lines[2:]:
        parts = line.strip().split()
        image_path = parts[0]
        attributes = parts[1:]
        # Replace '-' with '/' only when it is before 'img'
        new_image_path = image_path.replace('-img', '/img')
        f.write(f'{new_image_path} {" ".join(attributes)}\n')

print("Finished fixing the paths in list_attr_img.txt.")