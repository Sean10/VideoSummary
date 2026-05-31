# import logging
import os
os.environ["UNSTRUCTURED_TELEMETRY_ENABLED"] = "false"
os.environ["DO_NOT_TRACK"] = "true"
os.environ["SCARF_NO_ANALYTICS"] = "true"
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import UnstructuredMarkdownLoader, TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA

# 配置日志
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 加载Markdown文件
# 这里unstructure引入了nltk 下载动作, 很恶心.
# logging.debug("Loading Markdown file...")
# loader = UnstructuredMarkdownLoader("temp.md")
# documents = loader.load()
# logging.debug(f"Loaded {len(documents)} documents.")


logging.debug("Loading text file...")
loader = TextLoader("temp.md")
documents = loader.load()
logging.debug(f"Loaded {len(documents)} documents.")

# 分割文本
logging.debug("Splitting text...")
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
logging.debug(f"Split into {len(texts)} chunks.")

# 初始化OpenAI嵌入模型，添加endpoint和模型参数
logging.debug("Initializing OpenAI embeddings...")
embeddings = OpenAIEmbeddings(
    openai_api_key="REDACTED_API_KEY",
    openai_api_base="https://api.siliconflow.cn/v1",  # 添加自定义endpoint
    model="BAAI/bge-m3"  # 添加模型参数
)

# 创建向量数据库，指定持久化路径
logging.debug("Creating vector store with persistence...")
vectorstore = Chroma.from_documents(texts, embeddings, persist_directory="db")

# 尝试从本地加载向量数据库
if os.path.exists("db"):
    logging.debug("Loading vector store from local directory...")
    vectorstore = Chroma(persist_directory="db", embedding_function=embeddings)

# 如果向量数据库为空，则创建新的向量数据库
# if not vectorstore.get_all_documents():
#     logging.debug("No documents found in vector store, creating new one...")
#     vectorstore = Chroma.from_documents(texts, embeddings, persist_directory="db")
#     vectorstore.persist()  # 持久化到本地

# 初始化OpenAI语言模型，添加endpoint和模型参数
logging.debug("Initializing OpenAI language model...")
llm = OpenAI(
    temperature=0.5,
    openai_api_key="REDACTED_API_KEY",
    openai_api_base="https://api.siliconflow.cn/v1",  # 添加自定义endpoint
    model="Qwen/Qwen2.5-7B-Instruct"  # 添加模型参数
)

# 创建检索问答链
logging.debug("Creating retrieval QA chain...")
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# 使用关键词进行检索和总结
query = "2节点超融合高可用方案"
logging.debug(f"Running query: {query}")
result = qa_chain.run(query)
logging.debug(f"Result: {result}")
print(result)