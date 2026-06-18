from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """ 
You are an expert in answering user's questions about a pizza restaurant.

Answer the User's question based on the reviews provided to you.

Note:
1. Don't hallucinate.
2. Strictly frame the answers with the reviews given.
3. if thewre is no enough reviews for the question, then say that "There is not enough review for this question".

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n-------------------------")
    question = input("Ask your question (q to quit): ")

    print("\n\n")
    if question == "q":
        break

    reviews = retriever.invoke(question)  
    # print(reviews)  

    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)