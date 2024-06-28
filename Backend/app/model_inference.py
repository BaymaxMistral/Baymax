import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.messages import HumanMessage
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import PromptTemplate 
from fastapi import HTTPException
from dotenv import load_dotenv



load_dotenv()
ft_api_key = os.environ.get("FT_MISTRAL_API_KEY")
uft_api_key = os.environ.get("UFT_MISTRAL_API_KEY")

model_id = os.environ.get("MODEL_ID")

base_dir = os.path.abspath(__file__)



class eval_json_mcq(BaseModel):
    response: str = Field(description="Yes/No")
    description: str = Field(description="reason for your response")


class eval_json_html_format(BaseModel):
    html_format_content:str = Field(description="text to html reformat response")



class Process_user_query:
    def __init__(self,):
        try:
            self.ft_client = MistralClient(api_key=ft_api_key) # \\ finetuned model
            # self.uft_client = MistralClient(api_key=uft_api_key) # \\ using un-trained model for response filter
            self.uft_client = ChatMistralAI(api_key=uft_api_key, model_name='mistral-large-latest')  # \\ using langchain for un-trained model

        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Error :{error} | {base_dir}"
            )

    def get_prompt(self,user_query_val_prompt=None, change_to_html_temp=None, greetings_temp=None):
        if user_query_val_prompt:
            user_query_val_prompt="""You are a expert in categorizing user query
            if the query is related to any medical terms, your response should be 'Yes'.
            if it is not related to the medical terms or field, your response should be 'No' and answer the question and suggest user to ask about medical related questions in description.
            query:{query}
            
            \n{format_instructions}\n

            your helpful response below:

            """
            return user_query_val_prompt
        
        elif change_to_html_temp:
            change_to_html_temp = """
            You have to Reformat the below text into a html format.

            text : {text}

            note: refer the below response format:

            \n{format_instructions}\n

            your helpful response below:

            """

            return change_to_html_temp
        
    

    def filter_user_query(self, user_query):
        print("--filter_user_query--")

        parser = JsonOutputParser(pydantic_object=eval_json_mcq)

        prompt_initialize_question = PromptTemplate(
        template=self.get_prompt(user_query_val_prompt=True),
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        validation_chain = prompt_initialize_question | self.uft_client | parser
        try:
            self.val_response = validation_chain.invoke({"query": user_query})

        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Error :{error} | {base_dir}"
            )
        
            
        if self.val_response['response'].lower()=="yes":
            return user_query

    def get_response(self, user_query):
        print("--get_response--")
        try:
            self.ft_chat_response = self.ft_client.chat(
                model=model_id,
                messages=[ChatMessage(role='user', content=user_query)],
                max_tokens=1000
            )


        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Error :{error} | {base_dir}"
            )
        
    def parse_to_html(self,response):
        html = {"response": f"<p>{response}</p>", "status": 200}
        return html
    
    def response_to_html(self,text):
        print("--response_to_html--")
        
        parser = JsonOutputParser(pydantic_object=eval_json_html_format)

        prompt_change_to_html = PromptTemplate(
        template=self.get_prompt(change_to_html_temp=True),
        input_variables=["text"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        response_html_chain = prompt_change_to_html | self.uft_client | parser

        try:
            self.htlm_chain_response = response_html_chain.invoke({"text": text})

            return {"html_format_response":self.htlm_chain_response['html_format_content'], "status":200}

        except Exception as error:
            print("Error in reformatting the text to html format")
            
            return {"html_format_response":text, "status":500}
        
    
        
    def start_query_process(self, user_query):
        print("--start_query_process--")
        validate_response = self.filter_user_query(user_query)
        
        if validate_response:
            self.ft_response = self.get_response(validate_response)
            html_format_response = self.response_to_html(text=self.ft_chat_response.choices[0].message.content)
            if html_format_response['status']==200:
                return {"status":200,"response":html_format_response['html_format_response']}
            else:
                return {"status":200,"response":self.ft_chat_response.choices[0].message.content}

        else:
            return {"status":200,"response":self.val_response['description']}
        

