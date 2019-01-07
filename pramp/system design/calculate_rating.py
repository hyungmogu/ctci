data = [
    [3,3],
    [4,4],
    [2,4],
    [4,4],
    [1,2]
]

def calculate_rating(data):
    problem_solving = 0
    communication = 0

    size = float(len(data))

    for data_point in data:
        problem_solving += data_point[0]
        communication += data_point[1]

    problem_solving_avg = problem_solving / size
    communication_avg = communication / size

    print("Moe's current score in Pramp is:")
    print("Problem Solving: {0}, Communication: {1}".format(problem_solving_avg,communication_avg))


if __name__ == '__main__':
    calculate_rating(data)