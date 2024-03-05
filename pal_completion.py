from openai import OpenAI 

def pal_prompt(question: str):
    client = OpenAI(api_key='')
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "system",
          "content": "You are a helpful assistant that generates Python code to answer arithmetic questions. "
        },
        {
          "role": "user",
          "content": "Let's use python to solve math problems. You need to write python code to answer these math questions. Here is one example how to do it,\n\nAnswer the following question in Python: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?\n\ndef solution():\n    \"\"\"Olivia has $23. She bought five bagels for $3 each. How much money does she have left?\"\"\"\n    money_initial = 23\n    bagels = 5\n    bagel_cost = 3\n    money_spent = bagels * bagel_cost\n    money_left = money_initial - money_spent\n    result = money_left\n    return result\n\nNow it's your turn.\nAnswer the following question in Python: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?\n"
        },
        {
          "role": "assistant",
          "content": "def solution():\n    \"\"\"Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?\"\"\"\n    golf_balls_initial = 58\n    golf_balls_lost_tuesday = 23\n    golf_balls_lost_wednesday = 2\n    golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday\n    result = golf_balls_left\n    return result"
        },
        {
          "role": "user",
          "content": "Answer the following question in Python: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?"
        },
        {
          "role": "assistant",
          "content": "def solution():\n    \"\"\"There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?\"\"\"\n    computers_initial = 9\n    computers_per_day = 5\n    num_days = 4  # 4 days between monday and thursday\n    computers_added = computers_per_day * num_days\n    computers_total = computers_initial + computers_added\n    result = computers_total\n    return result"
        },
        {
          "role": "user",
          "content": "Answer the following question in Python: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?"
        },
        {
          "role": "assistant",
          "content": "def solution():\n    \"\"\"Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?\"\"\"\n    toys_initial = 5\n    mom_toys = 2\n    dad_toys = 2\n    total_received = mom_toys + dad_toys\n    total_toys = toys_initial + total_received\n    result = total_toys\n    return result"
        },
        {
          "role": "user",
          "content": "Answer the following question in Python: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?"
        },
        {
          "role": "assistant",
          "content": "def solution():\n    \"\"\"Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?\"\"\"\n    jason_lollipops_initial = 20\n    jason_lollipops_after = 12\n    denny_lollipops = jason_lollipops_initial - jason_lollipops_after\n    result = denny_lollipops\n    return result"
        },
        {
          "role": "user",
          "content": "Answer the following question in Python: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?"
        },
        {
          "role": "assistant",
          "content": "def solution():\n    \"\"\"Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?\"\"\"\n    leah_chocolates = 32\n    sister_chocolates = 42\n    total_chocolates = leah_chocolates + sister_chocolates\n    chocolates_eaten = 35\n    chocolates_left = total_chocolates - chocolates_eaten\n    result = chocolates_left\n    return result"
        },
        {
          "role": "user",
          "content": "Answer the following question in Python: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?"
        },
        {
          "role": "assistant",
          "content": "def solution():\n    \"\"\"If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?\"\"\"\n    cars_initial = 3\n    cars_arrived = 2\n    total_cars = cars_initial + cars_arrived\n    result = total_cars\n    return result"
        },
        {
          "role": "user",
          "content": "Answer the following question in Python: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?"
        },
        {
          "role": "assistant",
          "content": "def solution():\n    \"\"\"There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?\"\"\"\n    trees_initial = 15\n    trees_after = 21\n    trees_added = trees_after - trees_initial\n    result = trees_added\n    return result"
        },
        {
          "role": "user",
          "content": "Answer the following question in Python: Mishka bought 3 pairs of shorts, 3 pairs of pants, and 3 pairs of shoes. One pair of shorts costs $16.50. One pair of pants costs $22.50 and one pair of shoes costs $42. How many dollars did Mishka spend on all the clothing items?"
        },
        {
          "role": "assistant",
          "content": "def solution():\n    \"\"\"Mishka bought 3 pairs of shorts, 3 pairs of pants, and 3 pairs of shoes. One pair of shorts costs $16.50. One pair of pants costs $22.50 and one pair of shoes costs $42. How many dollars did Mishka spend on all the clothing items?\"\"\"\n    shorts_price = 16.50\n    pants_price = 22.50\n    shoes_price = 42.00\n    num_pairs_shorts = 3\n    num_pairs_pants = 3\n    num_pairs_shoes = 3\n    total_cost = (shorts_price * num_pairs_shorts) + (pants_price * num_pairs_pants) + (shoes_price * num_pairs_shoes)\n    result = total_cost\n    return result"
        },
        {
          "role": "user",
          "content": f'Answer the following question in Python: {question}'
        }  
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

def pal_answer(question: str):
    pal = pal_prompt(question)
    answer = extract_content(pal)
    return answer

    