---
title: "Collective Classification for Packed Executable Identification"
date: 2011-09-01
publishDate: 2020-06-11T11:55:59.631652Z
authors: ["Igor Santos", "Xabier Ugarte Pedrero", "Borja Sanz", "Carlos Laorden", "Pablo García Bringas"]
publication_types: ["1"]
abstract: "Malware is any software designed to harm computers. Commercial anti-virus are based on signature scanning, which is a technique effective only when the malicious executables have been previously analysed and identified. Malware writers employ several techniques in order to hide their actual behaviour. Executable packing consists in encrypting or hiding the real payload of the executable. Generic unpacking techniques do not depend on the packer used, as they execute the binary within an isolated environment (namely `sandbox') to gather the real code of the packed executable. However, this approach is slow and, therefore, a filter step is required to determine when an executable has been packed. To this end, supervised machine learning approaches trained with static features from the executables have been proposed. Notwithstanding, supervised learning methods need the identification and labelling of a high number of packed and not packed executables. In this paper, we propose a new method for packed executable detection that adopts a collective learning approach to reduce the labelling requirements of completely supervised approaches. We performed an empirical validation demonstrating that the system maintains a high accuracy rate while the labelling efforts are lower than when using supervised learning."
featured: false
publication: "*8th Annual Collaboration, Electronic messaging, Anti-Abuse and Spam Conference (CEAS)*"
tags: ["machine learning", "malware", "executable packing"]
doi: "10.1145/2030376.2030379"
---

