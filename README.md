# ![Maven](https://i.imgur.com/MaAla7t.png) Progress Bar 

Small Python app to show the progress of Maven builds in the command line, with a build ETA so that you can get back to
the [important stuff](https://xkcd.com/303/).

**Distill the verbose Maven output:**
![install](https://thumbs.gfycat.com/EnchantedDeafeningKestrel-size_restricted.gif)

**Into something informative about your build:**
![progress](https://thumbs.gfycat.com/ZigzagAthleticCusimanse-size_restricted.gif)

## Installation

The app requires that `python3` and `pip` be installed. Simply install using the bash script:
```bash
./install.sh
```
May require sudo privileges to copy script to `/usr/local/bin`


## Usage

Simply pipe the output of any `mvn` command into `mvnp`. Some examples:

```bash
# Simple clean install
mvn clean install | mvnp
# Also works in parallel
mvn -T 1.0C clean install | mvnp
# Also supports chained builds
(mvn install && mvn test && mvn package) | mvnp
```

**It also reports errors, and supports resuming builds:**
![resuming](https://thumbs.gfycat.com/FocusedIdenticalCirriped-size_restricted.gif)

## Tips
```bash
# Consider using an alias when you find the right config
alias my-mvnp="mvnp -e -t -n"
mvn clean install | my-mvp
```

## TODO:
- Create .bat and verify Windows operability
- Add cross platform build notifications
- Consider using [curses](https://docs.python.org/3/howto/curses.html) for a more interactive display
- Determine end of archive build for better ETA (currently beginning is read)
