def ws_length(data, offset):    #Page 79
    for i in range(data[offset+7]):
        scalable_signed_pos.append(offset+12+(6*i))
        scalable_signed_pos.append(offset+14+(6*i))

    return 10 + data[offset+7]*6 + data[offset+8]*2 + data[offset+9]*2

def dm_length(data, offset):    #Page 81
    for i in range(data[offset+6]):
        scalable_signed_pos.append(offset+10+(6*i))
        scalable_signed_pos.append(offset+12+(6*i))

    return 8 + data[offset+6]*6 + data[offset+7]*2

def am_length(data, offset):    #Page 82
    for i in range(data[offset+8]):
        scalable_signed_pos.append(offset+12+(6*i))
        scalable_signed_pos.append(offset+14+(6*i))

    return 10 + data[offset+8]*6 + data[offset+9]*2

def container_length(data,offset):  #Page 85
    for i in range(data[offset+8]):
        scalable_signed_pos.append(offset+12+(6*i))
        scalable_signed_pos.append(offset+14+(6*i))

    return 10 + data[offset+8]*6 + data[offset+9]*2

def sk_length(data, offset):    #Page 87
    return 6 + data[offset+4]*2 + data[offset+5]*2

def kobj_length(data, offset):    #Page 88
    for i in range(data[offset+5]):
        scalable_signed_pos.append(offset+9+(6*i)) 
        scalable_signed_pos.append(offset+11+(6*i))

    return 7 + data[offset+5]*6 + data[offset+6]*2

def but_length(data, offset):    #Page 90
    for i in range(data[offset+11]):
        scalable_signed_pos.append(offset+15+(6*i))
        scalable_signed_pos.append(offset+17+(6*i))

    return 13 + data[offset+11]*6 + data[offset+12]*2

def inputb_length(data, offset):    #Page 96
    scalable_unsigned_pos.append(offset + 4)
    return 13 + data[offset+12]*2

def inputs_length(data, offset):    #Page 97
    scalable_unsigned_pos.append(offset + 3)
    scalable_unsigned_pos.append(offset + 5)
    length = data[offset+16]
    return 17 + length + 2 + data[offset+18+length]*2

def inputn_length(data, offset):   #Page 100
    scalable_unsigned_pos.append(offset + 3)
    scalable_unsigned_pos.append(offset + 5)  
    return 38 + data[offset+37]*2

def inputl_length(data, offset):   #Page 103
    scalable_unsigned_pos.append(offset + 3)
    scalable_unsigned_pos.append(offset + 5)
    return 13 + data[offset+10]*2 + data[offset+12]*2

def outputs_length(data, offset):   #Page 108
    scalable_unsigned_pos.append(offset + 3)
    scalable_unsigned_pos.append(offset + 5)
    length = data[offset+14] + (data[offset+15] << 8)
    return 16 + length + 1 + data[offset+length+16]*2

def outputn_length(data, offset):   #Page 109
    scalable_unsigned_pos.append(offset + 3)
    scalable_unsigned_pos.append(offset + 5)
    length = data[offset+14] + (data[offset+15] << 8)
    return 29 + data[offset+length+28]*2

def outputl_length(data, offset):   #Page 112
    scalable_unsigned_pos.append(offset + 3)
    scalable_unsigned_pos.append(offset + 5)
    return 12 + data[offset+10]*2 + data[offset+11]*2

def outputline_length(data, offset):   #Page 114
    scalable_unsigned_pos.append(offset + 5)
    scalable_unsigned_pos.append(offset + 7)
    return 11 + data[offset+10]*2

def outputrect_length(data, offset):   #Page 117
    scalable_unsigned_pos.append(offset + 5)
    scalable_unsigned_pos.append(offset + 7)
    return 13 + data[offset+12]*2

def outputellipse_length(data, offset):   #Page 120
    scalable_unsigned_pos.append(offset + 5)
    scalable_unsigned_pos.append(offset + 7)
    return 15 + data[offset+14]*2

def outputpolygon_length(data, offset):   #Page 123
    scalable_unsigned_pos.append(offset + 3)
    scalable_unsigned_pos.append(offset + 5)

    for i in range(data[offset+12]):
        scalable_unsigned_pos.append(offset+14+(4*i))
        scalable_unsigned_pos.append(offset+16+(4*i))

    return 14 + data[offset+12]*4 + data[offset+13]*2

