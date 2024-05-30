from util import get_data


if __name__ == '__main__':
    data = get_data(__file__)
    # data = '''0.1 0.5 0.8'''
    
    probs = list(map(float, data.split()))
    probs_complement = [round(2 * prob * (1-prob), 3) for prob in probs]
    
    print(*probs_complement)
