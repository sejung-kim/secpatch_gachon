#!/usr/bin/env python3
# DESCRIPTION: Verilator: Verilog Test driver/expect definition
#
# Copyright 2024 by Wilson Snyder. This program is free software; you
# can redistribute it and/or modify it under the terms of either the GNU
# Lesser General Public License Version 3 or the Perl Artistic License
# Version 2.0.
# SPDX-License-Identifier: LGPL-3.0-only OR Artistic-2.0

import vltest_bootstrap

test.scenarios('simulator')


def gen(filename):
    with open(filename, 'w', encoding="latin-1") as fh:
        for copy in range(0, 32):  # pylint: disable=unused-variable
            for i in range(0, 256):
                fh.write(chr(i))


gen(test.obj_dir + "/t_sys_fread.mem")

test.compile()

test.execute(expect_filename=test.golden_filename)

test.passes()
