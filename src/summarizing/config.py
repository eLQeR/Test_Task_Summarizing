from langchain_huggingface import HuggingFacePipeline


#Create hugging face LLM pipeline with facebook bart model for summarization text
hugging_face_llm = HuggingFacePipeline.from_model_id(
    model_id="facebook/bart-large-cnn",
    task="summarization",
    model_kwargs={
        "max_length": 130,
        "min_length": 30,
        "do_sample": False
    }
)
