# Outline Of Project

This project is currently split into 2 directories:
1. [code](../code) where you will find the code for this project
2. [docs](../docs) where you will documentation for this project

# Reasoning For Code

This code was developed to help support teams & management:
- get a visual and data-driven feel for cases that needed special attention
- see high level view of current case load by individual engineer and/or teams
- automate reports whenever needed
- have both a graphical respresentation, as well as XLSX file review of insights

## What Was To Be Measured

Since most of the items to be measured (_e.g.:  case escalation, indications of custumor sentiment issues, etc_) are no longer something I can access or utilize, I will cover a few of the required items that I can emulate manually. These include:
- case age SLA alert (_is the case open past a certain age?_)
- customer requested escalation
- customer requested update
- duty manager involved
- escalated to engineering (business unit)
- case on hold
- last time case externally updated
- last time case was reviewed (by someone other than case owner)

Each "case" had it's own set of flags with particular parameters. You can view this in the `Case_Bools` class of the [code\classes.py](code\classes.py) file.

Each "flag" had at least the following attributes (others not included here because I no longer can easily pull data for them):
1. boolean (if flag was on or off)
2. weight (some flags had more weight than others)
3. date of last note that this indication was made in the ticket
4. URL of note (_which we will not have, but this did allow someone to go straight to the note in the ticket_)
5. days since flag turned on (_some flags were turned off & updated in the database, depending on the flag_)
6. user who made the note  (_which was helpful for the printout portion_)

More on this to come.