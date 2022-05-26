class ConfigReader():
    def __init__(self):
        self.fileData = dict()
        

    def readFile(self,configFile):
      fileContents = None

      #check if the file exists
      try:
          ConfigFile = open(configFile, "r")
          fileContents = ConfigFile.readlines()
          ConfigFile.close()
      except FileNotFoundError:
          print("Input file not found.")
          return

      #loop through each line in file
      for line in fileContents:
        #check for comment line
        if line[0]=='#' or line[0]==';':
            continue
        #check for new section
        elif line[0]=='[':
            index = line.index(']')
            section = line[1:index]
            self.fileData[section] = dict()
        else:
        #read name:value pair
            if '=' in line:
                name, value = line.split('=')
            elif ':' in line:
                name, value = line.split(':')

            #add content to current section
            self.fileData[section][name.strip()] = value.strip()


    def displayFile(self):
      file = self.fileData
      for section in file:
          print(str(section) + ' :')
          for option in file[section]:
              print(str(option) + ' = ' + file[section][option])
          print()


    # getting sections after strigfying them
    def getSections(self):
      file = self.fileData
      for section in file:
          print(str(section), type(str(section)))


def main():
  #create an object of class ConfigReader
  configFileReader = ConfigReader()
  
  #read file name from user
  #fileName = input("Enter the file name:")
  fileName = 'conf.ini'
  
  #invoke the readFile method
  configFileReader.readFile(fileName)
  
  #display the file contents
  configFileReader.displayFile()
  
  # display sections only
  configFileReader.getSections()

if __name__ == "__main__":
  main()