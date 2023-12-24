# Predicting-and-Analysing-the-Viral-Fragment-of-Songs



## 1. Abstract

This study systematically analyzes viral fragments of songs, particularly those popular on short-form content platforms like TikTok, Instagram Reels, and YouTube Shorts. The analysis focuses on identifying significant features present in viral fragments that distinguish them from the rest of the song. Additionally, the study compares various machine learning models to predict the viral fragment of unseen songs.

## 2. Introduction

Short-form video content, ranging between 15-60 seconds, has gained significant popularity on platforms like TikTok, Instagram Reels, and YouTube Shorts. This study aims to understand the characteristics that make certain song fragments socially popular and seeks to predict popular fragments for new songs. The shift towards vertical video viewing and in-the-moment mobile camera shoots has revolutionized content production and consumption.

## 3. Problem Statement

The project's goal is to analyze song fragments' popularity on short-form content platforms and predict popular fragments for new songs. The analysis involves understanding audio components such as bass, beats, rhythm, and lyrics to derive reasons behind a fragment's popularity.

## 4. Methodology

### 4.1 Data Acquisition

1. **Compilation of Popular Songs:**
   - A comprehensive list of popular songs on short-form content platforms (TikTok, Instagram Reels, YouTube Shorts) was compiled.

2. **Extraction of Viral Soundtracks:**
   - The most viral soundtracks corresponding to the identified popular songs were extracted from the short-form content applications.

3. **Audio File Separation:**
   - The audio files were separated from the extracted videos, and videos without a soundtrack were removed from consideration, as they do not provide information for analysis.

4. **Feature Extraction:**
   - Utilizing the pytube and pafy libraries in Python, features were extracted from the obtained soundtracks to be used for subsequent analysis.

### 4.2 Analysis

1. **Transformation to Amplitude and Sampling Rate:**
   - The data was initially transformed from .mp3 format to amplitude and a sampling rate of 22050.

2. **Exploration of Audio Features:**
   - Different features of the audio files were explored, including:
     - Spectral Centroid
     - Spectral Rolloff
     - Zero Crossing Rate
     - Spectrogram
     - Chromagram

3. **Librosa Library Usage:**
   - The Librosa library played a primary role in the analysis, providing tools for extracting meaningful insights from the audio data.

### 4.3 Modeling

1. **Dataset Creation:**
   - The full song was divided into windows of short duration, creating a dataset for training the models.

2. **Dynamic Time Warping (DTW):**
   - Dynamic time warping, an algorithm for measuring similarity between two temporal sequences, was used. It involved calculating the MFCC values for the audio signals.

3. **Machine Learning Models:**
   - Various machine learning models were implemented for prediction, including:
     - Logistic Regression
     - Weighted Logistic Regression
     - Naive Bayes
     - Support Vector Machines (SVM)
     - Weighted Support Vector Machines (SVM)
     - Random Forest
     - SVM Bagging Classifier

### 5. Performance Evaluation

1. **Model Testing:**
   - Multiple models were created and tested on the test data to assess their predictive capabilities.

2. **Best Model Selection:**
   - The model that predicted clips with the most overlap with the actual viral clip was considered the best.

3. **Evaluation Metrics:**
   - In addition to overlap, various evaluation metrics such as precision, recall, F1 score, and more were considered to comprehensively assess model performance.



## 6. Conclusion

This report presents an approach to predict and analyze the viral fragment of songs, focusing on acoustic features. By extracting MFCC features and building classification models, the study prioritizes recall, given the highly imbalanced dataset. Weighted Logistic Regression and Weighted SVM Classifier emerged as the best models with a recall value of 1.0 and a reasonable accuracy.
