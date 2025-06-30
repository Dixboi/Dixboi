## Unsatisfactory test

**Situation**

Mckenna has been struggling with the Decision Tree model for her dataset.

Although her model performs exceptionally well on the training data, its test performance is far from satisfactory.

Upon consulting her mentor, she was advised to prune the tree. However, Mckenna is unclear about how this would help resolve the issue.

**Explanation**

A Decision Tree is an algorithm with low bias and high variance. A Decision Tree makes almost no assumptions about the target function.

Because of its high variance, Decision Trees overfit easily to the training dataset. Mckenna experienced this when she tested the model on her test data.

To avoid overfitting, Mckenna should prune the tree. By doing so, she forces the tree to generalize better and make assumptions by reducing the number of nodes. In other words, by pruning the tree, she increases its bias and decreases its variance.

## Course notes

**Situation**

Alivia, a student taking a deep learning class on YouTube, is writing notes about the course and wants to capture the correct output size of a convolutional layer.

Her layer receives an input image of size 64x64. She is using a kernel size of 13, padding of 3, and a stride of 2.

What is the output size of the convolutional layer?

**Explanation**

Convolutions have many parameters that influence the output size, so let's go through the properties of the convolutional layer one by one.

First, we know the input size to be 64×64.

Next, we know that the kernel size is 13. This means we will move a sliding window of size 13×13 over the entire image. The window must fit entirely in the picture, so we cannot compute the convolution for the eight rows/columns on the border. Therefore, the resulting output so far would be 52×52.

Adding padding to the image is a way to avoid the reduction of the size. In this case, we added a padding of 3, giving us an extra 6 pixels in each direction for an output of 58x58.

Finally, we have a stride of 2. This means the sliding window will move by two rows/columns every time, reducing each output dimension's size by half.

Therefore, the final output size of the convolutional layer will be 29×29.

## Familiar loss

**Situation**

Adriana is a Machine Learning enthusiast.

She recently learned about "binary cross-entropy" during a colleague's discussion. Although familiar with various Machine Learning techniques, binary cross-entropy was new to her.

She opened a book and started reading about this loss function. Unfortunately, there was a question she couldn't answer.

Which neural network problems should use binary cross-entropy as their loss function?

**Explanation**

Binary cross-entropy is the loss function we use when training binary classifiers. When working on a binary classification task, we categorize every sample into two classes. For example, given images of dogs or cats, a binary classifier will decide whether a picture shows a dog or a cat.

But binary classifiers aren't the only time we use binary cross-entropy.

Binary cross-entropy is also the loss function we use in multi-label classification problems. These are problems where we categorize every sample into one or more classes. For example, organizing movies based on the type of content, for instance, violence, adult language, smoking, or sex, where each film could belong to one or more categories.

In multi-label classification models, the output layer returns values independently. It's helpful to think of a model that outputs ten possible classes as a combination of ten different binary classifiers, and thus binary cross-entropy helps.

Neither multi-class classification nor regression problems use binary-cross entropy.

## Sample arrays

**Situation**

Margot is a data analyst working at a financial technology company. Her team is developing a model to predict stock prices based on various features, such as company performance and market trends.

Margot is using the NumPy library to manipulate the data, and she wants to filter her dataset to return every sample corresponding to class 0. Every feature of her data is stored in a NumPy array `X`, and the target values are in a NumPy array `y`.

Margot can use `X[y == 0, :]` or `X[y == 0]` to filter the data and return every sample that belongs to class 0. To understand how this expression works, we can break it down:

We have `y == 0`, which will return `True` for every sample that belongs to class 0, and `False` otherwise. We use this as a selection mask on the set `X`, which will return every row that belongs to class 0.

To return every feature from `X`, we can use `:`. When slicing arrays, we can use `:` to specify a range of values along a particular axis. In this case, using `:` alone will return every column of the array. In this case, we can accomplish the same by omitting `:`.

The following code snippet illustrates how these two options work:
```
import numpy as np

X = np.array([[2, 1], [4, 3], [6, 5], [8, 7]])
y = np.array([0, 1, 1, 0])
print(X[y == 0, :])
print(X[y == 0])
```

You should get the following result:
```
[[2 1] [8 7]]
[[2 1] [8 7]]
```

## Blog encoding techniques

**Situation**

Stevie is writing a blog post about encoding techniques for handling categorical features in a dataset. She wants to add a fun question at the end of the post to test her readers' understanding of the topic.

She writes many different ideas, and now it's your turn to decide how Stevie should mark each statement.

Which statements regarding Label encoding and One-Hot encoding techniques are correct?

• One-Hot encoding generates new columns for each categorical feature.

• One-Hot encoding creates a unique numerical representation for each categorical feature.

• Label encoding generates two new labels for each categorical feature.

• Label encoding generates new columns for each categorical feature.

**Explanation**

Before analyzing this question, we must understand what "categorical data" means.

Categorical data are variables that contain label values rather than numeric values. For example, a variable representing the weather with values "sunny," "cloudy," and "rainy" is a categorical variable.

Although some algorithms can use categorical data directly, most can't: they require the data to be numeric. We can use One-Hot or Label encoding to do this.

One-Hot encoding creates a new feature for each unique value of the original categorical variable.

For example, assume we have a dataset with a single feature called "weather" that could have the values "sunny," "cloudy," and "rainy." Applying One-Hot Encoding will get us a new dataset with three features, one for each value of the original "weather" column.

