# Text Classifier

Project designed and implemented by **Santiago Fernández González**.

The aim of this project is implementing a program to classify text documents into classes according to their content, such as weather, sports, politics, etc.

#### Table of contents
1. [Information about implementation](#information-about-implementation)
2. [API Reference](#api-reference)
3. [Intruction for use](#instructions-for-use)
4. [Test all possible models](#test-all-possible-models)
5. [Analysis of results](#analysis-of-results)
6. [Known bugs](#known-bugs)

## Information about implementation

All the project was implemented using Python and separating the user interface from the classification library. On the one hand, the graphic interface was built using the web framework Django. I chose this option to be able to deploy the project to a server in production. On the other hand, the classification library was built using the strategy design pattern to achieve better independence between the different algorithms and the classifier itself.

Currently I have implemented the following **algorithms**:

- Parameterization algorithms: TF-IDF, Bag of words and Doc2Vec (a variation of Word2Vec).
- Classification algorithms: Linear Support Vector Classifier (a variation of Support Vector Machines) and Naive Bayes.

>Note: the only combination of algorithms that cannot be used is Doc2Vec with Naive Bayes. The reason is that the feature vector that returns Doc2Vec has negative values and the Naive Bayes algorithm does not accept them.

Respect to the implementation of the **parameterization algorithms**, TF-IDF and BagOfWords work well with the default parameters. However, I had to adjust the parameters of Doc2Vec to fit it better in this type of classification. In addition, it is the slowest algorithm, so it is necessary to find a balance between the accuracy and speed of the algorithm's training. Some of the parameters I modified were the vector size for each word and the number of epochs in the training.

> Note: The models trained with the Doc2Vec algorithm may return different results for consecutive classifications of the same text. This is due to the implementation of the algorithm.

In the case of the **classification algorithms**, I found that the default parameters work well for this type of classification and changing some parameters do not change much the results. However, a deeper research could achieve better results.


Respect to the **Reuters dataset**, I have chosen a implementation available in the *nltk* library. The difference with the original dataset is that it only focuses on the categories that have at least one document in the training set and the test set. After this, the dataset has 90 categories with a training set of 7769 documents and a test set of 3019 documents. In this project I don't use this default split in order to give the user the option of choosing the size of the training set.

This is a list of the categories available in the dataset:

*['acq', 'alum', 'barley', 'bop', 'carcass', 'castor-oil', 'cocoa', 'coconut', 'coconut-oil', 'coffee', 'copper', 'copra-cake', 'corn', 'cotton', 'cotton-oil', 'cpi', 'cpu', 'crude', 'dfl', 'dlr', 'dmk', 'earn', 'fuel', 'gas', 'gnp', 'gold', 'grain', 'groundnut', 'groundnut-oil', 'heat', 'hog', 'housing', 'income', 'instal-debt', 'interest', 'ipi', 'iron-steel', 'jet', 'jobs', 'l-cattle', 'lead', 'lei', 'lin-oil', 'livestock', 'lumber', 'meal-feed', 'money-fx', 'money-supply', 'naphtha', 'nat-gas', 'nickel', 'nkr', 'nzdlr', 'oat', 'oilseed', 'orange', 'palladium', 'palm-oil', 'palmkernel', 'pet-chem', 'platinum', 'potato', 'propane', 'rand', 'rape-oil', 'rapeseed', 'reserves', 'retail', 'rice', 'rubber', 'rye', 'ship', 'silver', 'sorghum', 'soy-meal', 'soy-oil', 'soybean', 'strategic-metal', 'sugar', 'sun-meal', 'sun-oil', 'sunseed', 'tea', 'tin', 'trade', 'veg-oil', 'wheat', 'wpi', 'yen', 'zinc']*

Of course, the number of documents related with each category used to train the model has a lot of influence on the results. Due to this, the categories with few documents will have worse results when trying to classify texts which talk about those topics.

## API Reference

<pre>
class <em>classifierlib.</em> <b>ClassifierModel</b> (<em>param_alg, classif_alg, dataset='Reuters', train_size=.7, saved_model=False</em>)
</pre>


### Parameters:

<pre>
	<b>param_alg : string</b>
		Parameterization algorithm for document representation (to create feature vectors). 

	<b>classif_alg : string</b>
		Classification algorithm. 

	<b>dataset : string, optional (default='Reuters')</b>
		Dataset used for training and testing. 

	<b>train_size : float in range [0.01,0.99], optional (default=.7)</b>
		Percentage of the dataset used for training.

	<b>saved_model : boolean, optional (default=False)</b>
		Only in case you want to use a model already trained. 
</pre>

### Attributes:

<pre>
	<b>models_dir: string</b>
        Relative path where saving the trained models.
</pre>

### Methods:

<pre>
    <b>train (self)</b>
        Train the model
        <em>Returns:</em>
            Accuracy of the model.

    <b>classify (self, texts)</b>
        Classify texts to obtain their topics.
        <em>Parameters:</em>
            <b>texts: array-like</b>
                List of texts to classify.
        <em>Returns:</em>
            List with the topics of the texts.

    <b>available_implementations (self)</b>
        Give information about the implemented algorithms and the saved models.
        <em>Returns:</em>
            String with the information.

    <b>save_model (self)</b>
        Save the model to use it later.

    <b>get_accuracy (self)</b>
        Return the accuracy of the model.
        <em>Returns:</em>
            Accuracy of the model.
</pre>


## Instructions for use

> **Warning**: it is recommended to visit the section [Known bugs](#known-bugs) before using the classifier.

This project was built using **Python 3.7.3** and it is recommended to create an **Anaconda environment** with the dependencies specified in the file *environment.yml*

In the case you want to run the classifier **locally**, after install all the dependencies, you have two options. The first one is using the **terminal**. Example:

```python
from classifierlib.ClassifierModel import ClassifierModel

# Create the model
classifier = ClassifierModel('BagOfWords', 'LinearSupportVectorMachines', train_size=.8)

# Training
classifier.train()
classifier.save_model()
print("Precision: {}".format(classifier.get_accuracy()))

# Classify some texts (defined earlier)
result = classifier.classify([text1,text2,text3])
print(result)

# --------------------------------------------------------
# USE A SAVED MODEL

classifier = ClassifierModel('BagOfWords', 'LinearSupportVectorMachines', saved_model=True)
result = classifier.classify([text1,text2,text3])
print(result)
```

The other option is using the **user interface** by running a Django local server. Due to the dependencies generated by the searchengine module, it is necessary to run the **Elasticsearch** server before running the Django server. This can be done executing the following commands in the terminal:

```
$ cd classificationWebsite/
$ python manage.py runserver
```

Then the server is running in **localhost:8000**. You will need a **user** to use the application:

`user: test`

`password: d73he-9s1_`

In the case you do not want to install everything locally, you can also test the classification application in my server. Just visit [https://textclassifier.online](https://textclassifier.online) and log in with the user I mentioned earlier. That website doesn't have the searchengine module.


## Test all possible models

Now I am goint to analyze the accuracy of the models in some real cases. It is also possible to check the accuracy of all models through the option *"Train all possible models"* in the user interface.

These are the texts used for the tests (they have nothing to do with the test set used after the training):

1. Possible categories: crude, oil, gas

Poland has tapped into its emergency oil reserves in order to keep key refineries operating after contaminated crude oil forced the shutdown of the Druzhba oil pipeline carrying oil from Russia to customers in Europe, the International Energy Agency (IEA) said on Tuesday. “Poland has notified us that they are releasing emergency oil stocks to maintain normal operations at their two refineries supplied on the line,” S&P Global Platts quoted a statement from the IEA. Last week, several countries, including Poland, shut down the flow of Russian crude oil via the Druzhba pipeline after traces of contamination were found. The oil was contaminated with organic chlorine, a substance used in oil production to boost output but dangerous in high amounts for refining equipment. The amounts of the chemical were found to be at levels much higher than the maximum allowable amount.

2. Possible categories: sugar, tea

For some, the thought of drinking tea without sugar might send shivers down their spine. But according to a new study, a spoonful of the sweet stuff isn´t necessary for an enjoyable cuppa. At least, that was the result of a month-long analysis by researchers from University College London and the University of Leeds, who examined the tea-drinking habits of 64 men who usually drank theirs sweetened with sugar. Participants were asked to either stop adding sugar to their tea overnight, gradually reduce the amount of sugar they added, or continue drinking sweetened tea as a control group.

3. Possible categories: coffee

Previous meta‐analysis showed an inverse association between coffee consumption and all‐cause mortality. However, the relationship between caffeinated and decaffeinated coffee consumption and all‐cause mortality is inconsistent. We aimed to identify and review the published evidence updating the association between coffee consumption and all‐cause mortality and, furthermore, to investigate the association of caffeinated and decaffeinated coffee consumption and all‐cause mortality

4. Possible categories: rice, jobs

The claim of millions of jobs in the rice sector was first made by President Buhari in November 2018, when he presented his administration’s scorecard at the time. He was represented at the event by the Minister of Agriculture and Rural Development, Audu Ogbeh. He said: “The impact of our intervention in the rice sector has resulted in job creation, increase in wealth, while reducing migration from rural to urban areas. As of July this year, the number of farmers has increased by 12 million. “The Rice Farmers Association (RIFAN) has five million members. The number of people working in rice mills, small or big is over 1.7 million. These include harvesters, loaders, off-loaders, transporters, distributors and markers.


### Test 1 

Training size: 70%

| parameterizers \ classifiers   | Linear Support Vector Machines | Naive Bayes |
|:------------------------------:|:------------------------------:| :----------:|
| **TF-IDF**                     |        0.953                   |     0.974   |
| **Bag of Words**               |        0.911                   |     0.749   |
| **Doc2Vec**                    |        0.859                   |     -----   |

Results when classifying the texts:
- TF-IDF & Linear Support Vector Machines: [('crude',), ('sugar',), ('coffee',), ('grain', 'rice')]
- TF-IDF & Naive Bayes: [('crude',), (), (), ()]
- Bag of Words & Linear Support Vector Machines: [('crude',), ('earn', 'sugar'), ('coffee',), ('grain', 'rice')]
- Bag of Words & Naive Bayes: [('crude',), ('grain', 'sugar'), ('coffee', 'gnp'), ('grain',)]
- Doc2Vec & Linear Support Vector Machines: [('crude',), ('sugar',), (), ()]

### Test 2

Training size: 90%

| parameterizers \ classifiers   | Linear Support Vector Machines | Naive Bayes |
|:------------------------------:|:------------------------------:| :----------:|
| **TF-IDF**                     |        0.957                   |     0.986   |
| **Bag of Words**               |        0.881                   |     0.690   |
| **Doc2Vec**                    |        0.869                   |     -----   |

Results when classifying the texts: 
- TF-IDF & Linear Support Vector Machines: [('crude',), ('sugar',), ('coffee',), ('grain', 'rice')]
- TF-IDF & Naive Bayes: [('crude',), (), (), ()]
- Bag of Words & Linear Support Vector Machines: [('crude', 'veg-oil'), ('earn', 'sugar'), ('coffee',), ('grain', 'rice')]
- Bag of Words & Naive Bayes: [('crude',), ('grain', 'sugar'), ('coffee', 'gnp', 'grain', 'sugar', 'wheat'), ('grain',)]
- Doc2Vec & Linear Support Vector Machines: [('crude',), ('sugar',), ('coffee',), ('grain',)]

## Analysis of results

As we can observe, the accuracy is quite high. However the results are not so good and despite increasing the number of documents for the training, the results do not change much. In some cases, the lack of success can be due to the shortage of documents to train the model. So I think the solution would be try a bigger dataset for training.


## Known bugs

- There is a bug when trying to load in the terminal a trained model that was saved through the user interface. The same problem happens in the opposite case. This is an error related with the way I save the data from the trained models. I am working on fixing it.