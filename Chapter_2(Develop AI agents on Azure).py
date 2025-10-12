###########
''' Get started with AI agent development on Azure'''
###########

###########
''' Develop an AI agent with Azure AI Foundry Agent Service'''

"""
Components of AI Agent:
- Model
- Knowledge
- Tool

"""
###########

###########
''' Integrate custom tools into your agent'''

"""
Custom tools available in Azure AI FOundry Agent Service

1. Custom Function
2. Azure Functions
3. OpenAPI specification tools
4. Azure Logic Apps

Now how to integrate these custom tools?
1. Function calling (As the name sugests)

Example: Defining and using a function
Start by defining a function that the agent can call. For instance, here's a fake snowfall tracking function:

import json

def recent_snowfall(location: str) -> str:
    #Fetches recent snowfall totals for a given location.
    #:param location: The city name.
    #:return: Snowfall details as a JSON string.

    mock_snow_data = {"Seattle": "0 inches", "Denver": "2 inches"}
    snow = mock_snow_data.get(location, "Data not available.")
    return json.dumps({"location": location, "snowfall": snow})

user_functions: Set[Callable[..., Any]] = {
    recent_snowfall,
}

# Toolset is the key
Register the function with your agent using the Azure AI SDK:

# Initialize agent toolset with user functions
functions = FunctionTool(user_functions)
toolset = ToolSet()
toolset.add(functions)
agent_client.enable_auto_function_calls(toolset=toolset)


# Create your agent with the toolset
agent = agent_client.create_agent(
    model="gpt-4o-mini",
    name="snowfall-agent",
    instructions="You are a weather assistant tracking snowfall. Use the provided functions to answer questions.",
    toolset=toolset
)


2. Azure Functions

Example: Using Azure Functions with a queue trigger
First, develop and deploy your Azure Function. In this example, imagine we have a function 
in our Azure subscription to fetch the snowfall for a given location.

When your Azure Function is in place, integrate add it to the agent definition as an 
Azure Function tool:


storage_service_endpoint = "https://<your-storage>.queue.core.windows.net"

azure_function_tool = AzureFunctionTool(
    name="get_snowfall",
    description="Get snowfall information using Azure Function",
    parameters={
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "The location to check snowfall."},
            },
            "required": ["location"],
        },
    input_queue=AzureFunctionStorageQueue(
        queue_name="input",
        storage_service_endpoint=storage_service_endpoint,
    ),
    output_queue=AzureFunctionStorageQueue(
        queue_name="output",
        storage_service_endpoint=storage_service_endpoint,
    ),
)

agent = agent_client.create_agent(
    model=os.environ["MODEL_DEPLOYMENT_NAME"],
    name="azure-function-agent",
    instructions="You are a snowfall tracking agent. Use the provided Azure Function to fetch snowfall based on location.",
    tools=azure_function_tool.definitions,
)

3. OpenAPI specification

Example: Using an OpenAPI specification
First, create a JSON file ( in this example, called snowfall_openapi.json) describing the API.

JSON

Copy
{
  "openapi": "3.0.0",
  "info": {
    "title": "Snowfall API",
    "version": "1.0.0"
  },
  "paths": {
    "/snow": {
      "get": {
        "summary": "Get snowfall information",
        "parameters": [
          {
            "name": "location",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "location": {"type": "string"},
                    "snow": {"type": "string"}
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
Then, register the OpenAPI tool in the agent defintion:


from azure.ai.agents.models import OpenApiTool, OpenApiAnonymousAuthDetails

with open("snowfall_openapi.json", "r") as f:
    openapi_spec = json.load(f)

auth = OpenApiAnonymousAuthDetails()
openapi_tool = OpenApiTool(name="snowfall_api", spec=openapi_spec, auth=auth)

agent = agent_client.create_agent(
    model="gpt-4o-mini",
    name="openapi-agent",
    instructions="You are a snowfall tracking assistant. Use the API to fetch snowfall data.",
    tools=[openapi_tool]
)

"""
###########


###########
'''Develop a multi-agent solution with Azure AI Foundry Agent Service'''
###########


###########
'''Integrate MCP Tools with Azure AI Agents'''
###########


###########
'''Develop an AI agent with Semantic Kernel'''
###########


###########
'''Orchestrate a multi-agent solution using Semantic Kernel'''
###########


###########
'''Discover Azure AI Agents with A2A'''
###########