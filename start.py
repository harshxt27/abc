def choose_pokemon(player_num):
    pokemons = {
        "1": {"name": "Bulbasaur", "hp": 45, "attack": 49, "defense": 49, "move": "Vine Whip"},
        "2": {"name": "Charmander", "hp": 39, "attack": 52, "defense": 43, "move": "Ember"},
        "3": {"name": "Squirtle", "hp": 44, "attack": 48, "defense": 65, "move": "Water Gun"}
    }
    print(f"Player {player_num}, choose your Pokémon:")
    for k, v in pokemons.items():
        print(f"{k}. {v['name']} (HP: {v['hp']}, ATK: {v['attack']}, DEF: {v['defense']}, Move: {v['move']})")
    choice = input("Enter your choice (1/2/3): ")
    return pokemons.get(choice, pokemons["1"]).copy()

def attack(attacker, defender):
    damage = max(1, attacker["attack"] - defender["defense"] // 2)
    defender["hp"] -= damage
    print(f"{attacker['name']} uses {attacker['move']}! It deals {damage} damage.")
    if defender["hp"] < 0:
        defender["hp"] = 0
    print(f"{defender['name']} has {defender['hp']} HP left.")

def pvp_battle():
    player1 = choose_pokemon(1)
    player2 = choose_pokemon(2)
    print(f"\nBattle Start! {player1['name']} vs {player2['name']}\n")
    turn = 1
    while player1["hp"] > 0 and player2["hp"] > 0:
        print(f"--- Turn {turn} ---")
        print("Player 1's turn:")
        attack(player1, player2)
        if player2["hp"] <= 0:
            print(f"{player2['name']} fainted! Player 1 wins!")
            break
        print("Player 2's turn:")
        attack(player2, player1)
        if player1["hp"] <= 0:
            print(f"{player1['name']} fainted! Player 2 wins!")
            break
        turn += 1

print("Welcome to the Pokémon Game!")
print("Please choose an option:")
print("1. Start New Game")
print("2. Load Game")
print("3. Exit")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    print("Starting a new PvP game...")
    pvp_battle()
elif choice == '2':
    print("Loading game...")
    # ...add logic to load a game...
elif choice == '3':
    print("Exiting the game. Goodbye!")
    # ...exit logic...
else:
    print("Invalid choice. Please restart and select a valid option.")