def outputmeter_length(data, offset):   #Page 125
    scalable_unsigned_pos.append(offset + 3)

    return 21 + data[offset+20]*2

def outputlbg_length(data, offset):   #Page 129
    scalable_unsigned_pos.append(offset + 3)
    scalable_unsigned_pos.append(offset + 5)

    return 24 + data[offset+23]*2

def outputabg_length(data, offset):   #Page 132
    scalable_unsigned_pos.append(offset + 3)
    scalable_unsigned_pos.append(offset + 5)
    scalable_unsigned_pos.append(offset + 12)

    return 27 + data[offset+26]*2

def pg_length(data, offset):   #Page 136
    scalable_unsigned_pos.append(offset + 3)

    length = data[offset+12] + (data[offset+13] << 8) + (data[offset+14] << 16) + (data[offset+15] << 24)
    return 17 + length + data[offset+16]*2

def nv_length(data, offset):   #Page 139
    return 7

def sv_length(data, offset):   #Page 139
    length = data[offset+3] + (data[offset+4] << 8)
    return 5 + length

def fonta_length(data, offset):   #Page 140
    id = data[offset] + (data[offset+1] << 8)
    if id < 20000:
        font_small_pos.append(offset+4)
    elif id > 40000:
        font_large_pos.append(offset+4)
    else:
        font_med_pos.append(offset+4)
    return 8 + data[offset+7]*2

def linea_length(data, offset):   #Page 143
    scalable_unsigned_pos.append(offset + 4)
    return 8 + data[offset+7]*2

def filla_length(data, offset):   #Page 145
    return 8 + data[offset+7]*2

def inputa_length(data, offset):   #Page 147
    length = data[offset+4]
    return 5 + length + 1 + data[offset + 5 + length]*2

def extendedia_length(data, offset):   #Page 148
    length = data[offset+4]
    return 5 + length + 1 + data[offset + 5 + length]*2

def objectp_length(data, offset):   #Page 149
    return 5

def macro_length(data, offset):   #Page 149
    length = data[offset+3] + (data[offset+4] << 8)
    return 5 + length

def cm_length(data, offset):   #Page 151
    length = data[offset+3] + (data[offset+4] << 8)
    return 5 + length

def gc_length(data, offset):   #Page 152 may need scaling added at a later date
    raise
    return 34

def wm_length(data, offset):   #Page 156 may need some scaling stuff added later
    raise  
    return 17 + data[offset+14]*2 + data[offset+15]*6 + data[offset+16]*2

def kg_length(data, offset):   #Page 180
    return 10 + data[offset+8]*2 + data[offset+9]*2

def olrl_length(data, offset):   #Page 182
    length = data[offset+3] + (data[offset+4] << 8)
    return 5 + length*7

def eod_length(data, offset):   #Page 183
    return 13 + data[offset+12]*2

def ern_length(data, offset):   #Page 184
    return 12

def eop_length(data, offset):   #Page 185
    return 9

def anim_length(data, offset):   #Page 186
    return 17 + data[offset+15]*6 + data[offset+16]*2

def aft1_length(data, offset):   #Page 259
    return 6 + data[offset+5]*6

def aft2_length(data, offset):   #Page 259
    return 6 + data[offset+5]*6

def ait1_length(data, offset):   #Page 262
    return 7 + data[offset+6]*6

def ait2_length(data, offset):   #Page 263
    return 6 + data[offset+5]*6

def acdt2_length(data, offset):   #Page 269
    return 6

