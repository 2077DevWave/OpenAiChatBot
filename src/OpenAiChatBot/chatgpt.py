##########################################################################################
##                                                                                      ##
## see Features and Documentation on github https://github.com/2077DevWave/ChatGPT-API  ##
##                                                                                      ##
##########################################################################################
import os
import platform
import subprocess
import threading
import winreg
import openai
import time

class ChatGPT:

    def __init__(self, api_key: str):
        '''
        we need an api key to access into openai
        your api key must be like this: 'sk-************************************************'
        
        '''
        openai.api_key = api_key

    class config:
        USER_NAME = "You"
        ASSISTANT_NAME = "ChatGPT"

    class chat:

        AI_MODEL = ""

        class Models:
            CHAT_GPT4 = "gpt-4"
            CHAT_GPT40314 = "gpt-4-0314"
            CHAT_GPT432K = "gpt-4-32k"
            CHAT_GPT432K0314 = "gpt-4-32k-0314"
            CHAT_GPT35TURBO = "gpt-3.5-turbo"
            CHAT_GPT35TURBO0301 = "gpt-3.5-turbo-0301"

        chat_msg: list[dict] = [
            {"role": "system", "content": "You are a helpful assistant."}]
        all_msg: list[str] = []

        def send_msg(self, msg: str):
            if self.AI_MODEL == "":
                self.AI_MODEL = self.Models.CHAT_GPT35TURBO
            self.chat_msg.append({"role": "user", "content": msg})
            chat_response = openai.ChatCompletion.create(
                model=self.AI_MODEL, messages=self.chat_msg)
            chat_response = chat_response.choices[0].message.content
            self.chat_msg.append({"role": "assistant", "content": msg})
            return chat_response

        def last_msg(self):
            return self.all_msg[-1]

        def save_chat(self):
            with open(file="chat_msg.txt", mode="w") as f:
                f.writelines(self.all_msg)

    class edit:

        def __init__(self, mode="text"):
            if mode == "text":
                self.AI_MODEL = self.Models.TEXT_EDITOR
            elif mode == "code":
                self.AI_MODEL = self.Models.CODE_EDITOR

        AI_MODEL = ""

        class Models:
            TEXT_EDITOR = "text-davinci-edit-001"
            CODE_EDITOR = "code-davinci-edit-001"

        def send_request(self, content: str, instruction: str):
            if ChatGPT.edit.AI_MODEL == "":
                ChatGPT.edit.AI_MODEL = ChatGPT.edit.Models.TEXT_EDITOR
            response = openai.Edit.create(
                model=self.AI_MODEL, input=content, instruction=instruction)
            response = response.choices[0].text
            return response

    class image:
        class Size:
            LARGE = "1024x1024"
            MEDIUM = "512x512"
            SMALL = "256x256"

        def create_image(prompt: str, size: str = Size.LARGE):
            respond = openai.Image.create(
                prompt=prompt, size=size, n=1, response_format="url")
            return respond.data[0].url

    class embed:
        def create_embed(prompt: str):
            respond = openai.Embedding.create(
                model="text-embedding-ada-002", input=prompt)
            return respond.data[0].embedding

    class moderation:

        def __init__(self):
            ChatGPT.moderation.AI_MODEL = ChatGPT.moderation.Models.STABLE

        AI_MODEL = ""
        data : dict = {}

        class Models:
            STABLE = "text-moderation-stable"
            LATEST = "text-moderation-latest"

        def create_moderation(self, prompt: str):
            respond = openai.Moderation.create(
                model=self.AI_MODEL, input=prompt)
            self.data = respond.results[0]
            return respond.results[0]

        def its_safe(self):
            for key,value in self.data.categories.items():
                if value:
                    return False
            return True

    class show:

        class loader:

            def __init__(self, msg: str = f"System is thinking... "):
                self.msg = msg
                self.stat = [True]

            def start(self):
                self.stat[0] = True
                threading.Thread(
                    target=ChatGPT.show.loader.loader_thread, args=(self,)).start()

            def stop(self, cond=False):
                self.stat[0] = cond
                time.sleep(1)

            def loader_thread(self):
                while self.stat[0]:
                    for i in ["/", "|", "-", "\\"]:
                        print(f"\r{self.msg} {i}", end="")
                        time.sleep(0.05)
                print("\r", end="")

        def change_assistant_name(assistant_name):
            if assistant_name != "":
                ChatGPT.config.ASSISTANT_NAME = assistant_name

        def change_user_name(user_name):
            if user_name != "":
                ChatGPT.config.USER_NAME = user_name

        def add_symbol(msg, type="system"):
            if type == "system":
                return f"{ChatGPT.config.ASSISTANT_NAME}: {msg}"
            elif type == "user":
                return f"{ChatGPT.config.USER_NAME}: {msg}"

    class Demo:

        def chat():
            ###### make an object to use chat features ######
            chat = ChatGPT.chat()
            
            ###### infinite loop ######
            while True:

                ###### input #######
                message = input(f"{ChatGPT.config.USER_NAME}: ")

                ###### exit chat rule #######
                if message == "exit":
                    break
                else:

                    ###### start loader #######
                    loading = ChatGPT.show.loader()
                    loading.start()
                    
                    ###### send new message #######
                    response = chat.send_msg(message)

                    ###### stop loader #######
                    loading.stop()

                    ###### show respond #######
                    print(ChatGPT.show.add_symbol(response, type="system"))

            ###### end infinite loop ######
            print("chat ended!")

        def edit():
            ###### explanation #######
            print("its edit content with some instructions like spell check or edit code")

            ###### input #######
            editor_type = input(f"you're content type (text or code): ")
            content = input(f"enter your content: ")
            instruction = input(f"enter your instruction: ")

            ##### loading #######
            loading = ChatGPT.show.loader()
            loading.start()

            ###### create obj from class #######
            editor = ChatGPT.edit(editor_type)

            ##### send request with editor #######
            response = editor.send_request(
                content=content, instruction=instruction)

            ##### stop loader #######
            loading.stop()

            ##### show respond #######
            print(response)

        def image():

            ###### inputs #######
            desc = input("Enter your image description : ")

            ##### loading #######
            loading = ChatGPT.show.loader()
            loading.start()

            ##### send request to create image url #######
            image = ChatGPT.image.create_image(
                prompt=desc, size=ChatGPT.image.Size.LARGE)

            ##### stop loader #######
            loading.stop()

            ##### show respond #######
            print(image)

        def embed():
            ###### inputs #######
            text = input("Enter your text : ")

            ##### loading #######
            loading = ChatGPT.show.loader()
            loading.start()

            ##### send request to create embed url #######
            embed = ChatGPT.embed.create_embed(
                prompt=text)

            ##### stop loader #######
            loading.stop()

            ##### show respond #######
            print(embed)

        def moderation():
            ###### inputs #######
            text = input("Enter your text : ")
            
            ###### create obj from class #######
            moderator = ChatGPT.moderation()
            
            ###### check text in ai #######
            result = moderator.create_moderation(prompt=text)
            
            ###### check result #######
            print(moderator.its_safe())   # False its means text have some unsafe word
        
    class debug:

        def __init__(self):
            print("debug mode maybe need you system password to change some settings \n if you dont want to insert your password you can change settings manually in document available at https://github.com/davinci-ai/ChatGPT/blob/master/")

        SYSTEM_OS = ""

        def __init__(self):
            if platform.system() == "Windows":
                self.SYSTEM_OS = ChatGPT.debug.system.WINDOWS
            elif platform.system() == "Linux":
                self.SYSTEM_OS = ChatGPT.debug.system.LINUX
            elif platform.system() == "Darwin":
                self.SYSTEM_OS = ChatGPT.debug.system.MAC

        class system:
            WINDOWS = "Windows"
            MAC = "MacOS"
            LINUX = "Linux"

        def Access_denied(self, connection_name="Wi-Fi"):
            if self.SYSTEM_OS == "Linux":
                # Replace the values below with the DNS server addresses you want to use
                dns_servers = ['178.22.122.100', '185.51.200.2']

                # Generate the DNS server lines to be written to the resolv.conf file
                dns_lines = [f'\nnameserver {ip}' for ip in dns_servers]

                # Write the DNS server lines to the resolv.conf file using sudo
                with open('/tmp/resolv.conf', 'w') as f:
                    f.writelines(dns_lines)
                os.system('sudo cp /tmp/resolv.conf /etc/resolv.conf')

                # Restart the networking service to apply the new DNS settings
                os.system('sudo systemctl restart systemd-resolved.service')

                print("DNS settings applied successfully")

            if self.SYSTEM_OS == "Windows":
                # os.system(f"netsh interface ipv4 set dns \"{connection_name}\" static 178.22.122.100 primary")

                # Replace the values below with the DNS server addresses you want to use
                dns_servers = ['8.8.8.8', '8.8.4.4']

                # Set the registry key values for the primary and secondary DNS servers
                dns_values = [int(ip.split('.')[-1]) for ip in dns_servers]
                dns_keys = [
                    f'DNSServerAddress{i+1}' for i in range(len(dns_servers))]

                # Open the registry key for network adapter settings
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 0, winreg.KEY_ALL_ACCESS) as key:
                    # Set the primary and secondary DNS server values
                    for i, dns_key in enumerate(dns_keys):
                        winreg.SetValueEx(
                            key, dns_key, 0, winreg.REG_DWORD, dns_values[i])

                # Refresh the network settings by releasing and renewing the IP address
                subprocess.run(['ipconfig', '/release'])
                subprocess.run(['ipconfig', '/renew'])

            if self.SYSTEM_OS == "MacOS":
                # os.system(f"sudo networksetup -setdnsservers {connection_name} 178.22.122.100")

                # Replace the values below with the DNS server addresses you want to use
                dns_servers = ['8.8.8.8', '8.8.4.4']

                # Generate the DNS server lines to be written to the resolv.conf file
                dns_lines = [f'nameserver {ip}' for ip in dns_servers]

                # Write the DNS server lines to the resolv.conf file using sudo
                with open('/tmp/resolv.conf', 'w') as f:
                    f.write('\n'.join(dns_lines))
                os.system('sudo cp /tmp/resolv.conf /etc/resolv.conf')

                # Restart the mDNSResponder service to apply the new DNS settings
                os.system('sudo killall -HUP mDNSResponder')


