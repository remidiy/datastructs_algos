# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def maxProfit(self, A):
#
#         if A:
#             buy = min(A)
#             buy_i = A.index(buy)
#             sell = max(A[buy_i:])
#             a1 = sell - buy
#
#             sell = max(A)
#             sell_i = A.index(sell)
#
#             buy = min(A[:sell_i+1])
#
#             a2 = sell - buy
#             print a1
#             print a2
#             return max(a1, a2)
#         else:
#             return 0



""" Brute force """
#
# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def maxProfit(self, A):
#
#         i = 0
#         m = 0
#         while i < len(A):
#             j = i+1
#             while j < len(A):
#                 if A[j] - A[i] > m:
#                     m = A[j] - A[i]
#                 j += 1
#             i += 1
#         return m


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):

        A = list(A)

        if A:
            m = 0
            buy = 0
            sell = 0

            while m <= (sell - buy):

                if m <= sell - buy:
                    m = sell - buy

                if len(A) <= 1:
                    break

                buy = min(A)
                buy_i = A.index(buy)
                sell = max(A[buy_i:])

                if buy != sell:
                    A.remove(buy)
                    A.remove(sell)
                else:
                    A.remove(buy)

            return m
        else:
            return 0



# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def maxProfit(self, A):
#
#         if A:
#             maxes = []
#
#             i = 0
#             while i < len(A):
#                 maxes.append(max(A[i:]) - A[i])
#                 i += 1
#
#             return max(maxes)
#         else:
#             return 0



