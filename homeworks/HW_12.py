def arithmetic_mean(*args):
    arith_mean = sum(args)/len(args)
    return arith_mean

def reverse_string(*args):
    rever_str = []
    for s in args:
        if not isinstance(s, str):
            print(TypeError(f"{s} is not string"))
            continue
        rever_str += [s[::-1]]
    return rever_str

def checking_if_h_in_the_word(a):
    while "h" not in a.lower():
        a = input("Please enter a word that contains 'h' letter: ")
    return("Finished")

