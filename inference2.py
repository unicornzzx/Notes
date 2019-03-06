"""Run inference a DeepLab v3 model using tf.estimator API."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import sys

import tensorflow as tf

import deeplab_model
from utils import preprocessing
from utils import dataset_util

from PIL import Image
import matplotlib.pyplot as plt

from tensorflow.python import debug as tf_debug

parser = argparse.ArgumentParser()

parser.add_argument('--data_dir', type=str, default='dataset/VOCdevkit/VOC2012/JPEGImages',
                    help='The directory containing the image data.')

parser.add_argument('--model_dir', type=str, default='./model',
                    help="Base directory for the model. "
                         "Make sure 'model_checkpoint_path' given in 'checkpoint' file matches "
                         "with checkpoint name.")

parser.add_argument('--base_architecture', type=str, default='resnet_v2_101',
                    choices=['resnet_v2_50', 'resnet_v2_101'],
                    help='The architecture of base Resnet building block.')

parser.add_argument('--output_stride', type=int, default=16,
                    choices=[8, 16],
                    help='Output stride for DeepLab v3. Currently 8 or 16 is supported.')

parser.add_argument('--debug', action='store_true',
                    help='Whether to use debugger to track down bad values during training.')

_NUM_CLASSES = 21


def main(unused_argv):
  # Using the Winograd non-fused algorithms provides a small performance boost.
  os.environ['TF_ENABLE_WINOGRAD_NONFUSED'] = '1'

  pred_hooks = None
  if FLAGS.debug:
    debug_hook = tf_debug.LocalCLIDebugHook()
    pred_hooks = [debug_hook]

  model = tf.estimator.Estimator(
      model_fn=deeplab_model.deeplabv3_plus_model_fn,
      model_dir=FLAGS.model_dir,
      params={
          'output_stride': FLAGS.output_stride,
          'batch_size': 1,  # Batch size must be 1 because the images' size may differ
          'base_architecture': FLAGS.base_architecture,
          'pre_trained_model': None,
          'batch_norm_decay': None,
          'num_classes': _NUM_CLASSES,
      })


  dataset_dir = '/media/zzx/DATA/frames/'
  save_dir = '/media/zzx/DATA/segmentation/'
  #dataset_dir = '/home/zzx/桌面/test/'
  #save_dir = '/home/zzx/桌面/save/'
  video_types = os.listdir(dataset_dir)[2:3]
  
  #part1 = video_types[0:10]
  for video_type in video_types:
    #print('video_type is: ' + video_type)
    type_dir = dataset_dir + video_type + '/'#原视频类型文件夹目录
    #print('type_dir is: ' + type_dir)
    save_type_dir = save_dir + video_type +'/'
    #print('save_type_dir is: ' + save_type_dir)
    videos = os.listdir(type_dir)#获取同一类型下视频文件的名称
    if not os.path.exists(save_type_dir):#在输出文件夹中创建对应的视频类型文件夹
      os.makedirs(save_type_dir)
      #print('mkdir--save_type_dir: ' + save_type_dir)
    for video in videos:
      video_dir = type_dir + video + '/'#原视频文件夹目录
      save_video_dir = save_type_dir + video +'/'
      #print('video_dir is: '+ video_dir)
      #print('save_video_dir is:' + save_video_dir)
      if not os.path.exists(save_video_dir):#在对应的输出视频类型文件夹中创建对应的输出视频文件夹
        os.makedirs(save_video_dir)
        #print('mkdir--save_video_dir: '+save_video_dir)
      frames = os.listdir(video_dir)#获取所有帧图片文件的名称
      frame_names = [os.path.join(video_dir,frame_name) for frame_name in frames]
      predictions = model.predict(
            input_fn=lambda: preprocessing.eval_input_fn(frame_names),
            hooks=pred_hooks)

      for pred_dict, image_path in zip(predictions, frame_names):
        image_basename = os.path.splitext(os.path.basename(image_path))[0]
        #print('image_basename is: '+image_basename)
        output_filename = image_basename + '_mask.png'
        
        path_to_output = os.path.join(save_video_dir, output_filename)
        #print('path_to_output is: '+path_to_output)
        print("generating:", path_to_output)
        mask = pred_dict['decoded_labels']
        mask = Image.fromarray(mask)
        plt.axis('off')
        plt.imshow(mask)
        plt.savefig(path_to_output, bbox_inches='tight')


if __name__ == '__main__':
  tf.logging.set_verbosity(tf.logging.INFO)
  FLAGS, unparsed = parser.parse_known_args()
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
