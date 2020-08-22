---
title: "Countering Entropy Measure Attacks on Packed Software Detection"
date: 2012-01-01
publishDate: 2020-06-11T11:55:59.664564Z
authors: ["Xabier Ugarte Pedrero", "Igor Santos", "Borja Sanz", "Carlos Laorden", "Pablo García Bringas"]
publication_types: ["1"]
abstract: "Malware writers usually employ several techniques to evade detection. For the last years, the number of variants detected each day has increased significantly. Traditional approaches such as signature scanning, one of the most common techniques employed by anti-virus companies, are becoming inefficient for the high amount of samples found in the wild. In order to bypass this kind of filters, malware writers usually obfuscate and transform the code of their creations. One of the methods employed is executable packing, which consists in compressing or ciphering the real malicious code, and injecting a decryption routine into the executable that will load and decompress it at run-time. Entropy is a common heuristic for the detection of packed executables. High entropy values indicate a random distribution of the bytes that compose the executable, a property very common in compressed and ciphered data. Unfortunately, this entropy measure can be altered by different techniques that modify randomness. In this paper, we detail various attacks found on real Zeus family samples, one of the most powerful and spread malware families at this moment, which are protected by custom made packers. In addition, we describe a method for obtaining an alternative entropy measure more resilient to these techniques, and evaluate it for the classification of packed/not-packed executables, obtaining satisfactory detection and false positive rates."
featured: false
publication: "*9th IEEE Consumer Communications and Networking Conference(CCNC2012)*"
tags: ["cryptography", "digital signatures", "invasive software", "pattern classification", "data compression", "entropy", "software metrics"]
doi: "10.1109/CCNC.2012.6181079"
---

