# Airline Seat Preference Agent (Intermediate-Advanced)

This project demonstrates how to build a **dynamic instruction system**
for an airline booking agent using the `agents` library.

## 🎯 Objective

The agent customizes responses based on a traveler's **seat preference**
and **travel experience**.

### Scenarios:

-   **Window + First-time:** Explain window benefits, mention scenic
    views, reassure about flight experience.\
-   **Middle + Frequent:** Acknowledge the compromise, suggest
    strategies, offer alternatives.\
-   **Any + Premium:** Highlight luxury options, upgrades, priority
    boarding.\
-   **Other cases:** General explanation of airline facilities.

------------------------------------------------------------------------

## ⚙️ Context Fields

-   `seat_preference` → (window / aisle / middle / any)\
-   `travel_experience` → (first_time / occasional / frequent / premium)

------------------------------------------------------------------------

## 📂 Code Structure

### `ASP` Class

``` python
class ASP(BaseModel):
    name : str = "adil"
    seat_pref : str
    travel_experiance : str
```

### `seat_prf` Function

Maps user travel experience input into an `ASP` object.

### `traveler_requirments` Function

Defines **dynamic instructions** for the agent depending on context.

### `triage_agent`

Agent configured with custom instruction logic.

### `main()`

Asks the traveler for their experience, builds context, and runs the
agent dynamically.

------------------------------------------------------------------------

## ▶️ Run Instructions

1.  Clone repository and install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

2.  Run the script:

    ``` bash
    python main.py
    ```

3.  Provide input when prompted:

    ``` text
    HELLO GUEST
    Please provide us your travel experiance (first_time/occasional/frequent/premium):
    ```

------------------------------------------------------------------------

## ✅ Example Run

**Input:**

    first time

**Output:**

    Explain window benefits, mention scenic views, reassure about flight experience

------------------------------------------------------------------------

## 📌 Notes

-   Context handling is done with `RunContextWrapper` and `ASP` model.\
-   Instructions are **dynamic**, meaning the LLM adapts based on seat
    preference and travel experience.
"# Airline_Seat_Preference_Agent" 
