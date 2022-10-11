# Author:
#    Philip Zubel - 07 Oct 2022

# This python script returns the total hours spent on the dissertation according to the timeline
import re

TIMELOG_MARKDOWN = "timelog.md"

total_time = 0

with open(TIMELOG_MARKDOWN) as f:
    for line in f:
        if "hour" in line:
            obj = re.search('\d*\.?\d+', line).group()
            total_time += float(obj)

print("Time spent on dissertation - {:.1f} hours".format(total_time))
