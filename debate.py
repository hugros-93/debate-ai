import json
import datetime
import openai

openai.api_key_path = "API_KEY.txt"


class Debate:
    def __init__(self, subject, total_rounds, nb_words):
        self.subject = subject
        self.total_rounds = total_rounds
        self.nb_words = nb_words
        self.round = 1
        self.messages = []
        self.datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.agents = []

        with open("debate_context.txt", "r") as f:
            debate_context = f.read()
        self.debate_context = debate_context.replace("[NB_WORDS]", nb_words)
        self.debate_context += "\nThe subject of the debate is: " + subject

    def export_debate_data(self):
        debate_data = {
            "subject": self.subject,
            "total_rounds": self.total_rounds,
            "nb_words": self.nb_words,
            "context": self.debate_context,
            "messages": self.messages,
        }

        for agent in self.agents:
            debate_data[agent.name] = {"opinion": agent.opinion, "tone": agent.tone}

        with open(f"output/{self.datetime}.json", "w") as f:
            json.dump(debate_data, f)

    def export_debate_summary(self):
        debate_summary = f"### Debate Summary - {self.datetime} ###\n\n"
        debate_summary += f"> Context: \n{self.debate_context}\n\n"
        debate_summary += f"> Rounds: {self.total_rounds}\n"
        debate_summary += f"> Agents:\n"
        for agent in self.agents:
            debate_summary += f"\t> name: {agent.name}\n\t\t- opinion: {agent.opinion}\n\t\t- tone: {agent.tone}\n"
        debate_summary += "\n### Start ###\n\n"
        for message in self.messages:
            for agent_name in message:
                debate_summary += f"> {agent_name}: {message[agent_name]}\n"
        debate_summary += "\n### End ###"

        with open(f"output/{self.datetime}.txt", "w", encoding="UTF-8") as f:
            f.write(debate_summary)


class DebateAgent:
    def __init__(self, name, subject, opinion, tone, debate_context):
        self.name = name
        self.subject = subject
        self.opinion = opinion
        self.tone = tone
        debate_context += "\nYour opinion in this debate is: " + opinion
        debate_context += "\nYour tone will be: " + tone
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
    nb_words = input("> Number of words per answer: ")
    total_rounds = input("> Number of rounds: ")
    total_rounds = int(total_rounds)
    debate = Debate(subject, total_rounds, nb_words)
    print("\t> Debate created!\n")

    # Debate agent creation
    for i in [0, 1]:
        agent_name = input(f"> Agent {i+1} name: ")
        agent_opinion = input(f"> {agent_name} opinion: ")
        agent_tone = input(f"> {agent_name} tone: ")
        debate.agents.append(
            DebateAgent(
                agent_name, subject, agent_opinion, agent_tone, debate.debate_context
            )
        )
        print(f"\t> {agent_name} created!\n")

    # Debate
    debate.round = 1
    while debate.round <= total_rounds:
        print(f"\n# ROUND {debate.round} #\n")

        for i in [0, 1]:
            debate.agents[i].argue()
            print(f"> {debate.agents[i].name}: {debate.agents[i].last_answer}\n")
            debate.messages.append(
                {debate.agents[i].name: debate.agents[i].last_answer}
            )
            debate.export_debate_data()
            debate.export_debate_summary()
            debate.agents[1 - i].listen(debate.agents[i].last_answer)

        debate.round += 1
