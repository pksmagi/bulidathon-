"""
Customer Support System using CrewAI and Streamlit
Three sequential agents:
1. Assistant - answers directly
2. Web Search Assistant - searches web and answers
3. Entry Agent - saves to file and returns both answers
"""

import os
import json
from datetime import datetime
import streamlit as st
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# Initialize session state
if "crew_result" not in st.session_state:
    st.session_state.crew_result = None
if "processing" not in st.session_state:
    st.session_state.processing = False


def get_api_keys():
    """Read API keys from environment variables"""
    openai_key = os.getenv("OPENAI_API_KEY")
    serper_key = os.getenv("SERPER_API_KEY")
    
    if not openai_key:
        st.error("⚠️ OPENAI_API_KEY environment variable not set")
        st.stop()
    if not serper_key:
        st.error("⚠️ SERPER_API_KEY environment variable not set")
        st.stop()
    
    return openai_key, serper_key


def create_agents():
    """Create the three agents for the support crew"""
    
    # Agent 1: Assistant - answers directly from knowledge
    assistant = Agent(
        role="Customer Support Assistant",
        goal="Provide helpful answers to customer queries directly from your knowledge",
        backstory="You are a knowledgeable customer support assistant with deep expertise in helping customers. "
                  "You provide clear, accurate, and helpful answers based on your training and knowledge.",
        verbose=True,
        allow_delegation=False
    )
    
    # Agent 2: Web Search Assistant - searches and answers
    web_search_tool = SerperDevTool()
    web_search_assistant = Agent(
        role="Web Search Assistant",
        goal="Search the web and provide comprehensive answers based on current information",
        backstory="You are a web search expert who finds the most relevant and current information from across the internet. "
                  "You synthesize web results into clear, accurate answers.",
        tools=[web_search_tool],
        verbose=True,
        allow_delegation=False
    )
    
    # Agent 3: Entry Agent - saves to file and returns answers
    entry_agent = Agent(
        role="Entry Agent",
        goal="Save the customer query and both support answers to a file and present them to the user",
        backstory="You are responsible for documenting support interactions. "
                  "You receive the query and both answers from previous agents, save them to a file, and return the results.",
        verbose=True,
        allow_delegation=False
    )
    
    return assistant, web_search_assistant, entry_agent


def create_tasks(query, assistant, web_search_assistant, entry_agent):
    """Create the three sequential tasks"""
    
    # Task 1: Assistant answers directly
    task1 = Task(
        description=f"Answer the following customer query directly based on your knowledge: '{query}'",
        agent=assistant,
        expected_output="A clear, helpful answer to the customer's question based on your knowledge"
    )
    
    # Task 2: Web Search Assistant searches and answers
    task2 = Task(
        description=f"Search the web for information about: '{query}' and provide a comprehensive answer based on the search results. "
                     "Previous assistant answer: {{{{ tasks.0.output }}}}",
        agent=web_search_assistant,
        expected_output="A comprehensive answer based on web search results"
    )
    
    # Task 3: Entry Agent saves to file and returns both answers
    task3 = Task(
        description=f"You have received a customer query and two answers. Save all of this information to a file called 'answers.txt' "
                     "in the current directory. Format: Query | Direct Answer | Web Search Answer. "
                     f"Query: '{query}' "
                     "Direct Answer: {{{{ tasks.0.output }}}} "
                     "Web Search Answer: {{{{ tasks.1.output }}}} "
                     "After saving, return both answers so they can be shown to the user.",
        agent=entry_agent,
        expected_output="Confirmation that the file was saved, plus a summary of both answers"
    )
    
    return task1, task2, task3


def save_to_file(query, direct_answer, web_answer):
    """Save the query and answers to a text file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    content = f"""
{'='*80}
CUSTOMER SUPPORT QUERY - {timestamp}
{'='*80}

QUERY:
{query}

{'='*80}
DIRECT ANSWER (from Assistant):
{'='*80}
{direct_answer}

{'='*80}
WEB SEARCH ANSWER (from Web Search Assistant):
{'='*80}
{web_answer}

