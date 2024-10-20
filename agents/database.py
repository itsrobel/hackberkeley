MESSAGES = []

def insert(msg):
    MESSAGES.append(msg)
    
def retrieve(msg):
    res = '\n\nDatabase:\n\n\n'
    for i in MESSAGES:
        res += i
    return res