type_dict = {
    0x00: {'name': 'working set', 'length': ws_length},
    0x01: {'name': 'data mask', 'length': dm_length},
    0x02: {'name': 'alarm mask', 'length': am_length},
    0x03: {'name': 'container object', 'length': container_length},
    0x04: {'name': 'soft key mask', 'length': sk_length},
    0x05: {'name': 'key object', 'length': kobj_length},
    0x06: {'name': 'button object', 'length': but_length},
    0x07: {'name': 'input boolean object', 'length': inputb_length},
    0x08: {'name': 'input string object', 'length': inputs_length},
    0x09: {'name': 'input number object', 'length': inputn_length},
    0x0A: {'name': 'input list object', 'length': inputl_length},
    0x0B: {'name': 'output string object', 'length': outputs_length},
    0x0C: {'name': 'output number object', 'length': outputn_length},
    0x25: {'name': 'output list object', 'length': outputl_length},
    0x0D: {'name': 'output line object', 'length': outputline_length},
    0x0E: {'name': 'output rectangle object', 'length': outputrect_length},
    0x0F: {'name': 'output ellipse object', 'length': outputellipse_length},
    0x10: {'name': 'output polygon object', 'length': outputpolygon_length},
    0x11: {'name': 'output meter object', 'length': outputmeter_length},
    0x12: {'name': 'output linear bar graph object', 'length': outputlbg_length},
    0x13: {'name': 'output arched bar graph object', 'length': outputabg_length},
    0x14: {'name': 'picture graphic object', 'length': pg_length},
    0x15: {'name': 'number variable object', 'length': nv_length},
    0x16: {'name': 'string variable object', 'length': sv_length},
    0x17: {'name': 'font attributes object', 'length': fonta_length},
    0x18: {'name': 'line attributes object', 'length': linea_length},
    0x19: {'name': 'fill attributes object', 'length': filla_length},
    0x1A: {'name': 'input attributes object', 'length': inputa_length},
    0x26: {'name': 'extended input attributes object', 'length': extendedia_length},
    0x1B: {'name': 'object pointer object', 'length': objectp_length},
    0x1C: {'name': 'macro object', 'length': macro_length},
    0x27: {'name': 'colour map object', 'length': cm_length},
    0x24: {'name': 'graphics context object', 'length': gc_length},
    0x22: {'name': 'window mask object', 'length': wm_length},
    0x23: {'name': 'key group object', 'length': kg_length},
    0x28: {'name': 'object label reference list object', 'length': olrl_length},
    0x29: {'name': 'external object definition list object', 'length': eod_length},
    0x2A: {'name': 'external reference name object', 'length': ern_length},
    0x2B: {'name': 'external object pointer object', 'length': eop_length},
    0x2C: {'name': 'animation object', 'length': anim_length},

    0x1D: {'name': 'auxiliary function type 1 object', 'length': aft1_length},
    0x1F: {'name': 'auxiliary function type 2 object', 'length': aft2_length},
    0x1E: {'name': 'auxiliary input type 1 object', 'length': ait1_length},
    0x20: {'name': 'auxiliary input type 2 object', 'length': ait2_length},
    0x21: {'name': 'auxiliary control designator type 2 object', 'length': acdt2_length},

}

with open('ISOBUS.iop', 'rb') as iop_file:
    data = [ord(x) for x in iop_file.read()]
    
boundaries = []
curr_pos = 0

scalable_unsigned_pos = []
scalable_signed_pos = []
font_large_pos = []
font_med_pos = []
font_small_pos = []

while curr_pos < len(data):
    obj_type = type_dict[data[curr_pos+2]]                # get the type of the current obj
    type_name = obj_type['name']                    # gets a human readable name of hte current onbj
    length = obj_type['length'](data, curr_pos)     # gets the length of hte current object\
    object_id = data[curr_pos] + (data[curr_pos+1] << 8)

    boundaries.append([type_name, object_id, curr_pos, curr_pos+length])
    curr_pos += length 

print boundaries
print scalable_unsigned_pos
with open ("unsigned_pos.txt", "w") as out_file:
    out_file.write(str(len(scalable_unsigned_pos)))
    for item in scalable_unsigned_pos:
        out_file.write("," + str(item))
print scalable_signed_pos
with open ("signed_pos.txt", "w") as out_file:
    out_file.write(str(len(scalable_signed_pos)))
    for item in scalable_signed_pos:
        out_file.write("," + str(item))
print font_large_pos
with open ("font_large_pos.txt", "w") as out_file:
    out_file.write(str(len(font_large_pos)))
    for item in font_large_pos:
        out_file.write("," + str(item))
print font_med_pos
with open ("font_med_pos.txt", "w") as out_file:
    out_file.write(str(len(font_med_pos)))
    for item in font_med_pos:
        out_file.write("," + str(item))
print font_small_pos
with open ("font_small_pos.txt", "w") as out_file:
    out_file.write(str(len(font_small_pos)))
    for item in font_small_pos:
        out_file.write("," + str(item))



file = open("scalable.txt","w")
file.write(",".join(str(x) for x in scalable_unsigned_pos))
file.write("\n")

file.write(",".join(str(x) for x in scalable_signed_pos))
file.write("\n")

file.write(",".join(str(x) for x in font_large_pos))
file.write("\n")

file.write(",".join(str(x) for x in font_med_pos))
file.write("\n")

file.write(",".join(str(x) for x in font_small_pos))
file.write("\n")
file.close()
