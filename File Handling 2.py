with open("./sample_data/emails.txt","r") as file:
  content = file.readlines()
  cleaned = list(set(i.strip().lower() for i in content))
  cleaned.sort()

print(*cleaned,sep='\n')
