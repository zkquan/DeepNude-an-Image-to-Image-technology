# DeepNude-an-Image-to-Image-technology

**After researching DeepNude technology, I have removed data related to DeepNude. Please don't ask me to get DeepNude.**

## DeepNude's technology stack

![](DeepNude_images/DeepNode_0.png)

+ [Python](https://www.python.org/) + PyQt 
+ [pytorch](https://pytorch.org/)
+ Deep learning computer vision

## Deep learning computer vision(guess)

### Image Inpainting 图像修复
You can refer to the NVIDIA papers [Image Inpainting for Irregular Holes Using Partial Convolutions](https://arxiv.org/abs/1804.07723) and [Partial Convolution based Padding](https://arxiv.org/abs/1811.11718).
Paper code [partialconv](https://github.com/NVIDIA/partialconv)

![](paper_images/2018_NVIDIA_Image_Inpainting.png)

In the image interface of Image_Inpainting(NVIDIA_2018).mp4 video, you only need to use tools to simply smear the unwanted content in the image. Even if the shape is very irregular, NVIDIA's model can “restore” the image with very realistic The picture fills the smeared blank. It can be described as a one-click P picture, and "no ps traces."
The study was based on a team from Nvidia's Guilin Liu et al. who published a deep learning method that could edit images or reconstruct corrupted images, even if the images were worn or lost pixels. This is the current 2018 state-of-the-art approach.

在 Image_Inpainting(NVIDIA_2018).mp4 视频中左侧的操作界面，只需用工具将图像中不需要的内容简单涂抹掉，哪怕形状很不规则，NVIDIA的模型能够将图像“复原”，用非常逼真的画面填补被涂抹的空白。可谓是一键P图，而且“毫无ps痕迹”。
该研究来自Nvidia的Guilin Liu等人的团队，他们发布了一种可以编辑图像或重建已损坏图像的深度学习方法，即使图像穿了个洞或丢失了像素。这是目前2018 state-of-the-art的方法。

### Image-to-Image-technology

#### Pix2Pix (need for paired train data)
You can refer to the paper [Image-to-Image Translation with Conditional Adversarial Networks](https://arxiv.org/abs/1611.07004)

Below is the output generated after training the Pix2Pix model for 200 epochs.

![](paper_images/pix2pix_1.png)

Learn more and hands on [pix2pix.ipynb](https://github.com/tensorflow/docs/blob/master/site/en/r2/tutorials/generative/pix2pix.ipynb) or [pix2pix-keras](https://github.com/williamFalcon/pix2pix-keras).

#### CycleGAN (without the need for paired train data)
CycleGAN uses a cycle consistency loss to enable training without the need for paired data. In other words, it can translate from one domain to another without a one-to-one mapping between the source and target domain.
This opens up the possibility to do a lot of interesting tasks like photo-enhancement, image colorization, style transfer, etc. All you need is the source and the target dataset.
CycleGAN使用循环一致性损失函数来实现训练，而无需配对数据。 换句话说，它可以从一个域转换到另一个域，而无需在源域和目标域之间进行一对一映射。
这开启了执行许多有趣任务的可能性，例如照片增强，图像着色，样式传输等。您只需要源和目标数据集。

You can refer to the paper [Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks](https://arxiv.org/abs/1703.10593)

![](paper_images/2017_Zhu_CycleGAN.png)

Learn more and hands on [cyclegan.ipynb](https://github.com/tensorflow/docs/blob/master/site/en/r2/tutorials/generative/cyclegan.ipynb)


## Windows version of DeepNude use process

> DeepNude can really achieve the purpose of Image-to-Image, and the generated image is more realistic.

![](DeepNude_images/DeepNode_1.png)
![](DeepNude_images/DeepNode_2.png)
![](DeepNude_images/DeepNode_3.png)
![](DeepNude_images/DeepNode_4.png)

Delete the color.cp36-win_amd64.pyd file in the deepnude root directory, and then add the [color.py](color.py) file to get the advanced version of deepnude.

## What can be improved?

1. Size. Including 156M DeepNude_Windows_v2.0.0.zip and 1.90G pyqtlib.rar;
2. Speed. It takes 30 seconds to convert a picture;
3. Content. Use the Image-to-Image neural network to automatically remove the clothes from women to reveal their nudity. This application applies the wrong application of deep learning.

+ DeepNude can be implemented using Tensorflow and uses model compression techniques. 
+ DeepNude should change the current practice of not respecting women.

## Future

In fact, we don't need Image-to-Image. We can use [GANs](https://arxiv.org/abs/1406.2661) to generate images directly from random values or generate images from text.
