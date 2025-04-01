def quote(fighter: str) -> str:
    newfighter = fighter.lower()

    if newfighter == 'George Saint Pierre' or newfighter == 'george saint pierre':
        return "I am not impressed by your performance."
    else:
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"

if __name__ == '__main__':
    fighter = str(input("Ingresa una cadena:"))
    print(quote(fighter))