A sample that had the value "cloudy" in the previous column will now have the value 0 for both "sunny" and "rainy" and the value 1 under the "cloudy" feature.

On the other hand, Label encoding replaces each categorical value with a consecutive number starting from 0.

For example, Label Encoding would replace our weather feature with a new one containing the values 0 instead of "cloudy," 1 instead of "rainy," and 2 instead of "sunny."

## Chat application

**Situation**

Raegan is a software engineer at a company that builds a chat application. Recently, she started taking an online course on machine learning and came across the concept of splitting datasets before training a model.

Although the course discussed the importance of splitting the data into train, validation, and test sets, it didn't mention why we do this.

Which of the following statements explain why we split a dataset before training a model?

• We split the dataset to prevent the model from overfitting.

• We split the dataset to reduce the memory needed to train the model.

• We split the dataset to make the training process faster.

• We split the dataset to evaluate the model's performance accurately.

**Explanation**

Imagine teaching a math class, and it's time to evaluate your students. You decide to leave them 100 exercises as their homework. These problems cover the content they need to master to ace the exam.

How can you design an exam that effectively identifies those who learned the material?

Let's assume you pick 20 of the same homework exercises and use them in your test. This strategy might result in false positives: students who memorize the solutions to their homework may get a high score, although they don't necessarily know how to reason. In machine learning, we call this "overfitting."

To ensure students don't overfit to their training exercises, you don't want to use the same homework to test their knowledge. Instead, you want to find new problems that evaluate the same material but are different enough to force the students to show their skills.

We want to do the same when training machine learning models. If we only evaluate our work in the same data we use to train the model, we might overfit and have a model that isn't capable of generalizing to different data. In other words, the model may "memorize" the training data and learn to return excellent predictions when tested.

If we split the dataset and leave a portion to evaluate how much the model learned, we will ensure that overfit won't happen. Therefore, we can accurately assess the model's performance and avoid overfitting.

## Animal characteristics

**Situation**

Kaylani is the tech lead of a project that aims to classify pictures of animals based on 10 different characteristics. Each animal can have one or more of these features, so the system should recognize and tag the animal photos appropriately.

The team used a convolutional neural network to build this system. The only question that remains is the best approach for designing the network.

Which would be the best approach for Kaylani and her team to design the network for classifying the photos?

• Kaylani should use a sigmoid activation function in the output layer. The loss function should be binary cross-entropy.

• Kaylani should use a sigmoid activation function in the output layer. The loss function should be categorical cross-entropy.

• Kaylani should use a softmax activation function in the output layer. The loss function should be binary cross-entropy.

• Kaylani should use a softmax activation function in the output layer. The loss function should be categorical cross-entropy.

**Explanation**

The team is trying to build a multi-label classification model. Every animal will be classified with one or more of the 10 characteristics in multi-label classification. This differs from multi-class classification, where every animal will only be classified into one category.

When building multi-label classification models, we need an output layer where every class is independent. Remember that we can have more than one active class for each input. The softmax activation function doesn't work because it uses every score to output the probabilities of each class.

Softmax is the correct output for multi-class classification. Sigmoid is the correct output for multi-label classification problems. The sigmoid function converts output scores to a value between 0 and 1, independently of all the other scores.

Multi-label classification problems borrow the same principles from binary classification problems. The difference is that we end up with multiple sigmoid outputs instead of one. In our example problem, we combine three different binary classifiers. This is why we should use a binary cross-entropy as the loss function.

In summary, multi-class classification models should use a softmax output with the categorical cross-entropy loss function. Multi-label classification models should use a sigmoid output and the binary cross-entropy loss function.

## Marine biologist

**Situation**

Aniyah is a marine biologist using machine learning to study the migratory patterns of various sea creatures. She needs to determine how close different species are to one another during their migrations.

Aniyah is considering using clustering algorithms like K-Means. These algorithms require measuring the similarity between observations in her dataset.

Euclidean distance is one of the most popular distance metrics for this task.

From the following list, select every correct statement about the Euclidean distance.

• The Euclidean distance between two points does not depend on which of the two points is the start and which is the destination. In other words, the distance between p and q is the same as between q and p.

• The Euclidean distance is a way to compute the distance between two points in two-dimensional spaces. The Euclidean distance doesn't work in multidimensional spaces.

• The Euclidean distance between two distinct points is always positive.

• Traveling from a point p to a point q via a point r cannot be any shorter than traveling directly from p to q.

**Explanation**

In one or more dimensions, we can use the Euclidean distance. For example, in a line, the distance between two points is the numerical difference between their coordinates. In a plane, the distance is the Pythagorean distance.

But can we use it in multidimensional spaces?

The answer is yes; the Euclidean distance works in multidimensional spaces. Intuitively, this should make sense because we can use it as the metric to compute the distance between multi-feature observations in our dataset.

The distance from a point p to another point q is the same regardless of whether we start from p or q. This distance is always a positive value as long as p and q are different points. If p and q are the same point, the distance is 0.

In the Euclidean plane, the distance between any two distant points is the length of the line segment joining them. So this segment joining points p and q can't be any shorter, regardless of whether we get from p to q via a third point r.

## Piece replacement

**Situation**

Lucille is a data scientist writing an article about a model developed to predict if a piece of equipment has to be replaced.

The model takes in the piece's characteristics and outputs a prediction based on the relationships between the input features and the target variable.

Lucille wants to explain how the coefficients, the parameters learned by the model during training, influence the final prediction.

