# Copyright 2017 - Demitri Plessas
# 
# Licensed under the GNU General Public License v3.0
# See https://github.com/LocalSymmetry/DetectingQuasars/blob/master/LICENSE
# for more information
# ==============================================================================

import tensorflow as tf
import numpy as np
import pandas as pd
from scipy import ndimage

def ImportImages(ImageFilenames, image_width, image_height):
    '''
    Convert a numpy array of file names into a numpy array of images of the center
    30 pixels by 30 pixels preserving the order of the list of filenames given.
    The numpy array with have dimensions (number_of_images, 30, 30, 3) with 
    the three image channels of Red, Green, and Blue.
    
    Parameters
    ----------
    ImageFilenames : numpy array
        A numpy array of the image filenames to classify from the base
        directory of the python file using this classifier.
    
    image_width : integer
    The number of pixels in the images' width.
    
    image_height : integer        
    The number of pixels in the images' height.
        
    '''
    print('Loading Images...')
    image_array = np.ndarray(shape=(len(ImageFilenames), 30, 30, 3), dtype=np.float32)
    image_num = 0
    width_center = image_width // 2
    height_center = image_height // 2
    for image in ImageFilenames:
        if image_num % 1000 == 0:
            print('Loaded image number %s' % str(image_num))
        try:
            image_data = (ndimage.imread(image).astype(float) - 255.0 / 2) / 255.0
            if image_data.shape != (image_width, image_height, 3):
                raise Exception('Unexpected image shape: %s' % str(image_data.shape))
            image_array[image_num, :, :, :] = image_data[(width_center-16):(width_center+14),(height_center-16):(height_center+14),:]
            image_num = image_num + 1
        except IOError as e:
            print('Could not read:', image, ':', e, ' , skipping.')
            image_num = image_num + 1
    return image_array

