## Project Description
ShAIyar is an assistant designed to enhance the reading experience of literature, particularly poetry, for bilingual individuals. The application ingests literature and provides transliteration, translation, and explanation of difficult words. It makes it easy to enjoy content originally created in languages the user is not proficient in.

The name "ShAIyar" combines "Shayar," the Urdu/Hindi word for "poet," with "AI" (Artificial Intelligence).

## Inspiration
In May’2025, I decided to read a classic Hindi poetry book, Madhushala. It was published in 1935 and is written by the iconic Harivansh Rai Bachchan. Even though Hindi is my second native language, my Hindi vocabulary wasn't so efficient to read this book smoothly especially when its language is relatively archaic for Today. I had to constantly Google words while reading which impended to trule enjoy the read. Moreover, its difficult to search Hindi words as I don't know how to type in Devanagari script.
I did not find any appropriate translations of the book online. However, I did find its digital copy in Public Domain. So I had an idea to translate it myself while maintaining the original essence as much as possible. I could then get this personlized translation printed out and read it effortlessly.


## Table of Contents
- [Project Description](#project-description)
- [Inspiration](#inspiration)
- [🎯 Goal](#-goal)
- [🧑‍🎓 Ideal Users](#-ideal-users)
- [🔍 Key Features](#-key-features)
  - [Literary Experience](#-literary-experience)
  - [System Features](#-system-features)
  - [Developer Features](#-developer-features)
- [Sample System Prompt, Input and Output](#sample-system-prompt-input-and-output)
- [Advantage of using LLM vs Traditional Translation Methods](#advnatage-of-using-llm-vs-traditional-translation-methods)
- [Success Metrics](#success-metrics)
- [Installation](#installation)
- [Usage](#usage)
  - [Command Line Interface](#command-line-interface)
  - [Programmatic Usage](#programmatic-usage)
- [Configuration](#configuration)
  - [Configuration Options](#configuration-options)
- [Architecture](#architecture)
  - [Modules](#modules)
  - [LLM Providers](#llm-providers)
- [Error Handling](#error-handling)
- [Logging](#logging)
- [📜 License](#-license)
- [👤 Author](#-author)




## 🎯 Goal

**ShAIyar** aims to offer a seamless and enriching reading experience for bilingual individuals, especially those exploring literature in a second language. The core objectives are:

- 🗣️ **Accessibility Through AI**: Make classic literary works more accessible via transliteration and translation.
- 🧠 **Enhanced Understanding**: Offer clear, context-aware explanations of complex or poetic vocabulary.
- 📖 **Poem-Level Exploration**: Allow users to select individual poems for deep exploration.
- 🔍 **Comprehension Boosters**: Break down literature with detailed explanations, cultural references, and vocabulary aids.

---

## 🧑‍🎓 Ideal Users

For individuals who straddle two languages — fluent in one, aspiring in another — and are eager to engage with literature that lies just beyond their linguistic comfort zone.

- 🔄 **Bilingual Readers**: Individuals with strong (C1–C2) proficiency in one language and intermediate (B1–B2) in another, seeking to explore literature in their less dominant language.
- 🌍 **Diaspora Communities**: People reconnecting with their heritage through classical texts in native scripts they may not read fluently.
- 📚 **Students & Scholars**: Those studying poetry, translation, culture, or linguistics who require deeper insights into poetic and contextual nuances.
- 🧠 **Curious Explorers**: Anyone passionate about poetry but hindered by script unfamiliarity or vocabulary gaps.

ShAIyar aims to bridge the gap between literary appreciation and linguistic confidence.

---

## 🔍 Key Features

### 📚 Literary Experience

- **Poem Selector**: Choose specific poems from a scanned book or PDF.
- **Transliteration**: Convert script (e.g., Hindi in Devanagari ➝ Latin script).
- **Translation**: Render lines in the user’s preferred language (e.g., English).
- **Line-by-Line Explanation**: Interpret each line with cultural and contextual insight.
- **Glossary Builder**: Automatically compiles a glossary of complex or poetic words, complete with meanings and usage.

### 🧩 System Features

- **Modular Architecture**: Clean, maintainable codebase with decoupled modules for parsing, processing, AI queries, and output generation.
- **Multi-LLM Support**: Plug-and-play support for Groq, OpenAI, and Google Gemini APIs.
- **Incremental Saving**: Automatically saves progress after each processed block to prevent data loss.
- **Progress Tracking**: Visual progress indicators and summaries while processing large documents.

### ⚙️ Developer Features

- **Robust Error Handling**: Retry logic and fallback mechanisms to handle API timeouts or failures gracefully.
- **Flexible Configuration**: Supports both inline and file-based settings for ease of use and environment customization.
- **Logging System**: Detailed logging for easy debugging and process monitoring.

---

## Sample System Prompt, Input and Output

You are a scholar in Hindi Poetry with as well as English literature

For any Hindi poems I submit, provide:
For each line:
1. Give the Hindi line. Include meanings of key Hindi words in the same line (in brackets or inline).
2. Give the English translation.
3. Briefly explain the line in English.
Keep it short and structured.

### For Example

### Input:

मुख से तू अविरत कहता जा — मधु, मदिरा, मादक हाला।
हाथों में अनुभव करता जा — एक ललित कल्पित प्याला।
ध्यान किए जा मन में सुमधुर, सुखकर, सुंदर साक़ी का
और बढ़ा चल, पथिक, न तुझको दूर लगेगी मधुशाला।।


### Output:
मुख से तू अविरत कहता जा मधु,
You keep saying sweet nothings from your lips, 
Explanation: The speaker is being flirted with or receiving sweet talk from someone.

मदिरा, मादक हाला।
Intoxicating, intoxicating wine, 
Explanation: The sweet talk is intoxicating and addictive.

हाथों में अनुभव करता जा — एक ललित कल्पित प्याला।
You're experiencing the tender touch of a delicate, ornate cup in your hands, 
Explanation: The speaker is receiving a gentle, loving touch, symbolized by the delicate cup.

ध्यान किए जा मन में सुमधुर, सुखकर,
Focus on the sweet, comforting joy in your heart, 
Explanation: The speaker is being comforted and experiencing joy.

सुंदर साक़ी का, और बढ़ा चल, पथिक,
The beautiful wine-pourer, and the wine flows, and the wine-pourer's charm, 
Explanation: The wine-pourer is beautiful, and their charm is increasing.

न तुझको दूर लगेगी मधुशाला।।
You won't feel far from the tavern of love. 
Explanation: The speaker is promising that the beloved won't feel distant from the place of love and affection.


## Advantage of Using LLM vs Traditional Translation Methods

### 1. Difficulty Assessment
- **LLM Capability**: Assess the difficulty level of each poem or individual word based on context and user familiarity.
- **Advantage**: Prioritizes the explanation of more complex parts, helping users focus their attention effectively.

### 2. Contextual Explanation
- **LLM Capability**: Provide nuanced, context-aware meanings of difficult words and phrases.
- **Advantage**: Goes beyond dictionary definitions to incorporate poetic nuance, idiomatic use, and cultural relevance.

### 3. Style Adaptation
- **LLM Capability**: Translate while preserving the poem’s original tone, rhythm, and literary devices.
- **Advantage**: Maintains the artistic and emotional essence of the original, improving literary fidelity.

### 4. Content Generation
- **LLM Capability**: Generate summaries, analyses, or thematic breakdowns of each poem.
- **Advantage**: Aids in deeper understanding and academic engagement with the text.

---

## Success Metrics

- **Reduced time spent looking up word meanings**  
  Users spend less time consulting external dictionaries or reference materials.

- **Improved comprehension of the poetry**  
  Users demonstrate a better grasp of themes, imagery, and vocabulary.

- **Increased user satisfaction with the reading experience**  
  Higher engagement levels and positive feedback from readers using LLM-supported tools.



## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line Interface

```bash
# Basic usage with default configuration
python main.py

# Specify input and output files
python main.py --input "input.docx" --output "output.docx"

# Use different LLM provider
python main.py --provider openai --model "gpt-4" --api-key "your_key"

# Verbose logging
python main.py --verbose

# Use configuration file
python main.py --config config.yaml
```

### Programmatic Usage

```python
from config import Config
from shaiyar_processor import ShAIyarProcessor

# Create configuration
config = Config()
config.file_config.input_docx_path = "input.docx"
config.file_config.output_docx_path = "output.docx"
config.llm_config.api_key = "your_api_key"

# Process document
processor = ShAIyarProcessor(config)
success = processor.process()
```

## Configuration

The application supports configuration through:
- Code defaults
- Configuration files (YAML/JSON)
- Command line arguments

### Configuration Options

- **LLM Settings**: Provider, model, API key, temperature, max tokens
- **File Settings**: Input/output paths, system message path, separators
- **Processing Settings**: Chunk size, delays, retry limits

## Architecture

### Modules

- **`config.py`**: Configuration management
- **`docx_reader.py`**: DOCX file reading and text extraction
- **`text_processor.py`**: Text cleaning and analysis
- **`llm_interface.py`**: LLM API abstraction
- **`output_writer.py`**: Output file writing
- **`shaiyar_processor.py`**: Main processing orchestration
- **`main.py`**: Command line interface

### LLM Providers

- **Groq**: Fast inference with llama3-70b-8192
- **OpenAI**: GPT models with comprehensive capabilities
- **Google**: Gemini models for text processing

## Error Handling

The application includes robust error handling:
- File not found errors
- API authentication errors
- Network timeouts
- Invalid configuration errors
- Automatic retry mechanisms

## Logging

Comprehensive logging is implemented throughout the application:
- File and console output
- Different log levels (DEBUG, INFO, WARNING, ERROR)
- Structured log messages with timestamps


## 📜 License
Distributed under the MIT License.

## 👤 Author
Karan Gupta