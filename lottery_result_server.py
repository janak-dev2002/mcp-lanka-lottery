"""
Sri Lanka Lottery Results MCP Server

This MCP server provides comprehensive access to lottery results from Sri Lanka's
National Lottery Board (NLB) and Development Lottery Board (DLB).

Features:
- Get lists of active lotteries from both NLB and DLB
- Fetch specific lottery results by draw number or date
- Get latest results for any lottery
- Comprehensive error handling and validation

Usage:
    python lottery_result_server.py
"""

from fastmcp import FastMCP
from srilanka_lottery import (
    scrape_nlb_result,
    scrape_dlb_result,
    scrape_nlb_active_lottery_names,
    scrape_dlb_lottery_names,
    scrape_nlb_latest_results,
    scrape_dlb_latest_results
)
import re
from typing import Union

# Initialize MCP server with detailed instructions
mcp = FastMCP(
    "Sri Lanka Lottery Results",
    version="2.0.0",
    instructions="""
    This server provides comprehensive lottery result information for Sri Lanka's 
    National Lottery Board (NLB) and Development Lottery Board (DLB).
    
    Available capabilities:
    1. Get lists of all active lotteries from NLB and DLB
    2. Fetch specific lottery results by draw number or date
    3. Get the latest results for any lottery (up to a specified limit)
    
    Lottery Name Format:
    - NLB: Use lowercase with hyphens (e.g., 'mega-power', 'govisetha', 'dhana-nidhanaya')
    - DLB: Use proper case with spaces (e.g., 'Ada Kotipathi', 'Jayoda', 'Shanida')
    
    Date Format: Always use YYYY-MM-DD (e.g., '2025-11-23')
    
    Common NLB Lotteries: Mega Power, Govisetha, Dhana Nidhanaya, Mahajana Sampatha, etc.
    Common DLB Lotteries: Ada Kotipathi, Jayoda, Lagna Wasana, Sasiri, Shanida, Super Ball, etc.
    """
)


def validate_date_format(date_str: str) -> bool:
    """Validate if date string is in YYYY-MM-DD format."""
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.match(pattern, date_str))


def normalize_nlb_lottery_name(name: str) -> str:
    """Normalize NLB lottery name to lowercase with hyphens."""
    return name.lower().replace(' ', '-')


# ==================== LOTTERY NAME TOOLS ====================

@mcp.tool(description="Get the list of all active NLB (National Lottery Board) lotteries currently available.")
def get_nlb_lottery_names() -> dict:
    """
    Retrieves the list of all active NLB lotteries.
    
    Returns:
        dict: Contains 'NLB_Active' key with sorted list of active lottery names,
              or 'error' key if the operation fails.
              
    Example:
        >>> get_nlb_lottery_names()
        {
            "NLB_Active": [
                "Dhana Nidhanaya",
                "Govisetha", 
                "Mahajana Sampatha",
                "Mega Power",
                ...
            ]
        }
    """
    try:
        result, _ = scrape_nlb_active_lottery_names()
        return result
    except Exception as e:
        return {"error": f"Failed to fetch NLB lottery names: {str(e)}"}


@mcp.tool(description="Get the list of all available DLB (Development Lottery Board) lotteries.")
def get_dlb_lottery_names() -> dict:
    """
    Retrieves the list of all available DLB lotteries.
    
    Returns:
        dict: Contains 'DLB' key with sorted list of lottery names,
              or 'error' key if the operation fails.
              
    Example:
        >>> get_dlb_lottery_names()
        {
            "DLB": [
                "Ada Kotipathi",
                "Jaya Sampatha",
                "Jayoda",
                "Kapruka",
                ...
            ]
        }
    """
    try:
        result = scrape_dlb_lottery_names()
        return result
    except Exception as e:
        return {"error": f"Failed to fetch DLB lottery names: {str(e)}"}


# ==================== NLB RESULT TOOLS ====================

@mcp.tool(description="Fetch NLB lottery result by draw number. Lottery name should be in lowercase with hyphens (e.g., 'mega-power', 'govisetha').")
def get_nlb_result_by_draw(lottery_name: str, draw_number: int) -> dict:
    """
    Fetches the NLB lottery result for a specific draw number.
    
    Args:
        lottery_name (str): Name of the lottery in lowercase with hyphens 
                           (e.g., 'mega-power', 'govisetha', 'dhana-nidhanaya')
        draw_number (int): The draw number to fetch (e.g., 4263)
    
    Returns:
        dict: Lottery result containing:
              - draw_number: The draw number
              - date: Draw date
              - letter: Winning letter
              - numbers: List of winning numbers
              Or 'error' key if the operation fails.
              
    Example:
        >>> get_nlb_result_by_draw('govisetha', 4263)
        {
            "draw_number": "4263",
            "date": "2025-11-22",
            "letter": "T",
            "numbers": ["13", "25", "29", "51"]
        }
    """
    try:
        if not isinstance(draw_number, int) or draw_number <= 0:
            return {"error": "Draw number must be a positive integer"}
        
        normalized_name = normalize_nlb_lottery_name(lottery_name)
        result = scrape_nlb_result(normalized_name, draw_number)
        return result
    except Exception as e:
        return {"error": f"Failed to fetch NLB result: {str(e)}"}


