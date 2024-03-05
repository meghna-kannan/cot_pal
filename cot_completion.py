from openai import OpenAI 

def cot_prompt(question: str):
    client = OpenAI(api_key='')
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "system",
          "content": "You are a helpful assistant that can solve math problems step by step. Always include the text `So the Answer is ` before the final answer "
        },
        {
          "role": "user",
          "content": "Question: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?"
        },
        {
          "role": "assistant",
          "content": "Answer:\nMichael started with 58 golf balls.\nAnd he lost 23 golf balls on tuesday.\nSo after losing 23 on tuesday, he had 58 -23 = 35.\nAnd then he lost 2 more golf balls on wednesday.\nSo after losing 2 more on wednesday, he had 35 - 2 = 33 golf balls.\nSo the answer is 33."
        },
        {
          "role": "user",
          "content": "Question: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?"
        },
        {
          "role": "assistant",
          "content": "Answer:\nThere were originally 9 computers.\nAnd 5 more computers were added from monday to thursday.\nThere are 4 days between monday and thursday.\nSo 5 * 4 = 20 computers were added in total.\nSo there are 9 + 20 = 29 computers now.\nSo the answer is 29."
        },
        {
          "role": "user",
          "content": "Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?"
        },
        {
          "role": "assistant",
          "content": "Answer:\nShawn started with 5 toys.\nAnd he got 2 toys each from his mom and dad.\nSo he got 2 + 2 = 4 toys.\nTherefore, he has 5 + 4 = 9 toys now.\nSo the answer is 9."
        },
        {
          "role": "user",
          "content": "Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?"
        },
        {
          "role": "assistant",
          "content": "Answer:\nJason started with 20 lollipops.\nThen he had 12 after giving some to Denny.\nSo he gave Denny 20 - 12 = 8 lollipops.\nSo the answer is 8."
        },
        {
          "role": "user",
          "content": "Question: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?"
        },
        {
          "role": "assistant",
          "content": "Answer:\nThere are 15 trees originally.\nAnd there were 21 trees after some more were planted.\nSo 21 - 15 = 6 trees were planted.\nSo the answer is 6."
        },
        {
          "role": "user",
          "content": "Question: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?"
        },
        {
          "role": "assistant",
          "content": "Answer:\nThere are originally 3 cars.\nAnd 2 more cars arrive.\nSo there are 3 + 2 = 5 cars now.\nSo the answer is 5."
        },
        {
          "role": "user",
          "content": "Question: Leah had 32 chocolates and her sister had 10 more chocolates than her. If they ate 35, how many pieces do they have left in total?"
        },
        {
          "role": "assistant",
          "content": "Answer:\nOriginally, Leah had 32 chocolates.\nAnd her sister had 10 more chocolates than her.\nSo her sister had 42 chocolates.\nSo in total they had 32 + 42 = 74 chocolates.\nThen they ate 35 chocolates.\nTherefore they had 74 - 35 = 39 chocolates left.\nSo the answer is 39."
        },
        {
          "role": "user",
          "content": "Question: A robe takes 2 bolts of blue fiber and half that much white fiber.  How many bolts in total does it take?"
        },
        {
          "role": "assistant",
          "content": "Answer:\nA robe takes 2 bolts of blue fiber and half that much white fiber.\nSo the robe takes 2 bolts of blue fiber and 1 bolt of white fiber (half of 2 bolts).\nTherefore, in total, the robe takes 2 + 1 = 3 bolts of fiber.\nSo the answer is 3."
        },
        {
          "role": "user",
          "content": "Question: Cynthia eats one serving of ice cream every night.  She buys cartons of ice cream with 15 servings of ice cream per carton at a cost of $4.00 per carton.  After 60 days, how much will she spend on ice cream?"
        },
        {
          "role": "assistant",
          "content": "Answer:\nCynthia eats one serving of ice cream every night.\nAnd there are 15 servings of ice cream per carton.\nSo in 60 days, she will eat 1 serving * 60 days = 60 servings of ice cream.\nEach carton of ice cream has 15 servings, so she will need 60 servings / 15 servings = 4 cartons of ice cream.\nEach carton costs $4.00, so she will spend 4 cartons * $4.00/carton = $16.00 on ice cream.\nSo the answer is $16.00."
        },
        {
          "role": "user",
          "content": f'question: {question}'
        },  
          
      ],
      temperature=0,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return response

def extract_content(response):
    content = None
    if hasattr(response, 'choices') and len(response.choices) > 0:
        first_choice = response.choices[0]
        if hasattr(first_choice, 'message') and hasattr(first_choice.message, 'content'):
            content = first_choice.message.content
    return content

def cot_answer(question: str):
    try:
        cot = cot_prompt(question)
        answer = extract_content(cot)
        return answer
    except Exception as e:
        print("Exception:", e)
        return "cot error"


    