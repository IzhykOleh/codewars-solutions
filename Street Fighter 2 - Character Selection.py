def street_fighter_selection(fighters, initial_position, moves):
    print(fighters)
    print(initial_position)
    print(moves)
    current_position = [initial_position[0],initial_position[1]]
    l=[]
    for m in moves:
        if m=="up":
            if current_position[0]==0: pass
            if current_position[0]==1: current_position[0]-=1
        elif m=="down":
            if current_position[0]==1: pass
            if current_position[0]==0: current_position[0]+=1
        elif m=="left":
            if current_position[1]==0: 
                current_position[1]=5
            else:
                current_position[1]-=1
        elif m=="right":
            if current_position[1]==5: 
                current_position[1]=0
            else:
                current_position[1]+=1
        l.append(fighters[current_position[0]][current_position[1]])
    return l
