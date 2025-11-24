# Understanding Model Context Protocol (MCP) 🧠

<div align="center">

**A Comprehensive Guide to MCP Servers, Tools, Resources, and Prompts**

*Learn by example using the Sri Lanka Lottery MCP Server*

[What is MCP?](#-what-is-mcp) • [Core Concepts](#-core-concepts) • [MCP Primitives](#-mcp-primitives) • [Building Servers](#-building-mcp-servers) • [Best Practices](#-best-practices)

</div>

---

## 📋 Table of Contents

- [What is MCP?](#-what-is-mcp)
- [Why MCP Matters](#-why-mcp-matters)
- [Core Concepts](#-core-concepts)
- [MCP Architecture](#️-mcp-architecture)
- [MCP Primitives](#-mcp-primitives)
  - [Tools](#1-tools-executable-functions)
  - [Resources](#2-resources-static-information)
  - [Prompts](#3-prompts-reusable-templates)
- [Building MCP Servers](#-building-mcp-servers)
- [Transport Protocols](#-transport-protocols)
- [Real-World Examples](#-real-world-examples)
- [Integration Patterns](#-integration-patterns)
- [Best Practices](#-best-practices)
- [Common Use Cases](#-common-use-cases)
- [Further Resources](#-further-resources)

---

## 🎯 What is MCP?

**Model Context Protocol (MCP)** is an **open protocol** developed by Anthropic that standardizes how AI applications communicate with external data sources and tools. Think of it as a universal adapter that allows Large Language Models (LLMs) to interact with databases, APIs, file systems, and other services in a consistent, secure way.

### The Problem MCP Solves

Before MCP, integrating AI assistants with external data required:
- ❌ Custom integrations for each data source
- ❌ Inconsistent APIs and data formats
- ❌ Security and permission management complexity
- ❌ Repeated implementation work for similar features

### The MCP Solution

With MCP, you get:
- ✅ **Standardized Protocol** - One protocol for all integrations
- ✅ **Reusable Components** - Build once, use everywhere
- ✅ **Secure Access** - Built-in permission and authentication
- ✅ **Ecosystem Growth** - Share and discover MCP servers

---

## 💡 Why MCP Matters

### For Developers

```python
# Without MCP: Custom integration for each AI assistant
class CustomClaudeIntegration:
    def get_data(self): ...
    
class CustomChatGPTIntegration:
    def get_data(self): ...
    
class CustomCursorIntegration:
    def get_data(self): ...

# With MCP: One server, all assistants
@mcp.tool()
def get_data():
    """Works with Claude, ChatGPT, Cursor, and more!"""
    return fetch_data()
```

### For AI Applications

MCP enables AI assistants to:
- 📊 Access real-time data (databases, APIs, files)
- 🔧 Execute actions (run commands, modify files, send emails)
- 🧩 Combine multiple data sources seamlessly
- 🔒 Maintain security and access control

### For Users

- 🚀 More powerful AI interactions
- 🔌 Easy-to-add capabilities (just configure, no coding)
- 🌐 Access to shared MCP server ecosystem
- 🔄 Consistent experience across different AI assistants

---

## 🧩 Core Concepts

### 1. MCP Server

An **MCP Server** is a program that:
- Exposes **tools**, **resources**, and **prompts** to AI clients
- Handles requests from MCP clients
- Manages connections to external data sources
- Provides structured responses

**Example:** The Sri Lanka Lottery MCP Server provides access to lottery results.

### 2. MCP Client

An **MCP Client** is an application that:
- Connects to MCP servers
- Discovers available tools and resources
- Sends requests and receives responses
- Presents data to users or LLMs

**Examples:** Claude Desktop, ChatGPT, Cursor IDE

### 3. Transport Protocol

The **Transport Protocol** defines how clients and servers communicate:
- **STDIO** - Standard input/output (local processes)
- **HTTP** - RESTful HTTP/HTTPS (remote servers)
- **SSE** - Server-Sent Events (streaming)

---

## 🏗️ MCP Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        USER                                 │
│                 "What are today's lottery results?"         │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                    MCP CLIENT                               │
│              (Claude Desktop, ChatGPT, etc.)                │
│                                                             │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   LLM Core  │  │  MCP Client  │  │  UI/Display  │      │
│  │             │←→│   Library    │←→│              │      │
│  └─────────────┘  └──────┬───────┘  └──────────────┘      │
└───────────────────────────┼─────────────────────────────────┘
                            │
                            │ MCP Protocol (STDIO/HTTP)
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                    MCP SERVER                               │
│            (Sri Lanka Lottery Server)                       │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │              MCP Server Framework                  │    │
│  │                 (FastMCP)                          │    │
│  └──────┬─────────────┬─────────────┬─────────────────┘    │
│         │             │             │                       │
│    ┌────▼───┐   ┌────▼────┐   ┌────▼────┐                 │
│    │ Tools  │   │Resources│   │ Prompts │                 │
│    │        │   │         │   │         │                 │
│    │ • NLB  │   │ • Info  │   │ • Check │                 │
│    │ • DLB  │   │ • Docs  │   │ • Guide │                 │
│    └────┬───┘   └────┬────┘   └────┬────┘                 │
│         │            │             │                       │
│         └────────────┼─────────────┘                       │
│                      │                                     │
│           ┌──────────▼───────────┐                         │
│           │  Business Logic      │                         │
│           │  (srilanka_lottery)  │                         │
│           └──────────┬───────────┘                         │
└──────────────────────┼─────────────────────────────────────┘
                       │
                       │ HTTP Requests
                       │
┌──────────────────────▼─────────────────────────────────────┐
│               EXTERNAL DATA SOURCES                         │
│                                                             │
│     ┌────────────────┐         ┌────────────────┐          │
│     │  NLB Website   │         │  DLB Website   │          │
│     │  www.nlb.lk    │         │  www.dlb.lk    │          │
│     └────────────────┘         └────────────────┘          │
└─────────────────────────────────────────────────────────────┘
```

### Request Flow

```
1. User asks question
   ↓
2. Client LLM determines which tool to call
   ↓
3. Client sends MCP request to server
   ↓
4. Server validates input parameters
   ↓
5. Server executes business logic
   ↓
6. Server fetches data from external source
   ↓
7. Server formats and returns response
   ↓
8. Client LLM processes response
   ↓
9. User sees formatted answer
```

---

## 🛠️ MCP Primitives

MCP defines three core primitives that servers can expose:

### 1. Tools (Executable Functions)

**Tools** are functions that the LLM can call to perform actions or retrieve data.

#### Anatomy of a Tool

```python
@mcp.tool(
    description="Brief description of what the tool does"
)
def tool_name(
    param1: str,  # Type-annotated parameters
    param2: int   # Help LLM understand expected inputs
) -> dict:      # Return type annotation
    """
    Detailed docstring explaining:
    - What the tool does
    - Parameter requirements
    - Return value format
    - Example usage
    """
    # Input validation
    if not param1:
        return {"error": "param1 is required"}
    
    # Business logic
    result = perform_action(param1, param2)
    
    # Structured response
    return {
        "success": True,
        "data": result
    }
```

#### Real Example from Lottery Server

```python
@mcp.tool(
    description="Fetch NLB lottery result by draw number. "
                "Provide lottery name in lowercase with hyphens "
                "(e.g., 'mega-power', 'govisetha') and a positive "
                "integer draw number."
)
def get_nlb_result_by_draw(lottery_name: str, draw_number: int) -> dict:
    """
    Fetches the NLB lottery result for a specific draw number.
    
    Args:
        lottery_name: Lottery name in lowercase with hyphens 
                     (e.g., 'mega-power', 'govisetha')
        draw_number: Positive integer representing the draw number
    
    Returns:
        dict: Contains draw_number, date, letter, and numbers
        
    Example:
        >>> get_nlb_result_by_draw('govisetha', 4263)
        {
            "draw_number": "4263",
            "date": "2025-11-22",
            "letter": "I",
            "numbers": ["12", "23", "60", "76"]
        }
    """
    # Validation
    if not lottery_name or not isinstance(lottery_name, str):
        return {"error": "Lottery name must be a non-empty string"}
    
    if not isinstance(draw_number, int) or draw_number <= 0:
        return {"error": "Draw number must be a positive integer"}
    
    # Normalize lottery name
    normalized_name = lottery_name.lower().replace(' ', '-')
    
    try:
        # Call scraping function
        result = scrape_nlb_result(normalized_name, draw_number)
        return result
    except Exception as e:
        return {"error": f"Failed to fetch result: {str(e)}"}
```

#### Tool Design Best Practices

1. **Clear Descriptions**: Help the LLM understand when to use the tool
2. **Type Annotations**: Guide parameter expectations
3. **Input Validation**: Check parameters before processing
4. **Structured Returns**: Use consistent JSON/dict formats
5. **Error Handling**: Return descriptive error messages
6. **Documentation**: Include docstrings with examples

#### Tool Categories in Lottery Server

**Discovery Tools:**
```python
get_nlb_lottery_names()  # List available NLB lotteries
get_dlb_lottery_names()  # List available DLB lotteries
```

**Query Tools:**
```python
get_nlb_result_by_draw(lottery, draw)    # Fetch by draw number
get_nlb_result_by_date(lottery, date)    # Fetch by date
get_nlb_latest_results(lottery, limit)   # Fetch recent results
```

**Batch Tools:**
```python
get_dlb_latest_results(lottery, limit=5)  # Multiple results at once
```

---

### 2. Resources (Static Information)

**Resources** provide static or semi-static information that enriches the AI's context.

#### Anatomy of a Resource

```python
@mcp.resource(
    "protocol://category/subcategory",  # URI-style identifier
    name="Human-readable name",          # Display name
    description="What this resource provides"
)
def resource_name() -> str:
    """
    Returns static information that helps the LLM:
    - Understand the domain
    - Learn usage patterns
    - Access reference documentation
    """
    return """
    # Resource Content
    
    Detailed information about:
    - Available features
    - How to use them
    - Examples and patterns
    - Important notes
    """
```

#### Real Example from Lottery Server

```python
@mcp.resource(
    "lottery://nlb/info",
    name="NLB Lottery Information",
    description="Comprehensive guide to NLB lotteries and their usage"
)
def nlb_lottery_info() -> str:
    """Provides detailed information about NLB lotteries."""
    return """
# NLB (National Lottery Board) Lotteries

## Available Lotteries

The following NLB lotteries are currently active:
- Govisetha
- Mega Power
- Dhana Nidhanaya
- Mahajana Sampatha
- Handahana
- Lucky 7
- Ada Sampatha
- Saubhagya
- Nimi Sampatha
- Lagna Vasana
- Sunday Fortune

## Lottery Name Format

For NLB lotteries, always use lowercase with hyphens:
- "Mega Power" → "mega-power"
- "Dhana Nidhanaya" → "dhana-nidhanaya"
- "Mahajana Sampatha" → "mahajana-sampatha"

## Available Tools

1. **get_nlb_result_by_draw(lottery_name, draw_number)**
   - Fetch result for a specific draw number
   - Example: get_nlb_result_by_draw('govisetha', 4263)

2. **get_nlb_result_by_date(lottery_name, date)**
   - Fetch result for a specific date
   - Date format: YYYY-MM-DD
   - Example: get_nlb_result_by_date('mega-power', '2025-11-22')

3. **get_nlb_latest_results(lottery_name, limit)**
   - Get the most recent results
   - Default limit: 5, Max recommended: 20
   - Example: get_nlb_latest_results('govisetha', 10)

## Result Format

NLB results include:
- Draw number
- Draw date
- Winning letter
- Winning numbers (4 numbers)

Example:
{
  "draw_number": "4263",
  "date": "2025-11-22",
  "letter": "I",
  "numbers": ["12", "23", "60", "76"]
}
"""
```

#### Resource Use Cases

1. **Documentation**: API reference, usage guides
2. **Schema Information**: Data structure definitions
3. **Domain Knowledge**: Business rules, terminology
4. **Examples**: Sample queries and responses
5. **Status Information**: Service health, availability

#### Resource vs Tool

| Feature | Resource | Tool |
|---------|----------|------|
| **Purpose** | Provide information | Execute actions |
| **Execution** | Read-only | Can modify state |
| **Updates** | Static or cached | Dynamic/real-time |
| **LLM Usage** | Context enrichment | Active function calls |
| **Examples** | Docs, schemas, help | Fetch data, run commands |

---

### 3. Prompts (Reusable Templates)

**Prompts** are pre-built templates that guide users through common workflows.

#### Anatomy of a Prompt

```python
@mcp.prompt(
    name="prompt-name",
    description="What this prompt helps with"
)
def prompt_function(
    param1: str = "default"  # Optional parameters with defaults
) -> str:
    """
    Returns a prompt template that:
    - Guides the user through a workflow
    - Provides context for the LLM
    - Suggests next steps
    """
    return f"""
I want to accomplish [task] with the following details:

1. Context: {param1}
2. Requirements: ...
3. Expected outcome: ...

Please help me by:
- Step 1: ...
- Step 2: ...
- Step 3: ...
"""
```

#### Real Example from Lottery Server

```python
@mcp.prompt(
    name="check-lottery-result",
    description="Guide for checking Sri Lanka lottery results"
)
def check_lottery_result_prompt() -> str:
    """Template for checking lottery results."""
    return """
I want to check lottery results for Sri Lanka. Here's what I need:

**Lottery Board:** [Choose: NLB or DLB]

**Lottery Name:** [Specify lottery name]
- For NLB: Use lowercase with hyphens (e.g., 'mega-power', 'govisetha')
- For DLB: Use exact capitalization (e.g., 'Ada Kotipathi', 'Shanida')

**Query Type:** [Choose one]
1. Latest results (specify how many)
2. Specific draw number (provide draw number)
3. Specific date (provide date in YYYY-MM-DD format)

Please help me:
1. First, show me available lotteries if I'm unsure
2. Then fetch the requested results
3. Display the winning numbers clearly
"""

@mcp.prompt(
    name="compare-lotteries",
    description="Compare results across multiple lotteries"
)
def compare_lotteries_prompt() -> str:
    """Template for comparing lottery results."""
    return """
I want to compare lottery results across different games.

**Lotteries to Compare:**
1. [First lottery name]
2. [Second lottery name]
3. [Add more as needed]

**Comparison Criteria:**
- Time period: [e.g., "Last 10 draws", "November 2025"]
- Aspects: [e.g., "Number frequency", "Letter patterns", "Win dates"]

Please:
1. Fetch results for all specified lotteries
2. Analyze patterns and trends
3. Present findings in an easy-to-understand format
4. Highlight any interesting insights
"""

@mcp.prompt(
    name="lottery-statistics",
    description="Generate statistics and analysis for lottery results"
)
def lottery_statistics_prompt() -> str:
    """Template for lottery statistical analysis."""
    return """
I want to analyze lottery statistics for better understanding.

**Lottery:** [Specify lottery name]

**Analysis Type:**
- [ ] Number frequency analysis
- [ ] Letter distribution
- [ ] Draw date patterns
- [ ] Historical trends
- [ ] Custom analysis: [specify]

**Time Range:**
- Last [X] draws
- Or date range: [YYYY-MM-DD] to [YYYY-MM-DD]

Please provide:
1. Detailed statistical breakdown
2. Visualizations (if possible)
3. Notable patterns or anomalies
4. Insights and observations
"""
```

#### Prompt Design Best Practices

1. **Clear Structure**: Use sections and formatting
2. **Placeholders**: Show where user input goes
3. **Options**: List available choices
4. **Guidance**: Explain what to do next
5. **Examples**: Include sample inputs
6. **Progressive**: Build complexity step-by-step

#### When to Use Prompts

✅ **Good Use Cases:**
- Complex multi-step workflows
- Common user tasks
- Domain-specific queries
- Educational/onboarding scenarios

❌ **Avoid for:**
- Simple single-tool calls
- Rarely-used edge cases
- Overly specific scenarios

---

## 🔨 Building MCP Servers

### Choosing a Framework

#### FastMCP (Python) - Recommended

```python
from fastmcp import FastMCP

# Initialize
mcp = FastMCP("My Server", version="1.0.0")

# Add tool
@mcp.tool()
def my_tool(param: str) -> dict:
    return {"result": param}

# Run server
if __name__ == "__main__":
    mcp.run()
```

**Pros:**
- ✅ Simple, Pythonic API
- ✅ Automatic validation
- ✅ Built-in HTTP support
- ✅ Great documentation

#### TypeScript SDK (Node.js)

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";

const server = new Server({
  name: "my-server",
  version: "1.0.0"
});

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [/* ... */]
}));
```

**Pros:**
- ✅ Official Anthropic SDK
- ✅ Type safety
- ✅ Comprehensive features

### Server Structure

```python
# my_mcp_server.py

from fastmcp import FastMCP

# 1. Initialize server
mcp = FastMCP(
    name="My MCP Server",
    version="1.0.0",
    instructions="Brief description of what this server does"
)

# 2. Define tools
@mcp.tool(description="Does something useful")
def my_tool(param: str) -> dict:
    """Tool implementation"""
    return {"result": process(param)}

# 3. Define resources
@mcp.resource("myapp://docs/guide")
def documentation() -> str:
    """Resource content"""
    return "Documentation here..."

# 4. Define prompts
@mcp.prompt()
def workflow_prompt() -> str:
    """Prompt template"""
    return "I want to..."

# 5. Run server
if __name__ == "__main__":
    mcp.run()  # Defaults to STDIO
    # Or: mcp.run(transport="http", host="0.0.0.0", port=8000)
```

### Deployment Options

#### 1. Local STDIO (Development)

```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["path/to/my_mcp_server.py"]
    }
  }
}
```

#### 2. FastMCP Cloud (Production)

```bash
# Deploy to FastMCP Cloud
# 1. Push to GitHub
git push origin main

# 2. Connect at fastmcp.cloud
# 3. Auto-deploys on push
```

Configuration:
```json
{
  "mcpServers": {
    "my-server": {
      "transport": "http",
      "url": "https://my-server.fastmcp.cloud"
    }
  }
}
```

#### 3. Self-Hosted HTTP

```python
# Run as HTTP server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
```

---

## 🔌 Transport Protocols

### STDIO (Standard Input/Output)

**Best for:** Local development, single-user scenarios

```
┌────────────┐         ┌────────────┐
│   Client   │ ←stdin→ │   Server   │
│            │ ←stdout→│            │
└────────────┘         └────────────┘
```

**Pros:**
- ✅ Simple setup
- ✅ No network configuration
- ✅ Fast local communication

**Cons:**
- ❌ Single client only
- ❌ Same machine required
- ❌ Process management needed

### HTTP/HTTPS (Streamable HTTP)

**Best for:** Production, multi-client, cloud deployment

```
┌────────────┐         ┌────────────┐
│  Client 1  │ ────┐   │            │
└────────────┘     │   │            │
                   ├──→│   Server   │
┌────────────┐     │   │  (HTTPS)   │
│  Client 2  │ ────┘   │            │
└────────────┘         └────────────┘
```

**Pros:**
- ✅ Multiple clients
- ✅ Remote access
- ✅ Secure (HTTPS)
- ✅ Standard web infrastructure

**Cons:**
- ❌ Requires hosting
- ❌ Network latency
- ❌ More complex setup

### Comparison

| Feature | STDIO | HTTP |
|---------|-------|------|
| **Clients** | Single | Multiple |
| **Location** | Local only | Remote capable |
| **Security** | Process isolation | HTTPS + Auth |
| **Complexity** | Simple | Moderate |
| **Use Case** | Development | Production |

---

## 🌟 Real-World Examples

### Example 1: Data Fetching Tool

```python
@mcp.tool(description="Fetch user data by ID")
def get_user(user_id: int) -> dict:
    """Fetches user information from database."""
    
    # Validation
    if user_id <= 0:
        return {"error": "Invalid user ID"}
    
    # Database query
    try:
        user = database.query(
            "SELECT * FROM users WHERE id = ?", 
            (user_id,)
        )
        
        if not user:
            return {"error": "User not found"}
        
        # Format response
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "created": user.created_at.isoformat()
        }
    except Exception as e:
        return {"error": f"Database error: {str(e)}"}
```

### Example 2: Action Tool

```python
@mcp.tool(description="Send email notification")
def send_email(to: str, subject: str, body: str) -> dict:
    """Sends an email via SMTP."""
    
    # Validation
    if not is_valid_email(to):
        return {"error": "Invalid email address"}
    
    if not subject or not body:
        return {"error": "Subject and body required"}
    
    # Send email
    try:
        smtp.send_message(
            from_addr=config.FROM_EMAIL,
            to_addr=to,
            subject=subject,
            body=body
        )
        
        return {
            "success": True,
            "message": f"Email sent to {to}"
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to send: {str(e)}"
        }
```

### Example 3: Resource with Dynamic Content

```python
@mcp.resource("app://stats/summary")
def stats_summary() -> str:
    """Provides current system statistics."""
    
    stats = get_system_stats()
    
    return f"""
# System Statistics

**Last Updated:** {datetime.now().isoformat()}

## Usage Metrics
- Active Users: {stats.active_users}
- Total Requests: {stats.total_requests:,}
- Average Response Time: {stats.avg_response_time}ms

## System Health
- CPU Usage: {stats.cpu_percent}%
- Memory Usage: {stats.memory_percent}%
- Disk Usage: {stats.disk_percent}%

## Recent Activity
{format_recent_activity(stats.recent_activity)}
"""
```

### Example 4: Multi-Step Prompt

```python
@mcp.prompt(
    name="data-export-workflow",
    description="Guide for exporting data"
)
def data_export_prompt() -> str:
    """Guides user through data export process."""
    return """
I want to export data from the system.

**Step 1: Select Data Source**
Which data would you like to export?
- [ ] User accounts
- [ ] Transaction history
- [ ] Product catalog
- [ ] Analytics data
- [ ] Custom query: _______________

**Step 2: Define Filters**
- Date range: [YYYY-MM-DD] to [YYYY-MM-DD]
- Status: [All / Active / Inactive]
- Additional filters: _______________

**Step 3: Choose Format**
- [ ] CSV
- [ ] JSON
- [ ] Excel (XLSX)
- [ ] PDF Report

**Step 4: Delivery Method**
- [ ] Download link
- [ ] Email to: _______________
- [ ] Upload to cloud storage

Please help me:
1. Validate my selections
2. Estimate export size
3. Generate the export
4. Provide download/delivery
"""
```

---

## 🔗 Integration Patterns

### Pattern 1: Database Access

```python
from fastmcp import FastMCP
import sqlite3

mcp = FastMCP("Database Access")

@mcp.tool()
def query_customers(status: str = "active") -> dict:
    """Query customer database."""
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    
    results = cursor.execute(
        "SELECT * FROM customers WHERE status = ?",
        (status,)
    ).fetchall()
    
    return {
        "count": len(results),
        "customers": [dict(row) for row in results]
    }
```

### Pattern 2: API Wrapper

```python
import requests

@mcp.tool()
def get_weather(city: str) -> dict:
    """Fetch weather data from API."""
    response = requests.get(
        f"https://api.weather.com/v1/current",
        params={"city": city, "key": API_KEY}
    )
    
    if response.status_code != 200:
        return {"error": "Weather API unavailable"}
    
    data = response.json()
    return {
        "city": city,
        "temperature": data["temp"],
        "conditions": data["conditions"],
        "humidity": data["humidity"]
    }
```

### Pattern 3: File System Access

```python
import os
from pathlib import Path

@mcp.tool()
def list_files(directory: str) -> dict:
    """List files in directory."""
    path = Path(directory)
    
    if not path.exists():
        return {"error": "Directory not found"}
    
    if not path.is_dir():
        return {"error": "Not a directory"}
    
    files = []
    for item in path.iterdir():
        files.append({
            "name": item.name,
            "type": "dir" if item.is_dir() else "file",
            "size": item.stat().st_size if item.is_file() else None
        })
    
    return {"directory": str(path), "files": files}
```

### Pattern 4: Web Scraping (Lottery Server)

```python
from bs4 import BeautifulSoup
import requests

@mcp.tool()
def scrape_lottery_result(lottery: str, draw: int) -> dict:
    """Scrape lottery results from website."""
    
    # Build URL
    url = f"https://www.nlb.lk/results/{lottery}"
    
    # Fetch page
    response = requests.get(url, params={"draw": draw})
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Parse results
    result_block = soup.find('div', class_='result-block')
    if not result_block:
        return {"error": "Results not found"}
    
    # Extract data
    numbers = [
        num.text.strip() 
        for num in result_block.find_all('span', class_='number')
    ]
    
    return {
        "draw_number": str(draw),
        "numbers": numbers,
        "date": result_block.find('span', class_='date').text
    }
```

---

## ✨ Best Practices

### Tool Design

1. **Single Responsibility**
   ```python
   # ✅ Good: One clear purpose
   @mcp.tool()
   def get_user_email(user_id: int) -> str:
       return database.get_email(user_id)
   
   # ❌ Bad: Multiple responsibilities
   @mcp.tool()
   def manage_user(action: str, user_id: int, **kwargs):
       if action == "get": ...
       elif action == "update": ...
       elif action == "delete": ...
   ```

2. **Descriptive Names**
   ```python
   # ✅ Good: Clear and specific
   get_customer_by_email()
   send_password_reset_email()
   calculate_order_total()
   
   # ❌ Bad: Vague or generic
   get_data()
   do_stuff()
   process()
   ```

3. **Comprehensive Validation**
   ```python
   @mcp.tool()
   def update_user(user_id: int, email: str) -> dict:
       # Validate all inputs
       if not isinstance(user_id, int) or user_id <= 0:
           return {"error": "Invalid user ID"}
       
       if not email or "@" not in email:
           return {"error": "Invalid email format"}
       
       # Check existence
       if not user_exists(user_id):
           return {"error": "User not found"}
       
       # Perform update
       ...
   ```

4. **Structured Responses**
   ```python
   # ✅ Good: Consistent structure
   {
       "success": True,
       "data": {...},
       "metadata": {
           "timestamp": "2025-11-24T10:00:00Z",
           "version": "1.0"
       }
   }
   
   # ❌ Bad: Inconsistent or unclear
   {"result": "ok", "info": "something"}
   ```

### Resource Design

1. **Keep Updated**
   ```python
   @mcp.resource("app://version")
   def version_info() -> str:
       # Include last updated timestamp
       return f"""
       Version: {APP_VERSION}
       Last Updated: {datetime.now().isoformat()}
       """
   ```

2. **Organize Hierarchically**
   ```
   app://docs/api          # API documentation
   app://docs/guides       # User guides
   app://docs/examples     # Code examples
   app://config/schema     # Configuration schema
   app://config/defaults   # Default values
   ```

3. **Include Examples**
   ```python
   @mcp.resource("app://docs/api")
   def api_docs() -> str:
       return """
       # API Documentation
       
       ## Endpoints
       
       ### GET /users
       Fetches user list
       
       **Example:**
       ```python
       get_users(status="active", limit=10)
       ```
       
       **Response:**
       ```json
       {"users": [...]}
       ```
       """
   ```

### Prompt Design

1. **Progressive Disclosure**
   ```python
   @mcp.prompt()
   def beginner_prompt() -> str:
       return """
       Let's start simple:
       1. First, choose...
       2. Then, specify...
       
       Once comfortable, you can also:
       - Advanced option 1
       - Advanced option 2
       """
   ```

2. **Clear Instructions**
   ```python
   return """
   Fill in the blanks:
   - Required field: [Enter value here]
   - Optional field (leave blank if not needed): _____
   
   Choose one:
   - [ ] Option A
   - [ ] Option B
   """
   ```

### Error Handling

1. **Descriptive Messages**
   ```python
   # ✅ Good: Tells user how to fix
   return {
       "error": "Date must be in YYYY-MM-DD format (e.g., '2025-11-24')"
   }
   
   # ❌ Bad: Vague
   return {"error": "Invalid date"}
   ```

2. **Error Categories**
   ```python
   return {
       "error": {
           "type": "ValidationError",
           "message": "Invalid email format",
           "field": "email",
           "suggestion": "Email must contain @ symbol"
       }
   }
   ```

### Security

1. **Input Sanitization**
   ```python
   import re
   
   def sanitize_input(text: str) -> str:
       # Remove potentially dangerous characters
       return re.sub(r'[^\w\s-]', '', text)
   ```

2. **Rate Limiting**
   ```python
   from functools import lru_cache
   from time import time
   
   @lru_cache(maxsize=1000)
   def rate_limit_key(user_id: str, window: int) -> str:
       return f"{user_id}:{int(time()) // window}"
   ```

3. **Authentication**
   ```python
   @mcp.tool()
   def protected_action(api_key: str, data: str) -> dict:
       if not verify_api_key(api_key):
           return {"error": "Unauthorized"}
       
       # Proceed with action
       ...
   ```

---

## 🎯 Common Use Cases

### 1. Database Integration
Connect LLMs to databases for querying and analysis

### 2. API Wrappers
Provide simplified access to complex APIs

### 3. File Operations
Enable AI to read/write files with permissions

### 4. Web Scraping
Extract data from websites (like this lottery server!)

### 5. System Management
Monitor and control system resources

### 6. Business Logic
Expose domain-specific operations

### 7. Data Transformation
Convert between formats and structures

### 8. External Services
Integrate with third-party platforms

---

## 📚 Further Resources

### Official Documentation

- **MCP Specification**: https://modelcontextprotocol.io
- **FastMCP Framework**: https://gofastmcp.com
- **FastMCP Cloud**: https://gofastmcp.com/deployment/fastmcp-cloud
- **Anthropic MCP Docs**: https://docs.anthropic.com/mcp

### Example Servers

- **Sri Lanka Lottery Server**: This project!
- **FastMCP Examples**: https://github.com/jlowin/fastmcp/tree/main/examples
- **MCP Servers Collection**: https://github.com/modelcontextprotocol/servers

### Community

- **MCP Discord**: Join discussions and get help
- **GitHub Discussions**: Share ideas and patterns
- **FastMCP Community**: Connect with other builders

### Learning Path

1. **Understand MCP Concepts** (this guide!)
2. **Try Existing Servers** (lottery server, file system)
3. **Build Simple Server** (hello world, basic tools)
4. **Add Complexity** (resources, prompts, validation)
5. **Deploy to Production** (FastMCP Cloud, HTTP)
6. **Share & Contribute** (GitHub, community)

---

<div align="center">

**Built with ❤️ using [FastMCP](https://gofastmcp.com)**

**Ready to build your own MCP server?** Start with the [Sri Lanka Lottery Server](README.md) as a reference!

*Last Updated: November 24, 2025*

</div>
