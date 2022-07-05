a =[{
        "color":"red",
        "price":40
    },
    {
        "color":"black",
        "price":400
    },
    {
        "color":"red",
        "price":40
    },
    {
        "color":"red",
        "price":40
    }]

# {
#     "red":80,
#     "black":400
# }
def addColorPrice(color_dict):
    sum_color = {}
    # print(a[0]["color"])
    for i in range(0,len(color_dict)):
        if color_dict[i]["color"] in sum_color:
            sum_color[color_dict[i]["color"]] += color_dict[i]["price"]
        else:
            sum_color[color_dict[i]["color"]]=color_dict[i]["price"]
    return sum_color

print(addColorPrice(a))