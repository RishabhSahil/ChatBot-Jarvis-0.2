from bs4 import BeautifulSoup as bs
import requests
import wikipedia as aiwiki
from pywikihow import search_wikihow
import wolframalpha
import webbrowser
import datetime
now = datetime.datetime.now()


try:
    app = wolframalpha.Client("KRJ4JH-GAL9UEAV7X")
except Exception:
    print('Some Feature Are Not Work')

def Search_result(command):
    user_query=str(command)
    try:
        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
        }
        page = requests.get(URL, headers=headers)
        soup = bs(page.content, 'html.parser')
        result = soup.find(class_='zCubwf').get_text()
        return result
    except:
        try:
            result = soup.find(class_='Z0LcW').get_text()
            return result
        except:
            try:
                result = soup.find(class_='hgKElc').get_text()
                return result
            except:
                try:
                    result2 = soup.find(class_='thODed').get_text()
                    return result2 
                except:
                    try:
                        result2 = soup.find(class_='CAEQAQ').get_text()
                        return result2
                    except:
                        try:
                            result2 = soup.find(class_='gsrt vk_bk FzvWSb YwPhnf').get_text()
                            return result2
                        except:
                            try:
                                if 'who invented ' in command:
                                    return "Rishabh kumar"  
                                elif 'wiki' in command:  
                                    query = command.replace("wiki","")
                                    query2 = query.replace("pedia","")     
                                    result_wiki = aiwiki.summary(query2,2)   
                                    return result_wiki  
                                elif "define" in command:   
                                    query = command.replace("define","")  
                                    result_wiki = aiwiki.summary(query,2)   
                                    return result_wiki   
                                elif 'who inve' in command:
                                    return "Rishabh kumar" 
                                elif 'who is rishabh' in command:
                                    return "The Founder of Rishabh Search Engine."    
                                else:
                                    result_wiki = aiwiki.summary(command,2)   
                                    return result_wiki      
                            except:
                                return "Data Not Available, I am Learning...!"         

def Wikisearchall(command):
    try:
        abc=str(command)
        if 'who invented' in command:
            return "Rishabh kumar"  

        elif 'who is rishabh' in command:
            return "The Founder of Rishabh Search Engine." 

        elif "how are you" in command:
            return "I am  Fine?"

        elif "hi" == command or "hey" == command or "who are you" in command:
            return "Hey, I am Jarvis 0.2"

        elif "what is your name" in command:
            return "My name is Jarvis 0.2"

        elif "open rishabh" in command:
            webbrowser.open("https://rishabhsahil.ml")
   
        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")     

        elif 'wiki' in command or "what is" in command or "who is" in command: 
            query=abc.replace('wiki ', '')
            query=abc.replace('wikipedia','')
            query=abc.replace('define','')
            result_wiki = aiwiki.summary(query,2)   
            return result_wiki  

        elif 'define' in command: 
            query=abc.replace('wiki ', '')
            query=abc.replace('wikipedia','')
            query=abc.replace('define','')
            result_wiki = aiwiki.summary(query,2)   
            return result_wiki    

        elif "how to" in command:
            query = str(command)
            text = query.replace("how to","")
            max_result = 1
            how_to_func = search_wikihow(text,max_result)
            assert len(how_to_func) == 1
            how_to_func[0]
            return how_to_func[0].summary

        elif "ip addres" in command or "ip adres" in command:
            try:
                ipAdd=requests.get('https://api.ipify.org').text
                return ipAdd
            except:                                
                print("")

        # elif "joke " in command:
        #     try:
        #         get = pyjokes.get_joke()
        #         return get
        #     except:
        #         pass
                       
        else:
            text_2 = str(command)
            text = text_2.replace("calculate","")
            text_3 = text.replace("ara","patna")
            text_4 = text_3.replace("outside","patna")
            text_5 = text_4.replace("inside","patna")
            try:
                res = app.query(text_5)
                answer=next(res.results).text
                return answer
            except:
                Search_result(command=text_5)

    except:
        Search_result(command=command)       
    # elif "define" in command:   
    #     query = command.replace("define","")  
    #     result_wiki = aiwiki.summary(query,2)   
    #     return result_wiki   
    # elif 'who inve' in command:
    #     return "Rishabh kumar" 
    # elif 'who is rishabh' in command:
    #     return "The Founder of Rishabh Search Engine."    
    # else:
    #     result_wiki = aiwiki.summary(command,2)   
    #     return result_wiki   
                   
def RISHABH(query):
    data01 = query 
    result = Wikisearchall(query)
    if None == result:
        result = Search_result(data01)
    
    return result

# data_save_q = []
# data_save_r = []
# data_save_t = []

def DataSaved(query, reply):
    data = {
        query: reply    
    }
 
# while True:
#     query = input(">> ")
#     reply = RISHABH(query=query.lower())
#     DataSaved(query, reply)
#     # for i in DataSaved(query, reply):
#     #     for j in range(0,1):
#     #         print(DataSaved(query, reply)[i])
#     print(DataSaved(query, reply))