Which of the following options represents the best way for Lucille to describe the role of the coefficients in the model?

• A positive coefficient suggests that the feature does not affect the prediction.

• A negative coefficient suggests that the feature does not affect the prediction.

• A positive coefficient suggests that the feature has a higher probability of positively affecting the prediction.

• A positive coefficient suggests that the feature has a higher probability of negatively affecting the prediction.

**Explanation**

The coefficients in the context of a model are the parameters learned by the model during training. They determine the relationship between the input features and the output predictions.

In this example, the coefficients are used to predict whether the piece has to be replaced. The coefficients weigh the input features and determine the final prediction.

The best way to describe the role of the coefficients is by saying that a positive coefficient indicates that the variable is more likely to influence the outcome positively. This means that the variable has a positive relationship with the target variable and increases the probability of the target being positive.

On the other hand, a negative coefficient indicates that the variable has a higher likelihood of negatively influencing the outcome. This means that the variable has a negative relationship with the target variable and decreases the probability of the target being positive.

## Specific outcomes

**Situation**

Tessa is a data scientist working in the field of Computer Vision. She has been assigned a project that involves building a model to predict specific outcomes based on visual data.

Before training her model, Tessa divides her dataset into a training set and a test set. She understands that shuffling the dataset before dividing it is crucial in ensuring accurate results.

What is the primary reason for shuffling the dataset before dividing it into a training and test set?

• To make sure the training set contains more data than the test set.

• To make sure the features in the training and test sets are the same.

• To make sure the class labels are evenly split between the training and test sets.

• To make sure the training set contains the same number of samples as the test set.

**Explanation**

The main reason for shuffling the dataset before dividing it into a training and test set is to ensure that the class labels are evenly distributed between the two sets.

This is important because if the class labels are not evenly distributed, one of the sets might not contain data that belongs to some of the labels. For example, assuming our dataset is sorted by the class label, we might assign every sample from one class to the training set and every sample from another to a test set.

Shuffling the dataset helps to mitigate this issue by randomly reordering the data, which helps to ensure that the training and test sets are representative samples of the entire data population.

## Main technique

**Situation**

Clara is a data scientist working for a weather forecasting company.

The company wants to improve its temperature forecasting capabilities, so Clara is tasked with building a model that can accurately predict the temperature of a city based on meteorological data such as humidity, pressure, wind speed, and previous temperature records.

Fortunately, she has access to labeled meteorological data and temperatures dataset, so she should be OK with building a model.

Which of the following is the main technique Clara should use to solve this task?

• Clustering

• Regression

• Classification

• Dimensionality Reduction

**Explanation**

The primary technique that Clara should use to solve this problem is regression.

Regression is a supervised learning technique that predicts a continuous value based on input features. In this example, Clara wants to predict the temperature of a city based on meteorological data such as humidity, pressure, wind speed, and previous temperature records. The temperature is a continuous value.

To do this, she will use a dataset of temperature records, with meteorological data and their corresponding temperature values. She can train a model to make predictions on new, unseen data.

## Soccer department

**Situation**

Joanna works in the analytics department of a soccer team. She analyzes player performance data to determine potential strategies for upcoming games.

Joanna is given a dataset with four categorical columns, one of which is the target value she needs to predict. The target class has two possible values. The three features each have 3, 3, and 2 possible values, respectively.

Joanna must generate a synthetic dataset with all unique samples, excluding duplicates.

What will be the length of this dataset?

• The length of the dataset will be 8.

• The length of the dataset will be 18.

• The length of the dataset will be 36.

• The length of the dataset will be 64.

**Explanation**

The length of a synthetic dataset will depend on the number of possible combinations of values that can be generated based on the number of possible values for each attribute.

To determine the number of possible combinations, we can calculate the product of the number of possible values for each attribute. In Joanna's case, there are 3 possible values for the first attribute, 3 for the second attribute, 2 for the third attribute, and 2 for the target class.

The product of these values is 3 x 3 x 2 x 2 = 36. This means Joanna's synthetic dataset will have 36 different examples, each with a different combination of values for the four columns.

## Perplexing problem

**Situation**

Despite their best efforts, Nicole's team was facing a perplexing problem: their machine learning model was not generalizing well to the test data.

Exhausted and ready to reconsider their approach, the team was about to regroup when Nicole had a sudden idea.

She took the training dataset, removed the target variable, and combined it with the test data. Then, she created a new binary target, assigning a 1 to every test sample and a 0 to every training sample.

"Train a classifier on this new dataset, and let's see how accurate the predictions are," she instructed her team.

Her team appeared puzzled. What is Nicole attempting to accomplish?

• This classifier will estimate how different the training data is from the test data, potentially explaining why the team is struggling.

• This classifier will turn the initial problem into a more straightforward approach that will serve as a baseline for the team to continue their work and find a better solution.

• This classifier will estimate the performance of the team's model on unseen test data. It will help the team understand whether they are overfitting or underfitting the training data.

• Combining the training and test data is never a good idea, so this classifier's results will not be valid.

**Explanation**

Nicole's approach should be familiar if you have experience participating in Kaggle competitions.

Popular validation techniques, like cross-validation, allow you to test your models on unseen data if that data comes from the same distribution as your training dataset. Unfortunately, that's not always the case, and even slight differences between the training and test data will considerably affect the result of your model.

Adversarial validation is a technique to estimate the difference between your training and test data. The Kaggle Book introduces it as follows:

