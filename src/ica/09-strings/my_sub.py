def name_subst(name, text):
    return text.replace("ZZZ", name)

print(name_subst("not zzz", "ZZZ"))