from langchain_ollama import OllamaEmbeddings
emb = OllamaEmbeddings(model="nomic-embed-text")
vec = emb.embed_query("How do I control weeds in sesame?")
print(len(vec))
print(vec[:5])