[adversarial validation] was long rumored among Kaggle participants and transmitted from team to team until it emerged publicly, thanks to a post by Zygmunt Zając on his FastML blog.

Nicole created a new dataset by joining the training and test data. The target of that new dataset is a binary variable differentiating the training and test samples. She can determine how easy it's to separate both datasets by running a classifier on that new data.

Adversarial validation relies on computing the ROC-AUC, a graph showing the True Positive Rate and the False Positive Rate at different classification thresholds. The area under this curve (AUC) measures the model's performance. A perfect model will have an area of 1.0, while a model that only makes mistakes will have an area of 0.0.

If they run the classifier and the ROC-AUC is around 0.5, Nicole will know that the training and test data are not easily distinguishable, which is good because it means the data comes from the same distribution. If the ROC-AUC is too high—closer to 1.0—the classifier can tell training and test data apart, which means they come from a different distribution.

Adversarial validation is a very clever technique. The result could help explain the team's struggle and guide it to continue.

## Learning hackathon

**Situation**

Jayla was participating in a machine learning hackathon with her teammates, working to develop a solution for a complex problem.

As the team brainstormed ideas, they started discussing the pros and cons of various algorithms. Jayla knew that some models were more sensitive to changes in training data than others.

Which of the following algorithms can be considered high-variance models?

• Decision Trees

• Linear Regression

• Logistic Regression

• k-Nearest Neighbors (KNN)

**Explanation**

Every machine learning algorithm deals with three types of errors: bias, variance, and irreducible error. We need to focus specifically on the variance error to answer this question.

Here is what Jason Brownlee has to say about variance: "Variance is the amount that the estimate of the target function will change if different training data was used."

In other words, variance refers to how much the answers given by the model will change if we use different training data. The model has high variance if the answers differ significantly when using different portions of our training dataset.

Generally, non-linear machine learning algorithms with a lot of flexibility are high variance. For example, Decision Trees and k-Nearest Neighbors are high-variance models. Linear models, on the other hand, are usually low-variance.

## NOR logic gate

**Situation**

We want to use a Perceptron to represent the NOR logic gate. As a reminder, here is how the NOR gate works:

0 nor 0 = 1
0 nor 1 = 0
1 nor 0 = 0
1 nor 1 = 0
Our Perceptron will have two inputs, two weights, and a bias parameter.

Which of the following parameters will make our Perceptron act as a NOR gate?

• w1 = -1.0, w2 = -1.0, b = 1.0

• w1 = 0.5, w2 = 0.5, b = -0.1

• w1 = -2.0, w2 = -1.0, b = 0.8

• You need more than one Perceptron to represent the NOR gate.

**Explanation**

We can represent a NOR gate using a single Perceptron. Here is a simple implementation with two input values, x1 and x2:
```
def perceptron(x1, x2, w1, w2, b):
    return int((x1*w1 + x2*w2 + b) > 0)
```
Using this function, we can try the different configurations suggested in this question. Here is an example of running the Perceptron for the NOR gate using a set of parameters:
```
w1 = -1.0
w2 = -1.0
b = 1.0
assert perceptron(0, 0, w1, w2, b) == 1
assert perceptron(0, 1, w1, w2, b) == 0
assert perceptron(1, 0, w1, w2, b) == 0
assert perceptron(1, 1, w1, w2, b) == 0
```
Notice how each assert validates a specific pair of inputs. If there are no errors, then we can conclude the parameters work.

## Smart home system

**Situation**

Phoenix is working on a Machine Learning model to optimize the energy consumption of a smart home system. She wants to implement the Gradient Descent optimization algorithm to train her model.

To balance the trade-off between computation speed and update accuracy, Phoenix is considering using Mini-Batch Gradient Descent. She wants to understand its benefits and characteristics.

Which of the following statements is true about Mini-Batch Gradient Descent?

• Mini-Batch Gradient Descent requires loading the entire dataset into memory for each update iteration.

• Mini-Batch Gradient Descent updates the model weights only after processing all the available training data.

• Mini-Batch Gradient Descent uses a batch of data (more than one sample but fewer than the entire dataset) during every iteration.

• Mini-Batch Gradient Descent is not a variant of Gradient Descent.

**Explanation**

Gradient Descent is a popular optimization algorithm in machine learning. It minimizes an objective function by iteratively updating the model weights based on the function's gradient. The number of samples used to compute the gradient in each iteration can vary.

Using a single sample is called Stochastic Gradient Descent (SGD). Using all the data at once is called Batch Gradient Descent. Using a batch of data—more than one sample but fewer than the entire dataset—is called Mini-Batch Gradient Descent.

Mini-Batch Gradient Descent strikes a balance between computation speed and update accuracy. It leverages the benefits of both Stochastic Gradient Descent and Batch Gradient Descent by processing multiple samples in each iteration. This approach allows for more accurate updates than SGD while being computationally more efficient than Batch Gradient Descent, which requires loading the entire dataset into memory.


## Straightforward and fast

**Situation**

While working on a data analysis project, Blair used the K-Means algorithm. This was her first time working with a clustering algorithm.

K-Means was straightforward and fast. Blair had all the code written in a few hours, but something was missing.

The documentation mentioned the "elbow method," but Blair wasn't sure how it would help her.

Which of the following statements is true about the elbow method?

• The elbow method determines the optimal number of clusters.

• The elbow method detects outliers present in a dataset.

