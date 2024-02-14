import os
import random
from shutil import copyfile
from tqdm import tqdm


def split_data(input_images_dir, input_labels_dir, output_dir, train_ratio, valid_ratio, test_ratio):
    # Create output directories
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'images', 'train'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'images', 'valid'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'images', 'test'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'labels', 'train'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'labels', 'valid'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'labels', 'test'), exist_ok=True)

    # Get list of image files
    image_files = os.listdir(input_images_dir)
    random.shuffle(image_files)

    # Calculate data split indices
    total_samples = len(image_files)
    train_split_index = int(total_samples * train_ratio)
    valid_split_index = int(total_samples * (train_ratio + valid_ratio))

    # Split data
    train_images = image_files[:train_split_index]
    valid_images = image_files[train_split_index:valid_split_index]
    test_images = image_files[valid_split_index:]

    # Copy images and labels to respective directories
    for split, images in zip(['train', 'valid', 'test'], [train_images, valid_images, test_images]):
        for image_file in tqdm(images, desc=f'Copying {split} images'):
            image_path = os.path.join(input_images_dir, image_file)
            label_path = os.path.join(input_labels_dir, image_file.rsplit('.', 1)[0] + '.txt')
            output_image_path = os.path.join(output_dir, 'images', split, image_file)
            output_label_path = os.path.join(output_dir, 'labels', split, image_file.rsplit('.', 1)[0] + '.txt')

            copyfile(image_path, output_image_path)
            copyfile(label_path, output_label_path)

    # Print counts
    print(f'Train set count: {len(train_images)}')
    print(f'Validation set count: {len(valid_images)}')
    print(f'Test set count: {len(test_images)}')



if __name__=="__main__":
    input_images_folder = "C:/_WORK/Data/Traffic Light - Object Detection/OUTPUT/Converter/v2/images"
    input_labels_folder = "C:/_WORK/Data/Traffic Light - Object Detection/OUTPUT/Converter/v2/labels"
    output_folder = "C:/_WORK/Data/Traffic Light - Object Detection/OUTPUT/YOLO/Dataset-YOLO-v2"
    
    # Example usage
    input_images_dir = input_images_folder
    input_labels_dir = input_labels_folder
    output_dir = output_folder
    train_ratio = 0.7
    valid_ratio = 0.15
    test_ratio = 0.15

    split_data(input_images_dir, input_labels_dir, output_dir, train_ratio, valid_ratio, test_ratio)
