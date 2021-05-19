'''
You are given a set of data that looks like the following:

    {
        'GOT_WORSE': {
            'test1': [
                (1234567, 'PASSED'),
                (1234568, 'PASSED'),
                (1234569, 'FAILED')
            ],
            'test2': [
                (3234567, 'PASSED'),
                (3234568, 'FAILED'),
                (3234569, 'FAILED'),
                (3234570, 'FAILED')
            ]
        },
        'GOT_BETTER': {
            'test3': [
                (2234565, 'FAILED'),
                (2234566, 'FAILED'),
                (2234567, 'PASSED'),
                (2234568, 'PASSED')
            ]
        }
    }

The data represents tests that got better or got worse across a period of time
where changes were checked into the code base.

For each test, `GOT_WORSE` data always starts with 'PASSED' and end with
'FAILED', with one transition in the middle. Similarly, `GOT_BETTER` data
always starts with 'FAILED' and end with 'PASSED', with one transition in
the middle.

The list under each test is guaranteed to be in order of `change_id`.

Based on this data, return a list of messages that looks like the following:

    ['change 1234569 broke test1',
     'change 3234568 broke test2',
     'change 2234567 fixed test3']

'''
from exercise2_data import case1_data


def blamer(test_data):
    '''
    @param test_data: test data as spec'd above
    @return: List[str]
    '''
    pass


if __name__ == '__main__':
    for line in blamer(case1_data):
        print(line)
