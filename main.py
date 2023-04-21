'''
Sample data prefix list POST

https://10.90.18.74:20051/dataservice/template/policy/list/dataprefix

{
  "name": "Demo-Data-Prefix-List",
  "description": "Desc Not Required",
  "type": "dataprefix",
  "entries": [
    {
      "ipPrefix": "77.77.0.0/16"
    },
    {
      "ipPrefix": "88.88.0.0/16"
    }
  ]
}

'''

network = '10.128.4.251'
mask = '0.127.248.0'

f = open(f'subnets.{network}.txt', 'w')
mask_octets = mask.split('.')
net_octets = network.split('.')
mask_string = net_string = ''
for octet in mask_octets:
    mask_string += format(int(octet), '08b')
for octet in net_octets:
    net_string += format(int(octet), '08b')
f.write(f'{network:15}: {net_string}\n{mask:15}: {mask_string}\n')
mask_list = list(mask_string)
mask_list.reverse()
mask_ones = mask_list.count('1')
mask_range = 2 ** mask_ones
place_value = 1
mask_values = []
for digit in mask_list:
    if digit == '1':
        mask_values.append(place_value)
    place_value *= 2
f.write(f'Mask Values: {mask_values}\nTotal masks:{mask_range}\n')
for value in range(mask_range):
    value_string = list(format(value, f'0{mask_ones}b'))
    value_string.reverse()
    net_add = 0
    for num, digit in enumerate(value_string):
        if digit == '1':
            net_add += mask_values[num]
    net_new = format((int(net_string, 2) + int(net_add)), '032b')
    f.write(f'{net_string} + {int(net_add):032b} = {net_new} -> '
          f' {int(net_new[0:8], 2)}.{int(net_new[8:16], 2)}.{int(net_new[16:24], 2)}.{int(net_new[24:32], 2)}\n')