• The elbow method pinpoints the biases within a dataset.

• The elbow method determines which features best explain observed patterns in a dataset.

**Explanation**

The elbow method is a way to determine the optimal number of clusters.

When running K-means, you can run the algorithm with a range of values of k, and for each value, calculate the sum of squared errors. Then, you can plot a line chart of these errors for each value of k.

If the line chart looks like an arm, then the "elbow" on the arm is the best number of clusters (k) that you should use.

The elbow method is a way to choose the point where diminishing returns are no longer worth the cost. It's a very popular technique when using clustering algorithms.

## Platform recommendations

**Situations**

Kendall is a data scientist at a tech company building a recommendation system for its e-commerce platform.

Before looking into more complex models, she wants to establish a good baseline. Kendall is considering trying two different models: a simple neural network and a linear regression model.

Which of the following statements are true for both Kendall's neural network and linear regression model?

• Both models require numeric inputs between 0 and 1, so Kendall must standardize the values.

• Both models need numeric input features, so Kendall must convert non-numeric features.

• The result from both models is the linear sum of weighted inputs.

• The result from both models is a probability vector.

**Explanation**

Although it is generally true that both models would perform better with scaled or standardized input features, neither model explicitly requires features to be within the range of 0 to 1.

Both neural networks and linear regression models require input features to be numeric. They cannot handle categorical features directly, so Kendall must transform non-numeric features before using them in either model.

The output of a linear regression model is a single numerical value, not a vector of probabilities. Neural networks do not necessarily have to produce such output either.

Lastly, while linear regression and neural networks involve a linear sum of weighted inputs, neural networks introduce non-linearities through activation functions. This key difference makes neural networks more powerful than linear regression.

## Fascinating trees

**Situation**

Amina, a software engineer passionate about problem-solving, recently became interested in machine learning. As she ventured into this new domain, she began experimenting with various models.

Soon, Amina discovered Decision Trees and found them fascinating. The model provided a unique balance of power and complexity.

Eager to share her enthusiasm, Amina started recommending Decision Trees to her colleagues who were also new to machine learning.

Which of the following statements would Amina likely mention as an advantage of using a Decision Tree?

• The predictions generated by a Decision Tree are easy to interpret and explain.

• A Decision Tree can solve regression and classification tasks.

• A Decision Tree is very resistant to overfitting.

• A Decision Tree doesn't require tuning to get good predictions.

**Explanation**

As a developer, Decision Trees have always made sense.

I'm not talking about building a good Decision Tree but how they work to find predictions. In a short sentence, a Decision Tree is just a bunch of nested conditions that get us to the final solution.

And this property is precisely what makes them very popular: we can look at a prediction and fully understand why the model arrived at that conclusion. In other words, the predictions generated by Decision Trees are easy to interpret, an essential advantage of using Decision Trees over more obscure techniques, like neural networks or Support Vector Machines.

Decision Trees, unfortunately, are prone to overfitting if we don't take careful care of their depth. In other words, unless we ensure our tree doesn't go too deep, it will tend to fit noisy samples and output the wrong prediction. We can control overfitting in a Decision Tree by "pruning."

Remember that while a single Decision Tree is prone to overfitting, using an ensemble of trees is more resistant. Here is a quote from "To Boost or not to Boost: On the Limits of Boosted Neural Networks":

[these experiments] confirm that training single large decision trees is prone to overfitting while boosted ensembles of decision trees are resistant to overfitting.

Many people relate Decision Trees with classification tasks, but they are also valuable for solving regression tasks. A classification task is when the predicted outcome is a discrete class, while the result of a regression task is a Real number. This flexibility makes Decision Trees very useful.

Finally, we discussed above how Decision Trees are prone to overfit if we aren't careful with their depth. This is just one of the hyperparameters that we can tune. Like with most techniques, Decision Trees require experimentation and tuning to improve the quality of their results.

## Studying errors

**Situation**

Collins is new to machine learning and has been studying tensors, an important data structure in the field.

As she dives deeper, she comes across various attributes related to tensors and wants to determine which ones accurately describe a tensor.

Which of the following are valid attributes that represent a tensor?

• Rank: This attribute refers to the number of dimensions, or axes, in the tensor.

• Interaction: This attribute describes the connections between the tensor's axes.

• Shape: This attribute represents the number of elements in each dimension.

• Cardinality: This attribute represents the numerical relationship between the tensor axes.

**Explanation**

Three primary attributes define a tensor:

1. Its rank, or the number of axes.
2. Its shape or the number of dimensions.
3. Its data type or the type of data contained in it.

The rank of a tensor refers to the tensor's number of axes.

Examples:

- Rank of a matrix is 2.
- Rank of a vector is 1.
- Rank of a scalar is 0.

The shape of a tensor describes the number of elements along each dimension.

Examples:
```
() — scalar
(2,) — vector
(3, 2) — matrix
(3, 2, 5) — 3D tensor
```

The data type of a tensor refers to the data type it stores:

Examples:
```
float32
float64
uint8
int64
```

## Reinforcement description

**Situation**

Reinforcement learning, also known as reinforcement machine learning, is a subcategory of machine learning and artificial intelligence.

Which of the following is the correct description of Reinforcement learning?

• Reinforcement learning is a type of machine learning where the model is not given any labeled training data. Instead, the model is only given a set of unlabeled data and is expected to discover the relationships and patterns within the data on its own.

