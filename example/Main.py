#! /usr/bin/env python3
import sys

def enter():
	print("Hello! I'll show more efficient coding paradigm (press enter to continue)")
	sys.stdin.readline()
	print("We use folder-names as namespaces")
	sys.stdin.readline()
	print("a.Aa")
	example = a.Aa
	example.insideAa(sys.stdin)

	print("Now let's use algo")
	print("Enter two numbers to add together:")
	one = sys.stdin.readline()
	two = sys.stdin.readline()
	print("Your answer is: {}".format(algo.Sum.sum(float(one), float(two))))

	sys.stdin.readline()
	print("We now compute sin: {}".format(algo.Sin.getSin(355/113)))


if __name__ == "__main__":
	enter()