A = [ 5607815, 3316671, 8567241, 1953452, 5821723, 2107782, 3199656, 6500702, 1660943, 6106567, 4568376, 8233467, 1638185, 377730, 5259135, 6478497, 6263692, 6552746, 3362077, 5708016, 4539867, 3711341, 5627255, 277600, 6143721, 6259753, 644473, 1507454, 5325058, 6165165, 763455, 9984969, 6976876, 3892567, 5070435, 3819938, 6924694, 933602, 7834567, 8291211, 6739477, 9545438, 3206097, 2323842, 7803322, 1174139, 3607685, 191039, 9269119, 3552617, 1102590, 4356323, 3522620, 1903537, 6280411, 2766528, 8424337, 798933, 4870234, 4125373, 6170402, 3232242, 4406431, 9635073, 5723402, 2327910, 8163383, 5725707, 5758243, 454498, 3448372, 6540483, 7792016, 8569648, 8405688, 7659716, 443181, 1904980, 8752774, 9782165, 3263420, 2362405, 1272399, 1975615, 4785564, 3483341, 8506282, 7863969, 5004535, 9952854, 6918848, 8383187, 9577668, 6675789, 1811729, 4958207, 2478774, 578257, 9573520, 4529624, 9746119, 5062452, 1196924, 3295753, 4622543, 3897334, 2580607, 3386517, 4009710, 5881831, 2870213, 3280031, 8424727, 4443991, 3244444, 9964755, 4594031, 7839146, 5373680, 2667045, 6297282, 6913168, 5055678, 2146177, 8295695, 1359236, 7583380, 2719127, 5199640, 5601038, 1312220, 4304211, 6553177, 8199378, 7163949, 2023984, 9975949, 9232517, 7609041, 5985920, 2054590, 454561, 5482916, 2660135, 8527838, 5410594, 8451992, 7345999, 2234795, 8673975, 3633757, 9745518, 9387763, 560237, 9080534, 389344, 1167825, 4136688, 7053800, 2653286, 1612350, 324971, 5303542, 7695126, 6462474, 1477306, 8658282, 5516828, 3331274, 7235006, 3043695, 464183, 791128, 5146645, 1268058, 9047045, 5906692, 2852023, 2808918, 424668, 3783527, 870647, 9842209, 8769941, 3230988, 4080059, 808752, 2986269, 8129732, 926836, 9900762, 5331852, 2426541, 9206044, 2499321, 7366685, 972680, 106298, 5150104, 9403466, 5873953, 7739451, 6417370, 3236401, 6093656, 5707253, 5454452, 6107483, 9374599, 9312912, 6579208, 4665036, 1630996, 4482086, 1223359, 5925059, 6524074, 6518129, 6895018, 2857112, 1636513, 1239114, 8312802, 1663398, 572307, 4703625, 5211559, 1380893, 1456101, 6065819, 9600368, 9441022, 2123889, 2184671, 7106036, 3965869, 4920784, 8015842, 4114180, 3599133, 5923431, 1808461, 1217301, 1290812, 5807580, 4731508, 4940020, 664661, 6448821, 6492504, 5503474, 9363166, 2560913, 1978557, 5269068, 6743412, 4613052, 6518355, 8765820, 8481497, 7208085, 1178264, 6798102, 4020672, 4951009, 3724074, 9127609, 983019, 1854053, 9501770, 2899978, 2171135, 4173484, 9873035, 1638504, 2651438, 5832207, 9705774, 7315991, 9817970, 8629270, 613202, 6918296, 1776124, 6962356, 6975889, 895334, 4811405, 850100, 8719686, 1806236, 6467911, 1990911, 5751179, 9353956, 4803564, 1110447, 7415615, 7697424, 9364223, 2609202, 9980425, 6504662, 438730, 7096, 864543, 5588596, 8553444, 5555148, 2654639, 6310408, 9534846, 5696310, 2928890, 1980839, 9822702, 7803880, 2356800, 3361458, 8987980, 6172620, 7747543, 4169127, 2728565, 3050660, 3670161, 1022716, 434886, 3411803, 6259457, 2317992, 4853792, 8705581, 292988, 7470821, 6403835, 9553616, 4337225, 2659007, 730082, 2559847, 3945856, 2153601, 5237701, 5764748, 9660799, 4539969, 170685, 212370, 8282356, 5506991, 3372242, 4863239, 4632840, 7486372, 3404761, 2030008, 7126876, 4131493, 8734738, 8314838, 1548351, 6480805, 4249811, 1571259, 9205448, 2427521, 832867, 3566223, 5745791, 2597785, 6431230, 6359451, 9767646, 574420, 4342246, 614000, 7690489, 6840508, 6111863, 644347, 1231520, 742068, 7986519, 9827536, 5543467, 7369407, 5057635, 7923319, 8576725, 6900488, 1200118, 568580, 7373741, 2558364, 174833, 7613505, 8434181, 1464602, 7812576, 27102, 4791057, 9868005, 2826819, 5442788, 5380453, 3597562, 3908561, 5398211, 5315627, 3207827, 8637328, 8597955, 2497694, 2250161, 4640236, 9777914, 1460764, 4614905, 3622121, 2933308, 212147, 6732249, 6934918, 4106945, 7820238, 1263668, 7934723, 10851, 4748252, 1868471, 6779158, 5039908, 2354783, 5305700, 907512, 8473936, 2892992, 7163961, 5847552, 7663992, 3022118, 5388845, 129743, 6759444, 3761572, 2886094, 3776463, 2262452, 9202035, 4709130, 4142810, 9528526, 8284933, 3601048, 7218568, 4007635, 6851267, 1094400, 1157543, 8896396, 3630488, 3913569, 7431417, 7940810, 2431491, 9398399, 3917452, 378696, 6595832, 2849208, 6774198, 2892564, 8601365, 3965601, 1361602, 3610413, 9097647, 6822748, 768909, 3940412, 7807849, 3962640, 5457629, 68084, 3808344, 8086366, 6199981, 630330, 7017026, 6581528, 7991368, 7260849, 2488089, 9627795, 7054955, 3937726, 6101693, 2209522, 9073455, 5212540, 6002591, 2213056, 9506702, 95580, 8278868, 1961097, 8405656, 5790083, 4815501, 4049881, 3730381, 9401831, 9315385, 4729693, 3244170, 4530984, 8447594, 3158546, 4527686, 1005095, 2909568, 5099776, 7310182, 2634443, 3935595, 1446518, 2008850, 9148499, 4008794, 4016283, 3800271, 4121992, 6822984, 8652133, 4368449, 3678178, 5408316, 2952491, 3449449, 5531885, 2981026, 8911713, 4979659, 9811554, 9131874, 4948553, 8560318, 8090951, 5279869, 6495665, 2639388, 3872645, 751353, 270170, 5632428, 5262014, 9439606, 8380009, 1683881, 7709117, 1609187, 2775511, 8713611, 9673113, 8266178, 3247266, 7688598, 2419076, 8130726, 4281383, 4098387, 750777, 3554234, 5167562, 3587083, 6456217, 3375243, 8057274, 3426629, 8761015, 2592124, 4583593, 124011, 8193267, 8906919, 404699, 4395250, 2814951, 2858604, 9677450, 4037192, 48661, 7667293, 5855839, 5378896, 9976243, 4591492, 6976922, 6144942, 6781098, 8056420, 7323926, 689153, 8798036, 3109311, 8048219, 8955574, 309664, 3471841, 3654327, 2291916, 8080146, 6792197, 2406223, 9796082, 8676278, 1094297, 5540654, 9673603, 5108186, 3610730, 1871505, 4474810, 8137990, 7226681, 5261676, 7791659, 2778211, 6382581, 232040, 3504602, 646515, 6453725, 98782, 817896, 5748588, 3941055, 1285149, 4337264, 4861734, 8300993, 6749827, 5695724, 3172210, 5424488, 1851985, 6138318, 3192075, 4163764, 1702368, 9721295, 4647749, 1297078, 2575264, 8872304, 3375483, 3576595, 9263545, 5358260, 4602058, 6726911, 724603, 5489608, 4273306, 9447189, 7730837, 7578065, 9442551, 4076682, 5273670, 3144124, 1068838, 8007390, 1349218, 9481145, 8747986, 1299448, 2942009, 6032122, 9074683, 5317375, 7540153, 923821, 7029808, 7081268, 3239598, 1900259, 444249, 6208751, 2176965, 5301232, 4033708, 6569996, 2601589, 4932029, 368930, 8008150, 8278580, 975447, 4769515, 40109, 9065589, 2830638, 4373745, 962734, 359324, 9230525, 7782387, 3143786, 8592633, 1270713, 4652111, 8138868, 9251607, 2015304, 6491330, 701924, 4385305, 9020963, 8443216, 2843285, 2597757, 4567213, 3431958, 7318803, 406638, 1410336, 9772604, 6193593, 3886822, 2615443, 4811289, 3258804, 3922039, 259239, 5033857, 1220404, 772527, 8277795, 6296312, 1260979, 2415601 ]
# A = [ 4194445, 5755801, 2855639, 4681951, 642183, 9606207, 6539770, 2929563, 2371075, 2065991, 4734767, 3035028, 9844237, 9859030, 5366228, 7126800, 3093826, 2064333, 4794134, 6009455, 1554282, 1141024, 9008908, 5564577, 5670584, 3701388, 305389, 9988838, 7607445, 8689404, 4606240, 721493, 8358372, 7969247, 2005188, 9381407, 9640526, 1257732, 3128856, 5674956, 7212588, 5699639, 3391536, 9223297, 303612, 246025, 4664705, 5533721, 1254106, 6723049, 7092956, 9115027, 4029515, 8682821, 3075505, 2455402, 8685967, 7823073, 8138079, 5223844, 7204268, 8388370, 4932424, 1163737, 5251626, 5026560, 5050075, 444693, 8416089, 6533127, 8849938, 9195466, 6912747, 318446, 2255659, 1324379, 1091239, 7558075, 9314612, 7170906, 3222755, 3626629, 184898, 4602309, 1596067, 2979905, 5350257, 2919884, 9904801, 722970, 8136001, 1391045, 6414844, 2205953, 4755182, 2798289, 5134693, 9826047, 432014, 6805799, 6827969, 7032606, 4696237, 5731657, 2733376, 4768391, 2782129, 4632527, 4485247, 9064703, 3372660, 9420437, 4193640, 2612882, 2867493, 8068152, 3907859, 124864, 5942858, 5168681, 5242568, 474474, 8675032, 1368145, 5358739, 4107643, 1657155, 9175880, 8535311, 8277280, 7462655, 5984330, 7676367, 498783, 9495820, 3076391, 3546466, 3806366, 1312460, 652185, 9729605, 2472157, 913603, 78321, 7611113, 6599149, 4055264, 8831043, 2431665, 6773353, 262124, 8150637, 3198010, 9990139, 811941, 7829764, 5725450, 223476, 4615776, 9894103, 5906398, 906269, 3967342, 1543460, 4301996, 1787414, 8254232, 1789655, 4230800, 5969792, 905489, 3258010, 9454136, 4249389, 6467504, 6519664, 4001349, 5026632, 5014202, 6667981, 3817855, 5034444, 6930070, 1349637, 1035425, 9252606, 6607642, 2524617, 1006652, 3528601, 2690079, 9721966, 4199938, 5762348, 128435, 4118901, 6892353, 2989545, 666501, 5888056, 8654317, 4248490, 762635, 5111086, 5764247, 1866872, 4293692, 9257206, 6891118, 6087668, 941907, 8810109, 6646582, 3630739, 446420, 351840, 4011717, 3143139, 7749114, 6392659, 9048202, 7016084, 2382421, 4446109, 8485561, 5782000, 3949229, 5221723, 8561121, 9303285, 1543066, 6108565, 2722519, 7758442, 6163843, 2755475, 1023498, 5443927, 312752, 9196009, 3221496, 2914945, 2653161, 4489388, 1959263, 5623432, 9971827, 3785009, 7319090, 7630374, 5217607, 8044924, 8769872, 8185537, 1597610, 7814177, 1029537, 7567770, 2258460, 5576548, 482655, 2612813, 3224455, 2585241, 1092094, 9877649, 7498080, 5699558, 2951043, 6086409, 9542232, 661452, 5836164, 4345098, 8307895, 6637498, 6272548, 6046123, 3646645, 774039, 2892326, 8990224, 7423970, 1974660, 2915143, 3225108, 7089874, 6573037, 562334, 4269980, 489996, 1186345, 8226531, 816581, 768322, 8850738, 4660865, 816794, 6128349, 9412437, 8816780, 8379353, 3537553, 4864852, 5573468, 79518, 6575334, 7596536, 6889113, 9602795, 6640332, 2332107, 6535110, 7488014, 9995147, 3170250, 5091560, 1360125, 7509497, 1121503, 7358828, 4794661, 7027205, 3332651, 9573810, 4093855, 7576965, 2998873, 7914729, 1092664, 1802541, 8724368, 558214, 2857902, 2716188, 2003935, 7168482, 6012254, 3643378, 6074238, 6647950, 6389831, 5109285, 866253, 381182, 1164871, 6275734, 1373355, 7017631, 5325732, 255703, 8151488, 9133852, 5909110, 3275900, 6061125, 475435, 3611189, 2999139, 4638073, 8973840, 2561265, 3769187, 6653732, 8312926, 8824383, 1472759, 4821429, 1483913, 862658, 5331434, 5223163, 9257756, 1027441, 4445934, 8306958, 9852026, 203971, 5610515, 9554829, 2882366, 5159575, 5463819, 2912256, 1762629, 2822314, 1863502, 3884780, 3574742, 8568504, 1253111, 503241, 6109333, 7496262, 7489733, 4319399, 9349740, 3945259, 8884655, 7607110, 8608523, 4386536, 9292660, 9617100, 5400748, 5880352, 8878708, 4242669, 7471856, 7150688, 9502486, 3485539, 2421557, 1965130, 7403648, 8796538, 6717060, 259999, 6321534, 2791184, 4094667, 4931963, 1782625, 497135, 931841, 7789116, 9062312, 1314376, 4186203, 2781984, 6351555, 6433207, 5584677, 6332921, 1563685, 1553136, 2297922, 8427601, 1826430, 3253257, 1884767, 5263589, 7242437, 4136563, 2669239, 4890360, 7994097, 3243588, 3024004, 6227582, 4667341, 5951200, 7625344, 5601489, 525262, 9273359, 6532814, 5958471, 4875336, 1980311, 2047533, 1693741, 5059206, 1441267, 8561945, 9413927, 267932, 9767893, 5708235, 8490874, 5875232, 4514791, 122809, 8169308, 5485225, 1258832, 6423197, 7401453, 63428, 6242952, 3935999, 5627757, 7677399, 7549112, 7071403, 1269499, 6408877, 4263892, 2386645, 2142089, 9680907, 8958646, 787007, 7100373, 3563871, 9002573, 369222, 2707131, 9279796, 2847105, 7396262, 8662258, 2403065, 8174614, 5792694, 6292058, 3741998, 2806982, 9193909, 4390354, 5450971, 9800176, 9442318, 848643, 3667121, 6013064, 7078994, 864441, 2124755, 987795, 3904413, 4436411, 3207605, 4372015, 400985, 3196209, 8094432, 1053017, 710448, 349168, 6789123, 7444730, 3441905, 3933247, 6882550, 6867729, 9164628, 165786, 716556, 1109737, 3671507, 6671443, 1236642, 1664765, 9329820, 5442137, 6931445, 3808660, 2034565, 8492007, 1031792, 2348823, 7364453, 4999931, 4322960, 8340199, 639089, 135093, 4657084, 8368461, 8517539, 6231696, 8261869, 8247731, 7867767, 7266041, 6158750, 7335486, 8035170, 4269642, 7393800, 7019543, 4434206, 3330723, 6580929, 4449142, 8067766, 3682033, 3698348, 3067274, 9752295, 1121939, 7713186, 1157402, 2462787, 8355113, 3140410, 3159795, 1928352, 5335266, 5919865, 505504, 2750149, 2786405, 2165156, 7275716, 2443565, 7820731, 3257234, 3943777, 3295474, 173055, 6809788, 6093159, 264240, 3204306, 9165393, 6552803, 8654172, 2492684, 2467027, 126724, 6043336, 3988090, 1145326, 9919194, 4786559, 1544896, 9566382, 6783344, 9457825, 8712145, 5598821, 2627075, 7848949, 4073282, 5164981, 5966346, 4412603, 7695179, 9612711, 3863295, 6957529, 7419982, 7950638, 9746913, 8971977, 6977344, 7509979 ]
# A = [2, 1]
# A = [ 2818230, 7403984, 4351468, 1421487, 7605160, 5208496, 7531934, 4591458, 7651855, 250947, 1336131, 5549968, 2745934, 6573497, 9601143, 8224571, 9244066, 1620843, 4761506, 5727354, 4182190, 8865163, 7279869, 9216523, 252942, 3202398, 2290997, 8091757, 9569131, 3906656, 7358869, 7619990, 276018, 4214248, 4699020, 3751510, 9494811, 5614974, 2330383, 4920447, 8233233, 5771379, 5387271, 5247002, 2798851, 4580226, 7126123, 9223141, 4360720, 952654, 5278877, 7601049, 9172042, 7172999, 3446110, 9529759, 5656352, 9906602, 1464921, 951934, 4423815, 3526455, 6026490, 5307933, 4637603, 3149180, 7678108, 6408158, 1823554, 7322846, 8179280, 8130526, 385824, 7905978, 2528980, 3322491, 2173099, 1749406, 466934, 3497518, 2739495, 6008331, 1030524, 61846, 986089, 1045022, 8830845, 1534615, 9536254, 9237340, 9203353, 5197059, 1184860, 2402093, 1838211, 7757451, 901528, 6212943, 5456136, 370866, 9865290, 3604544, 6866099, 7024190, 7613244, 7012449, 3873551, 9802651, 6650714, 6846584, 3903872, 7449458, 4120761, 6225790, 1670137, 1636815, 8512682, 2874798, 162065, 5390874, 3101607, 5958315, 2873041, 4223444, 5038522, 5058074, 2864072, 8164895, 7430173, 4424115, 2841038, 7619274, 7468778, 6757339, 108147, 5839529, 808426, 4566513, 985850, 4713855, 646205, 9911747, 3246726, 5291818, 4295981, 1374528, 7622505, 8334748, 8698645, 7519585, 4076941, 7723323, 5028998, 3115865, 5027729, 6919530, 2423739, 1370013, 2690390, 5924645, 4704505, 4274201, 9860863, 2821846, 4857089, 7291811, 9717035, 2957715, 7363440, 3407464, 2234964, 3441937, 9099661, 3342443, 169947, 3536322, 6581953, 9701320, 143325, 1882758, 4880942, 178333, 2103903, 3763435, 3804034, 160351, 6080523, 2814093, 71285, 1732979, 6398174, 4231145, 374785, 7063725, 6381409, 6083702, 4702676, 771579, 3591131, 6062420, 4849287, 7053875, 8069854, 1089340, 92121, 7503669, 732798, 1086717, 2385481, 6348071, 2838100, 824881, 7061849, 8141478, 9618819, 3285272, 5294837, 6847448, 205254, 5804693, 9003329, 4499343, 7167299, 1949312, 4724105, 5208013, 9855698, 2330204, 1439447, 8770858, 1172745, 9055583, 2756453, 8234567, 660042, 3740379, 2183230, 5256275, 5144704, 6773318, 2344280, 6351061, 7479950, 3837132, 9495498, 2293127, 5499529, 4600028, 7980115, 6916329, 165008, 4977094, 5989391, 6978460, 8974382, 3002467, 369490, 7358457, 3427519, 6690527, 2484554, 6894055, 4118013, 5706063, 3201441, 6617635, 3534067, 9394384, 5786754, 5691447, 5352500, 3048717, 5016373, 1197785, 4973348, 4547020, 2090052, 8895072, 9837158, 6370140, 5378049, 7527634, 3807007, 3595608, 4426079, 91857, 6093128, 2916780, 320446, 6581474, 5063989, 9011690, 2855805, 1032578, 6332948, 6940558, 4742373, 9205363, 2275906, 4101239, 4319632, 8017584, 273243, 306840, 2030888, 725886, 2099294, 5974877, 5834917, 5105295, 4665592, 889855, 5218209, 2674885, 5154083, 5713744, 4726731, 1325599, 4800337, 3111719, 3178669, 4723711, 4012295, 1580604, 8341477, 725012, 2695556, 6844029, 4430042, 3229941, 988497, 4751443, 545910, 2860429, 6348012, 4037558, 8846204, 7297396, 6641236, 8446508, 8644471, 9215112, 4788741, 2723132, 5538175, 8813487, 1462433, 9995385, 994472, 6566679, 9050630, 3783874, 8544424, 4582403, 4930326, 4177348, 9799972, 7800609, 3022793, 4713768, 7907017, 5540915, 9554864, 6435506, 896576, 5538647, 5082695, 5128707, 2957679, 5868123, 9693039, 8472225, 6032795, 919951, 832968, 100981, 5554412, 7669117, 551405, 616904, 2992569, 5468854, 1807976, 1347383, 6589893, 7722647, 5385991, 9050626, 9536384, 5461851, 222798, 8057883, 4815847, 4438863, 5578904, 5598404, 9891041, 8151085, 2268410, 7318330, 8092224, 6024578, 9790340, 7812178, 8291610, 5581711, 9718533, 2229029, 2477034, 9081398, 5002812, 4346005, 6694790, 7067074, 4061467, 8959420, 4090118, 8716593, 3707959, 7926725, 1370824, 7149519, 7424369, 4113675, 1403883, 7695160, 6592368, 3886945, 9427735, 8925744, 7176769, 9749169, 1339101, 6271186, 957137, 5547734, 5082659, 4848758, 3386939, 8935019, 5468194, 6442874, 396444, 5954756, 687810, 6072404, 8555928, 2442260, 2412764, 2517499, 453564, 1845066, 6615528, 3431520, 2627738, 7715009, 2741654, 5800083, 478968, 9251990, 2995142, 5803195, 9639400, 7998957, 8013719, 1606479, 497328, 1032644, 5004691, 7443000, 7183249, 8148579, 1163167, 6684732, 661682, 9585333, 9448812, 7322890, 2000123, 871741, 273085, 530397, 2906894, 575186, 2556814, 9433785, 5770832, 5837737, 3802230, 4291063, 2130932, 6793816, 5785814, 6657700, 2959074, 2665495, 9000064, 6094831, 3227013, 4509619, 526613, 7645518, 2940566, 4217142, 2177934, 6718959, 844680, 9553335, 1069491, 4764705, 8222745, 2734749, 6040044, 9371270, 1968993, 757608, 8540893, 2689715, 4223815, 3649825, 2470767, 6158455, 5434537, 3919068, 2965045, 7888337, 7847468, 373265, 3297223, 3608097, 1240562, 6921819, 4811336, 6694914, 8260877, 9230285, 3687095, 1359942, 1855636, 557784, 2395724, 3811953, 4470339, 3760941, 911677, 1477370, 476750, 9690382, 2539050, 7228163, 9782933, 7478784, 9347698, 2559260, 9862494, 9552852, 4578014, 6149106, 1866575, 7141552, 2276642, 5820590, 2261020, 978370, 8408520, 8964851, 1096442, 106023, 4923887, 3403126, 5115334, 7810976, 1294157, 5882149, 179810, 573943, 5342822, 1667567, 7583568, 8757906, 780710, 4176770, 2375601, 2461778, 8315516, 4723632, 1530786, 3929497, 3917918, 1322702, 2789462, 757308, 8575710, 5685342, 5477788, 3122238, 3586979, 8950164, 8586154, 94485, 8002454, 4946044, 4998138, 3739685, 9837965, 7502652, 8833439, 9969221, 8021000, 9233204, 6570880, 7250314, 5039647, 5893527, 9211984, 2038397, 6511919, 8877455, 752764, 2499203, 2480176, 1827374, 6804769, 4470847, 8296687, 3163524, 8874133, 9432065, 5051656, 2651853, 6607048, 5180658, 5146566, 8749158, 6190608, 7370819, 4725295, 2562160, 7565474, 1773015, 7379799, 9654350, 3364795, 3795953, 9413132, 7710802, 555359, 8133311, 7874918, 4573823, 7227227, 3339370, 8522042, 489579, 9935953, 9782434, 4131616, 9138304, 2366952, 5317914, 5917916, 5317929, 3499620, 2579954, 8470950, 4696093, 2445404, 8458527, 7087512, 1835382, 2935682, 2248203, 7257377, 4250632, 7800541, 1438373, 1935509, 4609858, 6428077, 5889942, 2040230, 9284119, 6927789, 3755695, 8230016, 5061658, 6126861, 8381613, 1699422, 5695729, 3759795, 3020058, 6432333, 3620590, 3494078, 2670738, 9851169, 2209099, 36514, 7993830, 6147331, 3844898, 638243, 5498655, 7774470, 6049962, 5737976, 3209282, 5319973, 105807, 280480, 3038014, 2908996, 7204697, 8416417, 1542666, 9919925, 7490193, 8545176, 8203752, 7675473, 6455813, 4448974, 2991507, 1087872, 6340322, 3220267, 7182228, 1731454, 2369584, 9670375, 3642037, 3683497, 857753, 5176793, 6657855, 8351001, 6282716, 4981493, 6571767, 6725099, 2468176, 7829100, 1901985, 2510244, 6437379, 9140916, 9587833, 9121404, 4234250, 8288032, 8503387, 2295433, 7662906, 3314685, 6674184, 594622, 850719, 338585, 4470123, 1345997, 9943784, 3209176, 6711988, 8931282, 5508895, 2702366, 1926067, 8944293, 9850655, 8082451, 4138907, 6755045, 6297924, 7076881, 2122868, 3453252, 9719174, 1639503, 9944786, 9779515, 1960043, 8376785, 1027781, 5826218, 5046451, 8909752, 4397042, 9906586, 8642050, 3626505, 7714116, 5572543, 7295667, 5089588, 9524314, 6425538, 2357711, 9083569, 7218322, 6908219, 895357, 1754135, 1788977, 4198073, 647968, 7933619, 5249473, 1063166, 4605675, 3810108, 9335994, 9797533, 3124844, 504744, 3979040, 3732193, 8843017, 621547, 4440684, 8584575, 4740994, 9828449, 3294772, 5526089, 3369810, 8524988, 9082123, 3326337, 907245, 3784194, 2522459, 6603118, 9368820, 3075533, 1710630, 1398165, 555428, 3572260, 4385406, 1344849, 7088684, 2214393, 9872026, 3697757, 8211255, 1795972, 7606984, 1389704, 6540277, 2727691, 7262417, 8988907, 5583647, 5848156, 5918842, 4294431, 3101607, 6755965, 3509889, 8645854, 6639453, 6699494, 3573234, 49993, 3908980, 8106248, 2763237, 85998, 3968038, 3186302, 1053340, 4235749, 780712, 9225689, 3833342, 5023150, 3109621, 5333018, 1434513, 2137412, 3032764, 4432590, 6735382, 9327359, 7192059, 9275350, 8780180, 6803486, 1452435, 9049344, 6627394, 76520, 4849361, 4295383, 2631532, 2990622, 2745628, 8311828, 100024, 4184536, 8177940, 9556529, 9434463, 7258198, 8227231, 8640883, 8377443, 159206, 1673761, 5780546, 2747022, 6701259, 2586986, 7246750, 9001054, 3500800, 8471615, 5246367, 3992375, 3495200, 9895105, 9333789, 2738101, 5458438, 4849705, 6663769, 6826715, 7589716, 5702826, 6274231, 3767533, 9389116, 1403529, 916829, 7262593, 6219422, 9983974, 2862701, 1592837, 5666794, 7123802, 8642624, 8853795, 2472804, 1284575, 6439574, 5203624, 2645951, 469259, 7791367, 3094928, 8093298, 9385093, 1142794, 8935348, 9960382, 1754016, 586594, 18567, 3239903, 2839742, 6881502, 8689227, 1631401, 2209794, 4620661, 9117227, 8187461, 3848443, 7634484, 9690001 ]
# A = [1, 2]
# A = []
print Solution().maxProfit(A)


x = 9969147