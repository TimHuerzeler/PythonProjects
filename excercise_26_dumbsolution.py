a = ['2', '10', '5', '40', '42', '82', '42', '12', '27', '72', '27', '12', '75', '12', '27', '72',
     '57', '72', '27', '12', '75', '81', '75', '12', '27', '72', '57', '19', '57', '72', '27', '12', '75', '81', '36', '81']

grades = ['2', '10', '5', '40', '42', '82', '42', '12', '27', '72', '27', '12', '75', '12', '27', '72',
          '57', '72', '27', '12', '75', '81', '75', '12', '27', '72', '57', '19', '57', '72', '27', '12',
          '75', '81', '36', '81', '75', '12', '27', '72', '57', '19', '95', '19', '57', '72', '57', '19',
          '95', '38', '95', '19', '57', '19', '95']
b = [[2], [10], [5], [40], [42], [82], [42], [12], [27], [72], [27], [12], [75], [12], [27], [72], [57], [72],
     [27], [12], [75], [81], [75], [12], [27], [72], [57], [19], [57], [72], [27], [12], [75], [81], [36], [81],
     [75], [12], [27], [72], [57], [19], [95], [19], [57], [72], [27], [12], [75], [81], [36], [58], [36], [81], [75], [12]]

print(list(map(lambda letter: {letter: grades.count(letter)}, set(grades))))