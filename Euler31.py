import numpy as np

# # Start at 2 because one from the 2pound coin and one from when
# # Single coins are not acknowledged when looping because they fill the gaps
# total = 2
# layers = [2,5,10,20,50,100]
#
# for x in range(2,201):
#     currentLayers = []
#     for layer in layers:
#         if layer > x : break
#         currentLayers.append(layer)
#
#     currentLayers.reverse()
#     for layer in currentLayers:
#         moded = x % layer
#         if moded == 0 or ( moded) in

# Brute force method
total = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
for pound in range(2):
    for fifPence in range(4):
        for twePence in range(10):
            for tenPence in range(20):
                for fivPence in range(40):
                    for twoPence in range(100):
                        for pence in range(200):
                            if 100 * pound + 50 * fifPence + 20 * twePence + 10 * tenPence + 5 * fivPence + 2 * twoPence + pence == 200:
                                total += 1
                                if total % 1000 ==0:
                                    print('thousand')
print(total)
