class College1:
    trade=""
    def Subjects(self, t):
        self.trade=t
        if self.trade=="CSE":
            print("College1 " + self.trade + " Subjects: HTML, CSS, JavaScript")
        if self.trade=="IT":
            print("College1 " + self.trade + " Subjects: Python, DataScience, Machine Learning")

class College2():
    trade=""
    def Subjects(self, t):
        self.trade=t
        if self.trade=="CSE":
            print("College2 " + self.trade + " Subjects: HTML, CSS, JavaScript, BootStrap, React")
        if self.trade=="IT":
            print("College2" + self.trade + " Subjects: Python, DataScience, Machine Learning, Java, .Net")

c1=College1()
c1.Subjects("CSE")

c2=College2()
c2.Subjects("CSE")