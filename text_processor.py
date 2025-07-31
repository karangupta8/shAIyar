"""
Text processing functionality for the ShAIyar project.
Handles text cleaning, splitting, and analysis.
"""

import re
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)


class TextProcessor:
    """Handles text processing operations."""
    
    def __init__(self):
        """Initialize the text processor."""
        self.logger = logging.getLogger(__name__)
    
    def clean_text(self, text: str) -> str:
        """
        Clean and normalize text.
        
        Args:
            text: Raw text to clean
            
        Returns:
            str: Cleaned text
        """
        if not text:
            return ""
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove special characters if needed
        # text = re.sub(r'[^\w\s]', '', text)
        
        return text.strip()
    
    def split_text_into_chunks(self, text: str, chunk_size: int = 1000) -> List[str]:
        """
        Split text into chunks of specified size.
        
        Args:
            text: Text to split
            chunk_size: Maximum size of each chunk
            
        Returns:
            List[str]: List of text chunks
        """
        if not text:
            return []
        
        chunks = []
        words = text.split()
        current_chunk = []
        current_size = 0
        
        for word in words:
            word_size = len(word) + 1  # +1 for space
            
            if current_size + word_size > chunk_size and current_chunk:
                chunks.append(' '.join(current_chunk))
                current_chunk = [word]
                current_size = word_size
            else:
                current_chunk.append(word)
                current_size += word_size
        
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        
        return chunks
    
    def analyze_text_block(self, text_block: str) -> dict:
        """
        Analyze a text block and return statistics.
        
        Args:
            text_block: Text block to analyze
            
        Returns:
            dict: Analysis results including word count, character count, etc.
        """
        if not text_block:
            return {
                "word_count": 0,
                "character_count": 0,
                "line_count": 0,
                "is_empty": True
            }
        
        lines = text_block.split('\n')
        words = text_block.split()
        
        return {
            "word_count": len(words),
            "character_count": len(text_block),
            "line_count": len(lines),
            "is_empty": False,
            "average_words_per_line": len(words) / len(lines) if lines else 0
        } 