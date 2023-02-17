#install pygenomeviz
from pygenomeviz import GenomeViz

genome_list = (
    {"name": "Genome 01", "size": 1000, "cds_list": ((150, 200, 1), (500, 700, -1), (750, 950, 1))},
    {"name": "Genome 02", "size": 1300, "cds_list": ((50, 200, 1), (350, 450, 1), (700, 900, -1), (950, 1150, -1))},
    {"name": "Genome 03", "size": 1200, "cds_list": ((150, 300, 1), (350, 450, -1), (500, 700, -1), (700, 900, -1))},
    {"name": "Genome 04", "size": 1500, "cds_list": ((250, 300, -1), (360, 450, 1), (560, 700, -1), (760, 900, 1))},
    {"name": "Genome 05", "size": 1250, "cds_list": ((50, 280, -1), (356, 450, -1), (500, 600, -1), (660, 900, -1))},
)

gv = GenomeViz(tick_style="axis")
for genome in genome_list:
    name, size, cds_list = genome["name"], genome["size"], genome["cds_list"]
    track = gv.add_feature_track(name, size)
    for idx, cds in enumerate(cds_list, 1):
        start, end, strand = cds
        track.add_feature(start, end, strand, label=f"Gene{idx:01d}", linewidth=1, labelrotation=0, labelvpos="top", labelhpos="center", labelha="center")

# Add links between "genome 01" and "genome 02"
gv.add_link(("Genome 01", 150, 300), ("Genome 02", 50, 200))
gv.add_link(("Genome 01", 700, 500), ("Genome 02", 900, 700))
gv.add_link(("Genome 01", 750, 950), ("Genome 02", 1150, 950))
# Add links between "genome 02" and "genome 03"
gv.add_link(("Genome 02", 50, 200), ("Genome 03", 150, 300), normal_color="skyblue", inverted_color="lime", curve=True)
gv.add_link(("Genome 02", 350, 450), ("Genome 03", 450, 350), normal_color="skyblue", inverted_color="lime", curve=True)
gv.add_link(("Genome 02", 900, 700), ("Genome 03", 700, 500), normal_color="skyblue", inverted_color="lime", curve=True)
gv.add_link(("Genome 03", 900, 700), ("Genome 02", 1150, 950), normal_color="skyblue", inverted_color="lime", curve=True)
# Add links between "genome 03" and "genome 04"
gv.add_link(("Genome 03", 600, 700), ("Genome 04", 800, 900), normal_color="yellow", inverted_color="lime", curve=True)
# Add links between "genome 04" and "genome 05"
gv.add_link(("Genome 04", 300, 250), ("Genome 05", 150, 260), normal_color="red", inverted_color="red", curve=True)


gv.savefig("Figure.jpg")



