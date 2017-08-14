from numpy import *
def compute_error(b,m,points):
    err=0
    #computer error for each predicted line
    for i in range(len(points)):
        err += math.pow((points[i,1]-((m*points[i,0])+b)),2)
    return err/float(len(points))

def gradient_descent_runner(pts,initial_b,initial_m,l_rate,iterations):
    b= initial_b
    m= initial_m
    for i in range (iterations):
        b,m=step_gradient(b,m,array(pts),l_rate)
    return [b,m]

def step_gradient(b_current,m_current,arr,l_rate):
    #gradient descent main step
    b_gradient=0
    m_gradient=0
    for i in range(0,len(arr)):
        x=arr[i,0]
        y=arr[i,1]
        b_gradient+=  -(2/len(arr)) * (y - ((m_current*x) + b_current))
        m_gradient+=  -(2/len(arr)) * x * (y - ((m_current*x) + b_current))
    new_b=b_current - (l_rate*b_gradient)
    new_m=m_current - (l_rate*m_gradient)
    return [new_b,new_m]

def run():
    points= genfromtxt('data.csv',delimiter=',')
    #defining hyper-parameters
    learning_rate=0.0001
    #y=mx+b
    initial_b=0
    initial_m=0
    #number of iterations
    iterations=1000
    [b,m]=gradient_descent_runner(points,initial_b,initial_m,learning_rate,iterations)
    print("final value of b: "+str(b))
    print("Final value of m: "+str(m))
    print("Error value after 1000 iterations is :"+str(compute_error(b,m,points)))





if __name__=='__main__':
    run()
