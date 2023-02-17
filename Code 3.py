from pygenomeviz import GenomeViz

exon_regions1 = [(0, 210), (300, 480), (590, 800), (850, 1000), (1030, 1300)]
exon_regions2 = [(1500, 1710), (2000, 2480), (2590, 2800)]
exon_regions3 = [(3000, 3300), (3400, 3690), (3800, 4100), (4200, 4620)]

gv = GenomeViz()
track = gv.add_feature_track(name=f"Exon Features", size=5000)
track.add_exon_feature(exon_regions1, strand=1, plotstyle="box", label="box", labelrotation=0, labelha="center")
track.add_exon_feature(exon_regions2, strand=-1, plotstyle="arrow", label="arrow", labelrotation=0, labelha="center", facecolor="darkgrey", intron_patch_kws={"ec": "red"})

exon_labels = [f"exon{i+1}" for i in range(len(exon_regions3))]
track.add_exon_feature(exon_regions3, strand=1, plotstyle="bigarrow", label="bigarrow", facecolor="lime", linewidth=1, exon_labels=exon_labels, labelrotation=0, labelha="center", exon_label_kws={"y": 0, "va": "center", "color": "blue"})

gv.savefig("Figure.png")
