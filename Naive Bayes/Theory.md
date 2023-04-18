
# Naive Bayes
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Naive Bayes is a classification algorithm that is based on Bayes' theorem. It is a simple yet powerful algorithm that is widely used in machine learning for text classification, spam filtering, sentiment analysis, and other related applications.

## Bayes' Theorem
Bayes' theorem is a mathematical formula that describes the probability of an event, based on prior knowledge of conditions that might be related to the event. In the context of machine learning, it is used to calculate the probability of a class label given a set of features or attributes.

## Naive Bayes Algorithm
The Naive Bayes algorithm is called "naive" because it assumes that all features or attributes are independent of each other, which is often not true in real-world scenarios. Despite this simplification, Naive Bayes has shown to be very effective in many applications.

The algorithm works by first _calculating the prior probability_ of each class label based on the training data. Then, for a new input, it calculates the probability of each class label given the input features using Bayes' theorem. Finally, it selects the class label with the highest probability as the output.

## Types of Naive Bayes
There are three main types of Naive Bayes classifiers:

1.**Gaussian Naive Bayes**: Assumes that the input features follow a Gaussian distribution.

2.**Multinomial Naive Bayes**: Used for discrete data such as text, where each feature represents the count of a particular word.

3.**Bernoulli Naive Bayes**: Used for binary data, where each feature represents the presence or absence of a particular word.

## Advantages and Limitations
The advantages of Naive Bayes include its simplicity, speed, and ability to handle high-dimensional data. However, its assumption of independence between features can lead to suboptimal performance in some cases. Additionally, Naive Bayes can suffer from the "zero-frequency problem" when a feature has not been observed in the training data for a particular class label.
