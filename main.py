boat_side = 'Right'
missionaries_on_right = 3
missionaries_on_left = 0
cannibals_on_right = 3
cannibals_on_left = 0


print('M =',missionaries_on_left ,'c =',cannibals_on_left,'|------b|','M =',missionaries_on_right,'c =',cannibals_on_right)

while True:
    missionaries = int(input("No of missionaries:"))
    cannibals = int(input("no of cannibals:"))
    if (missionaries+cannibals)!=1 and (missionaries+cannibals)!=2:
        print("Invalid move")
        continue
    if boat_side == "Right":
        if(missionaries_on_right <missionaries) or (cannibals_on_right<cannibals):
            print("invalid moves")
            continue
        missionaries_on_right = missionaries_on_right - missionaries
        cannibals_on_right = cannibals_on_right - cannibals
        missionaries_on_left+=missionaries
        cannibals_on_left+=cannibals
        print('M =', missionaries_on_left, 'c =', cannibals_on_left, '|b-----|', 'M =', missionaries_on_right, 'c =',
              cannibals_on_right)
        boat_side = "Left"
    else:
        if(missionaries_on_left<missionaries) or (cannibals_on_left<cannibals):
          print("invaliduu")
          continue
        missionaries_on_left = missionaries_on_left-missionaries
        cannibals_on_left = cannibals_on_left-cannibals
        missionaries_on_right+=missionaries
        cannibals_on_right+=cannibals
        print('M =', missionaries_on_left, 'c =', cannibals_on_left, '|------b|', 'M =', missionaries_on_right, 'c =',
              cannibals_on_right)
        boat_side = "Right"
    if(missionaries_on_right<cannibals_on_right and missionaries_on_right>0) or (missionaries_on_left<cannibals_on_left and missionaries_on_left>0):
        print("You Loose")
        break

    if(missionaries_on_left == 3 and cannibals_on_left ==3):
        print("Winneu")
        break






