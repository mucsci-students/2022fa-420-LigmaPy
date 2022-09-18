# import pytest
# import sys
# import interface

# # this decorator is keep this thing from looping forever 
# def run_once(f):
#     def wrapper(*args, **kwargs):
#         if not wrapper.has_run:
#             wrapper.has_run = True
#             return f(*args, **kwargs)
#     wrapper.has_run = False
#     return wrapper

# # override the input 
# class MockInputFunction:
#     def __init__(self, return_value=None):
#         self.return_value = return_value
#         self._orig_input_fn = __builtins__['input']
#     @run_once
#     def _mock_input_fn(self, prompt):
#         print(prompt + str(self.return_value))
#         return self.return_value
#     def __enter__(self):
#         __builtins__['input'] = self._mock_input_fn

#     def __exit__(self, type, value, traceback):
#         __builtins__['input'] = self._orig_input_fn

# @run_once
# def run():
#     """ function to test """
#     z = interface.Interface()
#     x = z.run()


# with MockInputFunction(return_value='eixt'):
#     run()
#     print("tested class addition")


# # with MockInputFunction(return_value='addClass test2'):
# #     func()
# #     print("tested class addition")
