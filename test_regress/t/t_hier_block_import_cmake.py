#!/usr/bin/env python3
# DESCRIPTION: Verilator: Verilog Test driver/expect definition
#
# Copyright 2024 by Wilson Snyder. This program is free software; you can
# redistribute it and/or modify it under the terms of either the GNU
# Lesser General Public License Version 3 or the Perl Artistic License
# Version 2.0.
# SPDX-License-Identifier: LGPL-3.0-only OR Artistic-2.0

import vltest_bootstrap

test.scenarios('vlt_all')
# CMake build executes from a different directory than the Make one.
test.top_filename = os.path.abspath("t/t_hier_block_import.v")

# stats will be deleted but generation will be skipped if libs of hierarchical blocks exist.
test.clean_objs()

test.setenv('TEST_ROOT', test.t_dir + "/t_hier_block_import")

test.compile(verilator_make_cmake=True,
             verilator_make_gmake=False,
             verilator_flags2=[
                 '$TEST_ROOT/t_hier_block_import_def.vh',
                 '-f $TEST_ROOT/t_hier_block_import_args.f', '-I$TEST_ROOT'
             ],
             threads=(6 if test.vltmt else 1))

test.execute()

test.file_grep(test.obj_dir + "/VsubA/subA.sv", r'^module\s+(\S+)\s+', "subA")
test.file_grep(test.stats, r'HierBlock,\s+Hierarchical blocks\s+(\d+)', 2)

test.passes()
