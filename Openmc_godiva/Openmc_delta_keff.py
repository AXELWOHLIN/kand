
import math
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew 
from scipy.stats import norm, kurtosis


uncert1 = np.array([8.873654661206411e-05, 8.912118534630502e-05, 8.812919397684031e-05, 0.00010061385716091277, 9.553089806145291e-05, 8.399155429332873e-05, 8.684108679201866e-05, 9.054345839374736e-05, 9.196848297951765e-05, 8.93492333610218e-05, 0.00010567013494728788, 0.00010079570805707158, 9.09745483658844e-05, 8.621806347253984e-05, 0.00010123397204278362, 8.76430273542242e-05, 0.00010489206699610704, 9.979410733437633e-05, 8.77297788176893e-05, 9.708138853362849e-05, 8.992443214207586e-05, 0.0001015320173149882, 9.396329667451037e-05, 8.81279187520762e-05, 8.827268529416947e-05, 9.723360116451453e-05, 0.00010014998365613344, 9.467936382508107e-05, 8.837552271393441e-05, 9.540853961611109e-05, 7.412013233075076e-05, 9.929403005089789e-05, 7.989974161409366e-05, 8.412642062454535e-05, 9.438603181600374e-05, 9.660251999669281e-05, 0.00010282212634712845, 8.36773519015779e-05, 9.116100630544002e-05, 8.713814088315426e-05, 8.599525176894744e-05, 9.205245263482871e-05, 0.00010317473202748286, 8.031355256150282e-05, 0.00010120785642028072, 8.517811492853315e-05, 9.04510257766702e-05, 9.359201882099538e-05, 8.369650945967384e-05, 8.855801253929903e-05, 8.717173117113153e-05, 0.00010292282237443719, 8.951331201630091e-05, 7.912473715346436e-05, 9.767464911844466e-05, 9.338580095555302e-05, 9.344172966850616e-05, 9.580656839640587e-05, 9.434861116204577e-05, 9.713103638643606e-05, 9.823142500070363e-05, 9.359201888509467e-05, 9.936064327124568e-05, 9.166614809522094e-05, 9.68535475907538e-05, 9.010018246066501e-05, 9.744335272214871e-05, 9.658050224817961e-05, 0.00010055652929250448, 9.442862089590915e-05, 9.520529384566878e-05, 9.456013090221239e-05, 8.865983822772862e-05, 9.820488613375853e-05, 9.729339269023144e-05, 8.746392643388955e-05, 9.145444272637628e-05, 9.547439185567412e-05, 8.67914758748296e-05, 9.896084561626199e-05, 9.278653322912057e-05, 8.395473156628737e-05, 8.521510461522924e-05, 9.187233570518578e-05, 8.339990307705161e-05, 7.97593526995541e-05, 8.194964047413107e-05, 7.986498875686193e-05, 8.51662842257949e-05, 9.157363509237248e-05, 7.930594832554187e-05, 9.524088907319418e-05, 8.462933472395428e-05, 9.500480871792863e-05, 9.157277588550193e-05, 9.185952717890893e-05, 8.073297022050576e-05, 9.055419449800128e-05, 9.031388418741611e-05])
delta_keff = np.array([-0.00863895703995865, -0.0004270116145389524, 0.003431714609999803, 0.02879377671802219, -0.002186310690175941, 0.013979067402185574, 0.02212612207525866, -0.0038656377309433942, 0.011341413276454215, 0.015238920062220052, -0.011833207847230964, -0.008782628803241543, -0.0021681635312295056, -0.012446423118119498, 0.013413934035424901, 0.018103204498623127, -0.000646448999057081, -0.018775382158269016, -0.0021098866757301993, -0.008335286332783132, 0.011854454825653837, -0.007167302045662072, -0.018418469829541317, 0.013881321832605042, 0.016497389381715966, 0.008745794581086708, -0.009086533201514535, -0.008872522388507997, -0.013593140762918288, 0.004229084295162222, 0.0020725274555504214, -0.019109442827658585, -0.00733525874158647, -0.0050091181612128555, 0.0020411947166341093, -0.008157426013394309, 0.0021236463622512636, 0.010365921379551724, -0.006190469214507277, -0.02130376854377536, 0.005321621888009109, 0.0009014204092313571, 0.008149454136595624, 0.0010740822797929983, -0.012651586264503911, -0.011876084417737132, 0.008664799126298695, 0.018393650163278874, -0.0025946282892677086, -0.004345925184281119, 0.0036869172955901197, 8.71938761474178e-05, 0.006366641196328571, 0.003920346577109823, 0.02389797456653464, -0.013780936682138534, 0.0021549596651904146, -0.009801345936126138, 0.010989027814383157, 0.004318732035509254, 0.008664799126216538, -0.005238419962627305, -0.005328746832333198, 0.00830801187150576, -0.006077107947195626, -0.006987615570382522, 0.010517493313497939, 0.008005356653339568, -0.020389519918438515, -0.013995088007218048, -0.014554433852571158, -0.006401838568114271, -0.0007130761035609723, -0.002366852774955852, 0.000731320708976746, -0.007826712605967567, -0.0023648175376145275, -0.0017419049903867334, -0.004722662818639645, -0.008315031299943598, 0.004172988659442822, 0.010466203562907728, -0.007287277689985938, -0.009577085402569963, -0.010543748205235626, -0.0036763903508010287, 0.006278627919358071, -0.003484045437787797, -0.0005430293587985746, 0.02518235950562908, -0.008909087923684056, 0.00444394753165267, -0.001984512440519226, 0.006711254695876745, 0.00786614883749448, -0.0009153138471604816, -0.003451600763828222, 0.004828008057249034])
uncert=uncert1*10**5

