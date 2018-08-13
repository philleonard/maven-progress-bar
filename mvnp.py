#!/usr/bin/env python3
import sys
import re
import progressbar
import argparse
from colorama import init, Fore

init()
progressbar.streams.wrap_stdout()
progressbar.streams.wrap_stderr()
parser = argparse.ArgumentParser()
parser.add_argument('-w', action='store_true', help="Output WARNINGS produced by Maven")
parser.add_argument('-dc', action='store_true', help="Disable all console colouring")
parser.add_argument('-e', action='store_true', help="Output everything after ERROR produced by Maven")
parser.add_argument('-t', action='store_true', help="Write estimated finish time. ☕️ or ⚔️ ? https://xkcd.com/303/")
parser.add_argument('-n', action='store_true', help="Output artifact names built by Maven")
args = parser.parse_args()
warn = args.w
artifacts = args.n
absolute_time = args.t
after_error = args.e
disable_colour = args.dc


def get_colour(colour):
    if disable_colour:
        return ""
    return colour


error_c = "[" + get_colour(Fore.LIGHTRED_EX) + "ERROR" + get_colour(Fore.RESET) + "]"
info_c = "[" + get_colour(Fore.CYAN) + "INFO" + get_colour(Fore.RESET) + "]"
warning_c = "[" + get_colour(Fore.YELLOW) + "WARNING" + get_colour(Fore.RESET) + "]"


bar_format = \
    [
        "Maven build: ",
        get_colour(Fore.YELLOW),
        progressbar.Percentage(),
        get_colour(Fore.RESET),
        " ",
        progressbar.Counter(format='(%(value)d of %(max_value)d)'),
        get_colour(Fore.LIGHTGREEN_EX),
        progressbar.Bar(marker="\u2588"),
        get_colour(Fore.RESET),
        " ",
        progressbar.Timer(),
        " ",
        get_colour(Fore.MAGENTA),
        progressbar.AbsoluteETA(format='Finishes: %(eta)s', format_finished='Finished at %(eta)s')
        if absolute_time else progressbar.AdaptiveETA(),
        get_colour(Fore.RESET)
    ]


def ansi_length(o):
    ansi_occ = re.findall(r'\x1B\[[0-?]*[ -/]*[@-~]', o)
    ansi_len = 0
    for occ in ansi_occ:
        ansi_len += len(occ)
    return len(o) - ansi_len


def match():
    count = 0
    bar = None
    error = False
    current_max = 0

    for line in sys.stdin:
        if warn:
            match_warn = re.findall("WARN", line)
            if len(match_warn) > 0:
                sys.stdout.write(line.replace("[WARNING]", warning_c))

        match_error = re.findall("ERROR", line)
        if len(match_error) > 0 or (error & after_error):
            error = True
            sys.stderr.write(line.replace("[ERROR]", error_c).replace("[INFO]", info_c).replace("[WARNING]", warning_c))

        matched = re.findall("\[[0-9]+/[0-9]+\]", line)
        if len(matched) > 0:
            if artifacts:
                nline = line.strip("[INFO] ")
                art = find_between(nline, "Building", "[")
                fline = "{}  {}".format("⚒️️", nline.replace(art, get_colour(Fore.CYAN) + art + get_colour(Fore.RESET)))
                sys.stdout.write(fline)
            prog = matched[0][1:len(matched[0]) - 1]
            fraction = prog.split("/")
            if bar is None or int(fraction[1]) is not current_max:
                current_max = int(fraction[1])
                bar = progressbar.ProgressBar(
                    widgets=bar_format,
                    widget_kwargs={'samples': 2},
                    max_value=current_max + 1,
                    redirect_stdout=True,
                    custom_len=lambda o: ansi_length(o))
            count += 1

            # Corner case to allow for chained mvn, or if build resumed then sync
            if count > current_max:
                count = int(fraction[0])

        if bar is not None:
            bar.update(count)

    if not error:
        bar.finish()

    sys.stderr.flush()
    progressbar.streams.flush()


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


if __name__ == "__main__":
    try:
        match()
    except KeyboardInterrupt:
        progressbar.streams.unwrap_stdout()
