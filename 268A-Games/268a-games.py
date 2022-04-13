if __name__ == "__main__":
  team_colors_home = []
  team_colors_guest = []
  counter = 0
  n = int(input())
  for _ in range(n):
      team_colors = input().split()
      team_colors_home.append(team_colors[0])
      team_colors_guest.append(team_colors[1])
  h = list(set(team_colors_home))
  cntH = [None]*len(h)
  cntG = [None]*len(h)
  for i in range(len(h)):
      cntH[i] = team_colors_home.count(h[i])
      cntG[i] = team_colors_guest.count(h[i])
  sum = 0
  for i in range(len(cntG)):
      sum += cntH[i]*cntG[i]
  print(sum)