• Reinforcement learning is a type of machine learning where the model is trained on labeled data, which consists of input data and corresponding correct output labels. The model can then make predictions on new, unseen data by using the patterns it learned from the training data.

• Reinforcement learning is a type of machine learning that involves training an agent to take action in an environment to maximize a reward. This is done through a process of trial and error, where the agent receives feedback in the form of rewards or punishments based on its actions and uses this feedback to adjust its behavior and improve its performance over time.

• Reinforcement learning is a type of machine learning where the training data consists of a mixture of labeled and unlabeled examples. It leverages the availability of labeled examples to improve the model's performance while still making use of the vast amount of unlabeled data that is often available.

**Explanation**

Reinforcement learning is a type of machine learning that involves training an agent to take action in an environment to maximize a reward. This is done through a process of trial and error, where the agent receives feedback in the form of rewards or punishments based on its actions and uses this feedback to adjust its behavior and improve its performance over time.

Unsupervised learning is a type of machine learning where the model is not given any labeled training data. Instead, the model is only given a set of unlabeled data and is expected to discover the relationships and patterns within the data on its own.

Supervised learning is a type of machine learning where the model is trained on labeled data, which consists of input data and corresponding correct output labels. The model can then make predictions on new, unseen data by using the patterns it learned from the training data.

Finally, Semi-supervised learning is a type of machine learning where the training data consists of a mixture of labeled and unlabeled examples. It leverages the availability of labeled examples to improve the model's performance while still making use of the vast amount of unlabeled data that is often available.

## Social campaign

**Situation**

Milani works at a marketing agency that specializes in social media campaigns.

The agency has collected vast text data from various social media platforms but lacks labels. To optimize future campaigns, Milani wants to classify the sentiment of each text sample. However, she knows she cannot proceed with supervised learning without labeled data.

Milani must decide on a technique for obtaining labels for the data.

Which of the following techniques could Milani use to label the data?

• Hire a team to review and label each text sample manually.

• Use user reactions or comments on the text samples to automatically generate labels.

• Apply a supervised learning method to deduce the labels directly from the existing data.

• Implement semi-supervised learning to spread labels across the entire dataset.

**Explanation**

To use a supervised learning method, Milani needs to produce labels for the data. There are various techniques she can use to achieve this.

The most common approach to labeling data is by using human labelers. Milani could hire a team to review each text sample and assign an appropriate sentiment label (e.g., positive, negative, or neutral).

Sometimes, feedback from existing interactions can be used to create labels, known as "direct labeling." For instance, Milani could use likes, dislikes, or other reactions to text samples on social media platforms to approximate the sentiment. Although direct labeling may not always capture the "true ground truth," it is a viable approach.

The third choice suggests using a supervised learning method to infer the labels from the existing dataset. However, this is not feasible since supervised learning requires labels, which Milani lacks.

Lastly, semi-supervised learning could be used if Milani already had a small portion of labeled data. The method would then generate labels for the remaining data. However, there is no indication that Milani has any labeled data, making semi-supervised learning an unsuitable option.

Other techniques to generate labels include active learning and weak supervision.

## Implementing neural networks

**Situation**

Maggie is learning to implement neural networks and has discovered the importance of using non-linearities.

She learned that if she doesn't add non-linearities to the model, the network won't solve the problem.

Which of the following options will add non-linearities to Maggie's neural network?

• Using convolution operations as part of the network.

• Using Stochastic Gradient Descent to train the network.

• Implementing the backpropagation process.

• Using Rectifier Linear Unit (ReLU) as an activation function.

**Explanation**

For a neural network to learn complex patterns, we must ensure that the network can approximate any function, not only linear ones. This is why we call it "non-linearities."

The way we do this is by using activation functions.

An interesting fact: the Universal approximation theorem states that, when using non-linear activation functions, we can turn a two-layer neural network into a universal function approximator. This is an excellent illustration of how powerful neural networks are.

Some of the most popular activation functions are sigmoid and ReLU.

A convolution operation is a linear operation. You can check this answer in Stack Exchange for an excellent explanation.

Finally, neither Stochastic Gradient Descent nor backpropagation has anything to do with the linearity of the network operations.

## Sister dice

**Situation**

Alayah has a box containing a 6-sided and a 12-sided die.

She asks her sister to randomly pick one out, roll it, and share the result. Her sister tells her that the result is 2.

What is the probability that Alayah's sister picked the 6-sided die?

• The probability is 1/2

• The probability is 2/3

• The probability is 3/4

• The probability is 1/3

**Explanation**

Let's assume that A represents the event of rolling the die and getting a 2, B1 represents pulling out the 6-sided die, and B2 represents pulling out the 12-sided die.

We can compute the probability that Alayah's sister picked the 6-sided die using the Bayes theorem:
```
P(B1|A) = (P(A|B1)*P(B1))/P(A)
P(B1|A) = (1/12)/P(A)

P(A) = P(A|B1)*P(B1)+P(A|B2)*P(B2)
P(A) = 1/12 + 1/24​
P(A) = 1/8

P(B1|A) = (1/12)/(1/8)
P(B1|A) = 2/3​
```
Thus, the answer is 2/3.

## Convolutional paper

**Situation**

Annabelle is writing a paper about convolutional layers.

Her examples are small images of size 8x8. Annabelle wants to find different combinations of parameters for the convolutional layer that give her a similar-sized output.

Assuming Annabelle inputs an 8x8 picture to a convolutional layer, which of the following parameters will give her an output size of 2x2?

