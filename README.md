# Seedling

Quick and easy molecular phylogenies.

## Warning

The method used for tree-construction is purely my effort, so it should be
considered extremely inaccurate. Take the biological relevance of these trees
with a grain of salt, but do have fun with the program!

## Installation

Clone this repository to your local machine with git, then install with Python.

```console
git clone https://github.com/shanedrabing/seedling.git
cd seedling
python setup.py install
```

You should probably recompile the binaries as well.

For Windows:

```console
./src/compile.bat
```

For *NIX:

```console
./src/compile.sh
```

## Getting Started

Run the program with Python.

```txt
python seedling.py
```

## Example Usage

This is what the console output looks like:

```txt
Please enter taxa searches on any line:

Felis
                  "Felis" search: 2.8 sec
Canis
                   "Felis" prune: 6.7 sec
                  "Canis" search: 5.3 sec
                   "Felis" score: 0.7 sec
                   "Felis" build: 0.1 sec
                    "Felis" done: 10.3 sec
                   "Canis" prune: 11.5 sec
                   "Canis" score: 3.5 sec
                   "Canis" build: 0.1 sec
                    "Canis" done: 20.4 sec
exit
```

*Hint: wait for one process's "search" phase to end before you try another. I
believe the network adapter doesn't like being hounded by multiple processes.*

## Example Output

Here is our resultant "Felis" (cat genus) molecular phylogeny:

```txt
                            ╭ MT499915.1 Felis catus (Domestic cat)
                      ╭ 100 ┤
                      │     ╰ KP202275.1 Felis silvestris lybica (Near Eastern wildcat)
                ╭ 100 ┤
                │     ╰────── NC_028310.1 Felis silvestris (Wild cat)
          ╭ 100 ┤
          │     ╰──────────── KP202273.1 Felis silvestris bieti (Chinese desert cat)
     ╭ 99 ┤
     │    ╰────────────────── NC_028308.1 Felis margarita (Sand cat)
─ 97 ┤
     │    ╭────────────────── NC_028309.1 Felis nigripes (Black-footed cat)
     ╰ 97 ┤
          ╰────────────────── NC_028307.1 Felis chaus (Jungle cat)
```

Here is our resultant "Canis" (dog genus) molecular phylogeny:

```txt
                                                                         ╭ MK948871.1 Canis lupus orion (Greenland wolf)
                                                                   ╭ 100 ┤
                                                                   │     ╰ MH746950.1 Canis lupus lupus (Eurasian wolf)
                                                             ╭ 100 ┤
                                                             │     ╰────── MZ042325.1 Canis lupus familiaris (Dog)
                                                       ╭ 100 ┤
                                                       │     ╰──────────── KC896375.1 Canis lupus campestris (Steppe wolf)
                                                 ╭ 100 ┤
                                                 │     ╰────────────────── KC461238.1 Canis lupus desertorum
                                           ╭ 100 ┤
                                           │     ╰──────────────────────── MZ042323.1 Canis lupus baileyi (Mexican gray wolf)
                                     ╭ 100 ┤
                                     │     ╰────────────────────────────── GQ374438.1 Canis lupus chanco (Mongolian wolf)
                               ╭ 100 ┤
                               │     │     ╭────────────────────────────── LC520095.1 Canis lupus hodophilax (Japanese wolf)
                               │     ╰ 100 ┤
                               │           ╰────────────────────────────── KF661092.1 Canis sp. Russia/33,500
                         ╭ 100 ┤
                         │     ╰────────────────────────────────────────── MH035676.1 Canis lupus dingo (Dingo)
                    ╭ 99 ┤
                    │    │    ╭─────────────────────────────────────────── NC_027956.1 Canis lupaster (African golden wolf)
                    │    ╰ 99 ┤
                    │         ╰─────────────────────────────────────────── KF573616.1 Canis lupus laniger (Tibetan wolf)
               ╭ 98 ┤
               │    │                      ╭────────────────────────────── MZ367921.1 Canis rufus (Red wolf)
               │    │                ╭ 100 ┤
               │    │                │     ╰────────────────────────────── MZ042357.1 Canis latrans (Coyote)
               │    │          ╭ 100 ┤
               │    │          │     ╰──────────────────────────────────── MZ367914.1 Canis lupus lycaon (Eastern Canadian wolf)
               │    │    ╭ 100 ┤
               │    │    │     ╰────────────────────────────────────────── MZ042364.1 Canis lupus (Gray wolf)
               │    ╰ 99 ┤
               │         ╰──────────────────────────────────────────────── KT448274.1 Canis aureus (Golden jackal)
          ╭ 97 ┤
          │    ╰────────────────────────────────────────────────────────── KT448280.1 Canis mesomelas (Black-backed jackal)
     ╭ 94 ┤
     │    ╰─────────────────────────────────────────────────────────────── KT448271.1 Canis adustus (Side-striped jackal)
─ 92 ┤
     ╰──────────────────────────────────────────────────────────────────── KF661079.1 Canis sp. Belgium/36,000
```

*Hint: Check out the "docs" folder for more examples!*
