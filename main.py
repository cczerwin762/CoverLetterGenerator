import os
import openai

def main():
    strRoleDescription = input("Please copy and paste the description for your role from the job board: ")
    blnResumeExists = False
    strGPTAPIKey = ""
    strResume = ""
    if (os.path.isfile("./resume/resume.txt")):
        blnResumeExists = True
    if not blnResumeExists:
        strResume = input("No resume texted. Please copy and paste a text file of your resume: ")
    else:
        strReplaceResume = input("Would you like to continue with your current resume or replace it (1 - replace. any other entry will keep ur current resume): ")
        if strReplaceResume == "1": 
            strResume = input("Please copy and paste a text file of your resume: ")
            # delete resume
    openai.api_key = strGPTAPIKey
    if strResume != "":
        message = [{"role": "user", "content": ("Please summarize my resume: " + strResume)}]
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=message
        )
        strResume = chat.choices[0].message.content
        with open("./resume/resume.txt", "w+") as f :
            f.writelines(strResume)
    else: 
        with open("./resume/resume.txt", "r") as f:
            strResume = f.read()
if __name__ =="__main__":
    main()