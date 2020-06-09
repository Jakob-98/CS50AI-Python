from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave), 
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    
    Implication(AKnight, And(AKnave, AKnight)) #What a knight says is true, so it it a straightforward and implication
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave), 
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    Implication(AKnight, And(AKnave, BKnave)), 
    Implication(AKnave, Not(And(AKnave, BKnave))) #What a knave says is false, so it is a not and implication
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave), 
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    Implication(AKnight, Or(And(AKnight, BKnave), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnave)))), #if A is a knave, reverse (not) statement
    Implication(BKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(BKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))) #idem for B

    )

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave), 
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)), 


# A says either "I am a knight." or "I am a knave.", but you don't know which.

    Or(Implication(AKnight, AKnight), #I should really learn proper indentation..
    Implication(AKnave, Not(AKnight)),
    Implication(AKnave, AKnave),
    Implication(AKnight, Not(AKnave))
     ),

# B says "A said 'I am a knave'."
    Implication(BKnight, And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))),
    Implication(BKnave, Not(And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave))))),
# B says "C is a knave."
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

# C says "A is a knight."

    Implication(CKnave, Not(AKnight)),
    Implication(CKnight, AKnight)
)



def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
