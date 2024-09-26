import tkinter as tk
from tkinter import messagebox
import random

suits = ['قلوب', 'أندية', 'ماس', 'خشب']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'جاك', 'كوين', 'كينغ', 'آس']
deck = [f'{rank} من {suit}' for suit in suits for rank in ranks]


random.shuffle(deck)


rank_values = {str(i): i for i in range(2, 11)}
rank_values.update({'جاك': 11, 'كوين': 12, 'كينغ': 13, 'آس': 14})



def deal_cards(num_players, cards_per_player):
    hands = {f'لاعب {i + 1}': [] for i in range(num_players)}
    for _ in range(cards_per_player):
        for player in hands:
            hands[player].append(deck.pop())
    return hands



def card_value(card):
    rank = card.split(' ')[0]
    return rank_values[rank]



def draw_card(player_hand):
    return random.choice(player_hand)



def show_hands_and_winner():
    num_players = int(player_count_entry.get())
    cards_per_player = int(cards_count_entry.get())

    if num_players * cards_per_player > len(deck):
        messagebox.showerror("خطأ", "!ليس هناك بطاقات كافية")
        return

    hands = deal_cards(num_players, cards_per_player)

    result_text = ""
    player_cards = {}

    for player, cards in hands.items():
        drawn_card = draw_card(cards)
        player_cards[player] = drawn_card
        result_text += f'{player}: {", ".join(cards)} - سحب بطاقة: {drawn_card}\n'


    winner = max(player_cards, key=lambda player: card_value(player_cards[player]))
    result_text += f"\nالفائز هو: {winner} ببطاقة {player_cards[winner]}"

    result_label.config(text=result_text)



root = tk.Tk()
root.title("لعبة البطاقات")
root.geometry("400x500")
root.configure(bg="#f0f8ff")


title_label = tk.Label(root, text="لعبة البطاقات", font=("Arial", 24), bg="#f0f8ff", fg="#333")
title_label.pack(pady=10)

tk.Label(root, text="عدد اللاعبين:", bg="#f0f8ff").pack(pady=5)
player_count_entry = tk.Entry(root)
player_count_entry.pack(pady=5)

tk.Label(root, text="عدد البطاقات لكل لاعب:", bg="#f0f8ff").pack(pady=5)
cards_count_entry = tk.Entry(root)
cards_count_entry.pack(pady=5)

deal_button = tk.Button(root, text="وزع البطاقات والعب", command=show_hands_and_winner, bg="#4CAF50", fg="white",
                        font=("Arial", 12))
deal_button.pack(pady=20)

result_label = tk.Label(root, text="", justify=tk.LEFT, bg="#f0f8ff", font=("Arial", 12))
result_label.pack(pady=5)


root.mainloop()