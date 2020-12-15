import random


class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, n):
        total = self.contents
        if n >= len(total):
            return self.contents
        out = []
        for i in range(n):
            k = random.randrange(0, len(total))
            out.append(total[k])
            total.pop(k)
        return out


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_succeeded = 0

    save = hat.contents.copy()
    for i in range(num_experiments):
        hat.contents = save.copy()
        drawn = hat.draw(num_balls_drawn)
        drawn_balls = {}
        for j in drawn:
            drawn_balls[j] = drawn_balls.get(j, 0) + 1
        b = True
        for k, v in expected_balls.items():
            if drawn_balls.get(k, 0) < v:
                b = False
                break
        if b:
            num_succeeded += 1
    return num_succeeded/num_experiments
