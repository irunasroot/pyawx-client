"""
Author: Dennis Whitney
Email: dennis@runasroot.com
Copyright (c) 2021, iRunAsRoot
"""

# ## How do I want this to look?
# Each API grouping type gets its own model
# Each model object has the API endpoint defined
# Each model object should have the related POST, GET, PUT, DELETE commands builtin
# Each model object should be caching values from the API
# I want to be able to make changes to the object and then call .save() or similar to post the changes back to the API

# How do I cache this dataset?
# I would like to have some kind of class that is created as an attribute that way when the attribute is added
#  to said object it has the ability to have cached data storing the old value and updating for the new value
#  this would allow users to possibly revert any changes if needed.
#  e.g. Object.some_attr.revert() or something like that
# if this is also too convoluted which I think it might be then the dataset can be stored in a private dict object.
#   When .save() is called it checks for changes against the cached dataset and posts the changes accordingly.
#   This method can still allow for some revert mechanism, but might be on the object itself instead of the attribute


# How to connect if you just want a specific object dataset?
# When calling any one of these types of objects you should be either passing in client info or getting the client
# object so the endpoint can be called
# if this is too convoluted then just make the user create an initial client object that retrieves the asked for data