@mcp.tool(description="Fetch NLB lottery result by date. Date must be in YYYY-MM-DD format (e.g., '2025-11-23'). Lottery name should be in lowercase with hyphens.")
def get_nlb_result_by_date(lottery_name: str, date: str) -> dict:
    """
    Fetches the NLB lottery result for a specific date.
    
    Args:
        lottery_name (str): Name of the lottery in lowercase with hyphens
                           (e.g., 'mega-power', 'govisetha', 'handahana')
        date (str): The date in YYYY-MM-DD format (e.g., '2025-11-23')
    
    Returns:
        dict: Lottery result containing:
              - draw_number: The draw number
              - date: Draw date
              - letter: Winning letter
              - numbers: List of winning numbers
              Or 'error' key if the operation fails.
              
    Example:
        >>> get_nlb_result_by_date('govisetha', '2025-11-22')
        {
            "draw_number": "4263",
            "date": "2025-11-22",
            "letter": "T",
            "numbers": ["13", "25", "29", "51"]
        }
    """
    try:
        if not validate_date_format(date):
            return {"error": "Date must be in YYYY-MM-DD format (e.g., '2025-11-23')"}
        
        normalized_name = normalize_nlb_lottery_name(lottery_name)
        result = scrape_nlb_result(normalized_name, date)
        return result
    except Exception as e:
        return {"error": f"Failed to fetch NLB result: {str(e)}"}


@mcp.tool(description="Get the latest NLB lottery results. Specify how many recent results you want (default 5, max recommended 20).")
def get_nlb_latest_results(lottery_name: str, limit: int = 5) -> dict:
    """
    Fetches the latest results for a specified NLB lottery.
    
    Args:
        lottery_name (str): Name of the lottery in lowercase with hyphens
                           (e.g., 'mega-power', 'govisetha')
        limit (int): Maximum number of recent results to return (default: 5, max recommended: 20)
    
    Returns:
        dict: Contains 'NLB_Results' key with list of recent results, each containing:
              - draw: Draw number
              - date: Draw date
              - letter: Winning letter
              - numbers: List of winning numbers
              Or 'error' key if the operation fails.
              
    Example:
        >>> get_nlb_latest_results('govisetha', 3)
        {
            "NLB_Results": [
                {
                    "draw": "4263",
                    "date": "2025-11-22",
                    "letter": "T",
                    "numbers": ["13", "25", "29", "51"]
                },
                {...},
                {...}
            ]
        }
    """
    try:
        if not isinstance(limit, int) or limit <= 0:
            return {"error": "Limit must be a positive integer"}
        
        if limit > 50:
            return {"error": "Limit should not exceed 50 for performance reasons"}
        
        normalized_name = normalize_nlb_lottery_name(lottery_name)
        # Get session from scrape_nlb_active_lottery_names
        from srilanka_lottery.scraper import get_nlb_session
        session = get_nlb_session()
        result = scrape_nlb_latest_results(session, normalized_name, limit)
        return result
    except Exception as e:
        return {"error": f"Failed to fetch latest NLB results: {str(e)}"}


# ==================== DLB RESULT TOOLS ====================

@mcp.tool(description="Fetch DLB lottery result by draw number. Lottery name must match exactly (e.g., 'Ada Kotipathi', 'Jayoda', 'Shanida').")
def get_dlb_result_by_draw(lottery_name: str, draw_number: int) -> dict:
    """
    Fetches the DLB lottery result for a specific draw number.
    
    Args:
        lottery_name (str): Exact name of the DLB lottery (case-sensitive)
                           Valid: 'Ada Kotipathi', 'Jayoda', 'Lagna Wasana', 'Sasiri', 
                           'Shanida', 'Super Ball', 'Supiri Dhana Sampatha', 
                           'Jaya Sampatha', 'Kapruka'
        draw_number (int): The draw number to fetch (e.g., 2608)
    
    Returns:
        dict: Lottery result containing:
              - draw_info: Draw information
              - date_info: Draw date
              - letter: Winning letter
              - numbers: List of winning numbers
              - prize_image: URL to prize image (if available)
              Or 'error' key if the operation fails.
              
    Example:
        >>> get_dlb_result_by_draw('Ada Kotipathi', 2608)
        {
            "draw_info": "Ada Kotipathi 2608",
            "date_info": "2025-05-01",
            "letter": "Y",
            "numbers": ["11", "22", "33", "44"],
            "prize_image": "https://..."
        }
    """
    try:
        if not isinstance(draw_number, int) or draw_number <= 0:
            return {"error": "Draw number must be a positive integer"}
        
        result = scrape_dlb_result(lottery_name, draw_number)
        return result
    except Exception as e:
        return {"error": f"Failed to fetch DLB result: {str(e)}"}


