# Classification-OpenAI-API: A Hilariously Serious Research Adventure

Welcome to the intriguing world of text classification using OpenAI models accessed via API. Prepare yourself for a journey filled with cutting-edge research, witty experiments, and a touch of humor. In this repository, you'll find the notebook that served as the playground for my text classification adventures. The star of the show? None other than the magnificent `gpt-3.5-turbo` model. However, fear not! The techniques discussed here can be adapted to any OpenAI model that utilizes the `openai.ChatCompletion.create` endpoint. Let's dive in!

## Data Format: Decoding the Enigma

Let's unravel the mystery of the data format we'll be working with. Behold, the enigmatic table:



| id          | text        | HS    | 
| ----------- | ----------- |---|
| 90909      | text-to-classify       |0|
| 10101   | text-to-classify        |1|

S, my dear friend, stands for "Hate Speech." It's the label that will determine whether a piece of text falls into the realm of hate speech (`1`) or if it's free from such negativity (`0`). Remember, it's all about spreading love, even in the data!



## The Research Duo: Two Notebook Wonders

Within this repository, you'll encounter not one, but two extraordinary notebooks. Allow me to introduce you to this dynamic duo:

### 1. Development: Where Curiosity Meets Chaos

In this first notebook, we embark on a thrilling journey of development. Brace yourself as we run five iterations on the test dataset, randomly selecting examples from the train dataset. Oh, and when I say randomly, I mean it! We're talking equal probability [weighting](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html#pandas-dataframe-sample) here, folks! The excitement never ends. After each exhilarating run, I meticulously store the results in a JSON format, capturing the essence of our research.

### 2. Evaluation: Unraveling the Metrics Tapestry

The second notebook is all about evaluation. Here, we gather our findings and weave them into a beautiful tapestry of metrics. We calculate the average of each metric, painting a vivid picture of our text classification prowess. It's a symphony of precision, recall, and F1 scores, with a touch of statistical elegance. Prepare to be amazed!

So, my dear fellow researcher, embark on this captivating expedition with me as we delve into the depths of text classification using OpenAI models. With a mix of top-notch research and a sprinkle of humor, we're bound to uncover fascinating insights and have a great time along the way. Let's begin this enchanting adventure together!

---

Acknowledgement: This readme was written by ChatGPT with my structure and idea :) 
