class Config:
  SECRET_KEY = 'SUPER_SECRET'
  WTF_CSRF_ENABLED = False # To not have in the test_hello_post the error AssertionError: False is not true : HTTP Status 301, 302, 303, 305, 307 expected but got 200 obtuve este error corriendo el ultimo test
