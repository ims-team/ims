
class Console():
  ip= "0"
  def __init__(self, ip):
    self.ip=ip
  
  
def getIP():
  return(Console.ip)
def main(IP):
 Console(IP)

    

if __name__ == "__main__": main()