keff = [0.993483547695236, 0.9848445906552773, 0.993056536080697, 0.9969152623052357, 1.0222773244132581, 0.99129723700506, 1.0074626150974215, 1.0156096697704946, 0.9896179099642926, 1.0048249609716902, 1.008722467757456, 0.981650339848005, 0.9847009188919944, 0.9913153841640064, 0.9810371245771164, 1.0068974817306608, 1.011586752193859, 0.9928370986961789, 0.9747081655369669, 0.9913736610195057, 0.9851482613624528, 1.0053380025208898, 0.9863162456495739, 0.9750650778656946, 1.007364869527841, 1.009980937076952, 1.0022293422763227, 0.9843970144937214, 0.984611025306728, 0.9798904069323177, 0.9977126319903982, 0.9955560751507864, 0.9743741048675774, 0.9861482889536495, 0.9884744295340231, 0.9955247424118701, 0.9853261216818416, 0.9956071940574872, 1.0038494690747877, 0.9872930784807287, 0.9721797791514606, 0.9988051695832451, 0.9943849681044673, 1.0016330018318316, 0.994557629975029, 0.980831961430732, 0.9816074632774988, 1.0021483468215346, 1.0118771978585148, 0.9908889194059682, 0.9891376225109548, 0.9971704649908261, 0.9935707415713834, 0.9998501888915645, 0.9974038942723458, 1.0173815222617706, 0.9797026110130974, 0.9956385073604264, 0.9836822017591098, 1.004472575509619, 0.9978022797307452, 1.0021483468214525, 0.9882451277326086, 0.9881548008629027, 1.0017915595667417, 0.9874064397480403, 0.9864959321248534, 1.0040010410087339, 1.0014889043485755, 0.9730940277767974, 0.9794884596880179, 0.9789291138426648, 0.9870817091271217, 0.992770471591675, 0.9911166949202801, 0.9942148684042127, 0.9856568350892684, 0.9911187301576214, 0.9917416427048492, 0.9887608848765963, 0.9851685163952923, 0.9976565363546788, 1.0039497512581437, 0.98619627000525, 0.983906462292666, 0.9829397994900003, 0.9898071573444349, 0.999762175614594, 0.9899995022574481, 0.9929405183364374, 1.018665907200865, 0.9845744597715519, 0.9979274952268886, 0.9914990352547167, 1.0001948023911127, 1.0013496965327304, 0.9925682338480755, 0.9900319469314077, 0.998311555752485]

delta_keff = delta_keff/keff[0]*10**5
print(np.std(delta_keff))
print(np.mean(delta_keff))
std_dev = np.std(delta_keff)
mean = np.mean(delta_keff)
kurt = kurtosis(delta_keff)
skewness = skew(delta_keff)

std_dev2 = np.std(uncert)
mean2 = np.mean(uncert)
kurt2 = kurtosis(uncert)
skewness2 = skew(uncert)



plt.hist(delta_keff, bins=25, density=False)

# Set the plot title and axis labels
plt.title(f'delta k_eff total monte carlo (pcm)')
plt.xlabel('delta k_eff (pcm)')
plt.ylabel('Number of Cases')
plt.figtext(.65, .85, f"mean = {round(mean,4)}")
plt.figtext(.65, .8, f"std dev = {round(std_dev,4)}")
plt.figtext(.65, .75, f"kurtosis = {round(kurt,4)}")
plt.figtext(.65, .7, f"skewness = {round(skewness,4)}")
plt.savefig('Openmc_delta_keff.png')
plt.clf()

plt.hist(uncert, bins=25, density=False)

plt.title(f"OpenMC's statistical uncertainty (pcm) [+,-]")
plt.xlabel('Statistical uncertainty (pcm)')
plt.ylabel('Number of Cases')
plt.figtext(.65, .85, f"mean = {round(mean2,4)}")
plt.figtext(.65, .8, f"std dev = {round(std_dev2,4)}")
plt.figtext(.65, .75, f"kurtosis = {round(kurt2,4)}")
plt.figtext(.65, .7, f"skewness = {round(skewness2,4)}")
plt.savefig('Openmc_stat_uncert.png')
plt.clf()