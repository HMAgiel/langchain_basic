from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from prompt.prompt import prompt
from model.config import llm



class Penjelasan(BaseModel):
    definisi: str = Field(description="Definisi singkat yang mudah dimengerti bahasanya")
    contoh: str = Field(description="Berikan contoh aplikasi pada kehidupan sehari-hari")
parser = PydanticOutputParser(pydantic_object=Penjelasan)


def respon(topik):
    prompt_akgir = prompt.partial(
    format_instructions=parser.get_format_instructions()
    )

    chain = prompt_akgir | llm | parser
    response = chain.invoke({"topic": topik})
    return response