if __name__ == "__main__":
  my_fun = lambda my_list: 0 if int(my_list[0]) % int(my_list[1]) == 0 else int(my_list[1]) - int(my_list[0]) % int(my_list[1])
  lst = [my_fun(input().split()) for _ in range(int(input()))]
  list(map((lambda x: print(x)), lst))
