---
tags:
        - Stars
        - Magnitude
        - Flux
        - Stellar_Magnitude
---

# Stellar Magnitude

## Logs Refresher
Log10 (x) - Count the zeros $\log_{10}(100) == 2$
$$ \log{100} = 2 $$
$$ 10^x = Antilog $$

## Stellar Magnitudes
Hipparchus.  The smaller the value, the brighter the object.  Sirius = $-1.4$ (very bright).  Neptune = $7.62$ (much less bright).  This is the 'apparent magnitude', how they appear.  The Sun is $-26$.  Naked eye range is 1 to 6.  Best resolution of telescope we have is about 30.

![Magnitude](https://earthsky.org/upl/2017/03/apparent-magnitude-scale-e1490133992818.jpg)
[Wikipedia - Apparent Magnitude](https://en.wikipedia.org/wiki/Apparent_magnitude)

**N.R. Pogson: For 2 objects, 5 magnitude difference corresponds to a factor of 100 brightness**

## Flux
Total flow light energy per unit area:
$$ Wm^{-2} \text{ OR } Js^{-1}m^{-2} $$

Apparent mag relation (Ratio of fluxes):
$$ \frac{Fm}{Fn} = 2.512^{n-m} \tag{Eq 2.1} $$
Note: Ratio = 100 == n-m of 5 (see above N.R. Pogson)

## Pogson's Relation
Difference in apparent magnitudes:
$$ m - n = -2.5 * \log_{10}{\frac{Fm}{Fn}} \tag{Eq 2.2} $$ 
$$ 1 - 6 = 100 \tag{As expected}$$

## Zero point of apparent Mag
For a star of m = 0, and Flux Fo, apparent mag of any star is:
$$ m = 2.5 \log_{10}\frac{Fm}{Fo} $$
[Wikipedia - Zero Point](https://en.wikipedia.org/wiki/Zero_Point_(photometry))

## Luminosity
The Sun is (Solar Luminosity): 
$$ 4 * 10^{26} Watts $$

## Inverse Square law 
![Luminosity](https://upload.wikimedia.org/wikipedia/commons/2/28/Inverse_square_law.svg)

[Astronomy Notes - Inverse Square Law](https://www.astronomynotes.com/starprop/s3.htm)

$$ \text{Surface Area Of Sphere} = 4\Pi r^2 $$

Observed Flux inversely proportional to squared distance:
$$ Flux = \frac{\text{Luminosity}}{\text{Surace Area of Sphere}} $$
$$ F = \frac{L}{4\Pi d^2} \tag{Eq. 2.4} $$

Hence:
$$ \frac{F_D}{F_d} = \frac{d^2}{D^2} \tag{Eq 2.5}$$
e.g. 1/3 distance ratio == 9/1 Flux ratio 

*Note: Gravity also has $r^2$ falloff $F = G\frac{m_1m_2}{r^2}$*

## Absolute Magnitude
Absolute magnuitude, similar to Pogson, but with absolute Luminosity ratio
$$ M - N = -2.5 * \log_{10}\frac{L_M}{L_N} $$

At 10pc from star, Absolute Mag == Apparent Mag

Therefore; from Eq 2.5, a star at distance d, flux $F_M$ at 10pc with observed flux $F_m$
$$ \frac{F_M}{F_m} = \frac{d^2}{10^2} \tag{Eq. 2.7} $$

Combined with Eq.2.2:
$$ m - M = 5 \log_{10}d - 5 \tag{Eq. 2.8} $$
(m - M) is the distance modulus

e.g. for distance 10pc:
$$ m - M = 5 \log_{10}10 - 5 $$
$$ m - M = 0 $$
Therefore: at 10pc M == m

# Worked Examples
Distance to Vega, given m = 0.03, M = 0.58

$$ 0.03 - 0.58= 5 \log_{10}d - 5 $$
$$ -0.55 = 5\log_{10}d - 5 $$
$$ 4.45 = 5 log_{10}d $$
$$ 10^0.89 = 7.76 pcs $$
== 25 Lightyears (distance to Vega)

# References
![YouTube Tutorial](https://www.youtube.com/watch?v=RmuklXC94Cs)