# OppdalsTreffet Age classifying

This project processes a list of participants in the bowling tournament OppdalsTreffet.

## What it does

- Takes a list of tournament participants.
- Uses each participant's license number to find the corresponding player ID used by bowling.no.
- Authenticates with bowling.no to access player birthdates, since the site requires login for that data.
- Compares each player's birthdate against tournament age cutoffs.
- Assigns players to the age group defined by the tournament organizers.

## Key points

- Input: participant list with license numbers.
- Authentication: login flow for bowling.no to retrieve protected birthdate information.
- Output: classification of participants into age groups.

## Purpose

The project automates the process of converting license numbers into bowling.no player IDs, retrieving birthdates securely, and grouping players by age for OppdalsTreffet.
