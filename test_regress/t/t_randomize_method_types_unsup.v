// DESCRIPTION: Verilator: Verilog Test module
//
// This file ONLY is placed under the Creative Commons Public Domain, for
// any use, without warranty, 2020 by Wilson Snyder.
// SPDX-License-Identifier: CC0-1.0

class Foo;
   rand int x;
endclass

class Cls;
   rand int assocarr[string];
   rand int dynarr[][];
   rand int q[$];
   rand Cls cls;
   rand int i;
   rand Foo foo;
   rand int y;
   int st;
   constraint dynsize {
      dynarr.size < 20;
      dynarr.size > 0;
      dynarr[1].size < 10;
   }
   constraint statedep { i < st + 2; }
   constraint q_size_elem {
      q.size < 5;
      q[i] < 10;
   }
   constraint global_constraint {
     foo.x < y;
  }
endclass

module t (/*AUTOARG*/);
   Cls obj;
   int res;

   initial begin
      obj = new;
      obj.foo = new;
      res = obj.randomize();
      res = obj.randomize() with { dynarr.size > 2; };
   end
endmodule
