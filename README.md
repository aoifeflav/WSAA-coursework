# WSAA-coursework

This repository contains all of my work from the Web Services and Applications module, part of Year 2 of the Higher Diploma in Data Analytics at ATU.

## Repository Overview

The repository is divided into three main sections:

1. **Assignments** – Contains graded coursework submitted throughout the semester.
2. **MyWork** – Contains lab work and exercises completed during the semester (not graded).
3. **Project** – Currently a work in progress. Details will be added here once the project is complete.

>  *Note: As the `mywork` folder is not graded and the final project is not et complete, their contents are not described in this README.*

This document focuses on the **Assignments** section.

---

## Assignments Folder Contents

### `assignment02-carddraw.py`

- This program uses the [Deck of Cards API](https://deckofcardsapi.com/) to simulate dealing a deck of cards.
- It shuffles the deck and "deals" 5 cards, printing the value and suit of each.
- The program checks for and congratulates the user if they've drawn:
  - A pair
  - A triple
  - A straight
  - All cards of the same suit

---

### `assignment03-cso.py`

- This script retrieves data from the Central Statistics Office (CSO).
- Specifically, it downloads the dataset for the Exchequer Account (Historical Series).
- The data is saved locally in a file named `CSO.json`.

---

### `CSO.json`

- This file contains the raw output from `assignment03-cso.py`.

---

### `assignment04-github.py`

- This script uses the GitHub API to:
  - Read a file from a private repository using API credentials.
  - Replace all instances of the name `"Andrew"` with `"Aoife"`.
  - Commit the changes and push them back to the repository automatically.

---

## Dependencies

All required Python packages are listed in `requirements.txt`:




