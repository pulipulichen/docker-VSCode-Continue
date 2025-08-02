#!/bin/bash

# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "pull meta-llama/Meta-Llama-3.1-8B-Instruct -> linbeiJiang/Llama-3.1-8B-Instruct"
ollama pull linbeiJiang/Llama-3.1-8B-Instruct

echo "pull nomic-ai/nomic-embed-text-v1 -> DC1LEX/nomic-embed-text-v1.5-multimodal"
ollama pull DC1LEX/nomic-embed-text-v1.5-multimodal

echo "pull Qwen/Qwen2.5-Coder-1.5B -> dagbs/qwen2.5-coder-1.5b-instruct-abliterated"
ollama pull dagbs/qwen2.5-coder-1.5b-instruct-abliterated

# 拉取 bge-m3
ollama pull bge-m3

ollama pull dengcao/Qwen3-Reranker-8B

# https://ollama.com/library/gemma2:2b
# ollama pull gemma2:9b

# https://ollama.com/library/gemma2:2b
# ollama pull llama3.2-vision:11b

# =================================================================

echo "Ollama is running"

# Wait for Ollama process to finish.
# ollama serve

wait $pid