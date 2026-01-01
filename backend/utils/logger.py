"""
Logging utility for agent actions and workflow tracking
"""

import logging
import os
from datetime import datetime


def setup_logger(name: str = "marketing_automation", log_file: str = None):
    """
    Setup logger with console and file handlers
    
    Args:
        name: Logger name
        log_file: Optional log file path
        
    Returns:
        Logger instance
    """
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Remove existing handlers
    logger.handlers = []
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    simple_formatter = logging.Formatter(
        '%(levelname)s: %(message)s'
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(simple_formatter)
    logger.addHandler(console_handler)
    
    # File handler
    if log_file is None:
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(
            log_dir,
            f"marketing_automation_{datetime.now().strftime('%Y%m%d')}.log"
        )
    
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)
    logger.addHandler(file_handler)
    
    return logger


class AgentLogger:
    """
    Specialized logger for agent actions
    """
    
    def __init__(self, agent_name: str):
        self.agent_name = agent_name
        self.logger = setup_logger(agent_name)
    
    def log_action(self, action: str, details: dict = None):
        """Log agent action with details"""
        message = f"[{self.agent_name}] {action}"
        if details:
            message += f" | Details: {details}"
        self.logger.info(message)
    
    def log_decision(self, decision: str, reasoning: str):
        """Log agent decision with reasoning"""
        message = f"[{self.agent_name}] Decision: {decision} | Reasoning: {reasoning}"
        self.logger.info(message)
    
    def log_error(self, error: str, exception: Exception = None):
        """Log agent error"""
        message = f"[{self.agent_name}] Error: {error}"
        if exception:
            message += f" | Exception: {str(exception)}"
        self.logger.error(message)
    
    def log_success(self, message: str):
        """Log successful completion"""
        self.logger.info(f"[{self.agent_name}] ✓ {message}")