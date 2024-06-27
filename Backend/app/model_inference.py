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


class Process_user_query:
    def __init__(self,):
        try:
            self.ft_client = MistralClient(api_key=ft_api_key) # \\ finetuned model
            # self.uft_client = MistralClient(api_key=uft_api_key) # \\ using un-trained model for response filter
            self.uft_client = ChatMistralAI(api_key=uft_api_key, model_name='mistral-medium-latest')  # \\ using langchain for un-trained model

        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Error :{error} | {base_dir}"
            )

    def get_prompt(self,user_query_val_prompt=None):
        if user_query_val_prompt:
            user_query_val_prompt="""You are a expert in categorizing user query
            if the query is related to any medical terms, your response should be 'Yes'.
            if it is not related to the medical terms or field, your response should be 'No' and suggest user to ask about medical related questions in description. 
            query:{query}
            
            \n{format_instructions}\n

            your helpful question below

            """
            return user_query_val_prompt


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

            print("validation chain response : ",self.val_response)

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
                messages=[ChatMessage(role='user', content=user_query)]
            )

        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Error :{error} | {base_dir}"
            )


    def start_query_process(self, user_query):
        print("--start_query_process--")
        val_response = self.filter_user_query(user_query)
        
        if val_response:
            self.ft_response = self.get_response(val_response)
            return {"status":200,"response":self.ft_chat_response.choices[0].message.content}
        
        else:
            return {"status":200,"response":self.val_response['description']}