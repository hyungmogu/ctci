data = [
    [4,4,4],
    [4,4,4],
    [3,4,4],
    [3,3,3],
    [4,4,4],
    [3,3,4],
    [4,4,4],
    [2,4,3],
    [4,4,4],
    [3,3,4],
    [2,2,2],
    [3,3,4],
    [2,3,3],
    [3,3,4],
    [3,3,4],
    [3,4,4],
    [3,2,3],
    [2,4,4],
    [1,1,3]
]

def calculate_rating(data):
    problem_solving = 0
    coding = 0
    communication = 0

    size = float(len(data))

    for data_point in data:
        problem_solving += data_point[0]
        coding += data_point[1]
        communication += data_point[2]

    problem_solving_avg = problem_solving / size
    coding_avg = coding / size
    communication_avg = communication / size

    print("Moe's current score in Pramp is:")
    print("Problem Solving: {0}, Coding: {1}, Communication: {2}".format(problem_solving_avg,coding_avg,communication_avg))


if __name__ == '__main__':
    calculate_rating(data)