# Maven Progress Bar
Small Python app to show the progress of Maven builds in the command line.

**Distill this madness:**
![install](https://thumbs.gfycat.com/EnchantedDeafeningKestrel-size_restricted.gif)

**Into something informative about your build**
![progress2](https://thumbs.gfycat.com/UnconsciousMelodicIvorygull-size_restricted.gif)

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

## TODO:
- Create .bat and verify Windows operability
- Determine end of archive build rather for better ETA
