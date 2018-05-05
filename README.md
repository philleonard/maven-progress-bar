# Maven Progress Bar
Small Python app to show the progress of Maven builds in the command line.

**Distill the verbose Maven output**
![install](https://thumbs.gfycat.com/EnchantedDeafeningKestrel-size_restricted.gif)

**Into something informative about your build**
![progress](https://thumbs.gfycat.com/ZigzagAthleticCusimanse-size_restricted.gif)

## Installation

The app requires that `python3` and `pip` be installed. Simply install using the bash script:
```bash
sh install.sh
```

### Usage

Simply pipe the output of any `mvn` command into `mvnp`. Some examples:

```bash
# Simple clean install
mvn clean install | mvnp
# Also works in parallel
mvn -T 1.0C clean install | mvnp
# Also works in parallel
mvn -T 1.0C clean install | mvnp
```

It also reports errors, and supports resuming builds:
![resuming](https://thumbs.gfycat.com/FocusedIdenticalCirriped-size_restricted.gif)

## TODO:
- Create .bat and verify Windows operability
- Consider using [curses](https://docs.python.org/3/howto/curses.html) for a more interactive display
- Determine end of archive build for better ETA (currently beginning is read)
