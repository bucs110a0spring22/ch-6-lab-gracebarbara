import turtle

def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
        count += 1
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1 
            count += 1
    return count    # the last print is 1

def linegraph(upper_bound = 0):
  graphturtle = turtle.Turtle()
  graphturtle.up()
  graphturtle.goto(0,0)
  graphturtle.down()
  writerturtle = turtle.Turtle()
  window = turtle.Screen()
  window.setworldcoordinates(0, 0, 10, 10)
  max_so_far = 0
  for i in range(1, upper_bound+1):
    result = seq3np1(i)
    print("The loop input value " + str(i) + " has " + str(result) + " iterations.")
    if result > max_so_far:
      max_so_far = result
      writerturtle.clear()
      writerturtle.up()
      writerturtle.goto(i, result)
      writerturtle.write("Maximum so far: " + str(max_so_far))
    window.setworldcoordinates(0,0, i+10, max_so_far+10)
    graphturtle.goto(i, result)
  window.exitonclick()
  
def main():
  seq3np1(3)
  start = int(input("Upper Bound Value: "))
  if start < 0:
    return False
  else:
    for i in range(1, start+1):
      count = seq3np1(i)
      print("Current Loop Value: " + str(i) + "  Number of Iterations: " + str(count))
  linegraph(upper_bound=start)
  
main()

