#List Comprehension


for x in range(0, 10):
      print(x*2)


a_group_of_items = [1,2,3,4,5,6,7,8,9]

a_new_list = [x for x in a_group_of_items]

print(a_new_list)



a_new_list = [x*2 for x in a_group_of_items]

print(a_new_list)




def do_something(num):
      num = num*5
      num += 5
      num /= 2
      return num

a_new_list = [do_something(x) for x in a_group_of_items]

print(a_new_list)





a_new_list = [x for x in a_group_of_items if x%2==0]

print(a_new_list)





a_new_list = [x for x in a_group_of_items if x%2==0 or x*2>4]

print(a_new_list)






class myClass:
      def __init__(self, a, b):
            self.a = a
            self.b = b

      def __repr__(self):
            return f"myClass(a: {self.a}, b: {self.b})"


a_new_list = [myClass(x, x*2) for x in range(1,10)]

print(a_new_list)


b_new_list = [z.b*3 for z in a_new_list]

print(b_new_list)











