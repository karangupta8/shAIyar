"""
Configuration management for the ShAIyar project.
Handles all configurable parameters and settings.
"""

import os
from typing import Dict, Any
import yaml
from dataclasses import dataclass
from pathlib import Path


@dataclass
class LLMConfig:
    """Configuration for LLM model settings."""
    provider: str  # 'groq', 'openai', 'google', 'huggingface'
    model_name: str
    api_key: str
    temperature: float = 0.7
    max_tokens: int = 4096
    chunk_size: int = 1000


@dataclass
class FileConfig:
    """Configuration for file paths and settings."""
    input_docx_path: str
    output_docx_path: str
    system_message_path: str
    separator: str = "\n*********\n"


@dataclass
class ProcessingConfig:
    """Configuration for text processing settings."""
    chunk_size: int = 1000
    delay_between_requests: float = 1.0
    max_retries: int = 3


class Config:
    """Main configuration class for the ShAIyar project."""
    
    def __init__(self, config_path: str = "config.yaml"):
        """
        Initialize configuration with default values or load from file.
        
        Args:
            config_path: Optional path to configuration file
        """
        self.llm_config = LLMConfig(
            provider="groq",
            model_name="llama3-70b-8192",
            api_key="",
            temperature=0.7,
            max_tokens=4096,
            chunk_size=1000
        )
        
        self.file_config = FileConfig(
            input_docx_path="Bachchans_Madhushala.docx",
            output_docx_path="Out_Bachchans_Madhushala.docx",
            system_message_path="System_Message.txt",
            separator="\n*********\n"
        )
        
        self.processing_config = ProcessingConfig(
            chunk_size=1000,
            delay_between_requests=1.0,
            max_retries=3
        )
        
        if config_path and Path(config_path).exists():
            self.load_from_file(config_path)
    
    def load_from_file(self, config_path: str) -> None:
        """
        Load configuration from a YAML file, overriding defaults.
        
        Args:
            config_path: Path to the configuration file
        """
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config_data = yaml.safe_load(f)

            if llm_data := config_data.get('llm_config'):
                for key, value in llm_data.items():
                    if hasattr(self.llm_config, key):
                        setattr(self.llm_config, key, value)

            if file_data := config_data.get('file_config'):
                for key, value in file_data.items():
                    if hasattr(self.file_config, key):
                        setattr(self.file_config, key, value)

            if proc_data := config_data.get('processing_config'):
                for key, value in proc_data.items():
                    if hasattr(self.processing_config, key):
                        setattr(self.processing_config, key, value)
        except (IOError, yaml.YAMLError) as e:
            print(f"Warning: Could not load or parse config file {config_path}. Using defaults. Error: {e}")
    
    def validate(self) -> bool:
        """
        Validate the configuration settings.
        
        Returns:
            bool: True if configuration is valid, False otherwise
        """
        if not self.llm_config.api_key:
            raise ValueError("API key is required")
        
        if not os.path.exists(self.file_config.input_docx_path):
            raise FileNotFoundError(f"Input file not found: {self.file_config.input_docx_path}")
        
        if not os.path.exists(self.file_config.system_message_path):
            raise FileNotFoundError(f"System message file not found: {self.file_config.system_message_path}")
        
        return True 