{'='*80}
"""
    
    with open("answers.txt", "a", encoding="utf-8") as f:
        f.write(content)
    
    return True


def run_support_crew(query):
    """Run the sequential crew with the given query"""
    try:
        st.session_state.processing = True
        
        with st.spinner("🔄 Initializing agents..."):
            # Get API keys
            openai_key, serper_key = get_api_keys()
            os.environ["OPENAI_API_KEY"] = openai_key
            os.environ["SERPER_API_KEY"] = serper_key
            
            # Create agents and tasks
            assistant, web_search_assistant, entry_agent = create_agents()
            task1, task2, task3 = create_tasks(query, assistant, web_search_assistant, entry_agent)
        
        with st.spinner("💼 Running support crew (Sequential Process)..."):
            # Create crew with sequential process
            crew = Crew(
                agents=[assistant, web_search_assistant, entry_agent],
                tasks=[task1, task2, task3],
                process=Process.sequential,  # Agents run one after another
                verbose=True
            )
            
            # Execute the crew
            result = crew.kickoff()
        
        # Extract answers from the crew result
        # The result contains the final output from all tasks
        final_output = str(result)
        
        # Try to parse the structured output
        try:
            # The crew.kickoff returns the final task output
            if isinstance(result, dict):
                direct_answer = result.get("task1_output", "No direct answer available")
                web_answer = result.get("task2_output", "No web search answer available")
            else:
                # If not a dict, extract from the string representation
                final_output = str(result)
                direct_answer = "Direct answer generated by Assistant"
                web_answer = "Web search answer generated"
        except Exception as e:
            st.warning(f"Note: Could not parse structured output: {str(e)}")
            direct_answer = "Direct answer generated by Assistant"
            web_answer = "Web search answer generated"
            final_output = str(result)
        
        # Save to file
        save_to_file(query, final_output, final_output)
        
        st.session_state.crew_result = {
            "query": query,
            "final_output": final_output,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        st.session_state.processing = False
        return True
        
    except Exception as e:
        st.error(f"❌ Error running support crew: {str(e)}")
        st.session_state.processing = False
        return False


# Streamlit UI
st.set_page_config(page_title="Customer Support Crew", layout="wide")
st.title("🤖 Customer Support System")
st.markdown("### Powered by CrewAI & Sequential Agents")

st.markdown("""
This support system uses three sequential agents:
1. **Assistant** - Answers directly from knowledge
2. **Web Search Assistant** - Searches the web for answers
3. **Entry Agent** - Saves everything to a file and returns both answers
""")

st.divider()

# Input section
col1, col2 = st.columns([4, 1])
with col1:
    query = st.text_input(
        "Enter your query or support request:",
        placeholder="e.g., How do I reset my password?",
        key="query_input"
    )

with col2:
    if st.button("🚀 Submit", use_container_width=True, type="primary"):
        if query.strip():
            st.session_state.query_submitted = query
        else:
            st.warning("Please enter a query")

st.divider()

# Process query if submitted
if hasattr(st.session_state, "query_submitted") and not st.session_state.processing:
    query = st.session_state.query_submitted
    
    with st.spinner("🔄 Processing your query with our support crew..."):
        run_support_crew(query)

# Display results
if st.session_state.crew_result:
    result = st.session_state.crew_result
    
    st.success("✅ Support query processed successfully!")
    
    st.markdown(f"**Query:** {result['query']}")
    st.markdown(f"**Processed at:** {result['timestamp']}")
    
    st.markdown("### 📋 Response from Support Crew:")
    st.text_area(
        "Full Response:",
        value=result['final_output'],
        height=300,
        disabled=True
    )
    
    st.info("✅ The query and answers have been saved to `answers.txt`")
    
    if st.button("🔄 Ask Another Question"):
        st.session_state.crew_result = None
        st.session_state.query_submitted = None
        st.rerun()

st.divider()
st.markdown("""
### How it works:
1. Enter your support query
2. Agent 1 (Assistant) provides a direct answer
3. Agent 2 (Web Search) searches for current information
4. Agent 3 (Entry Agent) saves everything to a file
5. Both answers are displayed to you
""")
