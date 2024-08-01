from langchain_ollama import OllamaLLM

model = OllamaLLM(model='llama3')

result = model.invoke(input_text='Hello, how are you?')
print(result)