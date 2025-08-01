"""
LLM interface abstraction for the ShAIyar project.
Provides a unified interface for different LLM providers.
"""

import time
from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import logging

logger = logging.getLogger(__name__)


class LLMInterface(ABC):
    """Abstract base class for LLM interfaces."""
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the LLM interface.
        
        Args:
            config: Configuration dictionary containing API keys and settings
        """
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.retry_count = 0
        self.max_retries = config.get('max_retries', 3)
    
    @abstractmethod
    def initialize_model(self) -> None:
        """Initialize the LLM model."""
        pass
    
    @abstractmethod
    def invoke(self, messages: List) -> str:
        """
        Invoke the LLM model with messages.
        
        Args:
            messages: List of messages to send to the model
            
        Returns:
            str: Model response
        """
        pass
    
    def create_messages(self, system_message: str, user_message: str) -> List:
        """
        Create a list of messages for the LLM.
        
        Args:
            system_message: System message content
            user_message: User message content
            
        Returns:
            List: List of messages
        """
        return [
            SystemMessage(content=system_message),
            HumanMessage(content=user_message)
        ]
    
    def handle_error(self, error: Exception) -> Optional[str]:
        """
        Handle errors during LLM invocation.
        
        Args:
            error: The exception that occurred
            
        Returns:
            Optional[str]: Error message or None
        """
        self.logger.error(f"LLM invocation error: {error}")
        
        if self.retry_count < self.max_retries:
            self.retry_count += 1
            self.logger.info(f"Retrying... Attempt {self.retry_count}/{self.max_retries}")
            time.sleep(2 ** self.retry_count)  # Exponential backoff
            return None
        else:
            self.retry_count = 0
            return f"Error after {self.max_retries} retries: {str(error)}"


class GroqInterface(LLMInterface):
    """Interface for Groq LLM API."""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.model = None
        self.initialize_model()
    
    def initialize_model(self) -> None:
        """Initialize the Groq model."""
        try:
            from langchain_groq import ChatGroq
            self.model = ChatGroq(
                model_name=self.config['model_name'],
                api_key=self.config['api_key'],
                temperature=self.config.get('temperature', 0.7)
            )
        except ImportError:
            raise ImportError("langchain_groq is required for Groq interface")
        except Exception as e:
            raise Exception(f"Failed to initialize Groq model: {e}")
    
    def invoke(self, messages: List) -> str:
        """
        Invoke the Groq model.
        
        Args:
            messages: List of messages
            
        Returns:
            str: Model response
        """
        try:
            result = self.model.invoke(messages)
            self.retry_count = 0  # Reset retry count on success
            return result.content
        except Exception as e:
            error_msg = self.handle_error(e)
            if error_msg:
                raise Exception(error_msg)
            return self.invoke(messages)  # Retry


class OpenAIInterface(LLMInterface):
    """Interface for OpenAI LLM API."""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.model = None
        self.initialize_model()
    
    def initialize_model(self) -> None:
        """Initialize the OpenAI model."""
        try:
            from langchain_openai import ChatOpenAI
            self.model = ChatOpenAI(
                model=self.config['model_name'],
                api_key=self.config['api_key'],
                temperature=self.config.get('temperature', 0.7),
                max_tokens=self.config.get('max_tokens', 4096)
            )
        except ImportError:
            raise ImportError("langchain_openai is required for OpenAI interface")
        except Exception as e:
            raise Exception(f"Failed to initialize OpenAI model: {e}")
    
    def invoke(self, messages: List) -> str:
        """
        Invoke the OpenAI model.
        
        Args:
            messages: List of messages
            
        Returns:
            str: Model response
        """
        try:
            result = self.model.invoke(messages)
            self.retry_count = 0  # Reset retry count on success
            return result.content
        except Exception as e:
            error_msg = self.handle_error(e)
            if error_msg:
                raise Exception(error_msg)
            return self.invoke(messages)  # Retry


class GoogleInterface(LLMInterface):
    """Interface for Google Gemini LLM API."""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.model = None
        self.initialize_model()
    
    def initialize_model(self) -> None:
        """Initialize the Google Gemini model."""
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
            self.model = ChatGoogleGenerativeAI(
                model=self.config['model_name'],
                google_api_key=self.config['api_key'],
                temperature=self.config.get('temperature', 0.7)
            )
        except ImportError:
            raise ImportError("langchain_google_genai is required for Google interface")
        except Exception as e:
            raise Exception(f"Failed to initialize Google model: {e}")
    
    def invoke(self, messages: List) -> str:
        """
        Invoke the Google Gemini model.
        
        Args:
            messages: List of messages
            
        Returns:
            str: Model response
        """
        try:
            result = self.model.invoke(messages)
            self.retry_count = 0  # Reset retry count on success
            return result.content
        except Exception as e:
            error_msg = self.handle_error(e)
            if error_msg:
                raise Exception(error_msg)
            return self.invoke(messages)  # Retry


class OllamaInterface(LLMInterface):
    """Interface for Ollama LLM API."""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.model = None
        self.initialize_model()

    def initialize_model(self) -> None:
        """Initialize the Ollama model."""
        try:
            from langchain_ollama import ChatOllama
            self.model = ChatOllama(
                model=self.config['model_name'],
                temperature=self.config.get('temperature', 0.7)
            )
        except ImportError:
            raise ImportError("langchain-ollama is required for Ollama interface. Please run 'pip install langchain-ollama'.")
        except Exception as e:
            raise Exception(f"Failed to initialize Ollama model: {e}")

    def invoke(self, messages: List) -> str:
        """
        Invoke the Ollama model.
        
        Args:
            messages: List of messages
            
        Returns:
            str: Model response
        """
        try:
            result = self.model.invoke(messages)
            self.retry_count = 0  # Reset retry count on success
            return result.content
        except Exception as e:
            error_msg = self.handle_error(e)
            if error_msg:
                raise Exception(error_msg)
            return self.invoke(messages)  # Retry


class LLMFactory:
    """Factory class for creating LLM interfaces."""
    
    @staticmethod
    def create_llm_interface(provider: str, config: Dict[str, Any]) -> LLMInterface:
        """
        Create an LLM interface based on the provider.
        
        Args:
            provider: LLM provider ('groq', 'openai', 'google', 'ollama')
            config: Configuration dictionary
            
        Returns:
            LLMInterface: Appropriate LLM interface instance
        """
        if provider.lower() == 'groq':
            return GroqInterface(config)
        elif provider.lower() == 'openai':
            return OpenAIInterface(config)
        elif provider.lower() == 'google':
            return GoogleInterface(config)
        elif provider.lower() == 'ollama':
            return OllamaInterface(config)
        else:
            raise ValueError(f"Unsupported LLM provider: {provider}") 