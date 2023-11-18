from datetime import datetime

def time_the_process(func):
    '''
    use this decorator to see how long the process is

    @time_the_process
    def your_function():
        # do something

    '''

    def inner(*args, **kwargs):                                                                                            
        start_time = datetime.now()
        print('\n\n')
        print('Function', func.__name__)
        print('Started at {}'.format(str(start_time)))
        func(*args, **kwargs)
        end_time = datetime.now()
        duration = end_time - start_time
        report_msg = 'Started at {} , finished at {} , duration = {}'.format(str(start_time), str(end_time), str(duration))
        print('\n')
        print(report_msg)
        print('\n\n')
    return inner