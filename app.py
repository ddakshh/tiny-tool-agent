from agent import run_agent
print("tiny tool started ")
while True :
    query = input("\nyou:")
    if query.lower() == "quit":
        break
    response = run_agent(query)
    with open("logs/logs.txt", "a") as file:
        file.write(f"User: {query}\n")
        file.write(f"Agent: {response}\n\n")

    print(f"\nAgent: {response}")    


