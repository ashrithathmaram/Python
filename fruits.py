fruits_list = ['banana', 'apple', 'peach', 'strawberry', 'leechi', 'pineapple', 'grapes', 'avocado', 'blueberries', 'blackberries', 'orange', 'guava', 'kiwi', 'papaya', 'watermelon', 'banana', 'apple', 'peach', 'strawberry', 'leechi', 'pineapple', 'grapes', 'avocado', 'blueberries', 'blackberries', 'orange', 'guava', 'kiwi', 'papaya', 'watermelon', 'banana', 'apple', 'peach', 'strawberry', 'leechi', 'pineapple', 'grapes', 'avocado', 'blueberries', 'blackberries', 'orange', 'guava', 'kiwi', 'papaya', 'watermelon', 'banana', 'apple', 'peach', 'strawberry', 'leechi', 'pineapple', 'grapes', 'avocado', 'blueberries', 'blackberries', 'orange', 'guava', 'kiwi', 'papaya', 'watermelon', 'banana', 'apple', 'peach', 'strawberry', 'leechi', 'pineapple', 'grapes', 'avocado', 'blueberries', 'blackberries', 'orange', 'guava', 'kiwi', 'papaya', 'watermelon', 'banana', 'apple', 'peach', 'strawberry', 'leechi', 'pineapple', 'grapes', 'avocado', 'blueberries', 'blackberries', 'orange', 'guava', 'kiwi', 'papaya', 'watermelon', 'banana', 'apple', 'peach', 'strawberry', 'leechi', 'pineapple', 'grapes', 'avocado', 'blueberries', 'blackberries', 'orange', 'guava', 'kiwi', 'papaya', 'watermelon', 'banana', 'apple', 'peach', 'strawberry', 'leechi', 'pineapple', 'grapes', 'avocado', 'blueberries', 'blackberries', 'orange', 'guava', 'kiwi', 'papaya', 'watermelon', 'banana', 'apple', 'peach', 'strawberry', 'leechi', 'pineapple']

dict_1 = {}

for fruit in fruits_list:
  try:
    dict_1[fruit]
    dict_1[fruit] += 1
  except:
    dict_1[fruit] = 1
print (dict_1)
