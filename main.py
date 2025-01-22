import os
import openai

#GLOBALS
cstrCaptionSumRes = "Please summarize my resume: " 
cstrCaptionRes = "The following is a summary of my resume: "
cstrCaptionRole = "Could you please write me a professional coverletter for the following job description: "
def main():
    strRoleDescription = input("Please copy and paste the description for your role from the job board: ")
    
    strGPTAPIKey = ""
    if os.path.isfile("./api_keys/apiKey.txt"):
        with open("./api_keys/apiKey.txt","r") as f:
            strGPTAPIKey = f.read()
    else: 
        strGPTAPIKey = input("No api key for ChatGpt detected. Please copy and paste your api key here: ")
        # TODO: put in error catching in case the api key doesn't work
        with open("./api_keys/apiKey.txt","w+") as f:
            f.writelines(strGPTAPIKey)
    openai.api_key = strGPTAPIKey

    blnResumeExists = False
    strResume = ""
    if os.path.isfile("./resume/resume.txt"):
        blnResumeExists = True
    if not blnResumeExists:
        strResume = input("No resume texted. Please copy and paste a text file of your resume: ")
    else:
        strReplaceResume = input("Would you like to continue with your current resume or replace it (1 - replace. any other entry will keep ur current resume): ")
        if strReplaceResume == "1": 
            strResume = input("Please copy and paste a text file of your resume: ")
            # TODO: delete resume
    # TODO: encapsulate this following section into a function summarizeResume()
    if strResume != "":
        message = [{"role": "user", "content": (cstrCaptionSumRes + strResume)}]
        # TODO: Make extra text a global variable
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=message
        )
        strResume = chat.choices[0].message.content
        with open("./resume/resume.txt", "w+") as f :
            f.writelines(strResume)
    else: 
        with open("./resume/resume.txt", "r") as f:
            strResume = f.read()

    message = [{"role": "user", "content": (cstrCaptionRes + strResume + cstrCaptionRole + strRoleDescription)}]
    chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=message
        )
    coverLetter = chat.choices[0].message.content
    print(coverLetter)
    # TODO: save as txt file or pdf. 

if __name__ =="__main__":
    main()