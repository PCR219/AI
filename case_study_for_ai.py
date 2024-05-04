# -*- coding: utf-8 -*-
"""Case Study for AI

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12Jj07lRF8IFX5VQdfFMXBduH08tvyogj?usp=sharing
"""

import random

def is_safe(board, row, col):
    # Check for queens in the same column or diagonal
    for i in range(row):
        if board[i] == col or abs(row - i) == abs(col - board[i]):
            return False
    return True

def solve_queens_brute_force(board, row, max_iterations=1000):
    n = len(board)
    if row == n:
        return True
    iterations = 0
    for col in range(n):
        iterations += 1
        if iterations > max_iterations:
            return False  # Limit iterations for brute force
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens_brute_force(board, row + 1, max_iterations):
                return True
            board[row] = -1
    return False

def print_queens(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def eight_queens_brute_force():
    board = [-1] * 8
    if solve_queens_brute_force(board, 0):
        print("Brute Force Solution:")
        print_queens(board)
        return board
    else:
        print("No solution found.")
        return None

# Run brute force algorithm
brute_force_solution = eight_queens_brute_force()

import random

def is_safe(board, row, col):
    # Check for queens in the same column or diagonal
    for i in range(row):
        if board[i] == col or abs(row - i) == abs(col - board[i]):
            return False
    return True

def solve_queens_recursive(board, row):
    n = len(board)
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens_recursive(board, row + 1):
                return True
            board[row] = -1
    return False

def print_queens(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def eight_queens_recursive():
    board = [-1] * 8
    if solve_queens_recursive(board, 0):
        print("Recursive Solution:")
        print_queens(board)
        return board
    else:
        print("No solution found.")
        return None

# Run recursive algorithm
recursive_solution = eight_queens_recursive()

def genetic_algorithm_verbose():
    population_size = 10
    generations = 100
    population = [create_board() for _ in range(population_size)]
    for gen in range(generations):
        population.sort(key=lambda x: fitness_function(x))
        best_solution = population[0]
        print(f"Generation {gen+1}: Best solution (fitness = {fitness_function(best_solution)}): {best_solution}")
        if fitness_function(best_solution) == 0:
            print("Genetic Algorithm found a solution.")
            return best_solution
        new_population = []
        for _ in range(population_size // 2):
            parent1 = random.choice(population[:5])
            parent2 = random.choice(population[:5])
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.append(child1)
            new_population.append(child2)
        population = new_population
    print("Genetic Algorithm failed to find a solution.")
    return None

# Run genetic algorithm
genetic_solution_verbose = genetic_algorithm_verbose()