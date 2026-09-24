def eat_mangoes(count):
    if count == 0:
        print("hath khali ho gaya ladlee. chal nikal ab")
        return

    print(f"mere pass me {count} aam hai. ek kha leta hu")
    eat_mangoes(count-1)

eat_mangoes(5)