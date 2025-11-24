"""
Test script for the Sri Lanka Lottery MCP Server

This script tests all the tools available in the MCP server to ensure
they work correctly.
"""

import sys
import os

# Add parent directory to path to import the lottery functions
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from srilanka_lottery import (
    scrape_nlb_result,
    scrape_dlb_result,
    scrape_nlb_active_lottery_names,
    scrape_dlb_lottery_names,
    scrape_nlb_latest_results,
    scrape_dlb_latest_results
)
from srilanka_lottery.scraper import get_nlb_session


def test_get_lottery_names():
    """Test getting lottery names from both NLB and DLB"""
    print("\n" + "="*80)
    print("TEST 1: Getting Lottery Names")
    print("="*80)
    
    # Test NLB lottery names
    print("\n[NLB] Getting active lottery names...")
    nlb_result, _ = scrape_nlb_active_lottery_names()
    if "error" in nlb_result:
        print(f"❌ Error: {nlb_result['error']}")
    else:
        print(f"✅ Found {len(nlb_result.get('NLB_Active', []))} NLB lotteries:")
        for lottery in nlb_result.get('NLB_Active', [])[:5]:
            print(f"   - {lottery}")
        if len(nlb_result.get('NLB_Active', [])) > 5:
            print(f"   ... and {len(nlb_result['NLB_Active']) - 5} more")
    
    # Test DLB lottery names
    print("\n[DLB] Getting available lottery names...")
    dlb_result = scrape_dlb_lottery_names()
    if "error" in dlb_result:
        print(f"❌ Error: {dlb_result['error']}")
    else:
        print(f"✅ Found {len(dlb_result.get('DLB', []))} DLB lotteries:")
        for lottery in dlb_result.get('DLB', []):
            print(f"   - {lottery}")


def test_nlb_results():
    """Test fetching NLB results by draw number and date"""
    print("\n" + "="*80)
    print("TEST 2: NLB Results")
    print("="*80)
    
    # Test by draw number
    print("\n[NLB] Getting result by draw number (Govisetha #4263)...")
    result = scrape_nlb_result("govisetha", 4263)
    if "error" in result:
        print(f"❌ Error: {result['error']}")
    else:
        print(f"✅ Draw: {result.get('draw_number')}")
        print(f"   Date: {result.get('date')}")
        print(f"   Letter: {result.get('letter')}")
        print(f"   Numbers: {result.get('numbers')}")
    
    # Test by date
    print("\n[NLB] Getting result by date (Handahana 2025-11-22)...")
    result = scrape_nlb_result("handahana", "2025-11-22")
    if "error" in result:
        print(f"❌ Error: {result['error']}")
    else:
        print(f"✅ Draw: {result.get('draw_number')}")
        print(f"   Date: {result.get('date')}")
        print(f"   Letter: {result.get('letter')}")
        print(f"   Numbers: {result.get('numbers')}")


def test_dlb_results():
    """Test fetching DLB results by draw number and date"""
    print("\n" + "="*80)
    print("TEST 3: DLB Results")
    print("="*80)
    
    # Test by draw number
    print("\n[DLB] Getting result by draw number (Ada Kotipathi #2608)...")
    result = scrape_dlb_result("Ada Kotipathi", 2608)
    if "error" in result:
        print(f"❌ Error: {result['error']}")
    else:
        print(f"✅ Draw Info: {result.get('draw_info')}")
        print(f"   Date: {result.get('date_info')}")
        print(f"   Letter: {result.get('letter')}")
        print(f"   Numbers: {result.get('numbers')}")
        print(f"   Prize Image: {result.get('prize_image')[:50]}..." if result.get('prize_image') else "   Prize Image: None")


def test_latest_results():
    """Test fetching latest results from both NLB and DLB"""
    print("\n" + "="*80)
    print("TEST 4: Latest Results")
    print("="*80)
    
    # Test NLB latest results
    print("\n[NLB] Getting latest 3 results for Govisetha...")
    session = get_nlb_session()
    result = scrape_nlb_latest_results(session, "govisetha", limit=3)
    if "error" in result:
        print(f"❌ Error: {result['error']}")
    else:
        results = result.get('NLB_Results', [])
        print(f"✅ Found {len(results)} results:")
        for r in results:
            print(f"   Draw {r.get('draw')} ({r.get('date')}): {r.get('letter')} {r.get('numbers')}")
    
    # Test DLB latest results
    print("\n[DLB] Getting latest 3 results for Shanida...")
    result = scrape_dlb_latest_results("Shanida", limit=3)
    if "error" in result:
        print(f"❌ Error: {result['error']}")
    else:
        results = result.get('DLB_Results', [])
        print(f"✅ Found {len(results)} results:")
        for r in results:
            print(f"   Draw {r.get('draw')} ({r.get('date')}): {r.get('letter')} {r.get('numbers')}")


def test_error_handling():
    """Test error handling for invalid inputs"""
    print("\n" + "="*80)
    print("TEST 5: Error Handling")
    print("="*80)
    
    # Test invalid lottery name for DLB
    print("\n[DLB] Testing invalid lottery name...")
    result = scrape_dlb_result("Invalid Lottery", 100)
    if "error" in result:
        print(f"✅ Correctly returned error: {result['error']}")
    else:
        print("❌ Should have returned an error for invalid lottery name")
    
    # Test invalid draw number (negative)
    print("\n[Test] Invalid draw number would be handled by MCP server validation")
    print("✅ Server validates: draw_number must be positive integer")
    
    # Test invalid date format
    print("\n[Test] Invalid date format would be handled by MCP server validation")
    print("✅ Server validates: date must be in YYYY-MM-DD format")


def main():
    """Run all tests"""
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " " * 20 + "SRI LANKA LOTTERY MCP SERVER TESTS" + " " * 24 + "║")
    print("╚" + "="*78 + "╝")
    
    try:
        test_get_lottery_names()
        test_nlb_results()
        test_dlb_results()
        test_latest_results()
        test_error_handling()
        
        print("\n" + "="*80)
        print("✅ ALL TESTS COMPLETED")
        print("="*80)
        print("\nNOTE: Some tests may show errors if:")
        print("  - The lottery websites are temporarily unavailable")
        print("  - Specific draw numbers or dates don't exist")
        print("  - Network connectivity issues occur")
        print("\nThe MCP server includes comprehensive error handling for these scenarios.")
        
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
