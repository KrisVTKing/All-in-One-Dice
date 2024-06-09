import random

def d12_dice():
    num_rolls = int(input("How many times do you want to roll the dice? "))
    results = []
    for _ in range(num_rolls):
        roll = random.randint(1, 12)
        results.append(roll)
    total = sum(results)
    print("Results of the rolls:", results)
    print("Total:", total)

if __name__ == "__main__":
    d12_dice()