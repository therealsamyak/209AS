import random


# 4(a)
def simulate_flips(coin_type, num_flips):
    if coin_type == "fair":
        probs = [0.5, 0.5]  # H, T
    elif coin_type == "biased":
        probs = [0.25, 0.75]  # H, T
    else:
        raise ValueError("coin_type must be 'fair' or 'biased'")

    outcomes = ["H", "T"]
    sequence = random.choices(outcomes, weights=probs, k=num_flips)
    return sequence


def main():
    fair_sequences = []
    biased_sequences = []
    for _ in range(5):
        fair_sequences.append(simulate_flips("fair", 40))
    for _ in range(5):
        biased_sequences.append(simulate_flips("biased", 40))
    print("Generated 10 sequences of 40 flips each: 5 fair, 5 biased.")
    print(f"First fair sequence: {fair_sequences[0]}")
    print(f"First biased sequence: {biased_sequences[0]}")


if __name__ == "__main__":
    main()
