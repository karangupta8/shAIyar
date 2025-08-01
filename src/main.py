"""
Main entry point for the ShAIyar project.
Provides a command-line interface for document processing.
"""

import argparse
import logging
import sys
from pathlib import Path

from config import Config
from shaiyar_processor import ShAIyarProcessor


def setup_logging(level: str = "INFO") -> None:
    """
    Setup logging configuration.
    
    Args:
        level: Logging level
    """
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/shaiyar.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )


def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(description="ShAIyar - Document Processing Tool")
    parser.add_argument(
        "--input", "-i",
        type=str,
        help="Input DOCX file path"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output DOCX file path"
    )
    parser.add_argument(
        "--system-message", "-s",
        type=str,
        help="System message file path"
    )
    parser.add_argument(
        "--provider", "-p",
        type=str,
        choices=["groq", "openai", "google"],
        default="groq",
        help="LLM provider"
    )
    parser.add_argument(
        "--model", "-m",
        type=str,
        help="LLM model name"
    )
    parser.add_argument(
        "--api-key", "-k",
        type=str,
        help="API key for the LLM provider"
    )
    parser.add_argument(
        "--config", "-c",
        type=str,
        help="Configuration file path"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    # Setup logging
    log_level = "DEBUG" if args.verbose else "INFO"
    setup_logging(log_level)
    
    logger = logging.getLogger(__name__)
    logger.info("Starting ShAIyar document processing")
    
    try:
        # Load configuration
        config = Config(args.config)
        
        # Override configuration with command line arguments
        if args.input:
            config.file_config.input_docx_path = args.input
        if args.output:
            config.file_config.output_docx_path = args.output
        if args.system_message:
            config.file_config.system_message_path = args.system_message
        if args.provider:
            config.llm_config.provider = args.provider
        if args.model:
            config.llm_config.model_name = args.model
        if args.api_key:
            config.llm_config.api_key = args.api_key
        
        # Validate configuration
        config.validate()
        
        # Create processor and run
        processor = ShAIyarProcessor(config)
        success = processor.process()
        
        if success:
            logger.info("Document processing completed successfully")
            sys.exit(0)
        else:
            logger.error("Document processing failed")
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"Application error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 