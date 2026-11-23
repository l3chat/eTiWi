#!/usr/bin/env python3
"""Check project-local KiCad footprint invariants.

This is NOT a manufacturer land-pattern certification or PCB DRC.
"""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
DIR=ROOT/"eTiWi.pretty"

def pads(name):
    data=(DIR/(name+".kicad_mod")).read_text(encoding="utf-8")
    found=re.findall(r'\(pad "([^"]+)" (?:smd|thru_hole|np_thru_hole) \w+\s*\(at ([0-9.+-]+) ([0-9.+-]+)\)', data)
    if not found: raise AssertionError("no pads: "+name)
    return data,{num:(float(x),float(y)) for num,x,y in found}

def near(a,b,tol=0.01):
    return abs(a-b)<tol

def require(cond,msg):
    if not cond: raise AssertionError(msg)

L,lp=pads("Abracon_AOTA_B201610S3R3_101_T")
require(set(lp)=={"1","2"},"L1 pad numbers")
require(lp["1"][0]<0 and lp["2"][0]>0,"L1 marked pad1 must be on left")
require('(fp_circle (center -1.55 -1.15)' in L,"L1 dot needs to be at pad1 side")
P,pp=pads("LPS28DFW_CCLGA-7L_2.8x2.8mm_DRAFT")
require(set(pp)==set("1234567"),"LPS28DFW pad count")
require(pp["1"][0]<-1 and pp["4"][0]>1,"ST 1/4 opposing side contacts")
require(pp["6"][1]<0 and pp["5"][1]<0,"ST 6/5 top-row contacts in KiCad view")
require(pp["2"][1]>0 and pp["3"][1]>0,"ST 2/3 bottom-row contacts in KiCad view")
require(near(pp["7"][0],0) and near(pp["7"][1],0),"lid pad7 center")
require("(solder_mask_margin 0.05)" in P,"ST mask margin")
U,up=pads("TYPE-C-31-M-14")
for pad in ["A1","A4","A5","A6","A7","A9","A12","B1","B4","B5","B6","B7","B9","B12","S1"]:
    require(pad in up,"USB-C missing pad "+pad)
T,tp=pads("Touch_Electrode_8x12mm")
require(set(tp)=={"1"},"one capacitive electrode pad only")
require('(layers "F.Cu")' in T, "Touch pad requires F.Cu-only under soldermask")
require('(layers "F.Cu" "F.Paste" "F.Mask")' not in T, "Touch pad exposed metal prohibited")
print("FOOTPRINT GATE PASS: L1 pad polarity marker, ST LPS28DFW 7 pads, USB-C pad IDs, covered touch copper.")
print("This tests CAD source invariants only, NOT ST stencil, mechanical alignment, or PCB DRC.")
