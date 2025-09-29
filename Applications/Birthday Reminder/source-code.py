"""Tiny birthday reminder utility.

This module provides a small interactive `main()` function that can be used to
check and append birthdays. It's intentionally lightweight and safe to import.
"""

import datetime
from typing import List, Tuple


def _ordinal_suffix(n: int) -> str:
   """Return ordinal suffix for a positive integer (1 -> 'st', 2 -> 'nd', 3 -> 'rd', otherwise 'th')."""
   if 10 <= (n % 100) <= 20:
      return "th"
   return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")


def main() -> None:
   """Run a tiny birthday checker.

   Prompts to add a birthday and prints today's matches. Uses ISO date parsing
   for the add flow (yyyy-mm-dd). Safe to import; call `main()` to run.
   """
   today = datetime.date.today()
   bday_log: List[Tuple[str, Tuple[str, str, str]]] = [
      ("Ayushi", ("1999", "10", "19")),
      ("Yash", ("1999", "04", "21")),
   ]

   try:
      add = input("To add birthday type y:").strip().lower()
   except (EOFError, KeyboardInterrupt):
      # Non-interactive environment or user cancelled; just check preadded log
      add = ""

   if add.startswith("y"):
      new = input("Add birthday in format yyyy-mm-dd:")
      name = input("Whose bday?")
      try:
         d = datetime.date.fromisoformat(new)
         date = (str(d.year), f"{d.month:02d}", f"{d.day:02d}")
         bday_log.append((name, date))
      except ValueError:
         print("Invalid date format; expected yyyy-mm-dd. Skipping add.")

   for birthday in bday_log:
      byear, bmonth, bday = birthday[1]
      if int(bmonth) == today.month and int(bday) == today.day:
         age = today.year - int(byear)
         suffix = _ordinal_suffix(age)
         print(f"It's {birthday[0]}'s {age}{suffix} Birthday")


if __name__ == "__main__":
   main()

