from fastapi import HTTPException, APIRouter, Depends

from src.summarizing.config import hugging_face_llm
from src.summarizing.schemas import Text

router = APIRouter()


async def get_llm_model():
    return hugging_face_llm

@router.post("/summarize/")
async def summarize_text(input_text: Text, llm_model=Depends(get_llm_model)):
    #Check for valid input data
    if not len(input_text.text):
        raise HTTPException(status_code=400, detail="Provide text to summarize!")
    #Use async invoke for LLM with text from user, and return as result
    return {
        "result": await llm_model.ainvoke(
            input_text.text
        )
    }
