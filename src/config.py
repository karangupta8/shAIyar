"""
Configuration management for the ShAIyar project.
Handles all configurable parameters and settings.
"""

import os
from typing import Dict, Any, Optional
import yaml
from dataclasses import dataclass
from pathlib import Path


@dataclass
class LLMConfig:
    """Configuration for LLM model settings."""
    provider: str  # LLM provider, e.g., 'groq', 'openai', 'google', 'ollama'
    model_name: str  # Name of the model to use
    api_key: Optional[str] = None  # API key for the provider
    temperature: float = 0.7  # Controls randomness in generation
    max_tokens: int = 4096  # Maximum number of tokens to generate


@dataclass
class FileConfig:
    """Configuration for file paths and settings."""
    input_docx_path: str  # Path to the input .docx file
    output_docx_path: str  # Path for the output .docx file
    system_message_path: str  # Path to the system message text file
    separator: str = "\n*********\n"  # Separator between processed blocks in the output


@dataclass
class ProcessingConfig:
    """Configuration for text processing settings."""
    chunk_size: int = 1000  # Size of text chunks for processing (not currently used)
    delay_between_requests: float = 1.0  # Seconds to wait between LLM API calls
    max_retries: int = 3  # Maximum number of retries for a failed API call


class Config:
    """Main configuration class for the ShAIyar project."""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize configuration with default values or load from file.
        
        Args:
            config_path: Optional path to configuration file
        """
        # If no config path is provided, use the default.
        if config_path is None:
            config_path = "src/config.yaml"

        # Set default configurations for all sections
        self.llm_config = LLMConfig(
            provider="groq",
            model_name="llama3-70b-8192",
            api_key="your_api_key_here",
            temperature=0.7,
            max_tokens=4096
        )
        
        self.file_config = FileConfig(
            input_docx_path="src/InputOutput/Input_Madhushala.docx",
            output_docx_path="src/InputOutput/Output_Madhushala.docx",
            system_message_path="src/Data/System_Message.txt",
            separator="\n*********\n"
        )
        
        self.processing_config = ProcessingConfig(
            chunk_size=1000,
            delay_between_requests=1.0,
            max_retries=3
        )
        
        # If the config file exists, load it to override defaults
        if Path(config_path).exists():
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
            
            
            # Update LLM config from file if 'llm_config' section exists
            if llm_data := config_data.get('llm_config'):
                for key, value in llm_data.items():
                    if hasattr(self.llm_config, key):
                        setattr(self.llm_config, key, value)

            # Update File config from file if 'file_config' section exists
            if file_data := config_data.get('file_config'):
                for key, value in file_data.items():
                    if hasattr(self.file_config, key):
                        setattr(self.file_config, key, value)

            # Update Processing config from file if 'processing_config' section exists
            if proc_data := config_data.get('processing_config'):
                for key, value in proc_data.items():
                    if hasattr(self.processing_config, key):
                        setattr(self.processing_config, key, value)
        except (IOError, yaml.YAMLError) as e:
            # In case of error, print a warning and continue with default/existing settings.
            # Consider using logging for consistency with the rest of the application.
            print(f"Warning: Could not load or parse config file {config_path}. Using defaults. Error: {e}")
    
    def validate(self) -> bool:
        """
        Validate the configuration settings.
        
        Returns:
            bool: True if configuration is valid, False otherwise
            
        Raises:
            ValueError: If a required configuration value is missing or invalid.
            FileNotFoundError: If a required file does not exist.
        """
        # API key is mandatory for certain LLM providers
        providers_requiring_key = ['groq', 'openai', 'google']
        if self.llm_config.provider.lower() in providers_requiring_key and not self.llm_config.api_key:
            raise ValueError(f"API key is required for provider '{self.llm_config.provider}'")
        
        # Input document must exist
        if not os.path.exists(self.file_config.input_docx_path):
            raise FileNotFoundError(f"Input file not found: {self.file_config.input_docx_path}")
        
        # System message file must exist
        if not os.path.exists(self.file_config.system_message_path):
            raise FileNotFoundError(f"System message file not found: {self.file_config.system_message_path}")
        
        return True 