import datetime

def log_agent(agent_name):

    timestamp = datetime.datetime.now()

    print(
        f"[{timestamp}] "
        f"{agent_name} executed"
    )