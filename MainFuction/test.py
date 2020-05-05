wahserOrderMessage="2012年4月1日,123456,苏B23425,A"
messages=[]
for _ in wahserOrderMessage.split(','):
    messages.append(_)
for _ in messages:
    print(_)