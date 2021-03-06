# tensorflow code modified by grace gu, then pp

#from __future__ import absolute_import
#from __future__ import division
#from __future__ import print_function
 
#import argparse
#import sys
import numpy as np
import random
 
import tensorflow as tf
import json
import math
import pandas

#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
 
#FLAGS = None
 
#NUM_LOOPS = 10000
#BATCH_SIZE = 100


traits = ["Satisfaction",
    "Like_Parties",
    "Like_HangingOut",
    "Like_Hiking",
    "Like_BoardGames",
    "Like_VideoGames",
    "Like_WatchingTV",
    "Like_WatchingMovies",
    "Like_IndividualSports",
    "Like_TeamSports",
    "Like_ReadingBook",
    "PowerOfVulnerability",
    "FakeVideosOfRealPeople",
    "PharmacyOfTheFuture",
    "HowGreatLeadersInspireGreatAction",
    "LetMyDatasetChangeYourMindset",
    "MagicIngredientBringsLifeToPixar",
    "PowerOfIntroverts",
    "WhatGardeningToldMeAboutLife",
    "WhatIfGentrificationWasAboutHealing",
    "HighSchool_Math",
    "HighSchool_Physics",
    "HighSchool_Chemistry",
    "HighSchool_Bio",
    "HighSchool_English",
    "HighSchool_History",
    "HighSchool_Music",
    "HighSchool_Art",
    "HighSchool_Leader",
    "HighSchool_Engineering",
    "Rank_Understand",
    "Rank_FullOfIdeas",
    "Rank_Imagination",
    "Rank_DifficultyUnderstandingAbstract",
    "Rank_AlwaysPrepared",
    "Rank_AttentionToDetails",
    "Rank_GetChoresDoneRightAway",
    "Rank_ForgetToPutThingsBack",
    "Rank_StartConversations",
    "Rank_TalkToDifferentPeopleAtParties",
    "Rank_ThinkALotBeforeSpeaking",
    "Rank_DislikeGettingAttention",
    "Rank_QuietAroundStrangers",
    "Rank_SoftHeart",
    "Rank_TakeTimeOutForOthers",
    "Rank_MakePeopleFeelAtEase",
    "Rank_NotInterestedInOthersProblems",
    "Rank_FeelLittleConcernForOthers",
    "Rank_GetIrritatedEasily",
    "Rank_HaveFrequentMoodSwings",
    "Rank_WorryAboutThings",
    "Rank_RelaxedMostOfTheTime",
    "Rank_SeldomFeelBlue"]

def arrtotens_input(input_arr):
    pretensors = np.array(input_arr).transpose()
    tensors = [tf.constant(pretensor) for pretensor in pretensors]
    return dict(zip(traits, tensors))

