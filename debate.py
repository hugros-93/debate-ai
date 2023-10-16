import json
import datetime
import openai

openai.api_key_path = "API_KEY.txt"


class Debate:
    def __init__(self, subject, total_rounds):
        self.subject = subject
        self.total_rounds = total_rounds
        self.round = 1
        self.messages = []
        self.datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    def export_debate(self):
        debate_export = {
            "subject": self.subject,
            "total_rounds": self.total_rounds,
            self.agent_a.name: {"position": self.agent_a.position},
            self.agent_b.name: {"position": self.agent_b.position},
            "messages": self.messages,
        }
        with open(f"output/{self.datetime}.json", "w") as f:
            json.dump(debate_export, f)


class DebateAgent:
    def __init__(self, name, subject, position):
        self.name = name
        self.subject = subject
        self.position = position

        # Init prompt
        with open("debate_context.txt", "r") as f:
            debate_context = f.read()
        debate_context = debate_context + "\n" + subject
        debate_context = debate_context + "\n" + position

        # ChatGPT context messages
        self.messages = [{"role": "system", "content": debate_context}]

    def argue(self):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages
        )
        self.last_answer = response["choices"][0]["message"]["content"]
        self.messages.append({"role": "assistant", "content": self.last_answer})

    def listen(self, argument):
        self.messages.append({"role": "user", "content": argument})


if __name__ == "__main__":
    # Input
    print("### DEBATE AI ### ")
    subject = input("> Debate subject: ")
    total_rounds = input("> Number of rounds: ")
    total_rounds = int(total_rounds)
    debate = Debate(subject, total_rounds)
    print("\t> Debate created!\n")

    # Debate agent creation
    agent_a_name = input(f"> Agent 1 name: ")
    agent_a_position = input(f"> {agent_a_name} position: ")
    debate.agent_a = DebateAgent(agent_a_name, subject, agent_a_position)
    print(f"\t> {debate.agent_a.name} created!\n")

    agent_b_name = input(f"> Agent 2 name: ")
    agent_b_position = input(f"> {agent_b_name} position: ")
    debate.agent_b = DebateAgent(agent_b_name, subject, agent_b_position)
    print(f"\t> {debate.agent_b.name} created!\n")

    # Debate
    debate.round = 1
    while debate.round <= total_rounds:
        print(f"\n# ROUND {debate.round} #\n")

        debate.agent_a.argue()
        print(f"> {agent_a_name}: {debate.agent_a.last_answer}\n")
        debate.messages.append({debate.agent_a.name: debate.agent_a.last_answer})
        debate.export_debate()
        debate.agent_b.listen(debate.agent_a.last_answer)

        debate.agent_b.argue()
        print(f"> {agent_b_name}: {debate.agent_b.last_answer}\n")
        debate.messages.append({debate.agent_b.name: debate.agent_b.last_answer})
        debate.export_debate()
        debate.agent_a.listen(debate.agent_b.last_answer)

        debate.round += 1
