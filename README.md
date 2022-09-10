# Helium-Telegram-Bot
## NOTE: Work In Progress!
This is a repository for a Telegram bot for Helium API written in Python.

Available commands: 
- **/start**: Right now it returns placeholder text, it will be converted into first time setup for a hotspot owner with one or multiple hotspots.
- **[any text]** - this triggers echo action which returns text, otherwise not a command, back to the user.
- **bc_stats** - returns current blockchain statistics.
- **tk_supply** - returns Helium token supply data.
- **hs_data** - returns data for a hotspot, right now it pulls the hotspot id from a *.secret/secrets.json* HOTSPOT_ADDRESS attribute which was not included in the repository, will be replaced with ZODB persistent object DB.
