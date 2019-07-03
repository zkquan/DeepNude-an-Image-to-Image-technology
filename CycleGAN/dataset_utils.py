import tensorflow as tf
import tensorflow_datasets as tfds

import os
import sys
import matplotlib.pyplot as plt

AUTOTUNE = tf.data.experimental.AUTOTUNE

cycle_gan_dataset_name_list = ["apple2orange", "summer2winter_yosemite", "horse2zebra", "monet2photo",
                               "cezanne2photo", "ukiyoe2photo", "vangogh2photo", "maps",
                               "cityscapes", "facades", "iphone2dslr_flower", ]


def download_and_processing_cyclegan_dataset(task_name="apple2orange",
                                             BATCH_SIZE=1, BUFFER_SIZE=1000,
                                             IMG_WIDTH=256, IMG_HEIGHT=256):
    def random_crop(image):
        cropped_image = tf.image.random_crop(
            image, size=[IMG_HEIGHT, IMG_WIDTH, 3])

        return cropped_image

    # normalizing the images to [-1, 1]
    def normalize(image):
        image = tf.cast(image, tf.float32)
        image = (image / 127.5) - 1
        return image

    def random_jitter(image):
        # resizing to 286 x 286 x 3
        image = tf.image.resize(image, [286, 286],
                                method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)

        # randomly cropping to 256 x 256 x 3
        image = random_crop(image)

        # random mirroring
        image = tf.image.random_flip_left_right(image)

        return image

    def preprocess_image_train(image, label):
        image = random_jitter(image)
        image = normalize(image)
        return image

    def preprocess_image_test(image, label):
        image = normalize(image)
        return image

    cycle_gan_dataset_name_list = ["cycle_gan/apple2orange", "cycle_gan/summer2winter_yosemite",
                                   "cycle_gan/horse2zebra", "cycle_gan/monet2photo",
                                   "cycle_gan/cezanne2photo", "cycle_gan/ukiyoe2photo",
                                   "cycle_gan/vangogh2photo", "cycle_gan/maps",
                                   "cycle_gan/cityscapes", "cycle_gan/facades",
                                   "cycle_gan/iphone2dslr_flower", ]

    task_name = "cycle_gan/" + task_name
    if task_name not in cycle_gan_dataset_name_list:
        print("Not include this task!")
        print(f"You can choose task from {cycle_gan_dataset_name_list}")
        raise ValueError("not include this task!")

    # download data
    dataset, metadata = tfds.load(task_name, with_info=True, as_supervised=True)

    trainA_dataset, trainB_dataset = dataset['trainA'], dataset['trainB']
    testA_dataset, testB_dataset = dataset['testA'], dataset['testB']

    # processing data
    trainA_dataset = trainA_dataset.map(
        preprocess_image_train, num_parallel_calls=AUTOTUNE).shuffle(
        BUFFER_SIZE).batch(BATCH_SIZE)

    trainB_dataset = trainB_dataset.map(
        preprocess_image_train, num_parallel_calls=AUTOTUNE).shuffle(
        BUFFER_SIZE).batch(BATCH_SIZE)

    testA_dataset = testA_dataset.map(
        preprocess_image_test, num_parallel_calls=AUTOTUNE).shuffle(
        BUFFER_SIZE).batch(BATCH_SIZE)

    testB_dataset = testB_dataset.map(
        preprocess_image_test, num_parallel_calls=AUTOTUNE).shuffle(
        BUFFER_SIZE).batch(BATCH_SIZE)

    return trainA_dataset, trainB_dataset, testA_dataset, testB_dataset


def show_dataset(sampleA, sampleB, numder=0, sampleA_name="sampleA", sampleB_name="sampleB",
                 store_sample_image_path="sample_image"):
    if not os.path.exists(store_sample_image_path):
        os.mkdir(store_sample_image_path)
    plt.title(sampleA_name)
    plt.imshow(sampleA[0] * 0.5 + 0.5)
    save_path = os.path.join(store_sample_image_path, f"{str(numder)}_{sampleA_name}.png")
    plt.savefig(save_path)

    plt.title(sampleB_name)
    plt.imshow(sampleB[0] * 0.5 + 0.5)
    save_path = os.path.join(store_sample_image_path, f"{str(numder)}_{sampleB_name}.png")
    plt.savefig(save_path)


def cyclegan_data_explore():
    for task_name in cycle_gan_dataset_name_list:
        BATCH_SIZE = 1
        trainA_dataset, trainB_dataset, testA_dataset, testB_dataset = download_and_processing_cyclegan_dataset(
            task_name, BATCH_SIZE)
        store_sample_image_path = f"sample_image_{task_name}"
        i = 0
        for sampleA, sampleB in zip(trainA_dataset.take(3), trainB_dataset.take(3)):
            show_dataset(sampleA, sampleB, numder=i, sampleA_name="A", sampleB_name="B",
                         store_sample_image_path=store_sample_image_path)
            i += 1


def explore_one(task_name="apple2orange"):
    BATCH_SIZE = 1
    trainA_dataset, trainB_dataset, testA_dataset, testB_dataset = download_and_processing_cyclegan_dataset(
        task_name, BATCH_SIZE)
    i = 0
    for sampleA, sampleB in zip(trainA_dataset.take(3), trainB_dataset.take(3)):
        show_dataset(sampleA, sampleB, numder=i)
        i += 1


if __name__ == "__main__":
    print("You can choose a task from cycle_gan_dataset_name_list!")
    print(cycle_gan_dataset_name_list)
    task_name = "apple2orange"
    if len(sys.argv) == 2:
        task_name = sys.argv[1]
    print(f"You choose task_name is {task_name}")
    explore_one(task_name)
