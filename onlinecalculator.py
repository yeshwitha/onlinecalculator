app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():

    if request.method=="POST":
        operand=request.form['operand']

        if operand in ['add','+','ADD','sum','SUM'] :
            a = redirect("http://127.0.0.1:5000/add")

        else operand in ['sub','-','SUB','difference','DIFFERENCE']  :
            a = redirect("http://127.0.0.1:5000/sub")

        return a

    return render_template("intro.html")

@app.route('/add',methods=["GET","POST"])
def add():
    if request.method=="POST":
        A=request.form['firstnumber']
        B=request.form['lastnumber']
        x=Fraction(A)
        y=Fraction(B)
        C=(x)+(y)
        D=str(C).split('/')
        if len(D) == 2:
            E=int(D[0])/int(D[1])
            F=str(E).split(".")
            if F[1] == '0':
                return "Your result is %s\n" % F[0]
            else:
                return  "Your result is %s\n" %E
        else:
            G=str(C).split(".")
            return "Your result is %s \n" % G[0]

    return render_template("home.html")

@app.route('/sub',methods=["GET","POST"])
def sub():
    if request.method=="POST":
        A=request.form['firstnumber']
        B=request.form['lastnumber']
        x=Fraction(A)
        y=Fraction(B)
        C=(x)-(y)
        D=str(C).split('/')
        if len(D) == 2:
            E=int(D[0])/int(D[1])
            F=str(E).split(".")
            if F[1] == '0':
                return "Your result is %s\n" % F[0]
            else:
                return  "Your result is %s\n" %E
        else:
            G=str(C).split(".")
            return "Your result is %s \n" % G[0]

    return render_template("home.html")
    
if __name__ == '__main__':
   app.run(debug = True)