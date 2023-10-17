# `debate-ai`: simulate a debate with ChatGPT

## Overview


## Installation 💾
- Clone the repository
- Create a `venv` using the `requirements.txt`.
- Create a ChatGPT account and an API key, and add a text file `API_KEY.txt` in the root folder with your ChatGPT API key.
- Run the dashboard in command line: `> python debate.py`. 

## Input data
The script will require some input data, to enter directly in command line.

For the debate:
- `Debate subject`: The subject of the debate.
- `Number of words per answer`: The max number of words the agents can use in each answer.
- `Number of rounds`: The number of answers for each agent. 

For each agent:
- `Name`: Name the agent will be referred to.
- `Opinion`: The opinion the agent should defend.
- `Tone`: The tone the agent should use during the debate.

## Results
A `json` and a `txt` files will be created, with the debate parameters and the resulting discussion. Result files will be exported in the `output/` folder, named with datetime of when the discusion was created.

## Examples 🗣️
Bellow some examples

### Example 1
- __Subject of the debate:__ `Meteo`
- __Number of rouds:__ `5`
- __Agents:__
    - name: `A`, opinion: `good`, tone: `polite`
    - name: `B`, opinion: `bad`, tone: `agressive`

- __Results:__
> > A: I respect your opinion, but I believe Meteo is good.
>
> > B: No, Meteo is bad for numerous reasons. It's destructive and unpredictable.
>
> > A: I understand your concerns, but I respectfully disagree. Meteo has benefits such as providing necessary rainfall for agriculture and generating renewable energy.
>
> > B: Nonsense! Meteo causes havoc with natural disasters and ruins lives.
>
> > A: I understand your concerns about natural disasters, but it's crucial to recognize that Meteo also contributes to important natural cycles and weather patterns. With proper preparation and disaster management, we can mitigate the negative impacts and focus on harnessing its positive aspects.
>
> > B: Mitigate? Disaster management? Your naive optimism won't change the fact that Meteo brings nothing but chaos and destruction.
>
> > A: I understand your perspective, but it's important to approach Meteo with a balanced understanding. While it can have adverse effects, it also plays a significant role in maintaining ecological balance and driving essential weather patterns. With advanced technology and effective strategies, we can better manage and adapt to the challenges it presents.
>
> > B: Balanced understanding? Adaptation? Your delusion blinds you to the undeniable truth: Meteo is inherently detrimental and cannot be tamed or justified.
>
> > A: I appreciate your perspective, but I respectfully disagree. Meteo, like any natural phenomenon, has both positive and negative aspects. Through research, innovation, and responsible management, we can work towards minimizing its negative impacts and leveraging its benefits for the betterment of society and the environment.
>
> > B: Research, innovation, responsible management? Your optimism is misplaced. Meteo remains a force of destruction, and any perceived benefits are overshadowed by the devastation it causes.

### Example 2
- __Subject of the debate:__ `Est-ce que scribe est une bonne situation?`
- __Number of rouds:__ `5`
- __Agents:__
    - name: `Scribe`, opinion: `Scribe est une bonne situation.`, tone: `rêveur`
    - name: `Druide`, opinion: `Scribe n'est pas une bonne situation`, tone: `agressif`

- __Results:__
>> Scribe: Scribe est une bonne situation car il offre la chance de travailler avec des mots magnifiques.
>
>> Druide: Faux! Scribe est une perte de temps qui limite les opportunités.
>
>> Scribe: Scribe amplifie les compétences en écriture et encourage la créativité.
>
>> Druide: Arrête de te mentir à toi-même! Scribe est une carrière sans avenir.
>
>> Scribe: Scribe est une opportunité d'immortaliser des histoires et d'inspirer les générations futures.
>
>> Druide: Ce sont des illusions de grandeur! Scribe est un métier obsolète et insignifiant.
>
>> Scribe: Scribe préserve la mémoire collective et transmet le savoir ancestral.
>
>> Druide: C'est du passé! Scribe ne contribue en rien à notre société moderne.
>
>> Scribe: Scribe favorise la diffusion de connaissances cruciales pour une société éclairée.
>
>> Druide: Illusion de pertinence! Scribe ne sert à rien dans notre monde technologique.
>