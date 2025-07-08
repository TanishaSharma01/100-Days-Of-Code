import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 12)
# print(colors)

colors_list = []

for item in colors:
    first_color = item
    rgb = first_color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    new_color = (rgb.r, rgb.g, rgb.b)
    colors_list.append(new_color)

print(colors_list)

new_colors_list = [(219, 173, 124), (159, 180, 190), (134, 73, 53), (49, 102, 153), (245, 232, 236), (118, 82, 93), (179, 140, 150), (41, 46, 65), (162, 104, 151), (126, 173, 114)]