• Kernel size = 7, Padding = 0, Stride = 1

• Kernel size = 5, Padding = 0, Stride = 2

• Kernel size = 7, Padding = 2, Stride = 4

• Kernel size = 5, Padding = 2, Stride = 4

**Explanation**

To compute the output size, we can use the following formula:

`output = 1 + (input + 2 * padding - kernel) / stride`
Running every choice through this formula will give you the output of every case is the same 2x2.

Convolutions have many parameters that influence the output size. We can go through the properties of the convolutional layer one by one and complete one of the examples.

First, we know the input size to be 8x8.

Next, we know that the kernel size is 7. This means we will move a sliding window of size 7×7 over the entire image. Assuming a stride of 1, the output of this operation will be 2x2.

Adding padding to the image is a way to avoid the reduction of the size. In the first example, we didn't add any padding.

Finally, we have a stride of 1. This means the sliding window will move by one row and column every time. Since that's the stride we assumed at the beginning, the final output size of the convolutional layer will be 2×2.

You can apply the same thinking to every example.

## Significant impact

**Situation**

Trinity just started reading a book about machine learning and came across the concept of model coefficients.

She learned that coefficients are parameters learned by a machine learning model during training.

Trinity wants to understand how these coefficients can be used to determine the impact of a feature on a prediction. Specifically, she wants to know how to determine if a feature significantly impacts the prediction based on the coefficients.

How can Trinity determine if a feature significantly impacts the prediction based on the coefficients?

• A positive coefficient indicates that a feature significantly impacts the prediction.

• A negative coefficient indicates that a feature significantly impacts the prediction.

• The coefficient with a large magnitude indicates that a feature significantly impacts the prediction.

• The coefficients do not indicate the relationship between the feature and target variable.

**Explanation**

The coefficients in the context of a model are the parameters learned by the model during training. They determine the relationship between the input features and the output predictions.

Each feature in the model is assigned a coefficient, a numerical value representing that feature's importance in the prediction.

If a feature has a large magnitude coefficient, it has a strong relationship with the target variable and, therefore, significantly impacts the prediction. On the other hand, if a feature has a small magnitude coefficient, it means that it has a weak relationship with the target variable and, therefore, has a less significant impact on the prediction.

The sign of the coefficient only indicates the direction of the relationship between the feature and target variable but does not indicate the strength of the relationship.

In summary, the magnitude of the coefficient is the key factor that indicates the significance of a feature in the prediction.

## Climate researcher

**Situation**

Joanna is a climate change researcher.

She wants to analyze satellite images of the Amazon rainforest to spot deforestation hotspots to help policymakers act preventively. Joanna built a shallow neural network to predict deforestation patterns, but it's not as accurate as she'd like.

A deep neural network could be better.

What should Joanna do to transform her shallow neural network into a deep one?

• Joanna should change the activation function in the existing layers.

• Joanna should change the type of input data she's using.

• Joanna should add more layers to the network.

• Joanna should use a different optimization algorithm.

**Explanation**

Joanna should add more layers to the network to transform a shallow neural network into a deep one. A deep neural network is an artificial neural network with multiple layers between the input and output layers. The more layers we add, the "deeper" the network becomes.

Changing the activation function in the existing layers might affect the model's performance, but it won't make the network deeper. Activation functions play a role in introducing non-linearities, but they don't affect the depth of the network.

Changing the type of input data would not make the network deeper. Instead, it would likely require a model modification to accommodate the new data type, which doesn't address the depth issue.

A different optimization algorithm could improve the training process and performance but won't deepen the neural network. Optimization algorithms help minimize the loss function but don't increase the network's depth.

## Half the records

**Situation**

Celeste evaluated her model in a dataset with 10,000 records and got an accuracy of 90%.

She collected 1,000 new records and added half to the training set and the other half to the test set. After training a new model, she evaluated it with 10,500 records, and the accuracy decreased to 88%.

Which of the following is a valid conclusion about Celeste's model?

• Celeste's model is worse than before.

• Celeste's model is better than before.

• Celeste's model is the same as before.

• We don't know exactly whether Celeste's model is better or worse.

**Explanation**

When Celeste added 1,000 new records and split them between the training and test sets, the distribution of the test set changed. Since the new test set has a different distribution, we cannot directly compare the model's accuracy before and after adding the new records.

The decreased accuracy from 90% to 88% does not necessarily mean the model is worse.

It could be that the new data is more challenging for the model, or the model has improved in certain aspects but is not apparent in the overall accuracy. To accurately assess whether the model is better or worse, Celeste must evaluate the models on the same data with the same underlying distribution.

Here is a hypothetical scenario of two models illustrating how Model 2 could improve even when returning a lower accuracy:

- Model 1 accuracy on 10,000 records: 90% (9,000 records correctly classified.)
- Model 1 accuracy on the new 500 records: 10% (50 records correctly classified.)
- Model 2 accuracy on the 10,000 records: 91% (9,100 records correctly classified.)
- Model 2 accuracy on the new 500 records: 28% (140 records correctly classified.)
- Model 2 accuracy on the 10,500 records: 88% (9,240 records correctly classified.)

In this hypothetical example, Model 2 is better on the original 10,000 records (91% versus 90%) and the 500 new records (28% versus 10%.) But its accuracy is worse with the 10,500 test set (88% versus 90%.)