def QuasarClassifier(ImageFilenames, image_width, image_height):
    """Quasar Classifier

    Implements the Quasar Classifier trained in [1]. Returns a pandas
    dataframe with the image filename and the model determined
    probability of the image being of a quasar. Images in this model are
    expected to be image_width pixels by image_height pixels. 
    
    NOTE: The model will use the center 30 pixels by 30 pixels to classify, 
    and thus image_width and image_height must be at least 30 pixels each.
    
    Requires the InceptionConvNent.cpkt files from [2].

    Parameters
    ----------
    ImageFilenames : list
        A list of the image filenames to classify using this classifier.  

    image_width : integer
        The number of pixels in the images' width.
    
    image_height : integer        
        The number of pixels in the images' height.
        
        
    References
    ----------
    .. [1] https://github.com/LocalSymmetry/DetectingQuasars/blob/master/Model%20Training.ipynb
    
    .. [2] https://www.dropbox.com/sh/abig8qytnqrnsth/AAAUjNOwqA0M1S2EBzc7DURfa?dl=0
    """

    try:
        if image_height < 30:
            raise Exception('Invalid image_height. Images must be at least 30 pixels by 30 pixels.')
        if image_width < 30:
            raise Exception('Invalid image_height. Images must be at least 30 pixels by 30 pixels.')

        input_images = ImportImages(ImageFilenames, image_width, image_height)
        
        
        ######
        # Model Construction
        #####
    
        # Parameters for the Inception ConvNet.
        step_size = 2500
        remaining_size = input_images.shape[0] % step_size
        patch_size = 7
        num_hidden = 64
        num_channels = 3
        num_classes = 2
        image_size = 30
        # Number of new "channels" from the 7x7 convolution. The first convolution will have depth.
        depth = 128
        reduce_depth = 32 # The reduction of each 1x1 convolution before a large convolution in the inception module 
        inception_output_depth = 64 # The output depth of each convolution in the inception module.
        tunedinceptiongraph = tf.Graph()
        
        # The following function is from the tensorboard tutorial
        # https://www.tensorflow.org/get_started/summaries_and_tensorboard
        def variable_summaries(var):
          """Attach a lot of summaries to a Tensor (for TensorBoard visualization)."""
          with tf.name_scope('summaries'):
            mean = tf.reduce_mean(var)
            tf.summary.scalar('mean', mean)
            with tf.name_scope('stddev'):
              stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
            tf.summary.scalar('stddev', stddev)
            tf.summary.scalar('max', tf.reduce_max(var))
            tf.summary.scalar('min', tf.reduce_min(var))
            tf.summary.histogram('histogram', var)
        
        # Construction of the ConvNet Architecture
        with tunedinceptiongraph.as_default():
                
            # Input batch placeholders
            input_batch_normal = tf.placeholder(tf.float32, shape=(step_size, image_size, image_size, num_channels))
            input_batch_small = tf.placeholder(tf.float32, shape=(remaining_size, image_size, image_size, num_channels))
            
            # Variables for the model
            # Initialize all matrix weights from a truncated normal distribution.
            # Initialize biases as 0 for the first layer, and 1 there after.
            with tf.name_scope('weights'):
                layer1_weights = tf.Variable(tf.truncated_normal(
                        [patch_size, patch_size, num_channels, depth], stddev=0.1), 
                                                name='layer1_weights')
                variable_summaries(layer1_weights)
                    
                # Inception Module Variables
                # The 1x1 convolution that feeds into the 3x3 convolution.
                conv_1_1x1_weights = tf.Variable(tf.truncated_normal(
                        [1, 1, depth, reduce_depth], stddev=0.1), name='conv_1_1x1_weights')
                variable_summaries(conv_1_1x1_weights)
                # The 1x1 convolution that feeds into the 5x5 convolution.
                conv_2_1x1_weights = tf.Variable(tf.truncated_normal(
                        [1, 1, depth, reduce_depth], stddev=0.1), name='conv_2_1x1_weights')
                variable_summaries(conv_2_1x1_weights)
                # The 1x1 convolution that feeds into the concatenation.
                conv_3_1x1_weights = tf.Variable(tf.truncated_normal(
                        [1, 1, depth, inception_output_depth], stddev=0.1), name='conv_3_1x1_weights')
                variable_summaries(conv_3_1x1_weights)
                # The 1x1 convolution that follows the 3x3 max pooling.
                conv_4_1x1_weights = tf.Variable(tf.truncated_normal(
                        [1, 1, depth, inception_output_depth], stddev=0.1), name='conv_4_1x1_weights')
                variable_summaries(conv_4_1x1_weights)
                # The 3x3 convolution that follows conv_1_1x1.
                conv_3x3_weights = tf.Variable(tf.truncated_normal(
                        [3, 3, reduce_depth, inception_output_depth], stddev=0.1), name='conv_3x3_weights') 
                variable_summaries(conv_3x3_weights)
                # The 5x5 convolution that follows conv_1_1x1.
                conv_5x5_weights = tf.Variable(tf.truncated_normal(
                        [5, 5, reduce_depth, inception_output_depth], stddev=0.1), name='conv_5x5_weights') 
                variable_summaries(conv_5x5_weights)
            
                # Fully Connected Layer Variables
                fullconn_weights = tf.Variable(tf.truncated_normal(
                    [(image_size // 2) * (image_size // 2) * inception_output_depth * 4, num_hidden], stddev=0.1),
                        name='fullconn_weights')
                variable_summaries(fullconn_weights)
                outlayer_weights = tf.Variable(tf.truncated_normal([num_hidden, num_classes], stddev=0.1),
                                                name='outlayer_weights')
                variable_summaries(outlayer_weights)
                
            with tf.name_scope('biases'):
                layer1_biases = tf.Variable(tf.zeros([depth]), name='layer1_biases')
                variable_summaries(layer1_biases)
                
                # Inception Module Variables
                # The 1x1 convolution that feeds into the 3x3 convolution.
                conv_1_1x1_biases = tf.Variable(tf.truncated_normal(
                        [reduce_depth], stddev=0.1), name='conv_1_1x1_biases')
                variable_summaries(conv_1_1x1_biases)
                # The 1x1 convolution that feeds into the 5x5 convolution.
                conv_2_1x1_biases = tf.Variable(tf.truncated_normal(
                        [reduce_depth], stddev=0.1), name='conv_2_1x1_biases') 
                variable_summaries(conv_2_1x1_biases)
                # The 1x1 convolution that feeds into the concatenation.
                conv_3_1x1_biases = tf.Variable(tf.truncated_normal(
                        [inception_output_depth], stddev=0.1), name='conv_3_1x1_biases')
                variable_summaries(conv_3_1x1_biases)
                # The 1x1 convolution that follows the 3x3 max pooling.
                conv_4_1x1_biases = tf.Variable(tf.truncated_normal(
                        [inception_output_depth], stddev=0.1), name='conv_4_1x1_biases')
                variable_summaries(conv_4_1x1_biases)
                # The 3x3 convolution that follows conv_1_1x1.
                conv_3x3_biases = tf.Variable(tf.truncated_normal(
                        [inception_output_depth], stddev=0.1), name='conv_3x3_biases')
                variable_summaries(conv_3x3_biases)
                # The 5x5 convolution that follows conv_1_1x1.   
                conv_5x5_biases = tf.Variable(tf.truncated_normal(
                        [inception_output_depth], stddev=0.1), name='conv_5x5_biases')
                variable_summaries(conv_5x5_biases)
            
                # Fully Connected Layer Variables
                fullconn_biases = tf.Variable(tf.constant(1.0, shape=[num_hidden]), name='fullconn_biases')
                variable_summaries(fullconn_biases)
                outlayer_biases = tf.Variable(tf.constant(1.0, shape=[num_classes]), name='outlayer_biases')
                variable_summaries(outlayer_biases)
                    
            # Add the operation to save this model.
            saver = tf.train.Saver()
              
            # The Convolutional Network Architecture.
            def inceptionconvnet(data):
                # First convolutional layer
                with tf.name_scope('Conv1'):
                    conv1 = tf.nn.conv2d(data, layer1_weights, [1, 2, 2, 1], padding='SAME', name='conv1')
                    tf.summary.histogram('pre_activation_Conv1', conv1)
                    # Activation on the first convolution plus biases.
                    hidden1 = tf.nn.relu(conv1 + layer1_biases, name='hidden1')
                    tf.summary.histogram('activation_Conv1', hidden1)
            
                # Inception Module
                with tf.name_scope('Conv3x3'):
                    # Conv_1_1x1
                    conv_1_1x1 = tf.nn.conv2d(hidden1, conv_1_1x1_weights , [1, 1, 1, 1], padding='SAME', name='conv_1_1x1')
                    # Activation on Conv_1_1x1.
                    hiddenconv_1_1x1 = tf.nn.relu(conv_1_1x1 + conv_1_1x1_biases, name='hiddenconv_1_1x1')
                    # Conv_3x3 after Conv_1_1x1
                    conv_3x3 = tf.nn.conv2d(hiddenconv_1_1x1, conv_3x3_weights , [1, 1, 1, 1], padding='SAME', name='conv_3x3')
                    # Activation on Conv_3x3.
                    hiddenconv_3x3 = tf.nn.relu(conv_3x3 + conv_3x3_biases, name='hiddenconv_3x3')
                    tf.summary.histogram('activation_Conv3x3', hiddenconv_3x3)
                     
                with tf.name_scope('Conv5x5'):
                    # Conv_2_1x1
                    conv_2_1x1 = tf.nn.conv2d(hidden1, conv_2_1x1_weights , [1, 1, 1, 1], padding='SAME', name='conv_2_1x1')
                    # Activation on Conv_2_1x1.
                    hiddenconv_2_1x1 = tf.nn.relu(conv_2_1x1 + conv_2_1x1_biases, name='hiddenconv_2_1x1')
                    # Conv_5x5 after Conv_2_1x1
                    conv_5x5 = tf.nn.conv2d(hiddenconv_2_1x1, conv_5x5_weights , [1, 1, 1, 1], padding='SAME', name='conv_5x5')
                    # Activation on Conv_5x5.
                    hiddenconv_5x5 = tf.nn.relu(conv_5x5 + conv_5x5_biases, name='hiddenconv_5x5')
                    tf.summary.histogram('activation_Conv5x5', hiddenconv_5x5)
                    
                with tf.name_scope('MaxPooling'):
                    # Max Pooling
                    maxpool = tf.nn.max_pool(hidden1, ksize=[1,3,3,1], strides=[1,1,1,1], padding='SAME')
                    # 1x1 convolution after pooling
                    conv_4_1x1 = tf.nn.conv2d(maxpool, conv_4_1x1_weights , [1, 1, 1, 1], padding='SAME', name='conv_4_1x1')
                    # Activation on Conv_4_1x1.
                    hiddenconv_4_1x1 = tf.nn.relu(conv_4_1x1 + conv_4_1x1_biases, name='hiddenconv_4_1x1')
                    tf.summary.histogram('activation_MaxPooling', hiddenconv_4_1x1)
                    
                with tf.name_scope('Conv1x1'):
                    # Conv_3_1x1
                    conv_3_1x1 = tf.nn.conv2d(hidden1, conv_3_1x1_weights , [1, 1, 1, 1], padding='SAME', name='conv_3_1x1')
                    # Activation on Conv_3_1x1.
                    hiddenconv_3_1x1 = tf.nn.relu(conv_3_1x1 + conv_3_1x1_biases, name='hiddenconv_3_1x1')                
                    tf.summary.histogram('activation_Conv1x1', hiddenconv_3_1x1)
                    
                # Concatenate Convolutions with activation
                concat_layer = tf.nn.relu(tf.concat([hiddenconv_3x3,hiddenconv_5x5,conv_5x5,hiddenconv_5x5],3))
                    
                with tf.name_scope('FullConn'):
                    # Flatten the convolutions to a 2D tensor for the fully connected layer.
                    reshape = tf.reshape(concat_layer, [-1, (image_size // 2) * (image_size // 2) * inception_output_depth * 4], name='Reshape')
                    # Apply a hidden layer of a fully connected neural network.
                    preactivation3 = tf.matmul(reshape, fullconn_weights, name='preactiviation3')
                    # Activation on the hidden fully conected layer.
                    hidden3 = tf.nn.relu(preactivation3 + fullconn_biases, name='hidden3')
                    tf.summary.histogram('activation_FullConn', hidden3)    
                    # Output layer
                    output = tf.matmul(hidden3, outlayer_weights) + outlayer_biases
                    tf.summary.histogram('activation_output', output)
                        
                return output
                    
            # Output for batch data
            normal_prediction = tf.nn.softmax(inceptionconvnet(input_batch_normal))
            small_prediction = tf.nn.softmax(inceptionconvnet(input_batch_small)) # for the last batch of images
 

        # Due to memory issues, we will run our images through the Inception ConvNet in batches
        input_batch = []
        for i in range((input_images.shape[0] // step_size)+1):
            input_batch.append(input_images[i*step_size:(i+1)*step_size,:,:,:])
        del input_images # To save memory
        
        with tf.Session(graph=tunedinceptiongraph) as session:
            def predict():
                preds = []
                for i in range(len(input_batch)-1):
                    preds.append(normal_prediction.eval(feed_dict={input_batch_normal:input_batch[i]}))        
                preds.append(small_prediction.eval(feed_dict={input_batch_small:input_batch[len(input_batch)-1]}))
                return np.concatenate(tuple([batch for batch in preds]),axis=0)
            saver.restore(session, "./InceptionConvNet.ckpt")
            print("InceptionConvNet restored.")
            Predictions = predict()
       
        Output = pd.DataFrame()
        Output['Filename'] = ImageFilenames
        Output['QuasarProbability'] = Predictions[:,0]
        
        return Output
                 
    except IOError as e:
                print(e)                                   



            