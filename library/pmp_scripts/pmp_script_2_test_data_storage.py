# Import the functions you want to test (from the main data_storage script)
from data_storage import save_data, load_data

# Simulating agent data to test the logging system without running agents

# Test: Simulate and save some data for each agent
test_data_agent_1 = {"name": "John", "proficiency": "Beginner", "last_session": "2024-10-18"}
test_data_agent_2 = {"name": "Jane", "memory": "Good", "last_session": "2024-10-18"}
test_data_agent_3 = {"name": "Doe", "interaction": "Intermediate", "last_session": "2024-10-18"}
test_data_agent_4 = {"name": "Smith", "error_logging": "Active", "last_session": "2024-10-18"}

# Test saving data for each agent (locally, no backup for now)
save_data("Agent_1_Proficiency", test_data_agent_1)
save_data("Agent_2_Memory", test_data_agent_2)
save_data("Agent_3_Interaction", test_data_agent_3)
save_data("Agent_4_Error_Logging", test_data_agent_4)

# Optionally test backup for each agent (backup=True)
save_data("Agent_1_Proficiency", test_data_agent_1, backup=True)
save_data("Agent_2_Memory", test_data_agent_2, backup=True)
save_data("Agent_3_Interaction", test_data_agent_3, backup=True)
save_data("Agent_4_Error_Logging", test_data_agent_4, backup=True)

# Test loading the most recent saved data for Agent 1 (for example)
loaded_data_agent_1 = load_data("Agent_1_Proficiency")
print(f"Loaded data for Agent 1: {loaded_data_agent_1}")

# Test loading the most recent saved data for Agent 2
loaded_data_agent_2 = load_data("Agent_2_Memory")
print(f"Loaded data for Agent 2: {loaded_data_agent_2}")
