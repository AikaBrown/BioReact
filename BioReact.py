def RungeKutta4(T, X, S, y, h, μmax, Ks, V, F, Sr, I):
  """
  Description:
    In order to know the dynamic behaviour of a biochemical reactor, we have to simulate the developed model. 
    The model structure of the CONTINUOUS STIRRED TANK BIOREACTOR (CSTB) is comprised of the following set of equations:

    1) Biomass balance -->    dX/dT = x*(μ-D)
    2) Substrate balance -->  dS/dT = D*(Sf-s)- μ*x/y
    μ = μmax*s/(km+s)

    For solving the above differential–algebraic system, we have to used the fourth-order Runge–Kutta method. 
    This fuction takes the arguments presented in Args section and solve the fourth-order Runge–Kutta method to obtain a Data Frame
    with values of Time (T) in hours, Biomass (X) in g/L and substrate (S) in g/L. 


  Args:
    T:    Time in hours
    X:    Initial biomass concentration in g/L
    S:    Initial substrate concentration in g/L
    y:    The ratio of the amount of biomass produced to the amount of substrate consumed(g biomass/g substrate)
    h:    Step size (ΔT) in hours
    μmax: The maximum growth rate of the microorganism (h^-1)
    Ks:   substrate concentration at which 1/2 μmax is reached (g/L)
    V:    Volume of the reactor in L.
    F:    Feed flow in L/h
    Sr:   Feed substrate concentration (g/L)
    I:    Number of approximations

  Returns:
    DataFrame with values of Time (T) in hours, Biomass (X) in g/L and substrate (S) in g/L

  Extra:
    this function uses pandas abbreviated as pd:
     before use the function, run "import pandas as pd"
  """

  D=F/V # Dilution (h^-1)
  Valores_prueba = []
  Valores= [T, X, S]
  Valores_prueba.append(Valores)

  for i in range(I):
    
    #Calculate K1 and L1
    f1 = (μmax*X*S)/(Ks+S)-(X*D)
    f2 = D*(Sr-S) - (μmax*S/(Ks+S))*(X/y)
    K1=h*f1
    L1=h*f2

    #Calculate K2 and L2
    nT = T+h/2
    nX = X+K1/2
    nS = S+L1/2
    nf1 = (μmax*nX*nS)/(Ks+nS)-(nX*D)
    nf2 = D*(Sr-nS) - (μmax*nS/(Ks+nS))*(nX/y)
    K2=h*nf1
    L2=h*nf2
    
    #Calculate K3 and L3
    nT = T+h/2
    nX = X+K2/2
    nS = S+L2/2
    nf1 = (μmax*nX*nS)/(Ks+nS)-(nX*D)
    nf2 = D*(Sr-nS) - (μmax*nS/(Ks+nS))*(nX/y)
    K3=h*nf1
    L3=h*nf2

    #Calculate K4 and L4
    nT = T+h
    nX = X+K3
    nS = S+L3
    nf1 = (μmax*nX*nS)/(Ks+nS)-(nX*D)
    nf2 = D*(Sr-nS) - (μmax*nS/(Ks+nS))*(nX/y)
    K4=h*nf1
    L4=h*nf2
    #Calcular los nuevos valores de T, X, S
   
    T=T+h
    X= X+(1/6)*(K1+2*K2+2*K3+K4)
    S= S+(1/6)*(L1+2*L2+2*L3+L4)
    Valores= [T, X, S]
    Valores_prueba.append(Valores)
    df = pd.DataFrame(Valores_prueba, columns=['T', 'X', 'S'])
  return(df)

def biomass_substrate_plot(df):
  '''
  Description:
    Plot Biomass vs substrate concentration
  Args:
    df: a DataFrame with 3 columns and numerical index: 
        1) T: Time in hours
        2) X: Biomass in g/L
        3) S: Substrate in g/L
  Returns:
    a plot x= Biomass g/L, y= Substrate g/L
  
  Extra:
    this function uses matplotlib.pyplot abbreviated as plt:
      before use the function, run "import matplotlib.pyplot as plt"
  '''
  
  plt.style.use("ggplot")
  fig, ax=plt.subplots()
  ax.plot(df['X'], df['S'], linestyle="--", color='b')
  ax.set_xlabel("Biomasa (g/L)")
  ax.set_ylabel("Sustrato (g/L)")
  ax.set_title("Biomasa vs Sustrato\nDiagrama de Fases")


def biomass_time_plot(df):
  '''
  Description:
    Plot Biomass concentration vs time 
  Args:
    df: a DataFrame with 3 columns and numerical index: 
        1) T: Time in hours
        2) X: Biomass in g/L
        3) S: Substrate in g/L
  Returns:
    a plot x= Biomass g/L, y= Substrate g/L
  
  Extra:
    this function uses matplotlib.pyplot abbreviated as plt:
      before use the function, run "import matplotlib.pyplot as plt"
  '''
# Graficar biomasa vs tiempo
  plt.style.use("ggplot")
  fig, ax=plt.subplots()
  ax.plot(df['T'], df['S'], linestyle="--", color='y')
  ax2 = ax.twinx()
  ax2.plot(df['T'], df['X'], linestyle="--", color='g')
  ax.set_xlabel("Tiempo (h)")
  ax.set_ylabel("Sustrato/Biomasa (g/L)")
  ax.set_title("Biomasa y Sustrato vs Tiempo ")
  plt.show()
