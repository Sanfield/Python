class Capstr(str):
    def __new__(cls,string):
        string = string.upper()
        return str.__new__(cls,string)
    def __def__(self):
        print("重写del方法")
        
    
