def linearSearch(key):
  a=[]
  a.append(2);
  a.append(3);
  a.append(4);
  a.append(5);
  a.append(6);
  a.append(7);
  for i in range(len(a)):
    if(a[i]==key):
      s=1
      break
  if(s==1):
    print("Key Found")
  else:
    print("Key Not Found")
linearSearch(1)
