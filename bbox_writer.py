# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from pascal_voc_writer import Writer
import numpy as np


def write_bboxes(bboxes, classes, filename, frame, name):

    assert(len(bboxes) == len(classes))
    writer = Writer(filename, frame.shape[1], frame.shape[0])
    for i in range(len(bboxes)):
        bbox = bboxes[i]
        cls = classes[i]

        if bbox is None or cls is None:
            continue

        # Convert bbox to rect to match @dek's format
        p0 = bbox[:2]
        size = bbox[2:]
        p1 = p0 + size
        writer.addObject(cls, p0[0], p0[1], p1[0], p1[1])
    writer.save(name)

def write_firstboxes(bboxes, classes, filename):

    assert(len(bboxes) == len(classes))

    with open(filename, "w") as f:
        for i in range(len(bboxes)):
            bbox = bboxes[i]
            cls = classes[i]

            if bbox is None or cls is None:
                continue

            # Convert bbox to rect to match @dek's format
            p0 = bbox[:2]
            size = bbox[2:]
            p1 = p0 + size
            f.write("%s,%s,%s,%s,%s\n" % (p0[0], p0[1], p1[0], p1[1], cls))
def convert_rects_to_bboxes(rects):
    bboxes = []
    for rect in rects:
        p0 = rect[:2]
        p1 = rect[2:]
        size = p1 - p0
        bbox = np.array([p0, size]).reshape(-1)
        bboxes.append(bbox)
    return bboxes


def read_rects(filename):

    rects = []
    classes = []
    with open(filename, "r") as f:
        for line in f:
            try:
                *rect, cls = line.strip().split(",")
                assert(len(rect) == 4)
                rect = np.array(rect, dtype=float).astype(int)

                rects.append(rect)
                classes.append(cls)
            except Exception as e:
                continue

    return rects, classes


def read_bboxes(filename):

    rects, classes = read_rects(filename)
    bboxes = convert_rects_to_bboxes(rects)
    return bboxes, classes


def get_bbox_filename(filename):
    filename = os.path.splitext(os.path.basename(filename))[0]
    return "%s_rects.txt" % filename
