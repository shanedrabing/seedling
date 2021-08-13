# Seedling

Easy, quick molecular phylogenies.

## Warning

The method used for tree-construction is purely my effort, so it should be
considered extremely inaccurate. Take the biological relevance of these trees
with a grain of salt, but do have fun with the program!

## Installation

Clone this repository to your local machine with git, then install with Python.

```bash
git clone https://github.com/shanedrabing/seedling.git
cd pyrat
python setup.py install
```

## Getting Started

Run the program with Python.

```txt
python seedling.py
```

## Example Usage

This is what the terminal output looks like:

```txt
Please enter taxa searches on any line:

Canis
Felis
                  "Felis" search: 1.797000
                  "Canis" search: 4.718000
                   "Felis" prune: 3.953000
                   "Felis" score: 0.438000
                   "Felis" build: 0.078000
                   "Canis" prune: 10.875000
                   "Canis" score: 3.203000
                   "Canis" build: 0.110000
Ursidae
                "Ursidae" search: 2.656000
Cetacea
                "Cetacea" search: 5.156000
                 "Ursidae" prune: 14.578000
                 "Ursidae" score: 6.625000
                 "Ursidae" build: 0.172000
                 "Cetacea" prune: 39.578000
                 "Cetacea" score: 54.235000
                 "Cetacea" build: 1.422000
exit
```

*Hint: wait for one process's "search" phase to end before you try another. I
believe the network adapter doesn't like being hounded by multiple processes.*

## Example Output

Here is our resultant "Ursidae" (bear family) molecular phylogeny:

```txt
                                                                   ╭ MW491933.1 Ursus rossicus (Small cave bear)
                                                             ╭ 100 ┤
                                                             │     ╰ MW491932.1 Ursus kanivetz
                                                       ╭ 100 ┤
                                                       │     ╰────── KX641337.1 Ursus spelaeus (Cave bear)
                                                  ╭ 99 ┤
                                                  │    ╰──────────── KF437625.2 Ursus deningeri (Deninger's bear)
                                             ╭ 99 ┤
                                             │    ╰───────────────── MN311250.1 Ursus ingressus (Gamssulzen cave bear)
                                        ╭ 98 ┤
                                        │    │     ╭──────────────── MW491934.1 Ursus kudarensis kudarensis
                                        │    ╰ 100 ┤
                                        │          ╰──────────────── MH605139.1 Ursus kudarensis (Kudaro cave bear)
                                   ╭ 98 ┤
                                   │    │    ╭────────────────────── MW257206.1 Ursus arctos isabellinus (Himalayan brown bear)
                                   │    ╰ 99 ┤
                                   │         ╰────────────────────── MG066703.1 Ursus arctos pruinosus
                              ╭ 97 ┤
                              │    ╰──────────────────────────────── MW491935.1 Ursus kudarensis praekudarensis (Caucasian cave bear)
                         ╭ 96 ┤
                         │    │                                    ╭ NC_011118.1 Ursus thibetanus thibetanus
                         │    │                              ╭ 100 ┤
                         │    │                              │     ╰ NC_009331.1 Ursus thibetanus formosanus (Formosan black bear)
                         │    │                        ╭ 100 ┤
                         │    │                        │     │     ╭ KT964290.1 Ursus thibetanus (Asiatic black bear)
                         │    │                        │     ╰ 100 ┤
                         │    │                        │           ╰ EF667005.1 Ursus thibetanus ussuricus (Manchurian black bear)
                         │    │                   ╭ 99 ┤
                         │    │                   │    ╰──────────── NC_008753.1 Ursus thibetanus mupinensis
                         │    │              ╭ 99 ┤
                         │    │              │    ╰───────────────── MN935768.1 Ursus thibetanus laniger
                         │    │         ╭ 98 ┤
                         │    │         │    ╰────────────────────── AB863014.1 Ursus thibetanus japonicus (Japanese black bear)
                         │    │    ╭ 97 ┤
                         │    │    │    ╰─────────────────────────── KM257060.1 Ursus americanus (American black bear)
                         │    ╰ 97 ┤
                         │         ╰──────────────────────────────── FM177765.1 Helarctos malayanus (Malayan sun bear)
                    ╭ 96 ┤
                    │    ╰────────────────────────────────────────── MH931229.1 Melursus ursinus (Sloth bear)
               ╭ 94 ┤
               │    │         ╭───────────────────────────────────── NC_030174.1 Arctotherium sp.
               │    │    ╭ 97 ┤
               │    │    │    ╰───────────────────────────────────── MW556430.1 Tremarctos ornatus (Spectacled bear)
               │    ╰ 96 ┤
               │         ╰────────────────────────────────────────── NC_011116.1 Arctodus simus (Giant short-faced bear)
          ╭ 93 ┤
          │    ╰──────────────────────────────────────────────────── MH102403.1 Ailuropoda melanoleuca (Giant panda)
     ╭ 91 ┤
     │    ╰───────────────────────────────────────────────────────── LC595633.1 Ursus arctos (Brown bear)
─ 84 ┤
     ╰────────────────────────────────────────────────────────────── CM029679.1 Ursus maritimus (Polar bear)
```

*Hint: Check out the "out" folder for more examples!*
