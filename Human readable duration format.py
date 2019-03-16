def format_duration(seconds):
    if seconds == 0: 
        return "now"
        
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    days = hours // 24
    hours = hours % 24
    years = days // 365
    days = days % 365
    
    mas = [("years", years),
           ("days", days),
           ("hours", hours),
           ("minutes", minutes),
           ("seconds", seconds)]
           
    fil_mas = [x for x in mas if x[1]!=0]
    li = ["{} {}".format(x[1], x[0]) if x[1]!=1 else "{} {}".format(x[1], x[0][:-1]) for x in fil_mas]
    if len(li)==1:
        return li[0]
    else:
        return "{} and {}".format(", ".join(li[:-1]), li[-1])
