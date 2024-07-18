parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

# Your code here
def get_parking_lot(lista):
    state={
        "total_slots": 0,
        "available_slots": 0,
        "occupied_slots": 0

    }
    for array in lista:
        for numero in array:
            if numero == 2:
                state["available_slots"]+=1
                state["total_slots"]+=1
            elif numero == 1:
                state["occupied_slots"]+=1
                state["total_slots"]+=1

    return state



print(get_parking_lot(parking_state))
    
        