# 📁 Bedrock Learning Project Structure

```
bedrock-learning/
├── README.md                    # Main project documentation
├── requirements.txt             # Python dependencies
├── .gitignore                  # Git ignore file
├── config/
│   ├── __init__.py
│   ├── api_keys.py             # All API keys (hardcoded for learning)
│   └── models.py               # Model configurations
├── core/
│   ├── __init__.py
│   ├── bedrock_client.py       # Main Bedrock client setup
│   └── base_llm.py             # Base LLM class
├── models/
│   ├── __init__.py
│   ├── anthropic/
│   │   ├── __init__.py
│   │   ├── claude_haiku.py     # Claude Haiku specific
│   │   ├── claude_sonnet.py    # Claude Sonnet specific
│   │   └── claude_opus.py      # Claude Opus specific
│   ├── amazon/
│   │   ├── __init__.py
│   │   ├── titan_text.py       # Titan Text models
│   │   └── titan_embed.py      # Titan Embedding models
│   ├── meta/
│   │   ├── __init__.py
│   │   └── llama.py            # Llama models
│   └── cohere/
│       ├── __init__.py
│       └── command.py          # Cohere Command models
├── examples/
│   ├── __init__.py
│   ├── basic_chat.py           # Simple chat examples
│   ├── model_comparison.py     # Compare different models
│   ├── streaming.py            # Streaming responses
│   └── advanced/
│       ├── rag_example.py      # RAG implementation
│       ├── function_calling.py # Function calling
│       └── multimodal.py       # Image + text models
├── tutorials/
│   ├── 01_getting_started.py   # Your teach.py content
│   ├── 02_model_basics.py      # Model-specific tutorials
│   ├── 03_parameters.py        # Parameter tuning
│   └── 04_best_practices.py    # Best practices
├── utils/
│   ├── __init__.py
│   ├── helpers.py              # Helper functions
│   └── validators.py           # Input validation
└── tests/
    ├── __init__.py
    ├── test_models.py          # Model tests
    └── test_examples.py        # Example tests
```

## 🎯 Benefits of this structure:
- **Organized by model provider** (Anthropic, Amazon, Meta, etc.)
- **Separate configs** for easy key management
- **Progressive tutorials** from basic to advanced
- **Reusable components** in core/utils
- **Easy to extend** with new models/providers