def main():

    pd_df = pandas.read_json("Major_Mapping_Survey_2.json")
    pd_df['Major_2'] = pd_df['Major_2'].replace("", np.nan)
    pd_df1 = pd_df.filter(items = traits + ['Major_1'])
    pd_df2 = pd_df.filter(items = traits + ['Major_2'])
    pd_df2 = pd_df2.dropna(axis=0, subset=['Major_2'])
    pd_df2 = pd_df2.rename({'Major_2': 'Major_1'}, axis = 'columns')
    pd_df = pandas.concat([pd_df1, pd_df2])
    pd_df['Major_1'] = pd_df['Major_1'].replace("Undeclared", np.nan)
    pd_df = pd_df.dropna(axis=0, subset=['Major_1'])

    my_features = pd_df.filter(items = traits)
    target = pd_df['Major_1']

    with open("outdata.json", "r") as read_file:
        major_data = json.load(read_file)
        majors = major_data.keys()
    
    with open("Major_Mapping_Survey_2.json", "r") as read_file:
        data = json.load(read_file)
    '''
    alldataarr =[]
    alllabelsarr = []

    for person in data:
        if person["Major_1"] != "Undeclared":
            alllabelsarr.append(str(person["Major_1"]))
            add_data = []
            for trait in traits:
                if trait in person:
                    if person[trait] != 'N/A' and person[trait] != "":
                        add_data.append(int(person[trait]))
                    else:
                        add_data.append(0)
                else:
                    add_data.append(0)
            alldataarr.append(add_data)

            if person["Major_2"] != "":
                alllabelsarr.append(str(person["Major_2"]))
                alldataarr.append(add_data)

    '''
    input_cols = []
    for trait in traits:
        max_score = 6
        if trait == "Satisfaction":
            max_score = 8
        trait_column = tf.feature_column.categorical_column_with_identity(
            key=trait,
            num_buckets=max_score)
        print(trait_column)
        input_cols.append(trait_column)

    output_column = tf.feature_column.categorical_column_with_vocabulary_list(
        'Major',
        majors
    )
    estimator = tf.estimator.LinearClassifier(feature_columns=input_cols)
    '''
    alldata=arrtotens_input(alldataarr)
    alllabels=tf.constant(alllabelsarr)
    traindata=arrtotens_input(alldataarr[:int(len(alldataarr)*.9)])
    trainlabels=tf.constant(alllabelsarr[:int(len(alllabelsarr)*.9)])
    testdata=arrtotens_input(alldataarr[int(len(alldataarr)*.9):])
    testlabels=tf.constant(alllabelsarr[int(len(alllabelsarr)*.9):])
    '''

    def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
        """Trains a linear regression model of one feature.
      
        Args:
          features: pandas DataFrame of features
          targets: pandas DataFrame of targets
          batch_size: Size of batches to be passed to the model
          shuffle: True or False. Whether to shuffle the data.
          num_epochs: Number of epochs for which data should be repeated. None = repeat indefinitely
        Returns:
          Tuple of (features, labels) for next data batch
        """
      
        # Convert pandas data into a dict of np arrays.
        features = {key:np.array(value) for key,value in dict(features).items()}                                           
     
        # Construct a dataset, and configure batching/repeating.
        ds = tf.data.Dataset.from_tensor_slices((features,targets)) # warning: 2GB limit
        ds = ds.batch(batch_size).repeat(num_epochs)
        
        # Shuffle the data, if specified.
        if shuffle:
          ds = ds.shuffle(buffer_size=10000)
        
        # Return the next batch of data.
        # features, labels = ds.make_one_shot_iterator().get_next()
        return ds# features, labels

    def input_data(features, labels):
        ds = tf.data.Dataset.from_tensor_slices((features, labels))
        ds = ds.shuffle(100).repeat().batch(50)
        return ds

    for op in tf.get_default_graph().get_operations():
        print(str(op.name))

    estimator.train(input_fn = lambda:my_input_fn(my_features, target), steps = 100)
    '''
    # Create the model
    x = tf.placeholder(tf.float32, [None, 53])
    W = tf.Variable(tf.zeros([53, 2]))
    b = tf.Variable(tf.zeros([2]))
    #y = tf.matmul(x, W) + b
    y = tf.nn.softmax(tf.matmul(x, W) + b)
 
    # Define loss and optimizer
    y_ = tf.placeholder(tf.float32, [None, 2])
 
    # The raw formulation of cross-entropy,
    #
    #   tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.nn.softmax(y)),
    #                                 reduction_indices=[1]))
    #
    # can be numerically unstable.
    #
    # So here we use tf.nn.softmax_cross_entropy_with_logits on the raw
    # outputs of 'y', and then average across the batch.
     
    cross_entropy = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
 
    sess = tf.InteractiveSession()
    tf.global_variables_initializer().run()
    # Train
    for _ in range(NUM_LOOPS):
        idx = random.sample(range(len(traindata)), BATCH_SIZE)
        batch_xs = traindata[idx]
        batch_ys = trainlabels[idx]
 
        #batch_xs, batch_ys = diatom.train.next_batch(100)
        
        try:
            sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
        except ValueError:
            print(batch_xs, batch_ys)
            raise ValueError
 
    # Test trained model
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    #print(sess.run(accuracy, feed_dict={x: diatom.test.images,
    #                                    y_: diatom.test.labels}))
 
    acc = sess.run(accuracy, feed_dict={x: testdata, y_: testlabels})
    print(acc)
    prediction=tf.argmax(y,1)
    #print("predictions", prediction.eval(feed_dict={x: testdata}))
    probability=sess.run(y, feed_dict={x: alldata})
    # print(probability)
 
    np.savetxt('probability', probability)
    np.savetxt('accuracy', np.array([acc]))
    '''
if __name__ == '__main__':
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default='C:\\Users\\Priya Pillai\\Documents\\GitHub\\majorsortinghat\\data_analysis',
                                            help='Directory for storing input data')
    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main)
    '''
    main()