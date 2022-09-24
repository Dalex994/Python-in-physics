from pylab import *

# Données modifiables
A = 5	# amplitude suivant z, en dm (entre 0 et Amax)
T = 3	# période de l'onde en s (entre 2 et 10)
xM = 10	# abscisse de M en km (entre 0 et L)

# Données non modifiables!
v = 10   	# célérité en m/s
L = 0.040	# distance entre le bateau et la berge suivant x, en km
tmax = 30	# date de fin en s
Amax = 10	# amplitude maximale en dm

# Définition de t (500 points) et de la fonction périodique
t = linspace(0, tmax, 500)
def z(t):
	return 0.56*A*(sin(2*pi*t/T) - sin(4*pi*t/T))

# Définition des graphiques
fig = figure()
gcf().subplots_adjust(hspace = 0.7)

# Graphiques
fig.add_subplot(2, 1, 1)       # en x = 0
plot(t, z(t))
title("z(t) à la source")
xlabel("t (en s)")
ylabel("z (en dm)")
grid(True)
ylim(-Amax, Amax)
xlim(0, tmax)
text(0.29,-9.1, "Amplitude A=5dm" + "     Période T=3s")

fig.add_subplot(2, 1, 2)         # en xM
plot(t, z(t - 1000*xM/v))
title("z(t) à xM = "+str(xM)+" km de la source")
xlabel("t (en s)")
ylabel("z (en dm)")
grid(True)
ylim(-Amax, Amax)
xlim(0, tmax)

show()
