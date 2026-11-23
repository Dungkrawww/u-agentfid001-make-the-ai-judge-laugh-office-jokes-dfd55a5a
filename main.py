# u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a: one line about
# office life, under 200 characters. The program writes that single joke to
# /output/entry.txt.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = (
    "The printer, the Wi-Fi, and my motivation all broke at 9 a.m. \u2014 "
    "IT fixed the first two."
)

assert 1 <= len(JOKE) <= 199, f"joke is {len(JOKE)} chars, must be 1-199"
assert JOKE.strip(), "joke must not be only whitespace"

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
