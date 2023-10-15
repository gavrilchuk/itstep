class trikutnik:
    type="трикутник"
    count=3
    name="ABC"
    def __init__(self,name,a,b,c):
        self.name=name
        self.a=a
        self.b=b
        self.c=c



    def print_tr(self):
        print(f"Моє ім'я - {self.name}")
    def remane(self,new_name):
        self.name=new_name
        self.print_tr()

tr1=trikutnik('ABC',2,3,4)

tr1.print_tr()
