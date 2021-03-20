# 10 Dog Classification using Resnet 50

Working API endpoint - https://dog-breed-classification-new.herokuapp.com/predict
Model Training and evaluation - Resnet_50_10_classes.ipynb
Data Directory Preparation - Dog_breed_data_preparation.ipynb


## How to use the API
<hr>

give a Post request to above url with the following json 

    {
        "image" : <base 64 encoded image>
    }

the API will response with the folowing json

    {
        "breed": <predicted dog breed>,
        "score": <confidence score on prediction>
    }
<hr>

# Model Evaluation

## CONFUSION MATRIX

Validation data

![image](https://user-images.githubusercontent.com/57608352/111864464-0a388a80-8987-11eb-8650-5e64c9c8c809.png)


<hr>
Training Data

![image](https://user-images.githubusercontent.com/57608352/111864436-eaa16200-8986-11eb-9acd-9004f224fbbb.png)



## CLASSIFICATION REPORT

Validation Data

                        precision    recall  f1-score   support

                beagle       1.00      1.00      1.00        21
             chihuahua       1.00      0.93      0.97        15
              doberman       0.94      1.00      0.97        15
        french_bulldog       0.80      0.86      0.83        14
      golden_retriever       1.00      1.00      1.00        14
              malamute       1.00      1.00      1.00        17
                   pug       0.85      0.89      0.87        19
         saint_bernard       1.00      1.00      1.00        17
    scottish_deerhound       1.00      0.96      0.98        26
       tibetan_mastiff       1.00      0.93      0.96        14

              accuracy                           0.96       172
             macro avg       0.96      0.96      0.96       172
          weighted avg       0.96      0.96      0.96       172




Training Data

                        precision    recall  f1-score   support

                beagle       1.00      1.00      1.00        84
             chihuahua       1.00      1.00      1.00        56
              doberman       1.00      1.00      1.00        59
        french_bulldog       1.00      1.00      1.00        56
      golden_retriever       1.00      1.00      1.00        53
              malamute       1.00      1.00      1.00        64
                   pug       1.00      1.00      1.00        75
         saint_bernard       0.99      1.00      0.99        67
    scottish_deerhound       1.00      1.00      1.00       100
       tibetan_mastiff       1.00      0.98      0.99        55

              accuracy                           1.00       669
             macro avg       1.00      1.00      1.00       669
          weighted avg       1.00      1.00      1.00       669

# ROC Curve
validation data

![image](https://user-images.githubusercontent.com/57608352/111864474-1ae90080-8987-11eb-922d-3de8a9c18f82.png)

Training Data

![image](https://user-images.githubusercontent.com/57608352/111864484-2a684980-8987-11eb-9622-2e7e1b060d5c.png)
