# Sri Lanka Lottery MCP Server 🎰

<div align="center">

[![Python 3.14+](https://img.shields.io/badge/python-3.14+-blue.svg)](https://www.python.org/downloads/)
[![FastMCP](https://img.shields.io/badge/FastMCP-2.13.1-green.svg)](https://gofastmcp.com)
[![Hosted on FastMCP Cloud](https://img.shields.io/badge/Hosted%20on-FastMCP%20Cloud-blueviolet.svg)](https://gofastmcp.com/deployment/fastmcp-cloud)


**A cloud-hosted Model Context Protocol (MCP) server for accessing Sri Lanka lottery results**

**🌐 Available 24/7 on FastMCP Cloud - No local installation needed!**

[Features](#-features) • [Quick Connect](#-quick-connect-cloud-hosted) • [Usage](#-usage) • [MCP Concepts](#-understanding-mcp) • [Documentation](#-documentation)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Understanding MCP](#-understanding-mcp-model-context-protocol)
- [Quick Connect (Cloud Hosted)](#-quick-connect-cloud-hosted)
- [Local Development (Optional)](#-local-development-optional)
- [Available Tools](#-available-tools)
- [Usage Examples](#-usage-examples)
- [Client Integration](#-client-integration)
- [FastMCP Cloud Deployment](#️-fastmcp-cloud-deployment)
- [MCP Server Architecture](#️-mcp-server-architecture)
- [API Reference](#-api-reference)
- [Testing](#-testing)
- [Troubleshooting](#️-troubleshooting)
- [Acknowledgments](#-acknowledgments)
- [License](#-license)
- [Support & Contact](#-support--contact)

---

## 🎯 Overview

The **Sri Lanka Lottery MCP Server** is a **cloud-hosted** Model Context Protocol server that provides real-time access to lottery results from Sri Lanka's National Lottery Board (NLB) and Development Lottery Board (DLB). Deployed on **FastMCP Cloud**, this server is available 24/7 without requiring any local installation or server management.

### 🌟 Cloud-Hosted Benefits

This server is **live on FastMCP Cloud**, which means:
- ✅ **Always Available** - 24/7 uptime, access from anywhere
- ✅ **Zero Setup** - No local installation required, just add to Claude Desktop
- ✅ **Automatic Updates** - Latest features deployed automatically
- ✅ **Fast & Secure** - Enterprise-grade infrastructure with HTTPS
- ✅ **No Maintenance** - We handle all server management

### What is MCP?

**Model Context Protocol (MCP)** is an open protocol that standardizes how applications provide context to Large Language Models (LLMs). Think of it as a universal connector that allows AI assistants to interact with external data sources, APIs, and tools in a standardized way.

### Why This Project?

This MCP server demonstrates:
- ✅ **Cloud-hosted MCP deployment** on FastMCP Cloud
- ✅ **Real-world MCP implementation** with web scraping
- ✅ **Best practices** for building production MCP servers
- ✅ **Complete tool ecosystem** (tools, prompts, and resources)
- ✅ **Remote HTTP integration** with Claude Desktop and other MCP clients

---

## ✨ Features

### Core Capabilities

- 🎯 **Complete Coverage**: Access both NLB and DLB lottery results
- 🔍 **Multiple Query Methods**: Fetch results by draw number, date, or get latest results
- 📋 **Lottery Discovery**: Get lists of all active/available lotteries
- ✅ **Input Validation**: Comprehensive validation with descriptive error messages
- 📚 **Built-in Documentation**: Includes prompts and resources for self-service help
- 🚀 **FastMCP Framework**: Built on FastMCP for optimal performance
- 🔄 **Session Management**: Automatic cookie handling for reliable scraping
- 🎨 **Name Normalization**: Automatic lottery name formatting

### MCP Components

This server implements all three MCP primitives:

1. **Tools (9)**: Executable functions for fetching lottery data
2. **Prompts (3)**: Pre-built templates for common queries
3. **Resources (3)**: Static documentation and information endpoints

---

## 🧠 Understanding MCP (Model Context Protocol)

### What is MCP?

MCP is an open protocol that enables seamless integration between LLM applications and external data sources. It provides a standardized way to:

- **Connect** LLMs to various data sources
- **Expose** tools and functions that LLMs can use
- **Provide** context through resources and prompts
- **Maintain** secure, controlled access to external systems

### MCP Architecture

```
┌─────────────────┐
│   LLM Client    │  (e.g., Claude Desktop)
│  (MCP Client)   │
└────────┬────────┘
         │ MCP Protocol (STDIO/HTTP)
         │
┌────────▼────────┐
│   MCP Server    │  (This Project)
│                 │
│  ┌───────────┐  │
│  │   Tools   │  │  Functions the LLM can call
│  ├───────────┤  │
│  │  Prompts  │  │  Templates for common tasks
│  ├───────────┤  │
│  │ Resources │  │  Static data/documentation
│  └───────────┘  │
└────────┬────────┘
         │
    ┌────▼────┐
    │ External│
    │ Sources │  (NLB & DLB websites)
    └─────────┘
```

### MCP Primitives Explained

#### 1. **Tools** (Functions)
Tools are executable functions that the LLM can call to perform actions or retrieve data.

**Example from this project:**
```python
@mcp.tool(description="Fetch NLB lottery result by draw number.")
def get_nlb_result_by_draw(lottery_name: str, draw_number: int) -> dict:
    """Fetches the NLB lottery result for a specific draw number."""
    # Implementation
```

#### 2. **Prompts** (Templates)
Prompts are pre-built templates that guide users through common workflows.

**Example from this project:**
```python
@mcp.prompt()
def check_lottery_result_prompt() -> str:
    """Prompt template for checking lottery results."""
    return """I want to check lottery results for Sri Lanka..."""
```

#### 3. **Resources** (Information)
Resources provide static information that the LLM can access for context.

**Example from this project:**
```python
@mcp.resource("lottery://nlb/info")
def nlb_lottery_info() -> str:
    """Information about NLB lotteries and how to use them."""
    return """NLB Lottery Information..."""
```

### How MCP Enables AI Integration

1. **Discovery**: The LLM client queries the MCP server for available tools
2. **Execution**: User requests trigger tool calls through the MCP protocol
3. **Response**: The server executes the tool and returns structured data
4. **Context**: The LLM uses the data to formulate intelligent responses

---

## ⚡ Quick Connect (Cloud Hosted)

**This server is already live on FastMCP Cloud!** No installation needed - just connect and use.

### Add to Claude Desktop (5 seconds!)

1. Open your Claude Desktop configuration file:
   - **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
   - **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Linux:** `~/.config/Claude/claude_desktop_config.json`

2. Add this configuration:

```json
{
  "mcpServers": {
    "lanka-lottery-cloud": {
      "transport": "http",
      "url": "https://your-server-id.fastmcp.cloud",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY_HERE"
      }
    }
  }
}
```

3. Replace `your-server-id.fastmcp.cloud` with the actual FastMCP Cloud URL
4. Replace `YOUR_API_KEY_HERE` with your API key (if authentication is enabled)
5. Restart Claude Desktop

**That's it!** You can now use all lottery tools in Claude Desktop.

### Connect from Other MCP Clients

This server is accessible via HTTP from any MCP-compatible client:
- **ChatGPT** (Pro/Team/Enterprise with Developer Mode)
- **Cursor IDE**
- **VS Code with MCP extension**
- **Any custom MCP client**

See [Integration Guide](#-client-integration) for details.

---

## 🏠 Local Development (Optional)

Want to run the server locally or contribute? Here's how:

### Prerequisites

- **Python 3.14+** or higher
- **uv** package manager (recommended) or **pip**
- Internet connection for web scraping

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/janak-dev2002/lanka-lottery-mcp.git
cd lanka-lottery-mcp

# Install dependencies
uv pip install -e .

# Run tests
uv run testing/test_mcp_server.py

# Start local server (STDIO mode)
uv run lottery_result_server.py
```

**Dependencies:**
- `fastmcp>=2.13.1` - MCP server framework
- `beautifulsoup4>=4.12.0` - HTML parsing
- `requests>=2.31.0` - HTTP requests

### Important Note for Cloud Deployment

⚠️ **The `if __name__ == "__main__"` block in `lottery_result_server.py` is ignored by FastMCP Cloud.**

When deploying to FastMCP Cloud, the server is run differently than local STDIO mode. The cloud platform automatically handles server initialization, so any code inside the `if __name__ == "__main__"` block will not be executed. This is why you'll see it commented out in the server code.

- **Local development:** Uncomment the `if __name__ == "__main__"` block to run with STDIO transport
- **Cloud deployment:** The block is automatically ignored; no changes needed

### Local Testing

```python
from srilanka_lottery import scrape_nlb_result, scrape_dlb_lottery_names

# Get available DLB lotteries
dlb_lotteries = scrape_dlb_lottery_names()
print(dlb_lotteries)

# Get NLB result by draw number
result = scrape_nlb_result('govisetha', 4263)
print(result)
```

---

## 🛠️ Available Tools

The MCP server provides **9 comprehensive tools** organized into three categories:

### 1. Lottery Discovery Tools

#### `get_nlb_lottery_names()`
Get all active NLB (National Lottery Board) lotteries.

**Returns:**
```json
{
  "NLB_Active": [
    "Ada Sampatha",
    "Dhana Nidhanaya",
    "Govisetha",
    "Handahana",
    "Lucky 7",
    "Lagna Vasana",
    "Mahajana Sampatha",
    "Mega Power",
    "Nimi Sampatha",
    "Saubhagya",
    "Sunday Fortune"
  ]
}
```

#### `get_dlb_lottery_names()`
Get all available DLB (Development Lottery Board) lotteries.

**Returns:**
```json
{
  "DLB": [
    "Ada Kotipathi",
    "Jaya Sampatha",
    "Jayoda",
    "Kapruka",
    "Lagna Wasana",
    "Sasiri",
    "Shanida",
    "Super Ball",
    "Supiri Dhana Sampatha"
  ]
}
```

### 2. NLB Result Tools

#### `get_nlb_result_by_draw(lottery_name: str, draw_number: int)`
Fetch NLB lottery result by draw number.

**Parameters:**
- `lottery_name`: Lottery name in lowercase with hyphens (e.g., `'mega-power'`, `'govisetha'`)
- `draw_number`: Positive integer draw number

**Example:**
```python
get_nlb_result_by_draw('govisetha', 4263)
```

**Returns:**
```json
{
  "draw_number": "4263",
  "date": "2025-11-22",
  "letter": "I",
  "numbers": ["12", "23", "60", "76"]
}
```

#### `get_nlb_result_by_date(lottery_name: str, date: str)`
Fetch NLB lottery result by date.

**Parameters:**
- `lottery_name`: Lottery name in lowercase with hyphens
- `date`: Date in YYYY-MM-DD format (e.g., `'2025-11-22'`)

**Example:**
```python
get_nlb_result_by_date('mahajana-sampatha', '2025-11-21')
```

**Returns:**
```json
{
  "draw_number": "1234",
  "date": "2025-11-21",
  "letter": "A",
  "numbers": ["05", "18", "42", "73"]
}
```

#### `get_nlb_latest_results(lottery_name: str, limit: int = 5)`
Get the latest NLB lottery results.

**Parameters:**
- `lottery_name`: Lottery name in lowercase with hyphens
- `limit`: Number of results to return (default: 5, max recommended: 20)

**Example:**
```python
get_nlb_latest_results('govisetha', limit=3)
```

**Returns:**
```json
{
  "NLB_Results": [
    {
      "draw": "4263",
      "date": "Saturday November 22, 2025",
      "letter": "I",
      "numbers": ["12", "23", "60", "76"]
    },
    {
      "draw": "4262",
      "date": "Friday November 21, 2025",
      "letter": "E",
      "numbers": ["34", "55", "62", "80"]
    },
    {
      "draw": "4261",
      "date": "Thursday November 20, 2025",
      "letter": "T",
      "numbers": ["13", "25", "29", "51"]
    }
  ]
}
```

### 3. DLB Result Tools

#### `get_dlb_result_by_draw(lottery_name: str, draw_number: int)`
Fetch DLB lottery result by draw number.

**Parameters:**
- `lottery_name`: Exact lottery name with proper capitalization (e.g., `'Ada Kotipathi'`, `'Shanida'`)
- `draw_number`: Positive integer draw number

**Example:**
```python
get_dlb_result_by_draw('Ada Kotipathi', 2608)
```

**Returns:**
```json
{
  "draw_info": "Ada Kotipathi",
  "date_info": "Draw Number - 2608  |  2025-Apr-21 Monday",
  "letter": "Y",
  "numbers": ["33", "42", "55", "61"],
  "prize_image": "https://www.dlb.lk/front_img/..."
}
```

#### `get_dlb_result_by_date(lottery_name: str, date: str)`
Fetch DLB lottery result by date.

**Parameters:**
- `lottery_name`: Exact lottery name with proper capitalization
- `date`: Date in YYYY-MM-DD format

**Example:**
```python
get_dlb_result_by_date('Shanida', '2025-11-15')
```

#### `get_dlb_latest_results(lottery_name: str, limit: int = 5)`
Get the latest DLB lottery results.

**Parameters:**
- `lottery_name`: Exact lottery name with proper capitalization
- `limit`: Number of results to return (default: 5, max recommended: 20)

**Example:**
```python
get_dlb_latest_results('Jayoda', limit=5)
```

---

## 💡 Usage Examples

### Example 1: Get Available Lotteries

```python
# Get all NLB lotteries
nlb_lotteries = get_nlb_lottery_names()
print(f"Found {len(nlb_lotteries['NLB_Active'])} NLB lotteries")

# Get all DLB lotteries
dlb_lotteries = get_dlb_lottery_names()
print(f"Found {len(dlb_lotteries['DLB'])} DLB lotteries")
```

### Example 2: Check Today's Results

```python
# Get latest NLB result
latest_nlb = get_nlb_latest_results('govisetha', limit=1)
result = latest_nlb['NLB_Results'][0]
print(f"Govisetha Draw {result['draw']}: {result['letter']} {result['numbers']}")

# Get latest DLB result
latest_dlb = get_dlb_latest_results('Ada Kotipathi', limit=1)
result = latest_dlb['DLB_Results'][0]
print(f"Ada Kotipathi Draw {result['draw']}: {result['letter']} {result['numbers']}")
```

### Example 3: Check Specific Draw

```python
# Check NLB by draw number
result = get_nlb_result_by_draw('mega-power', 2166)
print(f"Mega Power #{result['draw_number']}: {result['numbers']}")

# Check DLB by draw number
result = get_dlb_result_by_draw('Shanida', 3500)
print(f"Shanida: {result['draw_info']}")
```

### Example 4: Historical Results by Date

```python
# Check NLB results for a specific date
result = get_nlb_result_by_date('govisetha', '2025-11-01')
print(f"Govisetha on 2025-11-01: {result['numbers']}")

# Check DLB results for a specific date
result = get_dlb_result_by_date('Jayoda', '2025-11-01')
print(f"Jayoda on 2025-11-01: {result['numbers']}")
```

### Example 5: Analyze Recent Trends

```python
# Get last 10 results for analysis
results = get_nlb_latest_results('govisetha', limit=10)

# Analyze winning letters
letters = [r['letter'] for r in results['NLB_Results']]
print(f"Recent winning letters: {letters}")

# Analyze number frequencies
all_numbers = []
for r in results['NLB_Results']:
    all_numbers.extend([int(n) for n in r['numbers']])
print(f"Number frequency: {dict.fromkeys(all_numbers)}")
```

---

## 🔧 Client Integration

### Claude Desktop (Recommended)

**This server is hosted on FastMCP Cloud**, so you connect via HTTP instead of local STDIO.

#### Configuration File Location

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

**macOS:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Linux:**
```
~/.config/Claude/claude_desktop_config.json
```

#### Cloud Configuration (Current Setup)

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "lanka-lottery-cloud": {
      "transport": "http",
      "url": "https://your-server-id.fastmcp.cloud",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY_HERE"
      }
    }
  }
}
```

**Important:**
- Replace `your-server-id.fastmcp.cloud` with the actual FastMCP Cloud URL
- Replace `YOUR_API_KEY_HERE` with your API key (if authentication is enabled)
- The server name will appear as "Sri Lanka Lottery Results" in Claude Desktop

#### Verification Steps

1. Save `claude_desktop_config.json`
2. Restart Claude Desktop completely
3. Look for the MCP server icon (🔌) in the chat interface
4. "Sri Lanka Lottery Results" should appear in available servers
5. Try a test prompt: "What NLB lotteries are available?"

### ChatGPT Integration

This server works with **ChatGPT Pro/Team/Enterprise** in both Chat and Deep Research modes.

#### Chat Mode (Requires Developer Mode)

1. Enable **Developer Mode** in ChatGPT settings
2. Add the server URL in MCP settings:
   ```
   Server URL: https://your-server-id.fastmcp.cloud
   Authorization: Bearer YOUR_API_KEY_HERE
   ```

#### Deep Research Mode

Deep Research mode can access MCP servers without Developer Mode for comprehensive lottery data analysis.

See the [ChatGPT Integration Guide](https://gofastmcp.com/integrations/chatgpt) for details.

### Other MCP Clients

This HTTP-based server works with any MCP-compatible client:
- **Cursor IDE** - Add to MCP settings
- **VS Code** - Use MCP extension
- **Custom Clients** - Connect via FastMCP Client library

---

## ☁️ FastMCP Cloud Deployment

### About This Deployment

This server is **deployed on FastMCP Cloud**, which provides:

✅ **24/7 Availability** - Always online, no local server needed  
✅ **Automatic Updates** - Changes deployed via GitHub integration  
✅ **HTTPS Security** - Secure connections with optional authentication  
✅ **Performance Monitoring** - Built-in logging and metrics  
✅ **Zero Maintenance** - Managed infrastructure  
✅ **Free Tier Available** - Free for personal use during beta  

### How It Works

1. **GitHub Integration** - Server code hosted in GitHub repository
2. **Auto-Deploy** - FastMCP Cloud monitors repo and deploys on push
3. **Unique URL** - Server available at `https://your-project.fastmcp.cloud`
4. **PR Previews** - Each PR gets its own test deployment URL
5. **HTTP Transport** - Remote access via HTTP/HTTPS (not STDIO)

### Deployment Architecture

```
┌─────────────────────┐
│  GitHub Repository  │
│  (Source Code)      │
└──────────┬──────────┘
           │ Push to main
           ↓
┌─────────────────────┐
│  FastMCP Cloud      │
│  - Build & Deploy   │
│  - HTTPS Endpoint   │
│  - Auto-scaling     │
└──────────┬──────────┘
           │ MCP over HTTP
           ↓
┌─────────────────────┐
│  MCP Clients        │
│  - Claude Desktop   │
│  - ChatGPT          │
│  - Cursor           │
│  - Custom Clients   │
└─────────────────────┘
```

### Want to Deploy Your Own?

If you want to deploy your own version or fork this server:

```bash
# 1. Fork this repository on GitHub

# 2. Sign in to FastMCP Cloud
# Visit: https://fastmcp.cloud

# 3. Create new project
# - Connect your GitHub repository
# - Set entrypoint: lottery_result_server.py:mcp
# - Deploy!

# 4. Get your unique URL
# https://your-project.fastmcp.cloud
```

### Learn More

- **FastMCP Cloud Docs**: https://gofastmcp.com/deployment/fastmcp-cloud
- **HTTP Deployment Guide**: https://gofastmcp.com/deployment/http
- **FastMCP Framework**: https://gofastmcp.com

---

### Example Prompts for Claude

Once integrated, try these prompts:

```
"What NLB and DLB lotteries are currently available?"

"Show me the results for Govisetha lottery draw number 4263"

"What were the lottery results for Ada Kotipathi on November 22, 2025?"

"Get me the last 10 results for Mega Power"

"What was the Mahajana Sampatha result for day before yesterday?"

"Compare the latest 5 results for Govisetha and Mega Power"
```

---

## 🏗️ MCP Server Architecture

### Server Structure

```python
# lottery_result_server.py

from fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP(
    "Sri Lanka Lottery Results",
    version="2.0.0",
    instructions="..."
)

# Define tools
@mcp.tool(description="...")
def get_nlb_result_by_draw(lottery_name: str, draw_number: int) -> dict:
    # Tool implementation
    pass

# Define prompts
@mcp.prompt()
def check_lottery_result_prompt() -> str:
    # Prompt template
    return "..."

# Define resources
@mcp.resource("lottery://nlb/info")
def nlb_lottery_info() -> str:
    # Resource content
    return "..."

# Run server
if __name__ == "__main__":
    mcp.run()
```

### Transport Protocol

This MCP server uses **HTTP (Streamable HTTP)** transport for cloud deployment:

```
┌─────────────┐                    ┌─────────────┐
│   Client    │ ←─── HTTPS ────────│  MCP Server │
│ (Claude AI) │                    │ (FastMCP    │
│             │                    │  Cloud)     │
└─────────────┘                    └─────────────┘
```

**Benefits of HTTP (Cloud):**
- ✅ Accessible from anywhere via URL
- ✅ Multiple clients can connect simultaneously
- ✅ No local server management required
- ✅ Secure HTTPS with optional authentication
- ✅ 24/7 availability with auto-scaling

**Local Development:**
The server can also run with STDIO transport for local testing. See [Local Development](#-local-development-optional) section.

### Tool Execution Flow

```
1. User Query (in Claude Desktop)
   ↓
2. Claude calls MCP tool
   ↓
3. MCP server validates input
   ↓
4. Server scrapes lottery website
   ↓
5. Data parsed and formatted
   ↓
6. Response sent back to Claude
   ↓
7. Claude presents result to user
```

### Error Handling Strategy

The server implements multi-layer error handling:

1. **Input Validation**: Check parameters before processing
2. **Network Errors**: Handle connection and timeout issues
3. **Data Parsing**: Detect missing or malformed data
4. **Descriptive Messages**: Return actionable error information

**Example error response:**
```json
{
  "error": "Date must be in YYYY-MM-DD format (e.g., '2025-11-23')"
}
```

---

## 📚 API Reference

### Lottery Name Formats

#### NLB Lotteries
**Format:** Lowercase with hyphens

| Display Name | API Name |
|--------------|----------|
| Mega Power | `mega-power` |
| Govisetha | `govisetha` |
| Dhana Nidhanaya | `dhana-nidhanaya` |
| Mahajana Sampatha | `mahajana-sampatha` |
| Handahana | `handahana` |
| Lucky 7 | `lucky-7` |

**Automatic Normalization:** The server automatically converts any format to the correct one.

#### DLB Lotteries
**Format:** Exact capitalization with spaces

| Lottery Name |
|--------------|
| Ada Kotipathi |
| Jayoda |
| Lagna Wasana |
| Sasiri |
| Shanida |
| Super Ball |
| Supiri Dhana Sampatha |
| Jaya Sampatha |
| Kapruka |

### Date Format

**Required Format:** `YYYY-MM-DD`

✅ **Correct:**
- `'2025-11-23'`
- `'2025-01-15'`
- `'2024-12-31'`

❌ **Incorrect:**
- `'23-11-2025'`
- `'11/23/2025'`
- `'Nov 23, 2025'`
- `'2025-1-5'` (must be zero-padded)

### Response Formats

#### NLB Result
```typescript
{
  draw_number: string,    // e.g., "4263"
  date: string,          // e.g., "2025-11-22"
  letter: string,        // e.g., "I"
  numbers: string[]      // e.g., ["12", "23", "60", "76"]
}
```

#### DLB Result
```typescript
{
  draw_info: string,     // e.g., "Ada Kotipathi 2608"
  date_info: string,     // e.g., "2025-Apr-21 Monday"
  letter: string,        // e.g., "Y"
  numbers: string[],     // e.g., ["33", "42", "55", "61"]
  prize_image: string    // URL to prize image
}
```

#### Latest Results
```typescript
{
  NLB_Results: [{        // or DLB_Results
    draw: string,
    date: string,
    letter: string,
    numbers: string[]
  }]
}
```

#### Error Response
```typescript
{
  error: string          // Descriptive error message
}
```

---

## 🧪 Testing

### Run Comprehensive Tests

```bash
cd lanka-lottery-mcp
uv run testing/test_mcp_server.py
```

### Expected Test Output

```
╔==============================================================================╗
║                    SRI LANKA LOTTERY MCP SERVER TESTS                        ║
╚==============================================================================╝

================================================================================
TEST 1: Getting Lottery Names
================================================================================

[NLB] Getting active lottery names...
✅ Found 11 NLB lotteries:
   - Ada Sampatha
   - Dhana Nidhanaya
   - Govisetha
   ...

[DLB] Getting available lottery names...
✅ Found 9 DLB lotteries:
   - Ada Kotipathi
   - Jayoda
   - Shanida
   ...

================================================================================
TEST 2: NLB Results
================================================================================

[NLB] Getting result by draw number (Govisetha #4263)...
✅ Draw: 4263
   Date: 2025-11-22
   Letter: I
   Numbers: ['12', '23', '60', '76']

...

================================================================================
✅ ALL TESTS COMPLETED
================================================================================
```

### Manual Testing

```python
# Test individual functions
from srilanka_lottery import scrape_nlb_result

# Test NLB result
result = scrape_nlb_result('govisetha', 4263)
print(result)

# Test with date
result = scrape_nlb_result('mahajana-sampatha', '2025-11-21')
print(result)
```

---

## ⚠️ Troubleshooting

### Common Issues and Solutions

#### Issue: "Lottery not found" Error

**Cause:** Incorrect lottery name format

**Solution:**
```python
# First, get the correct names
nlb_names = get_nlb_lottery_names()
dlb_names = get_dlb_lottery_names()

# Then use exact names from the list
result = get_nlb_result_by_draw('govisetha', 4263)  # ✅
result = get_dlb_result_by_draw('Ada Kotipathi', 2608)  # ✅
```

#### Issue: "Date must be in YYYY-MM-DD format" Error

**Cause:** Wrong date format

**Solution:**
```python
# ❌ Wrong
result = get_nlb_result_by_date('govisetha', '22-11-2025')

# ✅ Correct
result = get_nlb_result_by_date('govisetha', '2025-11-22')
```

#### Issue: Server Not Starting

**Cause:** Missing dependencies or Python version

**Solution:**
```bash
# Check Python version
python --version  # Should be 3.14+

# Reinstall dependencies
uv pip install -e .

# Try running directly
python lottery_result_server.py
```

#### Issue: Claude Desktop Not Detecting Server

**Cause:** Configuration file issues

**Solution:**
1. Verify `claude_desktop_config.json` location
2. Check JSON syntax (use a JSON validator)
3. Verify file paths are correct (use forward slashes or escaped backslashes)
4. Restart Claude Desktop completely

#### Issue: "Request failed" or "Result block not found"

**Cause:** Network issues or draw doesn't exist

**Solution:**
1. Check internet connection
2. Verify the draw number/date exists
3. Try a different lottery or date
4. Check if lottery websites are accessible

### Debug Mode

For detailed debugging, modify the server:

```python
# In lottery_result_server.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Getting Help

1. **Check Documentation**: Review this README thoroughly
2. **Run Tests**: Execute `uv run testing/test_mcp_server.py`
3. **FastMCP Docs**: Visit https://gofastmcp.com
4. **GitHub Issues**: Report bugs or ask questions

---

## 🙏 Acknowledgments

### Special Thanks

This project would not be possible without the excellent work of:

- **[Ishan Oshada](https://github.com/Ishanoshada)** - For creating the [Srilanka-Lottery](https://github.com/Ishanoshada/Srilanka-Lottery) library, which provides the core web scraping functionality for accessing NLB and DLB lottery data. This project builds upon and extends that work into an MCP server.

### Built With

- **[FastMCP](https://gofastmcp.com)** - Modern Python framework for building MCP servers
- **[FastMCP Cloud](https://gofastmcp.com/deployment/fastmcp-cloud)** - Managed hosting platform for MCP servers
- **[Requests](https://requests.readthedocs.io/)** - HTTP library for Python
- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)** - HTML parsing library
- **[Model Context Protocol](https://modelcontextprotocol.io/)** - Open protocol by Anthropic

### Hosted On

- **[FastMCP Cloud](https://fastmcp.cloud)** - Production deployment and hosting

### Data Sources

- **[National Lottery Board (NLB)](https://www.nlb.lk)** - Sri Lanka's National Lottery Board
- **[Development Lottery Board (DLB)](https://www.dlb.lk)** - Sri Lanka's Development Lottery Board

### Inspiration

This project demonstrates:
- Cloud-hosted MCP server deployment
- Real-world MCP server implementation
- Integration of web scraping with AI assistants
- Best practices for building production-ready MCP servers
- Remote HTTP transport for multi-client access

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 lanka-lottery-mcp

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 📞 Support & Contact

### Documentation

- **Full Documentation**: This README
- **FastMCP Cloud**: https://gofastmcp.com/deployment/fastmcp-cloud
- **HTTP Deployment**: https://gofastmcp.com/deployment/http
- **Claude Integration**: https://gofastmcp.com/integrations/claude-desktop
- **ChatGPT Integration**: https://gofastmcp.com/integrations/chatgpt

### Resources

- **FastMCP Documentation**: https://gofastmcp.com
- **FastMCP Cloud Platform**: https://fastmcp.cloud
- **MCP Specification**: https://modelcontextprotocol.io
- **Project Repository**: https://github.com/janak-dev2002/lanka-lottery-mcp

### Quick Reference

| Task | Method |
|------|---------|
| **Connect to Cloud** | Add HTTP config to Claude Desktop |
| **Server URL** | `https://your-server-id.fastmcp.cloud` |
| **Get NLB Names** | `get_nlb_lottery_names()` |
| **Get DLB Names** | `get_dlb_lottery_names()` |
| **NLB by Draw** | `get_nlb_result_by_draw('lottery', draw)` |
| **NLB by Date** | `get_nlb_result_by_date('lottery', 'YYYY-MM-DD')` |
| **DLB Latest** | `get_dlb_latest_results('Lottery', limit)` |
| **Local Dev** | `uv run lottery_result_server.py` |
| **Run Tests** | `uv run testing/test_mcp_server.py` |

---

<div align="center">

**Made with ❤️ for the Sri Lankan lottery community**

**Hosted on [FastMCP Cloud](https://fastmcp.cloud)** | **Powered by [FastMCP](https://gofastmcp.com)**

**Version 2.0.0** | **Last Updated: November 24, 2025**

[⬆ Back to Top](#sri-lanka-lottery-mcp-server-)

</div>