@mcp.tool(description="Fetch DLB lottery result by date. Date must be in YYYY-MM-DD format. Lottery name must match exactly.")
def get_dlb_result_by_date(lottery_name: str, date: str) -> dict:
    """
    Fetches the DLB lottery result for a specific date.
    
    Args:
        lottery_name (str): Exact name of the DLB lottery (case-sensitive)
                           Valid: 'Ada Kotipathi', 'Jayoda', 'Lagna Wasana', 'Sasiri',
                           'Shanida', 'Super Ball', 'Supiri Dhana Sampatha',
                           'Jaya Sampatha', 'Kapruka'
        date (str): The date in YYYY-MM-DD format (e.g., '2025-11-23')
    
    Returns:
        dict: Lottery result containing:
              - draw_info: Draw information
              - date_info: Draw date
              - letter: Winning letter
              - numbers: List of winning numbers
              - prize_image: URL to prize image (if available)
              Or 'error' key if the operation fails.
              
    Example:
        >>> get_dlb_result_by_date('Ada Kotipathi', '2025-05-01')
        {
            "draw_info": "Ada Kotipathi 2608",
            "date_info": "2025-05-01",
            "letter": "Y",
            "numbers": ["11", "22", "33", "44"],
            "prize_image": "https://..."
        }
    """
    try:
        if not validate_date_format(date):
            return {"error": "Date must be in YYYY-MM-DD format (e.g., '2025-11-23')"}
        
        result = scrape_dlb_result(lottery_name, date)
        return result
    except Exception as e:
        return {"error": f"Failed to fetch DLB result: {str(e)}"}


@mcp.tool(description="Get the latest DLB lottery results. Specify how many recent results you want (default 5, max recommended 20).")
def get_dlb_latest_results(lottery_name: str, limit: int = 5) -> dict:
    """
    Fetches the latest results for a specified DLB lottery.
    
    Args:
        lottery_name (str): Exact name of the DLB lottery (case-sensitive)
                           Valid: 'Ada Kotipathi', 'Jayoda', 'Lagna Wasana', 'Sasiri',
                           'Shanida', 'Super Ball', 'Supiri Dhana Sampatha',
                           'Jaya Sampatha', 'Kapruka'
        limit (int): Maximum number of recent results to return (default: 5, max recommended: 20)
    
    Returns:
        dict: Contains 'DLB_Results' key with list of recent results, each containing:
              - draw: Draw number
              - date: Draw date
              - letter: Winning letter
              - numbers: List of winning numbers
              Or 'error' key if the operation fails.
              
    Example:
        >>> get_dlb_latest_results('Ada Kotipathi', 3)
        {
            "DLB_Results": [
                {
                    "draw": "2608",
                    "date": "2025-05-01",
                    "letter": "Y",
                    "numbers": ["11", "22", "33", "44"]
                },
                {...},
                {...}
            ]
        }
    """
    try:
        if not isinstance(limit, int) or limit <= 0:
            return {"error": "Limit must be a positive integer"}
        
        if limit > 50:
            return {"error": "Limit should not exceed 50 for performance reasons"}
        
        result = scrape_dlb_latest_results(lottery_name, limit)
        return result
    except Exception as e:
        return {"error": f"Failed to fetch latest DLB results: {str(e)}"}


# ==================== PROMPTS ====================

@mcp.prompt()
def check_lottery_result_prompt() -> str:
    """Prompt template for checking lottery results."""
    return """I want to check lottery results for Sri Lanka. Please help me:

1. First, show me what lotteries are available (both NLB and DLB)
2. Then I'll tell you which lottery I'm interested in
3. I can check results by:
   - Specific draw number
   - Specific date (YYYY-MM-DD format)
   - Latest results (specify how many)
4. Finally, please wish me luck with the lottery!

Please guide me through this process."""


@mcp.prompt()
def nlb_lottery_guide_prompt() -> str:
    """Prompt template for NLB lottery guidance."""
    return """I want to check NLB (National Lottery Board) lottery results.

Important reminders:
- Lottery names should be in lowercase with hyphens (e.g., 'mega-power', 'govisetha')
- Dates should be in YYYY-MM-DD format
- I can check by draw number, date, or get latest results

Can you first show me the list of active NLB lotteries?"""


