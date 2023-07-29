import random
import numpy as np


def convert_day_to_string(day):
    if day == 0:
        return "Monday"
    elif day == 1:
        return "Tuesday"
    elif day == 2:
        return "Wednesday"
    elif day == 3:
        return "Thursday"
    elif day == 4:
        return "Friday"
    else:
        return "Day unavailable"


def convert_day_to_int(day):
    if day == "Monday":
        return 0
    elif day == "Tuesday":
        return 1
    elif day == "Wednesday":
        return 2
    elif day == "Thursday":
        return 3
    elif day == "Friday":
        return 4
    else:
        return "Day unavailable"


def convert_slot_to_string(slot):
    if slot == 0:
        return "8am"
    elif slot == 1:
        return "9am"
    elif slot == 2:
        return "10am"
    elif slot == 3:
        return "11am"
    elif slot == 4:
        return "12pm"
    elif slot == 5:
        return "1pm"
    elif slot == 6:
        return "2pm"
    elif slot == 7:
        return "3pm"
    else:
        return "Slot unavailable"


def convert_slot_to_int(slot):
    if slot == "8am":
        return 0
    elif slot == "9am":
        return 1
    elif slot == "10am":
        return 2
    elif slot == "11am":
        return 3
    elif slot == "12pm":
        return 4
    elif slot == "1pm":
        return 5
    elif slot == "2pm":
        return 6
    elif slot == "3pm":
        return 7
    else:
        return "Slot unavailable"


def change_course_to_dict(courses):
    new_dict = {}
    for c in courses:
        new_dict[c.code] = c.unit

    return new_dict


def is_valid_slot(course_schedule, course, day, slot):
    if (day, slot) in course_schedule[course]:
        return False
    if day > 0 and (day - 1, slot) in course_schedule[course]:
        return False
    if day < 4 and (day + 1, slot) in course_schedule[course]:
        return False
    return True


def fitness_function(schedule, courses):
    # Calculate the number of clashes in the schedule
    clashes = 0
    for course in courses:
        slots = schedule[course]
        for day, slot in slots:
            if not is_valid_slot(schedule, course, day, slot):
                clashes += 1
    return 1.0 / (clashes + 1)  # Higher fitness for fewer clashes


def initialize_population(courses, population_size):
    population = []
    for _ in range(population_size):
        schedule = {course: [] for course in courses.keys()}
        for course in courses.keys():
            for _ in range(courses[course]):
                day = random.randint(0, 4)
                slot = random.randint(0, 7)
                schedule[course].append((day, slot))
        population.append(schedule)
    return population


def crossover(parent1, parent2):
    # Two-point crossover
    crossover_point1 = random.randint(1, len(parent1) - 1)
    crossover_point2 = random.randint(crossover_point1, len(parent1) - 1)
    child1 = {}
    child2 = {}
    for course in parent1.keys():
        if random.random() < 0.5:
            child1[course] = parent1[course]
            child2[course] = parent2[course]
        else:
            child1[course] = parent2[course]
            child2[course] = parent1[course]
    return child1, child2


def mutate(schedule, courses):
    # Randomly move a course to a new time slot
    course_to_mutate = random.choice(list(courses.keys()))
    num_slots = len(schedule[course_to_mutate])
    if num_slots > 0:
        slot_to_mutate = random.randint(0, num_slots - 1)
        day = random.randint(0, 4)
        slot = random.randint(0, 7)
        schedule[course_to_mutate][slot_to_mutate] = (day, slot)


def genetic_algorithm(courses, population_size=100, generations=1000):
    population = initialize_population(courses, population_size)

    for generation in range(generations):
        # Calculate fitness for each schedule in the population
        fitness_scores = [(schedule, fitness_function(schedule, courses)) for schedule in population]
        fitness_scores.sort(key=lambda x: x[1], reverse=True)
        best_schedule, best_fitness = fitness_scores[0]

        if best_fitness == 1.0:
            break  # Solution found

        # Select parents for crossover using tournament selection
        parents = []
        for _ in range(population_size // 2):
            tournament = random.sample(fitness_scores, 5)
            tournament.sort(key=lambda x: x[1], reverse=True)
            parents.extend(tournament[:2])

        # Perform crossover and mutation to create new generation
        new_population = []
        for i in range(0, len(parents), 2):
            parent1, parent2 = parents[i][0], parents[i + 1][0]
            child1, child2 = crossover(parent1, parent2)
            mutate(child1, courses)
            mutate(child2, courses)
            new_population.extend([child1, child2])

        population = new_population

    return best_schedule


