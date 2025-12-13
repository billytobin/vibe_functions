from openai import OpenAI
import ast
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

# --------------------
# Helper
# --------------------

def _ask_llm(prompt, temperature=0):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.choices[0].message.content.strip()

# --------------------
# Numeric Operations
# --------------------

def vibe_add(a, b):
    return ast.literal_eval(_ask_llm(f"What is {a} + {b}? Respond ONLY with the number."))

def vibe_sub(a, b):
    return ast.literal_eval(_ask_llm(f"What is {a} - {b}? Respond ONLY with the number."))

def vibe_mul(a, b):
    return ast.literal_eval(_ask_llm(f"What is {a} * {b}? Respond ONLY with the number."))

def vibe_div(a, b):
    return ast.literal_eval(_ask_llm(f"What is {a} / {b}? Respond ONLY with the number."))

def vibefloor(x):
    return ast.literal_eval(_ask_llm(f"Return the floor of {x}. Respond ONLY with the number."))

def vibeceil(x):
    return ast.literal_eval(_ask_llm(f"Return the ceiling of {x}. Respond ONLY with the number."))

# --------------------
# Comparisons
# --------------------

def vibeequal(a, b):
    return _ask_llm(f"Are {a} and {b} equal? Answer true or false ONLY.") == "true"

def vibegreater(a, b):
    return _ask_llm(f"Is {a} greater than {b}? Answer true or false ONLY.") == "true"

def vibelower(a, b):
    return _ask_llm(f"Is {a} less than {b}? Answer true or false ONLY.") == "true"

# --------------------
# List Operations
# --------------------

def vibesort(items):
    return ast.literal_eval(_ask_llm(f"Sort this list in ascending order and return ONLY a Python list: {items}"))

def vibemin(items):
    return ast.literal_eval(_ask_llm(f"Return the minimum value from this list. Respond ONLY with the value: {items}"))

def vibemax(items):
    return ast.literal_eval(_ask_llm(f"Return the maximum value from this list. Respond ONLY with the value: {items}"))

def vibesum(items):
    return ast.literal_eval(_ask_llm(f"Return the sum of this list. Respond ONLY with the number: {items}"))

def vibelen(items):
    return ast.literal_eval(_ask_llm(f"Return the length of this list. Respond ONLY with the number: {items}"))

def vibecontains(items, value):
    return _ask_llm(f"Does this list contain {value}? Answer true or false ONLY. List: {items}") == "true"

# --------------------
# String Operations
# --------------------

def vibelowercase(s):
    return _ask_llm(f"Convert the following string to lowercase. Respond ONLY with the string: {s}")

def vibeuppercase(s):
    return _ask_llm(f"Convert the following string to uppercase. Respond ONLY with the string: {s}")

def vibereverse(s):
    return _ask_llm(f"Reverse the following string. Respond ONLY with the reversed string: {s}")

# --------------------
# Logic
# --------------------

def vibeand(a, b):
    return _ask_llm(f"What is {a} AND {b}? Answer true or false ONLY.") == "true"

def vibeor(a, b):
    return _ask_llm(f"What is {a} OR {b}? Answer true or false ONLY.") == "true"

def vibenot(a):
    return _ask_llm(f"What is NOT {a}? Answer true or false ONLY.") == "true"

# --------------------
# Extensions
# --------------------

def vibeindex(items, value):
    return ast.literal_eval(_ask_llm(
        f"Return the index of {value} in this list. Respond ONLY with the index: {items}"
    ))

def vibeabs(x):
    return ast.literal_eval(_ask_llm(
        f"Return the absolute value of {x}. Respond ONLY with the number."
    ))

def vibemod(a, b):
    return ast.literal_eval(_ask_llm(
        f"What is {a} modulo {b}? Respond ONLY with the number."
    ))

def viberound(x, n):
    return ast.literal_eval(_ask_llm(
        f"Round {x} to {n} decimal places. Respond ONLY with the number."
    ))
