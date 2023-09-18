from observer_pattern import Observable

def test_subscribe():
    counter = 0

    def plus_n(n):
        nonlocal counter
        counter += n
    
    def plus_2n(n):
        nonlocal counter
        counter += 2*n

    observable = Observable()
    observable.subscribe(plus_n)
    observable.subscribe(plus_2n)
    observable.notify(2)
    observable.notify(5)

    assert counter == 21

def test_unsubscribe():
    counter = 0

    def plus_one():
        nonlocal counter
        counter += 1
    
    observable = Observable()
    observable.subscribe(plus_one)
    observable.notify()
    observable.unsubscribe(plus_one)
    observable.notify()

    assert counter == 1
