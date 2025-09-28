import random
import matplotlib.pyplot as plt


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


# 4(b)
def simulate_flips_two(coin_type, num_flips):
    sequence = simulate_flips(coin_type, num_flips)

    # calculate posterior probability of biased coin after each flip
    prior_biased = 0.25
    prior_fair = 0.75
    posteriors = []
    for outcome in sequence:
        if outcome == "H":
            lik_biased = 0.25
            lik_fair = 0.5
        else:
            lik_biased = 0.75
            lik_fair = 0.5
        posterior_biased = (prior_biased * lik_biased) / (
            prior_biased * lik_biased + prior_fair * lik_fair
        )
        posteriors.append(posterior_biased)
        prior_biased = posterior_biased
        prior_fair = 1 - posterior_biased

    return sequence, posteriors


# 4(c) and 4(d)
def plot_likelihoods():
    # Fair coin simulations
    fair_posteriors_list = []
    for _ in range(5):
        _, post = simulate_flips_two("fair", 100)
        fair_posteriors_list.append(post)

    # Biased coin simulations
    biased_posteriors_list = []
    for _ in range(5):
        _, post = simulate_flips_two("biased", 100)
        biased_posteriors_list.append(post)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Plot fair
    for i, post in enumerate(fair_posteriors_list):
        ax1.plot(range(1, 101), post, label=f"Simulation {i + 1}")
    ax1.set_xlabel("Number of Flips")
    ax1.set_ylabel("Posterior Probability of Biased Coin")
    ax1.set_title("Evolution of Posterior Probability for Fair Coin Simulations (4(c))")
    ax1.legend()
    ax1.grid(True)

    # Plot biased
    for i, post in enumerate(biased_posteriors_list):
        ax2.plot(range(1, 101), post, label=f"Simulation {i + 1}")
    ax2.set_xlabel("Number of Flips")
    ax2.set_ylabel("Posterior Probability of Biased Coin")
    ax2.set_title(
        "Evolution of Posterior Probability for Biased Coin Simulations (4(d))"
    )
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.show()


def main():
    fair_sequences = []
    fair_posteriors = []
    biased_sequences = []
    biased_posteriors = []
    for _ in range(5):
        seq, post = simulate_flips_two("fair", 40)
        fair_sequences.append(seq)
        fair_posteriors.append(post)
    for _ in range(5):
        seq, post = simulate_flips_two("biased", 40)
        biased_sequences.append(seq)
        biased_posteriors.append(post)
    print("Generated 10 sequences of 40 flips each: 5 fair, 5 biased.")
    print(f"First fair sequence: {fair_sequences[0]}")
    print(f"First biased sequence: {biased_sequences[0]}")

    # chance that coin is biased
    # (closer to 0 = not biased, closer to 1 = biased)
    print(f"First fair posteriors (last 5): {fair_posteriors[0][-5:]}")
    print(f"First biased posteriors (last 5): {biased_posteriors[0][-5:]}")

    plot_likelihoods()


if __name__ == "__main__":
    main()
