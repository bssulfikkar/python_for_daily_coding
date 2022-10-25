try:
    # f = open('testfile.txt')
    # f = open('testfile.txt')
    f = open('corruprt_file.txt')
    if f.name == 'corruprt_file.txt':
        raise Exception
    # var = bad_var
# except Exception:
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error')
else:
    print(f.read())
    f.close()
finally:
    print("I am executing finally")
