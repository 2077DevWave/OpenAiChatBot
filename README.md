# ChatGPT API Module

The ChatGPT API module is designed to help developers create chatbots quickly and easily using the OpenAI API key. It provides several features to develop a chatbot, including text editing, image creation, embedding, and moderation. Additionally, it includes an auto-debugging feature to help you debug your code.

## Features
1. **chat/bot:** This feature allows you to chat with your bot using the OpenAI API. The bot will answer your questions based on your previous messages.
2. **Edit/bot:** This feature allows you to edit your text and code easily with a description.
3. **image/bot:** This feature allows you to create a photo with a description.
4. **embed/bot:** This feature allows you to make an embed of your text or content. It can be useful for deep learning or machine learning applications.
5. **moderation:** This feature allows you to secure your text by reading it and identifying harmful words.

## Requipment
To use this module, you will need to have an OpenAI API key. Once you have obtained the key, you can use the features of the module to develop your chatbot.
> you can get your own api key in [openai](https://platform.openai.com/account/api-keys) website. (login needed)

also you need to install following module to chatbot work correctly:
1. **openai :** chatgpt

> if you want to install requipment automatically run the following code in terminal (cmd):
```
pip install openai
```
OR
```
pip3 install openai
```
## Usage
to develope your chatbot at first you need to create an object from ChatGPT class like this:
```python
chatbot = ChatGPT(api_key='YOUR_API_KEY')
```

some feature need to make an object from feature class, following feature need to make an object:
```python
chatroom = chatbot.chat() # now you can chat with bot
editor = chatbot.edit()   # you can edit your code or text
moderator = chatbot.moderation() # its make your text harmless
```

Also you can use following feature directly:
```python
image = chatbot.image.create_image(prompt="YOUR_DESCRIPTION")  # url
embed = chatbot.embed.create_embed(prompt="YOUR_TEXT")         # json object
```
### Demo
we provide a demo class to test module feature easily, to test any feature you can run codes below:

```python
# Run only one of the lines at the same time

# chat bot feature
ChatGPT(api_key='YOUR_API_KEY').Demo.chat()

# edit code and text
ChatGPT(api_key='YOUR_API_KEY').Demo.edit()

# change text into embed
ChatGPT(api_key='YOUR_API_KEY').Demo.embed()

# generate picture from text
ChatGPT(api_key='YOUR_API_KEY').Demo.image()

#
ChatGPT(api_key='YOUR_API_KEY').Demo.moderation()
```

### Example Usage
Here's an example of how you can use the `chat/bot` feature to chat with your bot:

```python
###### make an object to use chat features ######
chat = ChatGPT.chat()

###### to make a loading just for beauty :) ######
loading = ChatGPT.show.loader()

###### infinite loop ######
while True:

    ###### input #######
    message = input(f"{ChatGPT.config.USER_NAME}: ")

    ###### exit chat rule #######
    if message == "exit":
        break
    else:

        ###### start loader #######
        loading.start()

        ###### send new message #######
        response = chat.send_msg(message)

        ###### stop loader #######
        loading.stop()

        ###### show respond #######
        print(ChatGPT.show.add_symbol(response, type="system"))

###### end infinite loop ######
print("chat ended!")
```
## Conclusion
ChatGPT is a powerful tool for developers who want to build conversational agents, text editors, image generators, and more using OpenAI's GPT-3.5 models. With its easy-to-use interface and powerful modules, ChatGPT makes it easy for developers to harness the power of OpenAI's language models to create innovative applications.
