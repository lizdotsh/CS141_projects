import mock
import io
import runpy

#Test program for Project 1
#Copyright Dana L Willner

def test_program(filename, exp_output, ret_val = None, sides = None):
  with mock.patch('builtins.input', return_value = ret_val, side_effect = sides):
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        runpy.run_path(filename)
  inp = sides
  if ret_val != None:
    inp = ret_val
  print('Testing with input',inp)
  try:
    assert fake_stdout.getvalue() == exp_output
    if(sides == None):
      sides = ''
    if(ret_val == None):
      ret_val = ''
    print('Expected Output:\n',exp_output, end = '', sep='')
    print('success!\n')
  except AssertionError:
    print('Expected Output:\n',exp_output,'Incorrect Output:\n', fake_stdout.getvalue(),sep='')


#Test reading
print('Testing reading.py\n')
try:
  test_program('reading.py','Your average reading pace is 1 minutes 12 seconds per page\n', sides = [100,2])
  test_program('reading.py','Your average reading pace is 2 minutes 28 seconds per page\n', sides = [500,20.5])
  test_program('reading.py','Your average reading pace is 0 minutes 30 seconds per page\n', sides = [1200,10])
  test_program('reading.py','Your average reading pace is 1 minutes 0 seconds per page\n', sides = [600,10])
  test_program('reading.py','Your average reading pace is 3 minutes 43 seconds per page\n', sides = [247,15.27635])
  
except IOError:
  print('No attempt')
except BaseException as e:
  print(e)
  

#Test rename.py
print('\nTesting rename.py\n')
try:
  test_program('rename.py', 'New name is Seq:1:23:42:13#0:Read_1\n', ret_val='HWI-EAS440_0386:1:23:42:13#0/1')
  test_program('rename.py', 'New name is Seq:1:243:974526381:13#0:Read_2\n', ret_val='HWI-EAS440_0386:1:243:974526381:13#0/2')
  test_program('rename.py', 'New name is Seq:1:23:42:13#0:Read_1\n', ret_val='TRSSSEDFA12349Q:1:23:42:13#0/1')
except IOError:
  print('No attempt')
except BaseException as e:
  print(e)

