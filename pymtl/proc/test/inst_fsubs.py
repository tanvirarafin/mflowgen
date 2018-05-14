#=========================================================================
# fsub.s
#=========================================================================

import random

from pymtl import *
from inst_utils import *

#-------------------------------------------------------------------------
# gen_basic_test
#-------------------------------------------------------------------------

def gen_basic_test():
  return """
    csrr x1, mngr2proc < 0x40a00000  # 5.0
    csrr x2, mngr2proc < 0x40800000  # 4.0
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    fmv.w.x f1, x1
    fmv.w.x f2, x2
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    fsub.s f3, f1, f2
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    fmv.x.w x3, f3
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    csrw proc2mngr, x3 > 0x3f800000  # 1.0
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
  """

#-------------------------------------------------------------------------
# gen_dest_dep_test
#-------------------------------------------------------------------------

def gen_dest_dep_test():
  return [
    gen_fp_rr_dest_dep_test( 5, "fsub.s", f2i(2), f2i(1), f2i(1) ),
    gen_fp_rr_dest_dep_test( 4, "fsub.s", f2i(3), f2i(1), f2i(2) ),
    gen_fp_rr_dest_dep_test( 3, "fsub.s", f2i(4), f2i(1), f2i(3) ),
    gen_fp_rr_dest_dep_test( 2, "fsub.s", f2i(5), f2i(1), f2i(4) ),
    gen_fp_rr_dest_dep_test( 1, "fsub.s", f2i(6), f2i(1), f2i(5) ),
    gen_fp_rr_dest_dep_test( 0, "fsub.s", f2i(7), f2i(1), f2i(6) ),
  ]

#-------------------------------------------------------------------------
# gen_src0_dep_test
#-------------------------------------------------------------------------

def gen_src0_dep_test():
  return [
    gen_fp_rr_src0_dep_test( 5, "fsub.s", f2i( 8), f2i(1), f2i( 7) ),
    gen_fp_rr_src0_dep_test( 4, "fsub.s", f2i( 9), f2i(1), f2i( 8) ),
    gen_fp_rr_src0_dep_test( 3, "fsub.s", f2i(10), f2i(1), f2i( 9) ),
    gen_fp_rr_src0_dep_test( 2, "fsub.s", f2i(11), f2i(1), f2i(10) ),
    gen_fp_rr_src0_dep_test( 1, "fsub.s", f2i(12), f2i(1), f2i(11) ),
    gen_fp_rr_src0_dep_test( 0, "fsub.s", f2i(13), f2i(1), f2i(12) ),
  ]

#-------------------------------------------------------------------------
# gen_src1_dep_test
#-------------------------------------------------------------------------

def gen_src1_dep_test():
  return [
    gen_fp_rr_src1_dep_test( 5, "fsub.s", f2i(14), f2i(1), f2i(13) ),
    gen_fp_rr_src1_dep_test( 4, "fsub.s", f2i(15), f2i(1), f2i(14) ),
    gen_fp_rr_src1_dep_test( 3, "fsub.s", f2i(16), f2i(1), f2i(15) ),
    gen_fp_rr_src1_dep_test( 2, "fsub.s", f2i(17), f2i(1), f2i(16) ),
    gen_fp_rr_src1_dep_test( 1, "fsub.s", f2i(18), f2i(1), f2i(17) ),
    gen_fp_rr_src1_dep_test( 0, "fsub.s", f2i(19), f2i(1), f2i(18) ),
  ]

#-------------------------------------------------------------------------
# gen_srcs_dep_test
#-------------------------------------------------------------------------

def gen_srcs_dep_test():
  return [
    gen_fp_rr_srcs_dep_test( 5, "fsub.s", f2i(20), f2i(1), f2i(19) ),
    gen_fp_rr_srcs_dep_test( 4, "fsub.s", f2i(21), f2i(3), f2i(18) ),
    gen_fp_rr_srcs_dep_test( 3, "fsub.s", f2i(22), f2i(5), f2i(17) ),
    gen_fp_rr_srcs_dep_test( 2, "fsub.s", f2i(23), f2i(7), f2i(16) ),
    gen_fp_rr_srcs_dep_test( 1, "fsub.s", f2i(24), f2i(9), f2i(15) ),
    gen_fp_rr_srcs_dep_test( 0, "fsub.s", f2i(25), f2i(4), f2i(21) ),
  ]

#-------------------------------------------------------------------------
# gen_srcs_dest_test
#-------------------------------------------------------------------------

