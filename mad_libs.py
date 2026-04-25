def get_input(word_type: str):
    user_input = input(f'Enter a {word_type}: ')
    return user_input

noun1 = get_input("noun")
verb1 = get_input("verb")
noun2 = get_input("noun")
verb2 = get_input("verb")

story = f"""
{noun1}: Hey {noun2}, something strange happened today...

{noun2}: What is it? You look worried.

{noun1}: I was trying to {verb1} near the old forest, and suddenly everything went quiet.

{noun2}: Quiet? That doesn't sound normal.

{noun1}: Exactly! Then I saw a shadow... it looked like it wanted to {verb2}.

{noun2}: Wait... you mean THAT legend is real?

{noun1}: I don’t know, but I got scared and ran away.

{noun2}: We can't ignore this. We should go back and check together.

{noun1}: Are you serious? What if it tries to {verb2} again?

{noun2}: Don’t worry, I’ll be with you. We’ll face it together.

{noun1}: Okay... let’s go. But if things get weird, we run!

{noun2}: Deal. And hey—maybe this will turn into an adventure.

{noun1}: Yeah... an adventure that started with me trying to {verb1}.

And so, {noun1} and {noun2} walked back toward the forest, ready to discover the truth behind the mysterious shadow...
"""

print(story)