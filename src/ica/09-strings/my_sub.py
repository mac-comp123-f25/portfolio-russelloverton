def name_subst(name, text):
    return text.lower().replace("zzz", name)

print(name_subst("not zzz", "zzz"))