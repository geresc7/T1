# Gerard Escardó Cabrerizo

#EX1
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=440                               # Freqüència de la sinusoide
fy=4000                       # Freqüència ex1
fz=50                         # Freqüència ex1
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
y = A * np.cos(2 * pi * fy * t)  # Senyal sinusoidal ex1
z = A * np.cos(2 * pi * fz * t)  # Senyal sinusoidal ex1
sf.write('so_exemple1.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav
sf.write('so_ex1_4000.wav', y, fm)   # Escriptura del senyal a un fitxer en format wav
sf.write('so_ex1_50.wav', z, fm)   # Escriptura del senyal a un fitxer en format wav

Tx=1/fx                                   # Període del senyal
Ty=1/fy                        # Període del senyal ex1
Tz=1/fz                        # Període del senyal ex1
Lsx=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide
Lsy=int(fm*5*Ty)              # Nº mostres ex1
Lsz=int(fm*5*Tz)             # Nº mostres ex1

plt.figure(0)                             # Nova figura
plt.plot(t[0:Lsx], x[0:Lsx])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide (440 Hz)')   # Títol del gràfic
plt.show() 
plt.figure(1)
plt.plot(t[0:Lsy], y[0:Lsy])   # Representació ex1
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide (4 kHz)')   # Títol del gràfic
plt.show() 
plt.figure(2)
plt.plot(t[0:Lsz], z[0:Lsz])   # Respresentació ex1
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide (50 Hz)')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 

import sounddevice as sd      # Importem el mòdul sounddevice per accedir a la tarja de so
sd.play(x, fm)                # Reproducció d'àudio

from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Lsx], N)           # Càlcul de la transformada de 5 períodes de la sinusoide
Y=fft(y[0 : Lsy], N)       #ex1
Z=fft(z[0 : Lsz], N)       #ex1
k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(3)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Lsx} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics

#ex1 --> 4 kHz
plt.figure(4)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(Y))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Lsy} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(Y)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics

#ex1 --> 50 Hz
plt.figure(5)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(Z))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Lsz} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(Z)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics



#EX2
x_r, fm_r = sf.read('so_ex1_4000.wav')      #llegir so
Tm_r=1/fm_r                                   #període de mostratge
fx_r = fm_r/2                               #Nyquist per coneixer la frecuencia del to
Tx_r=1/fx_r                                 #període de la senyal
Lsx_r=int(fm_r*5*Tx_r)               # Nombre de mostres corresponents a 5 períodes de la sinusoide       
Leng = len(x_r)                      #llargada de la señal
T_r = Leng*Tm_r                      # Durada de T segons
L_r = int(fm_r * T_r)                  # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t_r=Tm_r*np.arange(L_r) 

plt.figure(6)                             # Nova figura
plt.plot(t_r[0:Lsx_r], x_r[0:Lsx_r])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes del so_ex1 (4 kHz)')   # Títol del gràfic
plt.show() 