This is called the Simpson's paradox. When comparing two experiments, we need to make sure that we evaluate the same data or at least data having the same underlying distribution. If we change the distribution, we can't compare the results and may make the wrong conclusion.

## Explring birds

**Situation**

Cali is an avid birdwatcher and has decided to use her passion for birds to explore the capabilities of deep neural networks.

She gathers a diverse dataset of bird images covering different species, habitats, and behaviors. With this dataset, Cali begins experimenting with deep neural networks to see how well they can classify the images and recognize the distinct characteristics of each species.

Which of the following statements reasonably simplifies how the network operates?

• The earlier layers of a neural network compute simpler features than deeper layers.

• The deeper layers of a neural network compute more complex features than earlier layers.

• The earlier layers of a neural network compute more complex features than deeper layers.

• The deeper layers of a neural network compute simpler features than earlier layers.

**Explanation**

Think of a bird picture. You'll see the eyes, feathers, beak, and other characteristics. Notice how groups of pixels form edges, shapes, and the rest of the bird's features.

A reasonable explanation for how a neural network works are to assume that earlier layers focus on detecting more basic features, like edges and shapes of the image. Later layers could use these earlier pieces to form more recognizable shapes, like the eyes and beak of the bird.

While the network deals with pixels early on, the deeper we go into it, the more it will work with complete patterns until it reaches the output layer.

## Bias balance

**Situation**

Amari is working on a complex project involving a dataset with multiple features and non-linear relationships between them. She understands that the success of her machine learning model depends on finding the right balance between bias and variance.

A high-bias model makes more assumptions about the target function, which can lead to underfitting. On the other hand, low-bias models make fewer assumptions, allowing them to capture complex patterns more effectively.

Given the complexity of her project, Amari wants to avoid high-bias algorithms.

Which of the following algorithms should Amari stay away from?

• Linear Regression

• Neural Networks

• Random Forest

• Decision Trees

**Explanation**

Every machine learning algorithm deals with three types of errors: bias, variance, and irreducible error. We need to focus specifically on the bias error to answer this question.

Here is what Jason Brownlee has to say about bias: "Bias are the simplifying assumptions made by a model to make the target function easier to learn."

In other words, bias refers to the model's assumptions to simplify finding answers. The more assumptions it makes, the more biased the model is.

Often, linear models are high-bias. They are easier to understand but make too many assumptions about the target function, preventing them from performing well on complex problems. Linear and logistic regression are two examples of high-bias models.

Nonlinear models are usually low-bias. Decision Trees and k-Nearest Neighbors are two examples.


## Photos from the app

**Situation**

Briella is developing a machine learning model to classify photos from users for their company's new app.

She wants to use a Convolutional Neural Network, but a colleague suggested using a fully-connected neural network, arguing that it's a simpler approach.

Which of the following are good reasons for Briella to use a Convolutional Neural Network?

• Convolutional Neural Networks can learn a hierarchy of visual features similar to the human brain, which results in better performance.

• The number of parameters required for a Convolutional Neural Network is typically smaller than that of a fully-connected network.

• Convolutional Neural Networks are usually shallower than fully-connected networks, making the training process easier and faster.

• Convolutional Neural Networks can classify images even when the training data is highly imbalanced, without additional pre-processing steps.

**Explanation**

A Convolutional Neural Network (CNN) is a much better choice when dealing with image classification problems than a fully-connected network.

A CNN can learn visual features of increasing complexity. The initial layers typically learn to recognize low-level details, like edges and colors, while deeper layers can handle more complex structures, like corners and patterns. The final layers of a CNN can learn complex representations like faces or any complex objects.

CNNs require fewer parameters than fully-connected networks and reuse the same parameters over the whole image. The number of weights in a convolutional layer depends on the kernel size and the number of channels, not the image resolution. For example, in the AlexNet architecture, the five convolutional layers are responsible for only 4% of the parameters of the network. In comparison, the final three fully-connected layers contain the remaining parameters.

A CNN is more time and memory efficient than a fully-connected network, so we can use deeper networks with many layers, which is impossible in a fully-connected network. You should always expect CNNs to be deeper than fully-connected networks.

Finally, a CNN is not inherently immune to the issues caused by imbalanced datasets. When the training data is highly imbalanced, the model will likely be biased toward the majority class, which can lead to reduced performance in the minority class. Like a fully-connected network, a CNN requires appropriate handling of imbalanced datasets to ensure accurate and unbiased performance.

## Trading used cars

**Situation**

Emma worked at an online platform for trading used cars. Given her background in data science, she was tasked with building an automatic price recommendation system.

A crucial step in this project was to analyze the Manufacturer's Suggested Retail Price (MSRP) of the cars, which was the target variable for the predictive model.

One afternoon, while going through the data, she decided to plot a histogram of the MSRP to understand its distribution better.

Which of the following statements are correct regarding the distribution plot of the MSRP?

• The tail of the distribution is the histogram section that gradually decreases on one side.

• The head of the distribution is the area where the values are densely concentrated.

• A long tail in the histogram implies many values are widely spread away from the head.

• The head of the distribution falls right at the center of the histogram.

**Explanation**

Visualizing a histogram can definitely provide a lot of insight into the distribution of a variable.

The head of the distribution is the area where a significant number of values are concentrated. The position of this area is not necessarily at the center of the histogram, especially if the histogram is skewed to one side.

The distribution's tails are the histogram's parts that start narrowing down. When many values are spread out far from the head of the distribution, this is known as a long tail. You can see an example of a long tail in this image.
