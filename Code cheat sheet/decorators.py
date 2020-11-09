import sys


def try_catch(func):
    """wrapper function where we wrap try except arount func,
    we need to execute the function inside the wrapper function."""
    def wrap_func(*args, **kwargs):
        try:
            print('Inside try!!!')
            # this return will return the value of the addition to the wrapper function
            # func contains "test_function" and args = [1,2] and *args = 1 2
            return func(*args, **kwargs)
        except Exception as e:
            print('Inside Except!!!')
            print(e)
            sys.exit(1)
        finally:
            print('Finally section will always be executed')

    # Returning the wrapper function without executing it.
    return wrap_func


@try_catch
def test_function(x, y):
    print('Inside the function', x, y)

    if x + y > 3:
        # This exception will be caught by the decorator try catch
        raise Exception('New exception')
    return x + y


if __name__ == '__main__':
    print(test_function(1, 2))
    print(end='\n\n\n')
    print(test_function(1, 3))