
# AI Models for Customer Service Platform

This repository is part of a larger customer service platform project and focuses on the AI models developed for automating various aspects of customer service. We implemented four key models in this project:

- **Classification Model**: This model classifies customer chats into predefined categories.
- **Sentiment Model**: This model performs sentiment analysis on customer chats, determining whether the sentiment is positive, negative, or neutral.
- **Summary Model**: This model generates summaries of long customer chats.
- **Labeling Model**: This model labels customer chats based on predefined categories.
- **Semantic Search**: Performs a semantic search based on the provided question.

## Repository Structure

The repository is organized into three main directories:

1. **datasets**:  
   This directory contains the datasets used during the development of the models. The final dataset, which concatenates all other datasets, is also included here by name "Combined_Customer_Chat_Dataset".

2. **docker_config & API**:  
   This folder contains all the necessary configurations for deploying the models using FastAPI and Docker. It includes:
   - `main.py`: The FastAPI configuration file.
   - Docker-related files and dependencies for easy deployment of the AI models.

3. **models**:  
   This directory contains three Jupyter notebooks:
   - One for the **classification model** and its evaluation.
   - One for the **sentiment analysis model**.
   - One for the **summary and labeling models**.

## Datasets

The dataset used for training and evaluating the models was generated using GPT-4, following this prompt:

```
I want a dataset for NLP text classification and sentiment analysis tasks. I want this dataset so I can evaluate my models accuracy.
The domain target will be Customer chats and reviews, i want to classify the customer chat with the admins to number of classes. like: ["order","complaint","feedback",etc..]

##The dataset Structure##
The dataset should consist of 3 cols:
1) "chat_history"
2) "target_class"
3) target_sentiment"
* The first column is the chat history between the customer and the admin. it may be in Arabic or English.
* The second column is the class of this chat. your classes will be ["feedback", "support", "orders","complaint", "other"].
* The third column will be the sentiment of this chat. it will be "positive", "negative" or "natural".

## Dataset Size ##
The size of dataset should be containing 50 samples or rows.

## Dataset format ##
The format of the dataset should be csv file

## Examples ##
1)
chat_history: '''Customer: I can't log in to my account. Admin: Let me assist you.'''
target_class: "support"
target_sentiment: "negative"

2)
chat_history: '''Customer: I love your service! Admin: Thank you!'''
target_class: "feedback"
target_sentiment: "positive"

3)
chat_history: '''Customer: I'm not happy with my order. Admin: I'm sorry to hear that.'''
target_class: "complaint"
target_sentiment: "negative"

4)
chat_history: '''Customer: لقد أضفت طلبي ولكني لم أتلقى تأكيد بعد. Admin: سنتحقق من الأمر.'''
target_class: "orders"
target_sentiment: "negative"

## Notes ##
1) The dataset should not contain any duplicates.
2) The dataset should be balanced in "target_class" and "target_sentiment"
3) The dataset should contain "chat_history" examples in Arabic and English
4) Use your text classification model to find the "target_class" correctly. and take your all time to do that
5) Use your sentiment analysis model to find the "target_sentiment" correctly. and take your all time to do that.
6) Use three quotes like this ''' ''' not this " "
7) This is very important!: Before you generate the "target_class" and "target_sentiment" and the dataframe. make sure the length of the "chat_history" is exactly 50 to avoid errors, the three columns must be in the same length in the code.
```

## Deployment

### To deploy the models using Docker and FastAPI:
1. Ensure Docker is installed and running.
2. Navigate to the `docker_config_API` folder and run the following command for building the docker image:
   ```bash
   docker build --tag instahub-test .
   ```
   After that, run this command to run the container
   ``` bash
   docker run --name insthub-container-2 -d -p 8000:8000 instahub-test
   ```
3. The FastAPI application will be running and ready to handle API requests for classification, sentiment analysis, summarization, and labeling.

### To use the API by cloud
You can access this link:
```
instahub-docker-hub-gwdpdpdje3c8daen.germanywestcentral-01.azurewebsites.net\docs
```


For any issues or contributions, feel free to open a pull request or raise an issue.


