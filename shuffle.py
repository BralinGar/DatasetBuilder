import os, random, shutil

os.mkdir('train')
os.mkdir('validation')
os.mkdir('train/train_images')
os.mkdir('train/train_annotations')
os.mkdir('validation/validation_images')
os.mkdir('validation/validation_annotations')

image_paths = os.listdir('Images')
random.shuffle(image_paths)

for i, image_path in enumerate(image_paths):
  if i < int(len(image_paths) * 0.8):
    shutil.copy(f'Images/{image_path}', 'train/train_images')
    shutil.copy(f'Annotations/{image_path.replace("jpg", "xml")}', 'train/train_annotations')
  else:
    shutil.copy(f'Images/{image_path}', 'validation/validation_images')
    shutil.copy(f'Annotations/{image_path.replace("jpg", "xml")}', 'validation/validation_annotations')