@mcp.prompt()
def dlb_lottery_guide_prompt() -> str:
    """Prompt template for DLB lottery guidance."""
    return """I want to check DLB (Development Lottery Board) lottery results.

Important reminders:
- Lottery names must match exactly with proper capitalization (e.g., 'Ada Kotipathi', 'Jayoda')
- Dates should be in YYYY-MM-DD format
- I can check by draw number, date, or get latest results

Can you first show me the list of available DLB lotteries?"""


# ==================== RESOURCES ====================

@mcp.resource("lottery://nlb/info")
def nlb_lottery_info() -> str:
    """Information about NLB lotteries and how to use them."""
    return """
    NLB (National Lottery Board) Lottery Information
    ================================================
    
    Lottery Name Format:
    - Always use lowercase with hyphens
    - Examples: 'mega-power', 'govisetha', 'dhana-nidhanaya', 'mahajana-sampatha'
    
    Available Operations:
    1. Get list of active lotteries: get_nlb_lottery_names()
    2. Get result by draw number: get_nlb_result_by_draw(lottery_name, draw_number)
    3. Get result by date: get_nlb_result_by_date(lottery_name, date)
    4. Get latest results: get_nlb_latest_results(lottery_name, limit)
    
    Date Format: YYYY-MM-DD (e.g., '2025-11-23')
    
    Common NLB Lotteries:
    - Mega Power
    - Govisetha
    - Dhana Nidhanaya
    - Mahajana Sampatha
    - Handahana
    - And more...
    
    Example Usage:
    1. Get active lotteries first
    2. Choose a lottery (convert name to lowercase with hyphens)
    3. Fetch results by draw number, date, or get latest
    """


@mcp.resource("lottery://dlb/info")
def dlb_lottery_info() -> str:
    """Information about DLB lotteries and how to use them."""
    return """
    DLB (Development Lottery Board) Lottery Information
    ===================================================
    
    Lottery Name Format:
    - Must match exactly with proper capitalization
    - Examples: 'Ada Kotipathi', 'Jayoda', 'Shanida'
    
    Supported DLB Lotteries:
    - Ada Kotipathi
    - Jayoda
    - Lagna Wasana
    - Sasiri
    - Shanida
    - Super Ball
    - Supiri Dhana Sampatha
    - Jaya Sampatha
    - Kapruka
    
    Available Operations:
    1. Get list of lotteries: get_dlb_lottery_names()
    2. Get result by draw number: get_dlb_result_by_draw(lottery_name, draw_number)
    3. Get result by date: get_dlb_result_by_date(lottery_name, date)
    4. Get latest results: get_dlb_latest_results(lottery_name, limit)
    
    Date Format: YYYY-MM-DD (e.g., '2025-11-23')
    
    Result includes:
    - Draw information
    - Date
    - Winning letter
    - Winning numbers
    - Prize image URL (when available)
    """


@mcp.resource("lottery://usage/examples")
def usage_examples() -> str:
    """Examples of how to use the lottery MCP server."""
    return """
    Sri Lanka Lottery MCP Server - Usage Examples
    ==============================================
    
    Example 1: Get NLB lottery result by draw number
    -------------------------------------------------
    lottery_name = 'govisetha'
    draw_number = 4263
    result = get_nlb_result_by_draw(lottery_name, draw_number)
    
    Example 2: Get NLB lottery result by date
    ------------------------------------------
    lottery_name = 'mega-power'
    date = '2025-11-22'
    result = get_nlb_result_by_date(lottery_name, date)
    
    Example 3: Get latest 10 NLB results
    -------------------------------------
    lottery_name = 'dhana-nidhanaya'
    results = get_nlb_latest_results(lottery_name, limit=10)
    
    Example 4: Get DLB lottery result by draw number
    -------------------------------------------------
    lottery_name = 'Ada Kotipathi'  # Note: Exact capitalization required
    draw_number = 2608
    result = get_dlb_result_by_draw(lottery_name, draw_number)
    
    Example 5: Get latest 5 DLB results
    ------------------------------------
    lottery_name = 'Shanida'
    results = get_dlb_latest_results(lottery_name, limit=5)
    
    Example 6: Get all active lottery names
    ----------------------------------------
    nlb_lotteries = get_nlb_lottery_names()
    dlb_lotteries = get_dlb_lottery_names()
    
    Remember:
    - NLB lottery names: lowercase with hyphens
    - DLB lottery names: exact match with proper capitalization
    - Dates: YYYY-MM-DD format
    - Get lottery names first to ensure you use the correct format
    """

# if __name__ == "__main__":  # please uncomment this, when U use this in locally (STDIO)
#     mcp.run()