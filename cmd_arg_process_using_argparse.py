import argparse

parse = argparse.ArgumentParser()
parse.add_argument("--physics", help="Enter physics:")
parse.add_argument("--chemistry", help="Enter chemistry :")
parse.add_argument("--maths", help="Enter maths :")
           
args = parse.parse_args()

ps = int(args.physics)
cm = int(args.chemistry)
ma = int(args.maths)

print("Average point: ",round((ps + cm + ma) / 3,2))
