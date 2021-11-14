company = ["Apple", "Google", "Microsoft", "Meta", "IBM", "Amazon", "AT&T", "Cisco", "Intel", "Verizon"]
sentimentScore = [0.183, 0.162, 0.09, 0.17, 0.016, 0.17, 0.136, 0.31, 0.26, 0.101]
socialScore = [28.33, 42.5, 63.67, 39.67, 74.33, 28.33, 68.83, 70.17, 57.83, 69.67]
growthScore = [-0.54, -0.65, 0.22, -0.39, -4.5, -0.99, -0.64, -0.07, -11.48, 0.13]
npsScore = [47.0, 11.0, 45.0, -21.0, 27.0, 25.0, 15.0, 38.0, 52.0, 7.0]
npmScore = [25.88, 29.52, 38.51, 35.88, 6.4, 5.74, 0.67, 21.26, 26.89, 16.42]

for a in sentimentScore:
    sentimentScore[a] = (((1 + sentimentScore[a]) * (100 / 2)) * 0.2)

for b in socialScore:
    socialScore[b] = (((3.0 + socialScore[b]) * (100.0 / 6.0)) * 0.1)

for c in growthScore:
    growthScore[c] = (((15.0 + growthScore[c]) * (100.0 / 30.0)) * 0.4)

for d in npsScore:
    npsScore[d] = (((100.0 + npsScore[d]) * (100.0 / 200.0)) * 0.15)

for e in npmScore:
    npmScore[e] = (((npmScore[e] / 50) * 100) * 0.15)

company0 = [company[0], sentimentScore[0], socialScore[0], growthScore[0], npsScore[0], npmScore[0]]
company1 = [company[1], sentimentScore[1], socialScore[1], growthScore[1], npsScore[1], npmScore[1]]
company2 = [company[2], sentimentScore[2], socialScore[2], growthScore[2], npsScore[2], npmScore[2]]
company3 = [company[3], sentimentScore[3], socialScore[3], growthScore[3], npsScore[3], npmScore[3]]
company4 = [company[4], sentimentScore[4], socialScore[4], growthScore[4], npsScore[4], npmScore[4]]
company5 = [company[5], sentimentScore[5], socialScore[5], growthScore[5], npsScore[5], npmScore[5]]
company6 = [company[6], sentimentScore[6], socialScore[6], growthScore[6], npsScore[6], npmScore[6]]
company7 = [company[7], sentimentScore[7], socialScore[7], growthScore[7], npsScore[7], npmScore[7]]
company8 = [company[8], sentimentScore[8], socialScore[8], growthScore[8], npsScore[8], npmScore[8]]
company9 = [company[9], sentimentScore[9], socialScore[9], growthScore[9], npsScore[9], npmScore[9]]

exit()
