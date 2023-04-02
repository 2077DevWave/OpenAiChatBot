from chatgpt import ChatGPT

api_key = 'YOUR_API_KEY'

###### make an object to use chat features ######
chat = ChatGPT(api_key=api_key).chat()

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