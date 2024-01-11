display_pins_info = """HEX40 PIN_F18 Seven Segment Digit 4[0] 3.3-V LVTTL
HEX41 PIN_E20 Seven Segment Digit 4[1] 3.3-V LVTTL
HEX42 PIN_E19 Seven Segment Digit 4[2] 3.3-V LVTTL
HEX43 PIN_J18 Seven Segment Digit 4[3] 3.3-V LVTTL
HEX44 PIN_H19 Seven Segment Digit 4[4] 3.3-V LVTTL
HEX45 PIN_F19 Seven Segment Digit 4[5] 3.3-V LVTTL
HEX46 PIN_F20 Seven Segment Digit 4[6] 3.3-V LVTTL
HEX47 PIN_F17 Seven Segment Digit 4[7] 3.3-V LVTTL
HEX50 PIN_J20 Seven Segment Digit 5[0] 3.3-V LVTTL
HEX51 PIN_K20 Seven Segment Digit 5[1] 3.3-V LVTTL
HEX52 PIN_L18 Seven Segment Digit 5[2] 3.3-V LVTTL
HEX53 PIN_N18 Seven Segment Digit 5[3] 3.3-V LVTTL
HEX54 PIN_M20 Seven Segment Digit 5[4] 3.3-V LVTTL
HEX55 PIN_N19 Seven Segment Digit 5[5] 3.3-V LVTTL
HEX56 PIN_N20 Seven Segment Digit 5[6] 3.3-V LVTTL
HEX57 PIN_L19 Seven Segment Digit 5[7] 3.3-V LVTTL"""
switches_pins_info = """SW0 PIN_C10 Slide Switch[0] 3.3-V LVTTL
SW1 PIN_C11 Slide Switch[1] 3.3-V LVTTL
SW2 PIN_D12 Slide Switch[2] 3.3-V LVTTL
SW3 PIN_C12 Slide Switch[3] 3.3-V LVTTL
SW4 PIN_A12 Slide Switch[4] 3.3-V LVTTL
SW5 PIN_B12 Slide Switch[5] 3.3-V LVTTL
SW6 PIN_A13 Slide Switch[6] 3.3-V LVTTL
SW7 PIN_A14 Slide Switch[7] 3.3-V LVTTL
SW8 PIN_B14 Slide Switch[8] 3.3-V LVTTL
SW9 PIN_F15 Slide Switch[9] 3.3-V LVTTL"""
ds1 = []
ds2 = []
for e in display_pins_info.split('\n'):
    try:
        args = e.split(' ')
    except:
        continue
    if "HEX4" in args[0]:
        ds2 += [args[1]]
    else:
        ds1 += [args[1]]
print(f'ds1 pins: \n',"\n".join(ds1[::-1]),'\n')
print(f'ds2 pins: \n',"\n".join(ds2[::-1]))
switches = []
for e in switches_pins_info.split('\n'):
    try:
        args = e.split(' ')
    except:
        continue
    switches += [args[1]]
print(f'switches pins: \n',"\n".join(switches[::-1]))
"""
PIN_AB17
PIN_AA17
PIN_AB19
PIN_AA19

PIN_Y19
PIN_AB20
PIN_AB21
PIN_AA20
"""