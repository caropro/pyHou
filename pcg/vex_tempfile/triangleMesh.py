# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0

#vex
float edgelength = chf("length");

float val = edgelength/2;
vector pos_pt0 = set(val,0,0);
vector pos_pt1 = set(-val,0,0);
vector pos_pt2 = set(0,0,val);

int pt0 = addpoint(0,pos_pt0);
int pt1 = addpoint(0,pos_pt1);
int pt2 = addpoint(0,pos_pt2);

int prim_id = addprim(0,"poly");

addvertex(0,prim_id,pt0);
addvertex(0,prim_id,pt1);
addvertex(0,prim_id,pt2);