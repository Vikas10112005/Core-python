
a = 10
b = 0

try:
    c = a / 0
    print('division:', c)
except IndexError as e:
    print('indexerror exception:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError exception:', e)
except Exception as e:
    print('Exception:', e)
else:
    print('in else block')
finally:
    print('in finally block')