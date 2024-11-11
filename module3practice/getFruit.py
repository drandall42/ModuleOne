import fruits, argparse

FruitArg = argparse.ArgumentParser(
    prefix_chars='-'
)

FruitArg.add_argument('-name',
    required=True,
    type=str,
    help="The name of a fruit")

FruitArg.add_argument('-shape',
    required=True,
    type=str,
    help="The shape of the fruit")

FruitArg.add_argument(
    '-sweet',
    required=True,
    type=bool,
    help="Is the fruit sweet? Requires boolean True or False"
)

FruitArg.add_argument(
    '-colour',
    required=True,
    type=str,
    help="The colour of the fruit"
)

FruitArg.parse_args()

newFruit = fruits.myFruit("","","","")
fruits.printFruit(newFruit)