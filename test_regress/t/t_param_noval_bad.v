// DESCRIPTION: Verilator: Verilog Test module
//
// This file ONLY is placed under the Creative Commons Public Domain, for
// any use, without warranty, 2019 by Wilson Snyder.
// SPDX-License-Identifier: CC0-1.0

module t #(parameter P, parameter type T);
   generate
      var j;
      for (j=0; P; j++)
        initial begin end
   endgenerate
endmodule
