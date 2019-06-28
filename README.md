# DeepNude-an-Image-to-Image-technology

**After researching DeepNude technology, I have removed data related to DeepNude. Please don't ask me to get DeepNude.**

## DeepNude's technology stack

![](DeepNude_images/DeepNode_0.png)

+ [Python](https://www.python.org/) + PyQt 
+ [pytorch](https://pytorch.org/)
+ Image-to-Image-technology, You can refer to the paper [Image-to-Image Translation with Conditional Adversarial Networks](https://arxiv.org/abs/1611.07004)

## Image-to-Image-technology (Pix2Pix)
Below is the output generated after training the Pix2Pix model for 200 epochs.

![](DeepNude_images/pix2pix_1.png)

Learn more and hands on [pix2pix.ipynb](https://github.com/tensorflow/docs/blob/master/site/en/r2/tutorials/generative/pix2pix.ipynb)

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