def gen_srcs_dest_test():
  return [
    gen_fp_rr_src0_eq_dest_test( "fsub.s", f2i(26), f2i(1), f2i(25) ),
    gen_fp_rr_src1_eq_dest_test( "fsub.s", f2i(27), f2i(1), f2i(26) ),
    gen_fp_rr_src0_eq_src1_test( "fsub.s", f2i(28), f2i(0) ),
    gen_fp_rr_srcs_eq_dest_test( "fsub.s", f2i(29), f2i(0) ),
  ]

#-------------------------------------------------------------------------
# gen_value_test
#-------------------------------------------------------------------------

def gen_value_test():
  negzero = 0x80000000
  posinf  = 0x7f800000
  nans    = 0x7f800001

  return [

    gen_fp_rr_value_test( "fsub.s", f2i( 0.0), f2i( 0.0), f2i( 0.0) ),
    gen_fp_rr_value_test( "fsub.s", f2i( 1.0), f2i( 0.0), f2i( 1.0) ),
    gen_fp_rr_value_test( "fsub.s", f2i( 0.0), f2i( 1.0), f2i(-1.0) ),
    gen_fp_rr_value_test( "fsub.s", f2i( 1.0), f2i( 1.0), f2i( 0.0) ),
    gen_fp_rr_value_test( "fsub.s", f2i( 0.0), f2i( 0.0), f2i( 0.0) ),
    # basic neg
    gen_fp_rr_value_test( "fsub.s", f2i(-1.0), f2i( 0.0), f2i(-1.0) ),
    gen_fp_rr_value_test( "fsub.s", f2i( 0.0), f2i(-1.0), f2i( 1.0) ),
    gen_fp_rr_value_test( "fsub.s", f2i(-1.0), f2i( 1.0), f2i(-2.0) ),
    gen_fp_rr_value_test( "fsub.s", f2i( 1.0), f2i(-1.0), f2i( 2.0) ),
    gen_fp_rr_value_test( "fsub.s", f2i(-1.0), f2i(-1.0), f2i( 0.0) ),
    gen_fp_rr_value_test( "fsub.s", negzero,   f2i( 0.0), negzero   ),
    gen_fp_rr_value_test( "fsub.s", f2i( 0.0), negzero,   f2i( 0.0) ),
    gen_fp_rr_value_test( "fsub.s", negzero,   negzero,   f2i( 0.0) ),
    # basic exact
    gen_fp_rr_value_test( "fsub.s", f2i(0.5),   f2i(4.0),  f2i(-3.5)  ),
    gen_fp_rr_value_test( "fsub.s", f2i(4.0),   f2i(0.5),  f2i(3.5)   ),
    gen_fp_rr_value_test( "fsub.s", f2i(2.0),   f2i(2.0),  f2i(0.0)   ),
    gen_fp_rr_value_test( "fsub.s", f2i(0.125), f2i(0.75), f2i(-0.625)),
    gen_fp_rr_value_test( "fsub.s", f2i(0.75),  f2i(0.125),f2i(0.625) ),
    # basic inexact
    #gen_fp_rr_value_test( "fsub.s", f2i(0.3),   f2i(0.1), 0x3e4cccce ),
    gen_fp_rr_value_test( "fsub.s", f2i(0.4),   f2i(0.3), 0x3dcccccc ),
    gen_fp_rr_value_test( "fsub.s", f2i(0.4),   f2i(0.7), 0xbe999999 ),
    # riscv
    gen_fp_rr_value_test( "fsub.s", f2i(2.5),        f2i(1.0),        f2i(1.5 )       ),
    #gen_fp_rr_value_test( "fsub.s", f2i(-1235.1),    f2i(-1.1),      f2i(-1234)       ),
    #gen_fp_rr_value_test( "fsub.s", f2i(3.14159265), f2i(0.00000001), f2i(3.14159265) ),
    gen_fp_rr_value_test( "fsub.s", posinf,          posinf,          nans            ),

  ]

#-------------------------------------------------------------------------
# gen_random_test
#-------------------------------------------------------------------------

def gen_random_test():
  asm_code = []
  for i in xrange(100):
    src0 = random.randint(-0xfffff,0xfffff)
    src1 = random.randint(-0xfffff,0xfffff)
    dest = src0 - src1
    asm_code.append( gen_fp_rr_value_test( "fsub.s", f2i(src0), f2i(src1),
                                           f2i(dest) ) )
  return asm_code
