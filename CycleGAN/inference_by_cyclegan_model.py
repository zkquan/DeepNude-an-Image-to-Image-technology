import tensorflow as tf
import matplotlib.pyplot as plt
import os
import sys
from dataset_utils import download_and_processing_cyclegan_dataset, cycle_gan_dataset_name_list
from cyclegan_model import unet_generator, discriminator


def generate_images(idx, model, test_input, store_produce_image_dir):
    idx = idx + 1
    if not os.path.exists(store_produce_image_dir):
        os.mkdir(store_produce_image_dir)

    prediction = model(test_input)

    fig = plt.figure(figsize=(24, 24))

    display_list = [test_input[0], prediction[0]]
    title = ['Input Image', 'Predicted Image']

    for i in range(2):
        plt.subplot(1, 2, i + 1)
        plt.title(title[i])
        # getting the pixel values between [0, 1] to plot it.
        plt.imshow(display_list[i] * 0.5 + 0.5)
        plt.axis('off')
    save_image_path = os.path.join(store_produce_image_dir, f'{str(idx)}_{title[i]}.png')
    plt.savefig(save_image_path)
    # plt.show()
    plt.close(fig)


class CycleGAN_Inference_Manager(object):
    def __init__(self, checkpoint_path='./training_checkpoints', OUTPUT_CHANNELS=3):
        self.create_model_restore_weight(checkpoint_path, OUTPUT_CHANNELS)

    def create_model_restore_weight(self, checkpoint_path, OUTPUT_CHANNELS):
        # create model
        # B = generator_g(A), A = generator_f(B)
        self.generator_g = unet_generator(OUTPUT_CHANNELS, norm_type='instancenorm')
        self.generator_f = unet_generator(OUTPUT_CHANNELS, norm_type='instancenorm')

        discriminator_x = discriminator(norm_type='instancenorm', target=False)
        discriminator_y = discriminator(norm_type='instancenorm', target=False)

        generator_g_optimizer = tf.keras.optimizers.Adam(2e-4, beta_1=0.5)
        generator_f_optimizer = tf.keras.optimizers.Adam(2e-4, beta_1=0.5)

        discriminator_x_optimizer = tf.keras.optimizers.Adam(2e-4, beta_1=0.5)
        discriminator_y_optimizer = tf.keras.optimizers.Adam(2e-4, beta_1=0.5)

        ckpt = tf.train.Checkpoint(generator_g=self.generator_g,
                                   generator_f=self.generator_f,
                                   discriminator_x=discriminator_x,
                                   discriminator_y=discriminator_y,
                                   generator_g_optimizer=generator_g_optimizer,
                                   generator_f_optimizer=generator_f_optimizer,
                                   discriminator_x_optimizer=discriminator_x_optimizer,
                                   discriminator_y_optimizer=discriminator_y_optimizer)

        ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=5)

        # if a checkpoint exists, restore the latest checkpoint.
        if ckpt_manager.latest_checkpoint:
            ckpt.restore(ckpt_manager.latest_checkpoint)
            print('Latest checkpoint restored!!')
        else:
            print("Not found checkpoint!")

    def get_test_dataset(self, task_name="apple2orange", BATCH_SIZE=1):
        # prepare data
        _, _, testA_dataset, testB_dataset = download_and_processing_cyclegan_dataset(task_name, BATCH_SIZE)
        return testA_dataset, testB_dataset


if __name__ == "__main__":
    task_name = "apple2orange"
    print("You can choose a task from cycle_gan_dataset_name_list!")
    print(cycle_gan_dataset_name_list)
    if len(sys.argv) == 2:
        task_name = sys.argv[1]
    print(f"You choose task_name is {task_name}")

    inference_data_number = 5
    BATCH_SIZE = 1
    checkpoint_path = "./checkpoints/train"
    store_produce_image_dir_A2B = 'inference_images_A2B'
    store_produce_image_dir_B2A = 'inference_images_B2A'

    # create CycleGAN_Inference_Manager
    cyclegan_infer = CycleGAN_Inference_Manager(checkpoint_path)

    # prepare data
    testA_dataset, testB_dataset = cyclegan_infer.get_test_dataset(task_name, BATCH_SIZE)

    # Run the trained model on the test dataset
    # B = generator_g(A), A = generator_f(B)
    for idx, inp_A in enumerate(testA_dataset.take(inference_data_number)):
        generate_images(idx, cyclegan_infer.generator_g, inp_A, store_produce_image_dir_A2B)

    for idx, inp_B in enumerate(testB_dataset.take(inference_data_number)):
        generate_images(idx, cyclegan_infer.generator_f, inp_B, store_produce_image_dir_B2A)
