#!/usr/bin/env python3
"""
Lucky Lottery Simulator

An interactive lottery ticket generator with odds calculator and lucky number predictions.
Features:
  - Generate random lottery tickets
  - Calculate probability of winning
  - Find lucky numbers based on date
  - Multi-ticket draw simulator
"""

import random
from datetime import datetime
from collections import Counter
import math

class LotterySimulator:
    """A comprehensive lottery ticket simulator."""
    
    def __init__(self, num_balls=49, num_picks=6):
        """Initialize lottery parameters."""
        self.num_balls = num_balls
        self.num_picks = num_picks
    
    def generate_ticket(self):
        """Generate a single lottery ticket."""
        return sorted(random.sample(range(1, self.num_balls + 1), self.num_picks))
    
    def generate_multiple_tickets(self, count=5):
        """Generate multiple lottery tickets."""
        return [self.generate_ticket() for _ in range(count)]
    
    def calculate_odds(self):
        """Calculate odds of winning."""
        combinations = math.comb(self.num_balls, self.num_picks)
        probability = 1 / combinations
        return {
            'total_combinations': combinations,
            'probability': probability,
            'percentage': probability * 100,
            'odds_against': f"1 in {combinations}"
        }
    
    def get_lucky_numbers(self):
        """Generate lucky numbers based on current date."""
        today = datetime.now()
        day = today.day
        month = today.month
        year = today.year
        
        seed = day + month + year
        random.seed(seed)
        lucky = sorted(random.sample(range(1, self.num_balls + 1), self.num_picks))
        random.seed()  # Reset seed
        return lucky
    
    def simulate_draw(self, tickets_bought=1, num_draws=1):
        """Simulate lottery draws and check for wins."""
        player_tickets = self.generate_multiple_tickets(tickets_bought)
        
        results = []
        for _ in range(num_draws):
            winning_ticket = self.generate_ticket()
            matches = sum(1 for ticket in player_tickets 
                         if sum(1 for num in ticket if num in winning_ticket))
            results.append({
                'winning_ticket': winning_ticket,
                'matches': matches,
                'tickets_won': sum(1 for ticket in player_tickets 
                                  if set(ticket) & set(winning_ticket))
            })
        return results


def main():
    """Main function to demonstrate the lottery simulator."""
    print("\n🎰 LUCKY LOTTERY SIMULATOR 🎰\n")
    
    simulator = LotterySimulator()
    
    # Generate tickets
    print("Your 5 lottery tickets:")
    tickets = simulator.generate_multiple_tickets(5)
    for i, ticket in enumerate(tickets, 1):
        print(f"  Ticket {i}: {ticket}")
    
    # Show odds
    print("\n📊 Odds of winning:")
    odds = simulator.calculate_odds()
    print(f"  Total combinations: {odds['total_combinations']:,}")
    print(f"  Probability: {odds['percentage']:.10f}%")
    print(f"  {odds['odds_against']}")
    
    # Show lucky numbers
    print("\n✨ Today's lucky numbers:")
    lucky = simulator.get_lucky_numbers()
    print(f"  {lucky}")
    
    # Simulate a draw
    print("\n🎲 Simulating 3 draws...")
    results = simulator.simulate_draw(tickets_bought=5, num_draws=3)
    for i, result in enumerate(results, 1):
        print(f"  Draw {i}: Winning ticket = {result['winning_ticket']}, Matches = {result['matches']}")
    
    print("\n🍀 Good luck! 🍀\n")


if __name__ == "__main__":
    main()
