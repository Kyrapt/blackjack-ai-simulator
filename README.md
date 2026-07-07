# 🤖 Intelligent Blackjack with Serverless AI (Python OOP)

A complete **Blackjack (Twenty-One)** game simulator developed in Python utilizing the **Object-Oriented Programming (OOP)** paradigm. The core highlight of this project is the Dealer, whose game decisions are not bound by rigid rules but are evaluated in real-time by a Large Language Model via native HTTP requests.

---

## 🚀 Key Features Demonstrated

- **Object-Oriented Programming (OOP):** Robust and encapsulated modeling of real-world entities: `Card` and `Deck`.
- **Dunder Methods (Rich Comparison):** Advanced utilization of magic methods like `__str__` and `__lt__` (the `<` operator), enabling the deck to be natively sorted using Python's organic `.sort()` algorithm.
- **Dynamic Score Evaluation:** The system automatically calculates the value of the **Ace** as either 11 or 1 point to protect the player from busting unnecessarily.
- **Zero-Dependency AI Integration:** Direct communication with Chat AI APIs using purely Python's native standard libraries (`urllib.request` and `json`), completely bypassing the need for heavy external package installations.
- **Resilient Fallback Architecture:** Includes robust error handling. If the internet connection drops, the game autonomously triggers the classic casino algorithm (the Dealer hits on any hand below 17).

---

## 🛠️ Tech Stack

- **Core Language:** Python 3.x
- **Connectivity:** `urllib.request`, `json` (Python Standard Library)
- **AI Integration:** Serverless Chat API Inference

---

## 🎮 How to Run

Since the project is lightweight and independent, **no external package installation via `pip` is required**.

1. Download or clone this repository.
2. Open your terminal inside the project directory.
3. Run the following command:

```bash
python blackjack_ia.py
```

---

## 📄 Codebase Architecture

- `Card`: Manages card values, suits, and rich comparison sorting rules.
- `Deck`: Controls the instantiation of the 52 cards, shuffling, drawing mechanisms, and state resets.
- `decisao_ia_web`: Constructs the contextual game prompt, handles the outbound HTTP requests, and parses the API JSON response payload.
- `blackjack_com_ia`: The main controller coordinating user interaction and machine turn states.
